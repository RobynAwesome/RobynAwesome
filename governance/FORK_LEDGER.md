# Fork Ledger

**Owner:** RobynAwesome  
**Scope:** Forked repositories only  
**Baseline audit:** 2026-08-08  
**Objects governed:** 36 repositories  
**Purpose:** Preserve why each fork exists, where it came from, how far it has mutated, what may consume it, and when it should graduate or be retired.

## Governance invariant

A fork is **not** an owned product merely because it exists under `RobynAwesome`.

Every fork must have an explicit state:

- `RADAR` — ecosystem reconnaissance; do not import as architecture by default.
- `LEARNING` — curriculum, workshop, exercise, or skills acquisition.
- `REFERENCE` — architecture or implementation worth studying; no production dependency without validation.
- `CASE-STUDY` — external implementation used to validate or challenge a governance/system hypothesis.
- `EXPERIMENT` — actively mutated sandbox that has not graduated into an owned system.
- `PRODUCTIZED` — fork lineage remains, but the repository now carries an owned product/runtime responsibility.
- `ARCHIVED` — retained only as historical evidence; no active dependency.

## Lineage rules

1. **Upstream is provenance, not authority.** Upstream code can inform a decision but cannot silently become a Kopano Labs invariant.
2. **State changes require a receipt.** `REFERENCE -> EXPERIMENT`, `EXPERIMENT -> PRODUCTIZED`, and any repurpose must be documented in commit history or this ledger.
3. **Unknown provenance is a defect, not a guess.** `VERIFY-UPSTREAM` means the exact parent repository still needs to be resolved from GitHub fork metadata.
4. **Productized forks must declare semantic debt.** If the repository name or inherited lineage no longer describes its function, that debt must remain visible until migration or deliberate acceptance.
5. **External claims require local validation.** Benchmarks, security claims, architecture claims, model capabilities, and protocol guarantees remain untrusted until reproduced or bounded locally.
6. **Archive means no silent resurrection.** An archived fork returns to active use only through an explicit state transition.

## Ledger

| Repository | State | Source / provenance | Purpose | Local mutation | Consumer / relevance | Validation gate | Archive / graduation condition |
|---|---|---|---|---|---|---|---|
| `Top-AI-repos` | RADAR | `ishandutta2007/Top-AI-repos` | Broad AI/ML ecosystem reconnaissance | Upstream-oriented | Model/tool discovery | Verify any selected project independently before adoption | Archive if superseded by a better maintained radar source |
| `open-antigravity` | REFERENCE | `VERIFY-UPSTREAM` | Agent-first, model-agnostic IDE/gateway architecture | No owned product state recorded | MMAO/orchestration design reference | Separate implemented behavior from roadmap/vision before reuse | Graduate only if a bounded component is implemented and tested locally |
| `gstack` | REFERENCE | `garrytan/gstack` | AI software-factory roles, review, QA, security and release workflows | Upstream-oriented | Agent workflow design | Reproduce workflow value on an owned repository before standardizing | Archive if methodology stops being used or upstream is abandoned |
| `Project-Ideas-And-Resources` | LEARNING | `VERIFY-UPSTREAM` | Project ideas, user stories and teaching exercises | None recorded | KINTech/community curriculum | Validate external links and modernize stacks before teaching | Archive when no longer used as curriculum source |
| `model-mondays` | LEARNING | `microsoft/model-mondays` | Model selection, Foundry, agents, evaluation and AI curriculum | Upstream-oriented | Model IQ / teaching / platform radar | Recheck dated platform guidance before implementation | Archive by season when content is no longer current |
| `simplenote-mcp` | REFERENCE | `Automattic/simplenote-mcp` | MCP-accessible note memory with read-first/write-opt-in behavior | None recorded | MCP memory/connector design | Validate auth, write boundaries and Windows behavior locally | Graduate only if integrated behind explicit permissions |
| `three.js` | REFERENCE | `mrdoob/three.js` | WebGL/WebGPU 3D engine reference | Upstream tracking | 3D/visualization work | Prefer package dependency or pinned subtree over maintaining an unnecessary fork | Archive fork if no local engine changes are planned |
| `GitHub-Copilot-Dev-Workshop-18-04-2026` | LEARNING | `VERIFY-UPSTREAM` | Copilot CLI, MCP, custom agents and Agentic Workflows workshop | None recorded | Dev tooling curriculum | Preserve workshop receipts; do not treat examples as production defaults | Archive after learning outcomes are extracted |
| `scc26` | LEARNING | `CPUT-HPC-Club/scc26` | CPUT HPC Club 2026 cluster tasks | Course work / local execution possible | HPC capability development | Validate cluster results on actual assigned infrastructure | Graduate learnings into separate HPC notes/tools, not this training fork |
| `scc` | LEARNING | `chpc-tech-eval/scc` | CHPC Student Cluster Competition foundation material | Upstream-oriented | Linux/HPC systems foundation | Treat competition rules/timetables as date-bound | Archive as historical course evidence after current SCC cycle |
| `wp-docs-health-monitor` | CASE-STUDY | `VERIFY-UPSTREAM` | Evidence-backed documentation drift detection | None recorded | Validation/governance pattern | Reproduce scoring and false-positive behavior on an owned documentation corpus | Graduate pattern only after local benchmark and cost boundary |
| `create-block-theme` | REFERENCE | `WordPress/create-block-theme` | WordPress block-theme development tooling | None recorded | WordPress-specific work | Use only against a defined WordPress requirement and version | Archive fork if WordPress is outside active product scope |
| `devrel-demos` | REFERENCE | `GoogleCloudPlatform/devrel-demos` | Large Google Cloud examples/POC corpus | Upstream-oriented | Gemini, agents, Cloud Run, data, observability reference | Pull only bounded demos; validate service versions and costs | Archive fork if selective upstream retrieval replaces full fork |
| `forem` | REFERENCE | `forem/forem` | Community/social publishing platform architecture | Upstream-oriented | Community platform research | Do not make a KPGS dependency without security, scale and maintenance review | Archive local fork if no modifications are planned |
| `chessmates` | LEARNING | `VERIFY-UPSTREAM` | Flutter starter/project exploration | Minimal/unknown | Mobile learning | Establish an explicit objective before further mutation | Archive if no Flutter experiment is active at next audit |
| `azure-skills` | REFERENCE | `microsoft/azure-skills` | Skills + Azure MCP + Foundry MCP capability layering | Upstream-oriented | Orchestration, cloud governance and MCP architecture | Validate permissions, tool scope and cloud-cost boundaries before operational use | Graduate only as a bounded capability profile, never by blind import |
| `Deploy-a-RAG-application-with-vector-search-in-Firestore` | LEARNING | `VERIFY-UPSTREAM` | Text RAG, embeddings and Firestore vector search lab | None recorded | Retrieval/grounding curriculum | Re-run against current Gemini/Firestore APIs before reuse | Archive after extracting reusable retrieval patterns |
| `NIGHTPASS` | CASE-STUDY | `ODATANO/NIGHTPASS` | Governed disclosure, off-chain privacy and field-bound ZK attestations | Upstream-oriented | PKA/governance/privacy case study | Independently verify threat model, chain assumptions and proof semantics | Graduate concepts only after local formalization; never inherit compliance claims |
| `skilling-champion-extension` | ARCHIVED | `VERIFY-UPSTREAM`; upstream README states program discontinued | Historical Microsoft Skilling Champion extension | None relevant | Program history only | No active integration | Remain archived unless the program returns and requirements are revalidated |
| `Multimodal-Retrieval-Augmented-Generation-RAG-using-the-Vertex-AI-Gemini-API` | LEARNING | `VERIFY-UPSTREAM` | Multimodal document retrieval with text/images | None recorded | Multimodal grounding curriculum | Revalidate model/API names and benchmark retrieval quality | Archive after patterns are extracted into owned learning material |
| `pytorchTutorial` | LEARNING | `patrickloeber/pytorchTutorial` | PyTorch fundamentals and neural-network training curriculum | None recorded | ML foundations | Run exercises locally; update deprecated APIs when teaching | Archive when curriculum is superseded |
| `kiro-workshop` | CASE-STUDY | `VERIFY-UPSTREAM` | Spec-driven development, steering, hooks, skills, MCP and CLI agents | Workshop-oriented | Stateless-renter/toolchain case study | Separate Kiro-specific mechanics from generalizable governance patterns | Graduate only extracted protocols/patterns into owned repos |
| `python-engineer-notebooks` | LEARNING | `patrickloeber/python-engineer-notebooks` | Notebook reference collection | None recorded | Python/ML learning | Validate notebook dependencies before execution | Archive if unused after curriculum extraction |
| `Bookit-5s-Arena` | PRODUCTIZED | Fork lineage retained; exact parent `VERIFY-UPSTREAM` | Owned 5-a-side booking/product system | Significant local mutation; TypeScript evaluation and product features | FivesArena / owned product | CI, type checks, auth/payment validation, production smoke tests | Migrate to clean owned lineage only if fork provenance creates operational or legal confusion |
| `hackerrank-orchestrate-june26` | CASE-STUDY | `VERIFY-UPSTREAM` | Visual evidence adjudication: supported / contradicted / insufficient | Competition solution may mutate starter | PKA, evidence telemetry, model evaluation | No hardcoded labels; benchmark evidence quality and uncertainty handling | Graduate decision pattern into owned PKA tests; archive competition shell afterward |
| `Retro-older` | REFERENCE | `VERIFY-UPSTREAM` | Low-level custom OS/kernel/network/rendering reference | Local history unclear | Sovereign systems / real OS engineering | Boot/test in isolated VM; verify security/network claims before reuse | Keep as systems reference or graduate specific owned components |
| `evalbench` | REFERENCE | `GoogleCloudPlatform/evalbench` | Modular GenAI evaluation, scoring, experiments and reporting | Upstream-oriented | Validation infrastructure | Reproduce evaluator behavior on owned tasks; inspect judge/model bias | Graduate only the evaluation interfaces/metrics that pass local tests |
| `MLfromscratch` | LEARNING | `patrickloeber/MLfromscratch` | Classical ML algorithms implemented from first principles | None recorded | Mathematical/ML foundations | Run tests and verify derivations rather than trusting tutorial output | Archive when learning objectives are extracted |
| `Bindu` | CASE-STUDY | `getbindu/Bindu` | Agent identity, signed communication, A2A interoperability and payments | Upstream-oriented | Agent identity/governance/economic layer research | Validate cryptographic assumptions, protocol versions, trust boundaries and payment risk | Graduate concepts only after KPGS threat-model comparison |
| `Survey` | CASE-STUDY | `StackExchange/Survey` | Survey question bank, branching, schemas and longitudinal archive | Upstream-oriented | Forensic sociology / governed human-data collection | Validate methodology and privacy implications before adapting | Graduate schema/flow ideas into owned survey telemetry only with explicit purpose |
| `introduction-to-github` | LEARNING | `skills/introduction-to-github` | Git/GitHub fundamentals exercise | Exercise state | Beginner teaching | Preserve as teaching receipt; use current GitHub Skills instructions | Archive once replaced by owned lesson material |
| `snake-ai-pytorch` | LEARNING | `patrickloeber/snake-ai-pytorch` | Reinforcement-learning / Deep-Q-learning tutorial | None recorded | Game AI curriculum | Re-run training and measure convergence rather than assuming tutorial outcome | Archive when lesson has been converted into owned curriculum |
| `Money-managing-app` | PRODUCTIZED | Fork lineage retained; original upstream `VERIFY-UPSTREAM` | Repurposed 2026-08-07 into Kopano Labs + Cars4Mars production source | **REPURPOSED**; substantial identity and production mutation | Kopano Labs / Cars4Mars public surface | Production routes, owned assets, CI gates, deployment smoke tests, source-lineage receipts | Resolve semantic/provenance debt by rename/migration or explicitly accept it as permanent lineage |
| `workshop-build-with-gemini` | LEARNING | `patrickloeber/workshop-build-with-gemini` | Gemini prompting, multimodal, tools, Live API, MCP and model comparisons | Workshop-oriented | Gemini curriculum | Revalidate SDK/model versions before reuse | Archive by workshop version after extracting owned lessons |
| `lucebox` | REFERENCE | `Luce-Org/lucebox` | High-performance local LLM inference, CUDA/HIP and model-specific optimization | Fork tracks substantial upstream engineering; local intent is research | Sovereign/local inference research | Reproduce benchmarks on owned hardware; verify vendor/kernel constraints and licenses | Graduate only benchmarked components or integration patterns |
| `Awesome-AI-Code-Editor` | RADAR | `ishandutta2007/Awesome-AI-Code-Editor` | AI IDE/agent/CLI ecosystem radar | Upstream-oriented | Coding-agent market/tool discovery | Verify pricing, product status and capability claims at decision time | Archive when stale or superseded by a stronger tooling radar |

## Priority review queue

### P0 — identity / production lineage

- `Money-managing-app` — productized fork with semantic name/provenance debt.
- `Bookit-5s-Arena` — productized fork; exact upstream lineage should be resolved and recorded.

### P1 — high-value case studies

- `Bindu` — agent identity, signed communication, A2A and payments.
- `NIGHTPASS` — disclosure governance, private values and verifiable predicates.
- `hackerrank-orchestrate-june26` — evidence states including insufficient information.
- `wp-docs-health-monitor` — evidence-backed drift validation.
- `Survey` — governed question flow and longitudinal human-data structure.
- `kiro-workshop` — spec/steering/hooks/MCP/toolchain behavior.

### P2 — infrastructure / execution references

- `evalbench`
- `azure-skills`
- `gstack`
- `open-antigravity`
- `lucebox`
- `simplenote-mcp`

## Required metadata for future forks

Every new fork should add a ledger row containing:

```text
repository
state
upstream
fork_reason
local_mutation
consumer
validation_gate
archive_or_graduation_condition
last_audited
```

## State transition protocol

```text
RADAR ───────> REFERENCE ───────> EXPERIMENT ───────> PRODUCTIZED
   │               │                  │                    │
   ├──> LEARNING   ├──> CASE-STUDY    ├──> ARCHIVED       └──> ARCHIVED
   │               │                  │
   └──> ARCHIVED   └──> ARCHIVED      └──> REFERENCE
```

No transition is automatic. The commit, PR, issue, benchmark, deployment receipt, or explicit governance decision that caused the transition is the evidence.

---

**Ledger invariant:** `Fork -> Context -> Case -> Mutation -> Validation -> Graduation | Rejection | Archive`.
