# mcp-policy-guardian — Canonical Example Outputs (V1)

These examples are canonical for V1.
They support determinism testing and consumer integration.

Notes:
- repo_path is echoed exactly as provided.
- checks ordering and check_id values are fixed by the V1 contract.

---

## Example 1 — Valid repo (all artifacts present)

Input:
- repo_path: /repos/example-valid

Output:
```json
{
  "tool": "check_repo_policy",
  "repo_path": "/repos/example-valid",
  "ok": true,
  "checks": [
    { "check_id": "license_present", "ok": true, "details": "present: LICENSE" },
    { "check_id": "readme_present", "ok": true, "details": "present: README.md" },
    { "check_id": "security_present", "ok": true, "details": "present: SECURITY.md" },
    { "check_id": "contributing_present", "ok": true, "details": "present: CONTRIBUTING.md" },
    { "check_id": "codeowners_present", "ok": true, "details": "present: .github/CODEOWNERS" }
  ],
  "fail_closed": false
}
```

---

## Example 2 — Readable repo but missing one artifact (CODEOWNERS missing)

Input:
- repo_path: /repos/example-missing-codeowners

Output:
```json
{
  "tool": "check_repo_policy",
  "repo_path": "/repos/example-missing-codeowners",
  "ok": false,
  "checks": [
    { "check_id": "license_present", "ok": true, "details": "present: LICENSE" },
    { "check_id": "readme_present", "ok": true, "details": "present: README.md" },
    { "check_id": "security_present", "ok": true, "details": "present: SECURITY.md" },
    { "check_id": "contributing_present", "ok": true, "details": "present: CONTRIBUTING.md" },
    { "check_id": "codeowners_present", "ok": false, "details": "missing: .github/CODEOWNERS" }
  ],
  "fail_closed": true
}
```

---

## Example 3 — Invalid repo path (fail-closed)

Input:
- repo_path: /repos/does-not-exist

Output:
```json
{
  "tool": "check_repo_policy",
  "repo_path": "/repos/does-not-exist",
  "ok": false,
  "checks": [
    { "check_id": "license_present", "ok": false, "details": "fail-closed: repo_path_invalid" },
    { "check_id": "readme_present", "ok": false, "details": "fail-closed: repo_path_invalid" },
    { "check_id": "security_present", "ok": false, "details": "fail-closed: repo_path_invalid" },
    { "check_id": "contributing_present", "ok": false, "details": "fail-closed: repo_path_invalid" },
    { "check_id": "codeowners_present", "ok": false, "details": "fail-closed: repo_path_invalid" }
  ],
  "fail_closed": true
}
```