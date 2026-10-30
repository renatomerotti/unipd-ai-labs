# Troubleshooting — questions to ask yourself

## ⏯️ Start or stop the app

In VS Code's **terminal** (**Terminal → New Terminal**), the same on Mac and Windows:

| To | ⌨️ Type this in the terminal |
|---|---|
| Start the app, or find its address | `uv run start.py` |
| Stop the app | `uv run stop.py` |
| Stop an app you started with `uv run app.py` | Press **Ctrl+C** in its terminal (on a Mac too: the Control key) |

---

Not a manual. A list of things to **check** when something is wrong.

Most problems in this lab are not difficult. They are one unticked box, one
wrong folder, or one thing that was never actually run. Work down the list and
answer honestly — the point is to find what you skipped, and everybody skips
something.

Each question has a short code so that your instructor can say *"check F2"*
instead of explaining it twenty-five times.

---

## Start here — six questions that fix most of it

**S1 · Did you save the file?**
Look at the tab in VS Code. A **dot** instead of an **×** means unsaved. Press
Ctrl+S / Cmd+S. Nothing you have not saved exists as far as the tests are
concerned.

**S2 · Are you in the right folder in the terminal?**
Run `pwd` — the same on Mac and Windows. It must end in `unipd-ai-lab`. If it
does not, every command you ran went somewhere else.

**S3 · Did you read the test line yourself, or only the assistant's summary?**
In the assistant's tab, find `$ uv run pytest -q` and read the number printed
under it. An assistant saying "all tests pass" is a claim; that line is the
result.

**S4 · Is the app already running?**
Does `uv run start.py` print its address? It reuses a running lab app.
Do you need to stop one started by `start.py`? Use `uv run stop.py`. For a
foreground run with `uv run app.py`, press **Ctrl+C** in its terminal.

**S5 · Have you restarted VS Code since you changed a setting?**
Settings do not apply to windows and terminals that are already open. Close VS
Code completely and open it again.

**S6 · Is there a blue `Restricted Mode` bar at the top of VS Code?**
Then every extension is switched off, including the assistant — whatever the
sidebar shows you. Click **Manage** in that bar, then **Yes, I trust the
authors**. This is `SETUP.md` Step 6, and it produces no error of its own: the
assistant simply is not there.

---

## The assistant

**A1 · Is its panel blank, with nothing in its terminal?**
This failure produces no error message
at all. Check the setting from `SETUP.md` Step 5: press **Ctrl+Shift+P** /
**Cmd+Shift+P**, type `settings json`, and choose **Preferences: Open User
Settings (JSON)**. This line must be there:

```json
"python.terminal.activateEnvironment": false,
```

If it is missing, add it — mind the comma between entries — then save and
restart VS Code — see **S5**. The Python extension, which VS Code offers the
first time you open a `.py` file, switches this **on** unless the line is
already there.

**Line present and the panel is still blank?** A setting saved for the folder
rather than for you can override it. Search the settings for **activate
environment**, and look at the **Workspace** tab as well as **User**.

**A2 · Did you pick a model, and is it a free one?**
Open the assistant's settings and look at the model name. If nothing is
selected, or the model is not marked free, it will fail or quietly cost money.

**A3 · Is it refusing everything, or showing no models?**
Training stays off (`SETUP.md` Step 2), so only providers that do not train will
accept your requests. Try another free model from the list. If none answers,
tell your instructor — do not turn training back on.

**A4 · Did you paste the key with a space at the end?**
That is the usual cause of "invalid key". Delete the key on OpenRouter, make a
new one, and paste it carefully.

**A5 · Has it now failed the same step twice?**
Stop. Do not reword the prompt and send it again — that is the same request
wearing a hat, and it costs another slice of your daily allowance. Read the
relevant part of `specs/central-bank-game/`, work out what was ambiguous, and say what
you actually want. Once.

**A6 · Is it answering, but very slowly?**
Nothing is broken. Free models are shared with everyone. Wait, or switch to
another free model — that does not consume extra allowance.

**A7 · Is it repeating the same sentence over and over?**
It is stuck in a loop and will not stop by itself. Click in the **opencode**
tab and press **Esc** twice. Then switch to the second free model —
`SETUP.md`, *If you run out*, has the steps — and send the prompt there.

---

## The folder, and what the assistant can see

**F1 · Did you open `unipd-ai-lab`, or a folder above it?**
Look at the sidebar. The folder at the top should be `unipd-ai-lab`, showing
`docs`, `specs`,
`templates`, `tests`, `later-tests`, `start.py`, `stop.py`, `pyproject.toml`, `README.md`,
`.gitignore` — and the files you have built. **If you can see anything from the
rest of your life, you opened the wrong folder.** Close it and open
`unipd-ai-lab`. See [`privacy.md`](privacy.md).

**F2 · Are `specs/` and `docs/` actually in the sidebar?**
If the assistant invents phases, describes a different project, or says
`python app.py` instead of `uv run start.py`, it is not reading your files — it is
guessing. Check you opened `unipd-ai-lab` itself and not the folder above it.

**F3 · Did you rename `gitignore-template` to `.gitignore`?**
The leading dot matters, and your computer may be hiding it. On Mac press
**Cmd+Shift+.** to show hidden files.

---

## Running the application

**R1 · Does it say `Address already in use`?**
Did you use `uv run start.py`? It reuses a running lab app or tries a backup
port. The usual port is 8001; the backups are 8002 and 8003. If all are busy,
what does `server.log` say? See **S4** before stopping your own app.

**R2 · Are you opening the right address?**
Is it the address `start.py` printed, as in Row 15, followed by the page
path (such as `/economy`)? The usual port is 8001, but it may be 8002 or 8003.

**R3 · Did the terminal print an error when you started it?**
Read the **last** line, not the first. Then copy the whole error to the
assistant and send: `This is the error. Fix it.`

**R4 · Does the browser say `This site can't be reached`?**
In VS Code's terminal, does `uv run start.py` print an address? Open that
address. If it reports a problem, what is the last error in `server.log`?

---

## The tests

**T1 · Does it say `ModuleNotFoundError` or `no module named app`?**
You are probably not in the `unipd-ai-lab` folder — see **S2** — or
`pyproject.toml` was moved or renamed. It must be called exactly
`pyproject.toml` and sit beside `app.py`.

**T2 · Is the number lower than you expected?**
Expected: `3` after Phase 1, `7` after Phase 2, `13` after Phase 3, `18` after
Phase 4. A lower number means a test file is missing, not that tests failed.
The tests are ready-made, and each phase's prompt asks the assistant to move
its file from `later-tests/` into `tests/`. If it did not, send `Move
later-tests/test_phase_N.py into tests/.` with your phase's number. Never ask
the assistant to write them.

If instead it says `1 error during collection`, with `No module named 'models'`
or `cannot import name`, you copied the file in before the phase was built.
That is expected: send the step's prompt.

**T3 · Is `test_new_quarter_uses_the_previous_rate` the one failing?**
**Read this rather than fixing it quickly.** That test exists to catch one
specific mistake: calculating the new quarter from the policy rate you just submitted
instead of the policy rate on the *previous* quarter. If it fails, the policy lag has
been implemented backwards — and the application would still have run, and still
have looked right. That test failing is the lab working.

**T4 · Did tests that passed yesterday start failing?**
Something you changed since. Check **S1**, then run `uv run pytest -q` and read
which one fails — the name usually says what broke.

---

## Your daily allowance

**Q1 · Have you run out of requests?**
The error reads `Rate limit exceeded: free-models-per-day`. Ignore its offer to
add credits: the lab never needs money. It resets daily, and it belongs to your OpenRouter **account**, not to a model —
another free model on OpenRouter does not give you a fresh allowance. Follow the fallback order: DeepSeek V4.1 Flash Free (OpenCode) → North Mini Code (free) on OpenRouter → GLM-5.3-Flash Free (OpenCode) → the instructor, and carry on with the same step — `SETUP.md`, *If you run out*, has the
steps and the second choice. Still stuck: tell the instructor.

**Q2 · Are you spending requests on things you could do yourself?**
Editing two numbers, saving a file, running the tests and reading an error cost
nothing. Ask the assistant for work, not for keystrokes.

---

## Still stuck

**X1 · Is your project broken beyond repair?**
**Ask for a checkpoint.** There is a working copy of the project at the end of
each phase, and the instructor has them. Copy the **contents** of the one you
are given into your `unipd-ai-lab` folder, replacing what is there — not the
folder itself, which would leave you with `unipd-ai-lab/phase-1-complete/`. Then
look in `tests/`: drag any test for a **later** phase back into `later-tests/` —
`test_phase_3.py`, say, after a Phase 2 checkpoint — or it fails for code you
have not built yet. Then carry on from the next phase. You will have learned less than the person beside
you, and you will finish. Take that trade rather than losing a session.

**X2 · Is everything broken and you do not know why?**
**Ask for the rebuild prompt.** It rebuilds the project from `specs/` with an
assistant that has never seen your earlier work — which is also the argument in
[`methodology.md`](methodology.md) that written specifications outlive a lost
conversation.

**X3 · Have you been stuck for more than five minutes?**
**Say so.** Losing the session matters more than losing the step, and every
problem on this page has been seen before.
