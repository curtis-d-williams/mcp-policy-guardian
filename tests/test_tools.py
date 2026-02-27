from __future__ import annotations

from pathlib import Path

from mcp_policy_guardian.server import check_repo_policy


def test_check_repo_policy_fail_closed_on_missing_repo(tmp_path: Path) -> None:
    missing = tmp_path / "does_not_exist"
    out = check_repo_policy(str(missing))
    assert out["tool"] == "check_repo_policy"
    assert out["ok"] is False
    assert out["fail_closed"] is True
    assert len(out["checks"]) == 5


def test_check_repo_policy_pass(tmp_path: Path) -> None:
    (tmp_path / "LICENSE").write_text("x")
    (tmp_path / "README.md").write_text("x")
    (tmp_path / "SECURITY.md").write_text("x")
    (tmp_path / "CONTRIBUTING.md").write_text("x")
    (tmp_path / ".github").mkdir()
    (tmp_path / ".github" / "CODEOWNERS").write_text("* @owner")

    out = check_repo_policy(str(tmp_path))
    assert out["ok"] is True
    assert out["fail_closed"] is False
    assert all(c["ok"] for c in out["checks"])
