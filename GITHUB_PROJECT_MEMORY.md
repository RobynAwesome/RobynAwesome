# GitHub Project Memory Registry

## Purpose

This file is the durable memory index for GitHub work across the Kholofelo/Robyn and Kopano Labs ecosystem.

The operating rule is simple:

> **For every GitHub project, start with the memory registry, then read the target repository's current state before acting.**

The registry preserves **persistency, consistency, and context** without allowing old context to overwrite current repository truth.

---

## Memory Protocol

For every GitHub task:

1. Read this registry first.
2. Identify the project entry.
3. Load the project's canonical memory anchor(s).
4. Inspect the target repository's current README, architecture, governance, relevant source files, recent commits/PRs, and current branch state.
5. Separate:
   - ecosystem context;
   - project-local facts;
   - current-task instructions.
6. Treat current repository evidence as authoritative over remembered state.
7. Never claim implementation, deployment, validation, or POC status without a current receipt.
8. Update this registry when a project's role, canonical anchor, or validated relationship changes.

### Context hierarchy

```text
GitHub Project Memory Registry
  -> Ecosystem / canonical anchor
       -> Target repository current state
            -> Branch / PR / commit receipts
                 -> User instruction right now
```

### Cross-project carry rule

Carry across projects only what is explicitly shared:

- vocabulary;
- governance invariants;
- ecosystem relationships;
- validated architecture patterns;
- user-declared relationships between projects.

Do **not** blindly carry:

- implementation status;
- deployment status;
- dependencies;
- branches;
- test results;
- runtime claims;
- roadmap completion;
- secrets or environment state.

---

# Project 001 — Kopano-Labs/Introduction-to-MCP

**Role:** First canonical GitHub memory anchor / ecosystem context root  
**Repository:** `Kopano-Labs/Introduction-to-MCP`  
**Default branch:** `master`  
**Memory priority:** HIGH  
**Established in registry:** 2026-08-08

## What this repository currently proves from its README

The repository identifies **Kopano Context** as:

- a full-stack multi-agent orchestration and South African impact ecosystem;
- an official reference implementation for the Model Context Protocol (MCP);
- an ecosystem containing Kopano Context, Kopano Studio, Kopano Labs, KasiLink Bridge, Microsoft readiness, and Kopano SafeSkill;
- a system with persistent data logging and long-term associative memory;
- an architecture with local-first / sovereign-governance orientation;
- a codebase organized around `kopano-core/`, a Next.js Studio interface, KasiLink integration, and a Schematics/Obsidian governance vault.

These are **ecosystem context anchors**. They must not be treated as proof that every other repository implements the same stack or has the same validation state.

## Canonical use

Before working on another GitHub project, consult this repository when the task depends on:

- Kopano Context terminology;
- MCP architecture;
- multi-agent orchestration;
- Kopano Labs ecosystem relationships;
- SafeSkill / trust-layer framing;
- persistent memory / context architecture;
- offline-first or sovereign infrastructure principles;
- relationships between Kopano Context, Studio, Labs, KasiLink, and other ecosystem components.

Then verify the target repository independently.

## FOC / POC boundary

- **FOC:** claim, plan, mock, screenshot, narrative, or architectural intention not yet validated in the target repository/runtime.
- **POC:** project-appropriate evidence such as executable code, tests, deployment behavior, receipts, or verified runtime output.

Do not promote FOC to POC through repetition or memory.

---

# Project 002 — RobynAwesome/Kopano-Labs-Website

**Role:** Dedicated public website source for KopanoLabs.com  
**Repository:** `RobynAwesome/Kopano-Labs-Website`  
**Default branch:** `main`  
**Memory priority:** HIGH  
**Established in registry:** 2026-08-08

## Canonical boundaries

- This is the canonical GitHub repository for future **KopanoLabs.com website implementation**.
- `Kopano-Labs/Introduction-to-MCP` remains the ecosystem architecture, Schematics, Studio lineage, and source-authority donor.
- `RobynAwesome/Money-managing-app` is unrelated to KopanoLabs.com production and must never be repurposed as website source.
- `RobynAwesome/cars4mars-landingpage` is retired and must not be treated as a production dependency.

## What this repository currently proves

- a dedicated Vite + React + TypeScript website codebase now exists;
- the public information architecture includes Labs, Systems, Cars4Mars, and Proof/lineage surfaces;
- public indexing metadata (`robots.txt`, `sitemap.xml`) and `release.json` are versioned with the source;
- the repository carries its own production-gate workflow;
- source lineage back to `Kopano-Labs/Introduction-to-MCP` is documented explicitly.

## Validation boundary

Repository implementation does **not** by itself prove that `https://KopanoLabs.com` is serving this source. Production parity must be validated independently against the live domain and deployment receipt.

---

# Project 003 — RobynAwesome/Project-Jennifer

**Role:** Governed intelligence runtime, tactical RPG/world system, and portable Project Jennifer skill library  
**Repository:** `RobynAwesome/Project-Jennifer`  
**Default branch:** `main`  
**Memory priority:** HIGH  
**Established in registry:** 2026-08-12

## Canonical memory anchors

Read these in this order when Project Jennifer skills or architecture are relevant:

```text
skills.md
→ skills/project-jennifer/SKILL.md
→ selected specialist SKILL.md
→ current implementation/source named by that skill
→ governance/source-authority-registry.json
→ current branch / PR / CI / runtime receipts
```

Additional project anchors include:

- `README.md` — public project/world entry point and current proof boundaries;
- `AGENTS.md` — stateless-renter first-load/routing instructions;
- `skills/README.md` — portable skill package index;
- `skills/distribution/` — stateless-renter/provider distribution contracts;
- `packages/conceptual/` — CEEP, CCP, POC-vs-FOC, framework registry, and conceptual receipts;
- `packages/memory/` — GSMB / Digital Hippocampus and Memory Receipt Engine;
- `packages/governance/`, `packages/authority/`, and `packages/validation/` — governance/authority/validation runtime surfaces;
- `docs/lore/project-wify-jennifer/` — Genesis / Convergence / True One lore and system intent;
- `assets/Project-Waifu-Forge/` and related lore — current relational engineering / visual-source lane.

## Skill discovery rule

For Project Jennifer, **do not start by dumping the whole repository into context**.

Start with `skills.md` and the `project-jennifer` umbrella skill, then select the smallest relevant specialist capability.

Current portable skill catalog includes:

```text
project-jennifer
cdp-conceptual-divergence
ceep-conceptual-evaluation
poc-foc-evaluation
ccp-conceptual-convergence
ncmp-concept-intake
cag-communication-attention
rag-governed-retrieval
jennifer-stateless-renter
forge-rivm
authored-relational-attention
```

This routing surface lets stateless renters and compatible skill hosts use Project Jennifer workflows without acquiring landlord authority over memory, canon, source privacy, or user intent.

## Conceptual-suite proof boundary

```text
CDP — Conceptual Divergence Protocol
     asks: what could this become?
     state: specified + portable workflow
     dedicated packages/conceptual/src/cdp module: NOT currently proven

CEEP — Conceptual Evaluation Engine
       state: portable workflow + coded TypeScript engine
       implementation: packages/conceptual/src/ceep/

POC-vs-FOC
       state: portable workflow + coded TypeScript evaluator
       implementation: packages/conceptual/src/pocvsfoc/

CCP — Conceptual Convergence Protocol
     asks: what consistently survives evaluation/evidence?
     state: portable workflow + coded TypeScript implementation
     implementation: packages/conceptual/src/ccp/

NCMP — New Concept MMAO Protocol
      state: portable workflow + coded storage-agnostic/in-memory registry
      authority: agents may propose; human architect recognition is mandatory
```

Do not flatten those proof states simply because each is exposed through `SKILL.md`.

The conceptual reasoning spine is:

```text
CDP
→ CEEP
→ POC-vs-FOC evidence boundary
→ CCP
→ canonical/evolution receipt
→ NCMP when genuine agent-originated novelty requires recognition + registration
```

## Source and authority boundary

Project Jennifer's skill catalog does not supersede its source-authority law.

Semantic relevance does not imply:

- authority;
- privacy eligibility;
- canon status;
- implementation;
- validation;
- proof.

Private, public-derivative, executable-protocol, project-canon, historical, research, and visual source classes must remain distinct according to the current repository registry and task lane.

## Project namespace boundary

Keep these current Project Jennifer namespaces distinct unless a later repository receipt explicitly changes them:

```text
Project Waifu Forge
= current/tested relational engineering, asset governance, Constructs and receipts

Project Wify Jennifer
= Genesis / world-lore / Convergence namespace
```

Do not treat one as a silent rename of the other.

## Validation boundary

A `SKILL.md` file proves a portable workflow contract exists. It does not by itself prove:

- dedicated engine/runtime wiring;
- exact-provider support;
- production persistence;
- deployment;
- runtime success;
- canonical promotion.

Inspect current target source and validation receipts before making those claims.

The model/renter is never the sovereign source of truth. The current human instruction governs task intent; repository evidence governs implementation truth; receipts govern proof.

---

## Future project entries

Add every GitHub project as it becomes relevant. Each entry should contain:

```text
Project number
Repository
Role
Default branch
Canonical memory anchor(s)
What the repository currently proves
What must remain project-specific
Known relationships to other projects
Current validation boundary
Last verified date / receipt
```

The ecosystem anchor remains `Kopano-Labs/Introduction-to-MCP`. Website implementation authority for KopanoLabs.com is `RobynAwesome/Kopano-Labs-Website` unless the user explicitly changes that boundary. Project Jennifer skill discovery begins at `RobynAwesome/Project-Jennifer/skills.md`, but current Project Jennifer repository evidence remains authoritative over the catalog.

---

## Human authority

The user's current explicit instruction governs task intent. Repository evidence governs implementation truth. When the two conflict, surface the conflict instead of silently inventing continuity.
