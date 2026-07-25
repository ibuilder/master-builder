#!/usr/bin/env python3
"""Master Builder — MCP server (stdio).

Serves the Master Builder skill (the protocol + its reference library) over the Model
Context Protocol, so ANY MCP-capable agent can load references **on demand** instead of
swallowing the whole corpus. This restores, for non-Claude agents, the progressive
disclosure that the native Claude skill gets for free.

Design constraints (see references/build-doctrine.md):
  * **Zero dependencies.** Stock Python 3.9+ standard library only — no SDK to install,
    nothing to pin, nothing to break. MCP over stdio is newline-delimited JSON-RPC 2.0.
  * **Read-only.** Every tool is a read; the server never writes, never touches the
    network, and never executes anything. Irreversible actions do not exist here.
  * **Offline, $0 to run.**

Run:      python scripts/mcp_server.py
Self-test: python scripts/mcp_server.py --selftest

Client config (Claude Desktop / Claude Code / any MCP client):
    {
      "mcpServers": {
        "master-builder": {
          "command": "python",
          "args": ["/absolute/path/to/master-builder/scripts/mcp_server.py"]
        }
      }
    }

Protocol notes:
  * stdout carries MCP messages ONLY. All logging goes to stderr (spec requirement).
  * Tool failures are returned as results with isError=true, not JSON-RPC errors, so the
    agent can read and recover from them.
"""
from __future__ import annotations

import json
import os
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

SERVER_NAME = "master-builder"
# Protocol versions this server understands. If the client asks for one of these we echo
# it back; otherwise we answer with our latest and let the client decide.
SUPPORTED_PROTOCOL_VERSIONS = ("2025-06-18", "2025-03-26", "2024-11-05")
LATEST_PROTOCOL_VERSION = SUPPORTED_PROTOCOL_VERSIONS[0]

# Resolve the skill root: env override, else the repo containing this script.
ROOT = Path(os.environ.get("MASTER_BUILDER_HOME", Path(__file__).resolve().parent.parent))
REFS_DIR = ROOT / "references"
URI_SCHEME = "masterbuilder"

JSONRPC_PARSE_ERROR = -32700
JSONRPC_INVALID_REQUEST = -32600
JSONRPC_METHOD_NOT_FOUND = -32601
JSONRPC_INVALID_PARAMS = -32602
JSONRPC_INTERNAL_ERROR = -32603


def log(msg: str) -> None:
    """Log to stderr. Never stdout — stdout is reserved for MCP messages.

    Kept ASCII-safe: some consoles (notably Windows cp1252) can't encode the em-dashes
    used elsewhere in this repo, and a logging call must never take the server down.
    """
    line = f"[{SERVER_NAME}] {msg}"
    try:
        print(line, file=sys.stderr, flush=True)
    except UnicodeEncodeError:
        print(line.encode("ascii", "replace").decode("ascii"), file=sys.stderr, flush=True)


# --------------------------------------------------------------------------------------
# Skill corpus
# --------------------------------------------------------------------------------------

def _split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter, body). Kept inline so this file stays standalone."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[3:end].strip(), text[end + 4:].lstrip("\n")
    return "", text


def version() -> str:
    try:
        m = re.search(r"^##\s*\[(\d+\.\d+\.\d+)\]", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), re.M)
        return m.group(1) if m else "0.0.0"
    except OSError:
        return "0.0.0"


def protocol_text() -> str:
    """The core reasoning protocol — SKILL.md with its Claude-only frontmatter stripped."""
    return _split_frontmatter((ROOT / "SKILL.md").read_text(encoding="utf-8"))[1].strip()


def reference_index() -> list[dict[str, str]]:
    """[{name, description}] parsed from the reference table in SKILL.md, in its order.

    Falls back to the files on disk if the table can't be read, so the server still works
    if SKILL.md's formatting changes.
    """
    on_disk = {p.name for p in REFS_DIR.glob("*.md")} if REFS_DIR.is_dir() else set()
    index: list[dict[str, str]] = []
    try:
        body = protocol_text()
        for m in re.finditer(r"\|\s*`references/([^`]+)`\s*\|\s*(.+?)\s*\|", body):
            name = m.group(1)
            if name in on_disk:
                index.append({"name": name, "description": m.group(2).strip()})
    except OSError:
        pass
    listed = {r["name"] for r in index}
    for name in sorted(on_disk - listed):  # anything not in the table still gets served
        index.append({"name": name, "description": ""})
    return index


def reference_names() -> list[str]:
    return [r["name"] for r in reference_index()]


def read_reference(name: str) -> str:
    """Read one reference by filename. Validated against the known set (no path traversal)."""
    allowed = reference_names()
    if name not in allowed:
        # Be forgiving about a missing/extra .md, then fail with a useful message.
        alt = name if name.endswith(".md") else f"{name}.md"
        if alt in allowed:
            name = alt
        else:
            raise KeyError(
                f"Unknown reference {name!r}. Available: {', '.join(allowed)}. "
                f"Call master_builder_list_references to see what each one covers."
            )
    return (REFS_DIR / name).read_text(encoding="utf-8")


def _fold(s: str) -> str:
    """Lowercase and strip accents, so 'Koppen' finds 'Köppen' and 'facade' finds 'façade'."""
    return "".join(
        c for c in unicodedata.normalize("NFD", s.lower())
        if unicodedata.category(c) != "Mn"
    )


def search_corpus(query: str, limit: int = 20) -> list[dict[str, Any]]:
    """Accent- and case-insensitive substring search across the protocol + every reference."""
    hits: list[dict[str, Any]] = []
    docs: list[tuple[str, str]] = [("SKILL.md", protocol_text())]
    for name in reference_names():
        try:
            docs.append((name, read_reference(name)))
        except OSError:
            continue
    needle = _fold(query)
    for doc_name, text in docs:
        heading = ""
        for i, line in enumerate(text.splitlines(), start=1):
            if line.startswith("#"):
                heading = line.lstrip("#").strip()
            if needle in _fold(line):
                hits.append({
                    "source": doc_name,
                    "line": i,
                    "section": heading,
                    "text": line.strip()[:400],
                })
                if len(hits) >= limit:
                    return hits
    return hits


# --------------------------------------------------------------------------------------
# Tools
# --------------------------------------------------------------------------------------

TOOLS: list[dict[str, Any]] = [
    {
        "name": "master_builder_get_protocol",
        "description": (
            "Get the Master Builder Protocol — the core reasoning method for any real-estate "
            "development, construction, or built-environment question (ground-it-in-place rule, "
            "the 8-step protocol, professional boundaries, output conventions). Read this FIRST "
            "when a task touches the built environment, then pull the specific reference(s) the "
            "task needs with master_builder_read_reference."
        ),
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
        "annotations": {
            "title": "Get the Master Builder Protocol",
            "readOnlyHint": True, "destructiveHint": False,
            "idempotentHint": True, "openWorldHint": False,
        },
    },
    {
        "name": "master_builder_list_references",
        "description": (
            "List the available Master Builder reference documents and what each one covers "
            "(codes/jurisdictions, development lifecycle, real-estate finance, pro-forma review, "
            "construction delivery, digital/BIM toolkit, sustainability & carbon, build doctrine). "
            "Use this to decide which reference to read for the task at hand."
        ),
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
        "annotations": {
            "title": "List reference documents",
            "readOnlyHint": True, "destructiveHint": False,
            "idempotentHint": True, "openWorldHint": False,
        },
    },
    {
        "name": "master_builder_read_reference",
        "description": (
            "Read the full text of one Master Builder reference document by filename "
            "(e.g. 'real-estate-finance.md'). Load only the reference the task actually needs. "
            "Call master_builder_list_references first if unsure which one applies."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Reference filename, e.g. 'global-codes.md' or 'pro-forma-review.md'.",
                }
            },
            "required": ["name"],
            "additionalProperties": False,
        },
        "annotations": {
            "title": "Read a reference document",
            "readOnlyHint": True, "destructiveHint": False,
            "idempotentHint": True, "openWorldHint": False,
        },
    },
    {
        "name": "master_builder_localize",
        "description": (
            "Get the localization worksheet for a specific place — the six resolutions (place depth, "
            "adopted code stack, the full AHJ set, climate and hazard basis, market and delivery "
            "conventions, licensure) that together generate 'the book' governing a building at that "
            "location. Call this FIRST whenever a built-environment task names a city, country, or site, "
            "before giving any jurisdiction-specific answer. Returns the procedure and what to verify — "
            "it does not invent local values; look those up and say which are unverified."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "place": {
                    "type": "string",
                    "description": "The location, as specifically as known — e.g. 'Austin, Texas', 'Dubai (DDA free zone plot)', 'Vietnam'.",
                }
            },
            "required": ["place"],
            "additionalProperties": False,
        },
        "annotations": {
            "title": "Localization worksheet for a place",
            "readOnlyHint": True, "destructiveHint": False,
            "idempotentHint": True, "openWorldHint": False,
        },
    },
    {
        "name": "master_builder_search",
        "description": (
            "Search the whole Master Builder corpus (protocol + all references) for a term and get "
            "back matching lines with their source file, line number, and section heading. Use for "
            "narrow lookups — 'interest reserve', 'CBAM', 'ASCE 24', 'yield-on-cost', 'FIDIC' — when "
            "you don't want to load an entire reference."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Text to search for (case-insensitive)."},
                "limit": {
                    "type": "integer", "description": "Max results (default 20).",
                    "minimum": 1, "maximum": 200, "default": 20,
                },
            },
            "required": ["query"],
            "additionalProperties": False,
        },
        "annotations": {
            "title": "Search the corpus",
            "readOnlyHint": True, "destructiveHint": False,
            "idempotentHint": True, "openWorldHint": False,
        },
    },
]


def call_tool(name: str, args: dict[str, Any]) -> str:
    if name == "master_builder_get_protocol":
        return protocol_text()

    if name == "master_builder_list_references":
        lines = ["# Master Builder reference library", ""]
        for r in reference_index():
            lines.append(f"- **{r['name']}** — {r['description'] or '(no description)'}")
        lines += ["", "Read one with master_builder_read_reference(name=...)."]
        return "\n".join(lines)

    if name == "master_builder_read_reference":
        ref = args.get("name")
        if not isinstance(ref, str) or not ref.strip():
            raise ValueError("Parameter 'name' is required — the reference filename, e.g. 'global-codes.md'.")
        return read_reference(ref.strip())

    if name == "master_builder_localize":
        place = args.get("place")
        if not isinstance(place, str) or not place.strip():
            raise ValueError("Parameter 'place' is required — the location to localize for.")
        place = place.strip()
        try:
            dossiers = read_reference("jurisdiction-dossiers.md")
        except (KeyError, OSError):
            dossiers = ""
        # Serve the procedure + router verbatim from the reference: one source of truth.
        proc = ""
        start = dossiers.find("## 1. The localization procedure")
        end = dossiers.find("## 3. Worked dossier")
        if start != -1 and end != -1:
            proc = dossiers[start:end].rstrip().rstrip("-").rstrip()
        return "\n".join([
            f"# Localizing for: {place}",
            "",
            "Work the six resolutions below for this location. Treat every specific value as **to "
            "verify** until you have checked it against the currently adopted local code and the AHJ's "
            "live process — then say explicitly which items you verified and which remain assumptions.",
            "",
            proc or "(Procedure unavailable — read references/jurisdiction-dossiers.md directly.)",
            "",
            "---",
            "",
            "**Next:** read `climate-building-science.md` for what this climate forces on the envelope, "
            "and `global-codes.md` for the code family and load derivation. If a worked dossier in "
            "`jurisdiction-dossiers.md` covers a comparable jurisdiction, read it for the shape of the "
            "answer — but never transplant its values.",
        ])

    if name == "master_builder_search":
        query = args.get("query")
        if not isinstance(query, str) or not query.strip():
            raise ValueError("Parameter 'query' is required — the text to search for.")
        limit = args.get("limit", 20)
        if not isinstance(limit, int) or isinstance(limit, bool):
            limit = 20
        limit = max(1, min(200, limit))
        hits = search_corpus(query.strip(), limit)
        if not hits:
            return (
                f"No matches for {query!r}. Try a broader term, or "
                f"master_builder_list_references to browse what's covered."
            )
        out = [f"{len(hits)} match(es) for {query!r}:", ""]
        for h in hits:
            loc = f"{h['source']}:{h['line']}"
            sect = f" — *{h['section']}*" if h["section"] else ""
            out.append(f"- `{loc}`{sect}\n  {h['text']}")
        return "\n".join(out)

    raise KeyError(f"Unknown tool {name!r}. Available: {', '.join(t['name'] for t in TOOLS)}.")


# --------------------------------------------------------------------------------------
# Resources (same corpus, for clients that prefer resources over tools)
# --------------------------------------------------------------------------------------

def list_resources() -> list[dict[str, str]]:
    out = [{
        "uri": f"{URI_SCHEME}://protocol",
        "name": "Master Builder Protocol",
        "description": "The core reasoning method for built-environment work.",
        "mimeType": "text/markdown",
    }]
    for r in reference_index():
        out.append({
            "uri": f"{URI_SCHEME}://reference/{r['name']}",
            "name": r["name"],
            "description": r["description"],
            "mimeType": "text/markdown",
        })
    return out


def read_resource(uri: str) -> str:
    if uri == f"{URI_SCHEME}://protocol":
        return protocol_text()
    prefix = f"{URI_SCHEME}://reference/"
    if uri.startswith(prefix):
        return read_reference(uri[len(prefix):])
    raise KeyError(f"Unknown resource URI {uri!r}.")


# --------------------------------------------------------------------------------------
# JSON-RPC plumbing
# --------------------------------------------------------------------------------------

def _result(req_id: Any, result: Any) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": req_id, "result": result}


def _error(req_id: Any, code: int, message: str) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}}


def handle(msg: dict[str, Any]) -> dict[str, Any] | None:
    """Handle one JSON-RPC message. Returns a response, or None for notifications."""
    method = msg.get("method")
    req_id = msg.get("id")
    params = msg.get("params") or {}
    is_notification = "id" not in msg

    if not isinstance(method, str):
        return None if is_notification else _error(req_id, JSONRPC_INVALID_REQUEST, "Missing method.")

    # Notifications never get a response.
    if is_notification:
        return None

    if method == "initialize":
        asked = params.get("protocolVersion")
        negotiated = asked if asked in SUPPORTED_PROTOCOL_VERSIONS else LATEST_PROTOCOL_VERSION
        return _result(req_id, {
            "protocolVersion": negotiated,
            "capabilities": {"tools": {}, "resources": {}},
            "serverInfo": {
                "name": SERVER_NAME,
                "title": "Master Builder",
                "version": version(),
            },
            "instructions": (
                "Master Builder reasons about real-estate development, construction, and the built "
                "environment as one whole project. For any such question, call "
                "master_builder_get_protocol first, then load only the reference the task needs via "
                "master_builder_read_reference (or master_builder_search for a narrow lookup). "
                "Always ground the answer in a specific place — codes and permits are local; physics "
                "and money are universal."
            ),
        })

    if method == "ping":
        return _result(req_id, {})

    if method == "tools/list":
        return _result(req_id, {"tools": TOOLS})

    if method == "tools/call":
        name = params.get("name")
        args = params.get("arguments") or {}
        if not isinstance(name, str):
            return _error(req_id, JSONRPC_INVALID_PARAMS, "tools/call requires a string 'name'.")
        if not isinstance(args, dict):
            return _error(req_id, JSONRPC_INVALID_PARAMS, "tools/call 'arguments' must be an object.")
        try:
            text = call_tool(name, args)
            return _result(req_id, {"content": [{"type": "text", "text": text}], "isError": False})
        except (KeyError, ValueError, OSError) as exc:
            # Tool-level failure: report in the result so the agent can recover.
            return _result(req_id, {
                "content": [{"type": "text", "text": f"Error: {exc}"}],
                "isError": True,
            })

    if method == "resources/list":
        return _result(req_id, {"resources": list_resources()})

    if method == "resources/read":
        uri = params.get("uri")
        if not isinstance(uri, str):
            return _error(req_id, JSONRPC_INVALID_PARAMS, "resources/read requires a string 'uri'.")
        try:
            return _result(req_id, {"contents": [
                {"uri": uri, "mimeType": "text/markdown", "text": read_resource(uri)}
            ]})
        except (KeyError, OSError) as exc:
            return _error(req_id, JSONRPC_INVALID_PARAMS, str(exc))

    if method in ("prompts/list", "resources/templates/list"):
        key = "prompts" if method.startswith("prompts") else "resourceTemplates"
        return _result(req_id, {key: []})

    return _error(req_id, JSONRPC_METHOD_NOT_FOUND, f"Method not found: {method}")


def serve() -> int:
    log(f"v{version()} ready | root={ROOT} | refs={len(reference_names())}")
    for raw in sys.stdin:
        raw = raw.strip()
        if not raw:
            continue
        try:
            msg = json.loads(raw)
        except json.JSONDecodeError as exc:
            sys.stdout.write(json.dumps(_error(None, JSONRPC_PARSE_ERROR, f"Parse error: {exc}")) + "\n")
            sys.stdout.flush()
            continue
        try:
            response = handle(msg) if isinstance(msg, dict) else _error(
                None, JSONRPC_INVALID_REQUEST, "Batch requests are not supported."
            )
        except Exception as exc:  # never die on one bad message
            log(f"internal error: {exc!r}")
            response = _error(msg.get("id") if isinstance(msg, dict) else None,
                              JSONRPC_INTERNAL_ERROR, "Internal server error.")
        if response is not None:
            # json.dumps escapes newlines, so a message is always exactly one line.
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
    return 0


# --------------------------------------------------------------------------------------
# Self-test — exercises the server the way a client would
# --------------------------------------------------------------------------------------

def selftest() -> int:
    failures: list[str] = []

    def check(label: str, cond: bool, detail: str = "") -> None:
        if cond:
            print(f"  ok   {label}")
        else:
            print(f"  FAIL {label} {detail}")
            failures.append(label)

    print(f"Master Builder MCP server self-test (root={ROOT})")

    init = handle({"jsonrpc": "2.0", "id": 1, "method": "initialize",
                   "params": {"protocolVersion": "2025-06-18"}})
    check("initialize echoes supported protocol version",
          init["result"]["protocolVersion"] == "2025-06-18")
    check("initialize advertises tools + resources",
          {"tools", "resources"} <= set(init["result"]["capabilities"]))
    check("serverInfo carries name and version",
          init["result"]["serverInfo"]["name"] == SERVER_NAME
          and init["result"]["serverInfo"]["version"] != "0.0.0")

    unknown = handle({"jsonrpc": "2.0", "id": 2, "method": "initialize",
                      "params": {"protocolVersion": "1999-01-01"}})
    check("unsupported version negotiates down to latest supported",
          unknown["result"]["protocolVersion"] == LATEST_PROTOCOL_VERSION)

    check("notifications get no response",
          handle({"jsonrpc": "2.0", "method": "notifications/initialized"}) is None)

    tools = handle({"jsonrpc": "2.0", "id": 3, "method": "tools/list"})["result"]["tools"]
    check("tools/list returns all 5 tools", len(tools) == 5, f"got {len(tools)}")
    check("every tool is annotated read-only",
          all(t["annotations"]["readOnlyHint"] and not t["annotations"]["destructiveHint"] for t in tools))
    check("every tool has a schema and a description",
          all(t.get("inputSchema") and len(t.get("description", "")) > 40 for t in tools))

    proto = handle({"jsonrpc": "2.0", "id": 4, "method": "tools/call",
                    "params": {"name": "master_builder_get_protocol", "arguments": {}}})["result"]
    check("get_protocol returns the protocol body",
          not proto["isError"] and "Master Builder Protocol" in proto["content"][0]["text"])
    check("get_protocol strips the YAML frontmatter",
          not proto["content"][0]["text"].lstrip().startswith("---"))

    refs = reference_index()
    check("reference index is non-empty and described",
          len(refs) >= 8 and all(r["description"] for r in refs), f"got {len(refs)}")

    read = handle({"jsonrpc": "2.0", "id": 5, "method": "tools/call",
                   "params": {"name": "master_builder_read_reference",
                              "arguments": {"name": "real-estate-finance.md"}}})["result"]
    check("read_reference returns real content",
          not read["isError"] and "yield-on-cost" in read["content"][0]["text"].lower())

    bare = handle({"jsonrpc": "2.0", "id": 6, "method": "tools/call",
                   "params": {"name": "master_builder_read_reference",
                              "arguments": {"name": "global-codes"}}})["result"]
    check("read_reference tolerates a missing .md suffix", not bare["isError"])

    eviltest = handle({"jsonrpc": "2.0", "id": 7, "method": "tools/call",
                       "params": {"name": "master_builder_read_reference",
                                  "arguments": {"name": "../../../etc/passwd"}}})["result"]
    check("path traversal is rejected", eviltest["isError"])

    srch = handle({"jsonrpc": "2.0", "id": 8, "method": "tools/call",
                   "params": {"name": "master_builder_search",
                              "arguments": {"query": "interest reserve", "limit": 5}}})["result"]
    check("search finds a known term",
          not srch["isError"] and "real-estate-finance.md" in srch["content"][0]["text"])

    empty = handle({"jsonrpc": "2.0", "id": 9, "method": "tools/call",
                    "params": {"name": "master_builder_search",
                               "arguments": {"query": "zzzznotpresentzzz"}}})["result"]
    check("empty search returns guidance, not an error", not empty["isError"])

    loc = handle({"jsonrpc": "2.0", "id": 16, "method": "tools/call",
                  "params": {"name": "master_builder_localize",
                             "arguments": {"place": "Hanoi, Vietnam"}}})["result"]
    loc_text = loc["content"][0]["text"]
    check("localize names the place and serves the six resolutions",
          not loc["isError"] and "Hanoi, Vietnam" in loc_text
          and "R1" in loc_text and "R6" in loc_text)
    check("localize refuses to invent local values",
          "to verify" in loc_text.lower() and "never invent" in loc_text.lower())
    check("localize requires a place", handle({"jsonrpc": "2.0", "id": 17, "method": "tools/call",
          "params": {"name": "master_builder_localize", "arguments": {}}})["result"]["isError"])

    badtool = handle({"jsonrpc": "2.0", "id": 10, "method": "tools/call",
                      "params": {"name": "nope", "arguments": {}}})["result"]
    check("unknown tool reports isError with available tools",
          badtool["isError"] and "master_builder_get_protocol" in badtool["content"][0]["text"])

    check("unknown method returns -32601",
          handle({"jsonrpc": "2.0", "id": 11, "method": "bogus/method"})["error"]["code"]
          == JSONRPC_METHOD_NOT_FOUND)

    res = handle({"jsonrpc": "2.0", "id": 12, "method": "resources/list"})["result"]["resources"]
    check("resources/list mirrors the corpus", len(res) == len(refs) + 1)
    rr = handle({"jsonrpc": "2.0", "id": 13, "method": "resources/read",
                 "params": {"uri": f"{URI_SCHEME}://reference/global-codes.md"}})["result"]
    check("resources/read returns markdown", "Authority Having Jurisdiction" in rr["contents"][0]["text"])

    check("ping works", handle({"jsonrpc": "2.0", "id": 14, "method": "ping"})["result"] == {})

    # Every emitted message must be exactly one line (stdio framing requirement).
    check("responses contain no embedded newlines",
          "\n" not in json.dumps(handle({"jsonrpc": "2.0", "id": 15, "method": "tools/call",
                                         "params": {"name": "master_builder_get_protocol",
                                                    "arguments": {}}})))

    print()
    if failures:
        print(f"FAILED: {len(failures)} check(s): {', '.join(failures)}")
        return 1
    print("All checks passed.")
    return 0


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    if "--version" in sys.argv:
        print(version())
        return 0
    try:
        return serve()
    except KeyboardInterrupt:
        return 0
    except BrokenPipeError:
        return 0


if __name__ == "__main__":
    sys.exit(main())
