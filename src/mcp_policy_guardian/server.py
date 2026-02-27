from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

from fastmcp import FastMCP


mcp = FastMCP("mcp-policy-guardian")


@dataclass(frozen=True)
class CheckResult:
    check_id: str
    ok: bool
    details: str


def _abs_repo_path(repo_path: str) -> Path:
    p = Path(repo_path).expanduser()
    try:
        return p.resolve()
    except Exception:
        return p


def _exists(repo: Path, rel: str) -> bool:
    return (repo / rel).exists()


@mcp.tool()
def check_repo_policy(repo_path: str) -> Dict[str, Any]:
    """
    Deterministic check for standard repository governance artifacts.
    Network-free, read-only, fail-closed.

    Stable keys: tool, repo_path, ok, checks, fail_closed
    """
    repo = _abs_repo_path(repo_path)

    required = [
        ("has_license", "LICENSE"),
        ("has_readme", "README.md"),
        ("has_security_policy", "SECURITY.md"),
        ("has_contributing", "CONTRIBUTING.md"),
        ("has_codeowners", ".github/CODEOWNERS"),
    ]

    checks: List[CheckResult] = []

    if not repo.exists() or not repo.is_dir():
        checks = [
            CheckResult(check_id=cid, ok=False, details=f"Repo path invalid or not a directory: {repo}")
            for cid, _ in required
        ]
        ok = False
        fail_closed = True
    else:
        for cid, rel in required:
            present = _exists(repo, rel)
            checks.append(
                CheckResult(
                    check_id=cid,
                    ok=present,
                    details=f"Found {rel}" if present else f"Not found: {rel}",
                )
            )
        ok = all(c.ok for c in checks)
        fail_closed = (not ok)

    return {
        "tool": "check_repo_policy",
        "repo_path": str(repo),
        "ok": ok,
        "checks": [{"check_id": c.check_id, "ok": c.ok, "details": c.details} for c in checks],
        "fail_closed": fail_closed,
    }


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
