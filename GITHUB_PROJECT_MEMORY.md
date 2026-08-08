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

The ecosystem anchor remains `Kopano-Labs/Introduction-to-MCP`. Website implementation authority for KopanoLabs.com is `RobynAwesome/Kopano-Labs-Website` unless the user explicitly changes that boundary.

---

## Human authority

The user's current explicit instruction governs task intent. Repository evidence governs implementation truth. When the two conflict, surface the conflict instead of silently inventing continuity.
