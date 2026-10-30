# specs — what the assistant reads

Everything here describes the **Central Bank Game** feature. Project-level context is in
[`../docs/`](../docs/).

| Document | Answers | Read it |
|---|---|---|
| [central-bank-game/spec.md](central-bank-game/spec.md) | What must the finished application do? | Once, to understand the target |
| [central-bank-game/data-model.md](central-bank-game/data-model.md) | What are the numbers and the arithmetic? | Before Phase 2, and again before Phase 3 |
| [central-bank-game/plan.md](central-bank-game/plan.md) | How is it built, and in what order? | Once |
| [central-bank-game/tasks.md](central-bank-game/tasks.md) | What do I do next? | Every phase |
| [central-bank-game/validation.md](central-bank-game/validation.md) | How do I know it is done? | Every phase |
| [central-bank-game/clarifications.md](central-bank-game/clarifications.md) | What was ambiguous, and how was it settled? | When something seems underspecified |

## Source of truth

When two documents disagree, this is the order that wins:

```text
1. data-model.md    the arithmetic. Nothing overrides it.
2. spec.md          the behaviour contract.
3. tasks.md         the build order and the exact steps.
4. everything else  explanation. Never authoritative.
```

If you find a contradiction, **report it rather than picking one**. A
disagreement between documents is a defect in the specification, and silently
choosing a side hides it.

That is not a formality. Four review passes against this specification found
three contradictions of exactly this kind — see
[central-bank-game/clarifications.md](central-bank-game/clarifications.md).
