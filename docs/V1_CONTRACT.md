# mcp-policy-guardian — V1 Contract (Frozen)

Status: V1 frozen (effective at tag v0.1.0)

This document defines the V1 contract for the mcp-policy-guardian MCP server.
V1 is intentionally narrow: it is a deterministic, network-free, read-only governance primitive for presence-only repository policy artifacts.

---

## 1. Tool Surface (V1)

V1 exposes exactly one tool:

check_repo_policy(repo_path: string) -> object

No other tools are part of V1.

---

## 2. V1 Scope (Hard Boundary)

### 2.1 What V1 does

check_repo_policy(repo_path) checks presence only of the following paths:

1. LICENSE
2. README.md
3. SECURITY.md
4. CONTRIBUTING.md
5. .github/CODEOWNERS

It returns a deterministic JSON object containing:

- tool name
- repo_path (echoed input)
- ok (boolean)
- checks (array)
- fail_closed (boolean)

### 2.2 What V1 does NOT do (Non-Goals)

V1 does not perform:

- semantic validation of file contents
- policy quality checks
- linting of content or structure
- SPDX/license-type detection
- scoring, grading, or maturity models
- recommendations or remediation guidance
- heuristics or inference
- GitHub API calls
- network access of any kind
- branch protection checks

If a capability is not explicitly listed in “What V1 does,” it is out of scope.

---

## 3. Determinism and Fail-Closed Semantics

### 3.1 Determinism Requirements

For identical filesystem state at repo_path, output must be identical:

- stable keys and types
- stable ordering of checks
- stable check_id values
- stable details strings
- no timestamps
- no randomness
- no environment-dependent text

### 3.2 Network-Free and Read-Only

The tool must:

- make no network calls
- not modify repository files
- not write to disk
- not execute repository code

### 3.3 Fail-Closed Definition

If repo_path is invalid, unreadable, or not a directory:

- ok MUST be false
- fail_closed MUST be true
- every check MUST have ok: false
- details MUST be "fail-closed: repo_path_invalid"

If the repository is readable:

- each check is true if and only if the file exists
- ok = logical AND of all checks
- fail_closed = not ok

---

## 4. Output Schema (V1)

Top-level JSON object MUST contain exactly:

- tool (string) — always "check_repo_policy"
- repo_path (string)
- ok (boolean)
- checks (array)
- fail_closed (boolean)

No additional top-level keys are allowed in V1.

Each checks item MUST contain exactly:

- check_id (string)
- ok (boolean)
- details (string)

### 4.1 Check Ordering (Frozen)

The checks array MUST appear in this exact order:

1. license_present
2. readme_present
3. security_present
4. contributing_present
5. codeowners_present

### 4.2 Canonical Check IDs (Frozen)

- license_present
- readme_present
- security_present
- contributing_present
- codeowners_present

---

## 5. Backward Compatibility Rule

After tag v0.1.0:

- No changes to tool name or signature
- No new tools
- No changes to top-level keys
- No reordering of checks
- No changes to check_id values
- No new required files
- No semantic validation added under existing checks

Any violation of these rules requires a new major version (V2) and a new contract document.

---

## 6. Canonical Examples

Canonical outputs are defined in docs/EXAMPLE_OUTPUTS.md and are part of the V1 contract.