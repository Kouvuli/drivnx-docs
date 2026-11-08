# Review notes — DrivnX Phase 1 Development Direction (v3)

*Reviewed document:* `archive/Trison_Phase1_Team_Review_v3.pdf`, dated 20 October 2026, 21 pages (Markdown copy: [DrivnX_Phase1_Development_Direction.md](DrivnX_Phase1_Development_Direction.md))
*Review date:* 21 October 2026

Page numbers refer to the PDF. Quotes are copied exactly from the document.

**Overall:** it's a strong, well-organised draft. The scope boundary, the four-state trust model, the restraint in the security claims and the first vertical slice are all sound. The findings below are gaps and internal contradictions, not problems with the direction.

---

## Gaps and contradictions to fix before sign-off

All findings below were resolved on 30–31 October 2026; each one notes what changed.

### 1. The product name is still a placeholder

> **Resolved 30 October 2026:** the product and company are named **Conflux**; Trison Labs is the team. Renamed **DrivnX** on 7 November 2026. The Markdown copy uses the name; the archived PDF still shows the placeholder.

| Where | Evidence |
|---|---|
| Page 1, title block | "Trison Labs Product Name" |
| PDF properties (Title field) | "Trison Labs Product Name — Phase 1 Development Direction (Team Review)" |

**Suggested fix:** fill in the product name before the document goes out for sign-off.

---

### 2. There is no rule for content a user writes from scratch

> **Resolved 31 October 2026:** Added `New → Confirmed | User (manual entry)` to §12 and a sentence to the §3 hard rule.

The trust-state rules only let content reach **Confirmed** from **Inferred**. A user who writes a description themselves, with no AI or heuristic suggestion, has no valid path.

| Where | Evidence |
|---|---|
| Page 18, §12 "Trust-state rules" | The only route into Confirmed: "Inferred → Confirmed \| User (Accept or Edit) \| Allowed; recorded as a ProvenanceEvent" |
| Page 18, §12 | The only other "New →" rules: "New → Observed \| Profiling engine" and "New → Inferred \| Heuristic or AI" |
| Page 5, §3 trust model | Confirmed is "Created by: A person", which implies a person can author it directly |
| Page 10, §8 screens | Dictionary Review: "Review and edit descriptions and definitions" |
| Page 8, §6 AI modes | "No AI \| The full deterministic product remains usable." With AI off and no heuristic description, there is nothing Inferred to confirm. |

**Why it matters:** in "No AI" mode, the only way to build a dictionary is manual entry, and the domain layer as specified would reject it.

**Suggested fix:** add `New → Confirmed | User (manual entry) | Allowed; recorded as a ProvenanceEvent`.

---

### 3. The trust states have no way back

> **Resolved 31 October 2026:** §12 now covers edits (state unchanged, new revision), user demotion (Confirmed → Inferred, Defined → Confirmed), Reject/Defer (stay Inferred, leave the inbox; Deferred returns) and a "needs re-review" flag when a newer profile run contradicts the evidence.

Every rule moves forward. Nothing covers edits to confirmed items, demotion, what a rejected item becomes, or confirmed knowledge going stale.

| Where | Evidence |
|---|---|
| Page 18, §12 | The transition table lists only forward moves (New → Observed / Inferred, Inferred → Confirmed, Confirmed → Defined). |
| Page 18, §12 | "Reject / Defer \| User \| Review outcome kept in provenance (Proposed: not a separate trust state)". It doesn't say which state the item is left in. |
| Page 5, §3 | Dictionary and Contract are "Editable, versioned", but no rule says what an edit does to the state. |
| Page 12, §9 | "Let users correct CSV parsing in place, then re-profile", plus "History = previous profile runs" (Foundry row). Re-profiling is expected, so a new run can contradict a fact that was already Confirmed. |

**Suggested fix:** add rules for:
- Confirmed or Defined → edited (does it stay Confirmed, with a new ProvenanceEvent?);
- user demotion;
- where Rejected and Deferred items end up (kept as Inferred, or hidden);
- Confirmed items whose evidence changed in a newer profile run (a "needs re-review" flag).

---

### 4. Figure 1 decides two questions that are still open

> **Resolved 31 October 2026:** Figure 1, its text description and the §4 component table now say "SQLite + artifact files — ADR pending" and that Parquet means cached profile results, never copied source data.

**4a. Workspace storage is shown as already decided.**

| Where | Evidence |
|---|---|
| Page 6, Figure 1 | "Local Workspace Store (SQLite + project files)" |
| Page 6, §4 component table | "SQLite + project files for state" |
| Page 15, §11 open decisions | "Workspace storage \| SQLite only vs SQLite + artifact files" |
| Page 19, §12 "Decisions to close before Sprint 1" | "Workspace storage \| SQLite only vs SQLite + artifact files — shapes M1 persistence" |

**4b. Figure 1 shows source data copied into the workspace.**

| Where | Evidence |
|---|---|
| Page 6, Figure 1 (Local Workspace Store box) | "Stores project configuration, artifact metadata, and local files (SQLite, JSON, Parquet, etc.)." |
| Page 7, §5 | "files are referenced in place (never silently copied)" |
| Page 10, §7 threat model | "raw data not copied by default" |

**Suggested fix:** in Figure 1, label the store "SQLite (+ artifact files — ADR pending)" and remove "Parquet / local files" from it. Alternatively, explain that Parquet means cached profile results, not copied source data. The component table on page 6 needs the same change.

---

### 5. Figure 1's legend includes SLAs, which aren't in the Phase 1 contract

> **Resolved 31 October 2026:** "SLAs" removed from the Figure 1 legend and its text description.

| Where | Evidence |
|---|---|
| Page 6, Figure 1 legend (Defined) | "e.g., data contract (rules, constraints, SLAs)" |
| Page 5, §3 | Data Contract contains "Required, type, unique, accepted values, range, identifier, relationship rules" |
| Page 17, §12 | ContractRule: "Rule type (required, type, unique, accepted values, range, identifier, relationship), state" |

**Suggested fix:** remove "SLAs" from the legend. In ODCS terms they belong to a later phase, alongside validation and monitoring.

---

### 6. Sensitive-data detection is described as both closed and open

> **Resolved 31 October 2026:** Decided: rule-based, in M3. Removed from the §11 open decisions and added to the M3 deliverables.

| Where | Evidence |
|---|---|
| Page 12, §9 Databricks row | "Make sensitive-field detection rule-based (names/patterns), not AI \| Phase 1 (M3); closes an open ADR" |
| Page 16, §11 open decisions | "Sensitive-data detection \| Minimal in Phase 1 vs later (proposal: rule-based, not AI)" |
| Page 14, §10 milestones | The M3 deliverables, "Deterministic metrics, sampling, findings, profile UI", don't mention sensitive-field detection. |

**Suggested fix:** pick one. Either record it as decided (rule-based, M3), remove it from the §11 list and add it to M3, or reword §9 to say "proposed".

---

### 7. The contract-fields fix hasn't been carried through

> **Resolved 31 October 2026:** Purpose and limitations added to the §3 Contract row; new `Contract` entity in §12 owns many `ContractRule`s.

| Where | Evidence |
|---|---|
| Page 16, §11 inconsistencies | "Contract fields \| Some drafts also list dataset purpose and limitations in the Phase 1 subset. \| Include purpose and limitations as descriptive fields." |
| Page 5, §3 | The Data Contract "Contains" list has no purpose or limitations. |
| Page 17, §12 | ContractRule holds only rule type and state. "limitations" appears on **DictionaryEntry** instead. |

**Suggested fix:** if the resolution is accepted, add purpose and limitations to the §3 Contract row. Also add a contract-level entity (e.g. `Contract` with purpose and limitations, owning many `ContractRule`s) to the §12 domain model. Today there is no entity that holds contract-level fields at all.

---

### 8. Telemetry is off, but the key success measures need usage data

> **Resolved 31 October 2026:** §11 now states the method: moderated user sessions plus an opt-in local "review stats" export (counts only, no content).

| Where | Evidence |
|---|---|
| Page 9, §7 | "telemetry off by default" |
| Page 19, §12 | "redact credentials, connection strings, tokens and raw rows; telemetry off by default" |
| Page 14, §10 spike 4 | "What share of suggestions is accepted unchanged, edited, or rejected?" |
| Page 15, §11 | "AI descriptions save effort \| Accepted-unchanged / edited / rejected rates" |

**Why it matters:** the accept/edit/reject rates are already recorded locally in ProvenanceEvents, but nothing in the plan gets them back to the team.

**Suggested fix:** state the method. Options include moderated user sessions, or a local "review stats" export (counts only, no content) that the user chooses to share.

---

### 9. The AI spikes are scheduled before AI exists

> **Resolved 31 October 2026:** Spike 5 runs early on a clickable mock-up; spike 4 runs just before M8; the AI provider choice is due before M8.

| Where | Evidence |
|---|---|
| Page 14, §10 | Heading "Technical spikes to run early", including spike 4 "AI documentation" and spike 5 "AI privacy" |
| Page 14, §10 | AI arrives in milestone 8: "M8 AI enablement \| Provider abstraction, structured outputs, external provider, context preview…" |
| Page 15, §11 | "External AI provider and local model \| To be selected" |
| Page 19–20, §12 | "Decisions to close before Sprint 1" lists packaging, storage and contract schema, but not the AI provider. |

**Suggested fix:** either move spikes 4–5 to just before M8, or add the AI provider choice to the decisions needed early so the spikes can actually run early. Spike 5 (whether users understand the preview) could be run on a clickable mock-up with no provider at all.

---

### 10. The session token's delivery and scope aren't defined

> **Resolved 31 October 2026:** The token is required on every `/api/*` call except `/api/session` (§7, §12), token delivery is part of the workspace-packaging ADR, and a test is added to the first-commit list.

| Where | Evidence |
|---|---|
| Page 9, §7 | "per-launch session token · protect state-changing endpoints" |
| Page 19, §12 API outline | "/api/session \| Per-launch session token handshake" |
| Page 19, §12 | "All state-changing endpoints require the session token." |
| Page 17, §12 first slice | "Start the local runtime → browser opens", with no mention of how the browser gets the token |
| Page 19, §12 | Read endpoints return data: "/api/sources \| Connect, test, discover, preview" and "/api/profile-runs \| … results" |

**Why it matters:**
- **Delivery:** the launcher has to pass the token to the browser somehow, and that choice depends on the packaging ADR.
- **Scope:** read endpoints (previews, profile results, dictionary) return the user's data. As written, only Host/Origin checks protect them. The token is required only on state-changing calls.

**Suggested fix:** fold token delivery into the workspace-packaging ADR. Consider requiring the token on every `/api/*` call except `/api/session`. Add a test for it in the "Security that must be in the first commit" list (page 19).

---

## Minor points

| # | Point | Evidence |
|---|---|---|
| M1 | The ODCS version needs checking against the current standard. | Page 16: "Direction doc targets ODCS 3.2; reference doc links ODCS 3.0.1. \| Target 3.2 subset; confirm." Resolved: ODCS 3.2.0 (September 2026) is current; §11 confirms a 3.2 subset. |
| M2 | Figure 2 describes Soda as "monitoring", which is out of scope for Phase 1. | Page 11, Figure 2: Soda "Data quality checks and monitoring". Page 3: "Continuous monitoring" listed under Not in Phase 1. Resolved: Figure 2 and its description now say "Data quality checks". |
| M3 | Figure 2 leaves out Databricks and Foundry, though they get a full table in §9. | Page 12–13: "Lessons from enterprise platforms: Databricks and Palantir Foundry" (10 rows). Neither appears in Figure 2 (page 11). Resolved: the Figure 2 caption points to the Databricks and Foundry table. |
| M4 | Layout: Section 12's line in the contents table spills onto page 2 by itself. | Page 2 contains only "12 Engineering kickoff …". Resolved: `DrivnX_Phase1_Development_Direction.pdf` is regenerated from the Markdown (19 pages, no orphaned lines). |
| M5 | Layout: the last row of "Decisions to close before Sprint 1" sits alone on page 20. | Page 20 contains only the "Contract internal schema" row. Resolved: `DrivnX_Phase1_Development_Direction.pdf` is regenerated from the Markdown (19 pages, no orphaned lines). |
