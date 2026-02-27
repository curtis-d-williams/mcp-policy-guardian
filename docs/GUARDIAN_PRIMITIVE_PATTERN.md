# Guardian Primitive Pattern (Deterministic Governance MCP)

Status: Architectural Pattern  
Scope: Applies to deterministic, governance-grade MCP servers  
Audience: Maintainers building minimal, contract-frozen primitives  

---

## 1. Definition

A **Guardian Primitive** is a deterministic, network-free, read-only MCP tool designed to enforce a narrow governance invariant.

It is intentionally:

- Minimal in scope
- Non-interpretive
- Schema-stable
- Fail-closed
- Version-frozen

A Guardian Primitive is **not** a compliance engine, scoring system, linting framework, or advisory tool.

It is a governance building block.

---

## 2. Core Properties

### 2.1 Determinism (Mandatory)

For identical input state, output must be identical.

This includes:

- Stable JSON keys
- Stable ordering
- Stable identifier values
- Stable detail strings
- No timestamps
- No randomness
- No environment-dependent messages

Determinism is not optional.

---

### 2.2 Fail-Closed Semantics (Mandatory)

Invalid input or invariant violation must result in:

- ok = false
- fail_closed = true

A Guardian Primitive never degrades silently.

It does not guess.
It does not infer.
It does not partially succeed in ambiguous states.

---

### 2.3 Network-Free & Read-Only (Default)

Guardian Primitives:

- Make no network calls
- Do not mutate filesystem state
- Do not execute untrusted code
- Do not depend on external APIs

Any deviation from this must be explicitly declared in a future contract.

---

### 2.4 Presence / Structural Validation Only (Default)

Guardian Primitives validate:

- Presence
- Structure
- Explicit invariants

They do not validate:

- Semantic meaning
- Policy quality
- Intent
- Best-practice alignment
- Organizational maturity

Interpretation is out of scope.

---

## 3. Contract Discipline

Each Guardian Primitive MUST include:

- `docs/V1_CONTRACT.md`
- Canonical example outputs
- Explicit Non-Goals section
- Frozen check identifiers
- Frozen output schema
- Explicit backward compatibility rules

Once tagged (v0.1.0):

- Tool name is frozen
- Tool signature is frozen
- Output schema is frozen
- Check IDs are frozen
- Check ordering is frozen

Any breaking change requires a major version increment.

---

## 4. Non-Goals (Pattern-Level)

Guardian Primitives do NOT:

- Score repositories
- Rank maturity
- Provide remediation advice
- Infer intent
- Interpret policy meaning
- Aggregate risk
- Use heuristics
- Expand scope without contract revision

They enforce invariants.
Nothing more.

---

## 5. Versioning Discipline

v0.1.0 freeze indicates:

- Contract stable
- Schema stable
- Determinism guaranteed
- No hidden heuristics

Minor versions may:

- Improve internal implementation
- Fix bugs
- Improve documentation

Minor versions may NOT:

- Change schema
- Add checks
- Modify check identifiers
- Reinterpret output meaning

Major version required for any contract change.

---

## 6. Composition Rules (Future-Oriented)

Guardian Primitives may be composed by an orchestrator.

Composition must:

- Preserve determinism
- Preserve original outputs unmodified
- Avoid reinterpretation
- Avoid scoring
- Avoid inference

The orchestrator aggregates.
It does not reinterpret.

Composition is allowed.
Mutation is not.

---

## 7. Architectural Philosophy

A Guardian Primitive embodies:

- Constraint over feature expansion
- Explicit boundaries over implicit capability
- Freeze discipline over iteration sprawl
- Governance-first design

It is easier to build a complex tool.
It is harder to build a minimal one and stop.

Stopping is the discipline.

---

## 8. Current Implementations

This pattern is instantiated in:

- mcp-release-guardian
- mcp-policy-guardian

These serve as reference implementations of the pattern.

---

End of Pattern Document.