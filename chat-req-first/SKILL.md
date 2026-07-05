---
name: chat-req-first
description: "Chat-based requirements exploration workflow. Use when building UI/UX features, designing new pages, or implementing any user-facing change where requirements are ambiguous or could be interpreted multiple ways. Triggers: user asks to build/create/design/implement something without full specs; user shares a rough idea or wireframe; user says I want X but details are unclear; multiple design approaches exist; any task where confirming requirements before coding would prevent rework. Anti-trigger: simple, well-defined tasks with clear specs."
---

# Chat-Req-First: Confirm Before You Build

Before writing any code, explore requirements through structured chat. Never jump into implementation with ambiguous requirements.

## Core Principle

**Every ambiguous request gets a confirmation round.** The cost of a 2-minute chat is far lower than 2 hours of rework.

## Workflow

### Step 1: Parse the Request

Identify what the user wants and flag ambiguities:
- Missing dimensions (sizes, counts, breakpoints)
- Unstated interaction patterns (what happens after X?)
- Ambiguous terminology (what does "like iOS" mean exactly?)
- Multiple valid interpretations

### Step 2: Structure Your Confirmation

Organize your understanding into a clear confirmation message:

```
**Requirement Confirmation**

1. [Category A]: [Your understanding]
2. [Category B]: [Your understanding]
3. [Category C]: [Your understanding]

**Details to confirm:**
1. [Specific question about ambiguity A]
2. [Specific question about ambiguity B]
```

Rules for confirmation messages:
- **Rephrase, don't parrot** — show you understood the intent, not just the words
- **Number everything** — makes it easy for the user to point to specific items
- **Ask max 3 clarification questions** — don't overwhelm; batch the rest for later
- **Offer concrete options** when possible: "A) full-width B) 80% width C) card-based?"
- **Reference real examples** when the user uses metaphors: "like iOS 26" → describe what that means technically

### Step 3: Iterate Until Green

- User corrects → update understanding and re-confirm
- User confirms → proceed to implementation
- User adds new requirements → fold in and re-confirm affected parts only

### Step 4: Build with Confidence

Only after explicit confirmation:
1. Record confirmed requirements in a brief spec (can be in-chat, no separate doc needed)
2. Build
3. Reference the confirmed spec when user questions design choices

## Confirmation Templates

### For UI/UX Tasks

```
**UI Layout Confirmation**

- **Layout**: [Your understanding of structure]
- **Components**: [What elements exist]
- **Interaction**: [How user flows through it]
- **Responsive**: [Breakpoint behavior]
- **Animation**: [Motion/transition details]

**To confirm:**
1. [Layout question]
2. [Interaction question]
3. [Responsive question]
```

### For Feature Requests

```
**Feature Scope Confirmation**

- **Core behavior**: [What it does]
- **Edge cases**: [What happens at boundaries]
- **Integration**: [How it connects to existing system]
- **Priority**: [Must-have vs nice-to-have]

**To confirm:**
1. [Behavior question]
2. [Edge case question]
3. [Scope question]
```

## Anti-Patterns to Avoid

- **Don't build then ask** — "Here's what I made, is this right?" wastes time
- **Don't ask 10 questions at once** — overwhelm kills the conversation
- **Don't assume defaults silently** — if you're guessing, you should be asking
- **Don't confirm the obvious** — if something is standard and unambiguous, just do it
- **Don't re-confirm what was just confirmed** — track what's settled

## When to Skip Confirmation

Skip this workflow when:
- The task is a simple bug fix with clear reproduction steps
- The user provided detailed, unambiguous specs
- The change is trivial (typo, color tweak, one-line fix)
- You're following an established pattern the user has already approved
