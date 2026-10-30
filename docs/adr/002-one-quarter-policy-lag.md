# Architecture Decision Record (ADR) 002: the gap responds to the previous policy rate

**Status:** Accepted · 2026-09-10; updated for the realistic model, 2026-10-24.

## Context

The **policy rate**, the interest rate the central bank sets, affects demand
with a delay. Using the submitted policy rate for the newly displayed gap
would remove that lesson, even if the app still ran.

## Decision

Compute the new gap from the **previous** quarter's policy rate. Store the
submitted choice on the new quarter; it acts on the following quarter.
Financial stress also uses the move between the two preceding quarters, so a
move above 0.50 points has a second delayed effect. Round the gap before
computing core inflation and unemployment.

The test `test_new_quarter_uses_the_previous_rate` catches a current-choice
implementation. The data model specifies the stress and shock order as well.

## Consequences

**Good.** The delay is visible without claiming that every price reading must
rise first. At two decisions of 2.50, inflation goes **4.29 → 3.57 → 3.51**,
while core goes **3.10 → 3.48 → 3.57**. Unemployment goes
**4.22 → 4.47 → 4.54**. Fading food and energy prices can lower inflation before
the new policy rate acts.

**Surprising.** First-quarter gap and prices are independent of the submitted
policy rate, but the score can already differ because it charges for the move.
If both player and Taylor choose 2.50 first, both score **2.248**.

**Costly if wrong.** Both delayed effects must survive every phase. The prompt,
data model and tests state the order explicitly.
