# Setup

Getting from a bare laptop to a project ready to build.

Work through it in order, and check each step before moving to the next. None of
it assumes prior experience — but read as you go rather than clicking through.
Several of these steps decide what the assistant can see for the rest of the
course, and one of them decides whether your data stays private.

The eleven steps below are **setup** steps, done once. The numbered files in
`prompts/` are the **lab** steps, and they start afterwards — lab Step *N*
builds Phase *N*, so those two numbers always agree. When you ask for help, say
which of the two you mean.

> **Nothing here requires you to know Python.** You will not install Python at
> all — **Step 9** installs a tool that fetches it for you when needed.

> **Read [`docs/privacy.md`](docs/privacy.md) before Step 1.** It is the lab's
> only security briefing — four rules — and the steps below do
> not repeat it.

---

## Do this first: start the VS Code download

VS Code is the largest download, so start it now and do the rest while it runs.

Go to **https://code.visualstudio.com** and click the download button. Leave it
downloading. Do not wait for it.

> **Already have VS Code?** Do not download it again — but do not write off
> **Steps 4 to 6** either. Installing is the only part you skip, and the parts
> you do not skip matter more for you than for anyone starting clean.

---

## Step 1 — Create an OpenRouter account

OpenRouter is a shop that sells access to many artificial intelligence (AI) models through one account.
You will use a free one.

1. Go to **https://openrouter.ai**
2. Click **Sign in**, and create an account. Use **whichever email address you
   prefer** — your own or your university one. Use a password you have **not**
   used anywhere else.
3. Confirm your email if asked.

**Check:** you can see your name or avatar in the top-right corner.

> Some mail systems delay or block confirmation messages. If nothing arrives
> within a couple of minutes, make the account again with a different address
> rather than waiting — you have ten steps to go.

---

## Step 2 — Turn off training on your prompts

Some free models are free because the provider trains on what you send. In this
lab, that is switched **off** for everyone.

1. Go to **https://openrouter.ai/settings/privacy**
2. Find **Allow free endpoints that train on request data**. Make sure it is
   the one that says **free** — there is a similar setting for paid models.
3. Turn it **off**.


**Check:** **Allow free endpoints that train on request data** is off.

> **If no free model works in Step 8, leave this switch off** and tell the
> instructor. Do not turn it back on to get past the problem.

---

## Step 3 — Create an application programming interface (API) key

An application programming interface (API) key is a long secret string that proves a request came from you (the way one program talks to another). It is a password, so Rule 3 of `docs/privacy.md` applies from the
moment you create it.

1. Go to **https://openrouter.ai/keys**
2. Click **Create key**.
3. Give it a name — `unipd-lab` is fine.
4. **Expiration:** choose **30 days**. The key stops working by itself after
   the course.
5. **Credit limit** and **Reset limit:** leave them exactly as they are. Ignore
   the dollar amount — free models cost nothing, and you are not spending money.
6. **Copy it now.** You cannot see it again after you close the dialog.
7. **Leave this browser tab open.** Do not paste the key into a file, a note or
   a message. You need it in Step 8, and the safest place for it until then is
   the page it is already on.

Lost it, or closed the tab? Make another one. Keys are free, and an unused key
is deleted in one click at **https://openrouter.ai/keys**. That is always better
than writing this one down.


**Check:** you have a string starting with `sk-or-`, still on screen in an open
tab.

---

## Step 4 — Install VS Code

Your download has finished by now.

* **Windows:** run the installer. Accept the defaults.
* **Mac:** open the downloaded file and drag **Visual Studio Code** into
  **Applications**.

Open it once, so it finishes setting itself up.

**VS Code now includes Copilot**, its own AI assistant. Two assistants in one
window confuse each other, so disable it: **Extensions** in the left bar — four
small squares — search `copilot`, **Disable**.

**Check:** VS Code opens and shows a welcome tab, and Copilot is disabled.

> **Already have VS Code?** Nothing to install — but **Steps 5 and 6 are still
> yours**. Disable any other AI extension you installed yourself, such as
> Cline, the same way.

---

## Step 5 — Turn off two settings

The first keeps the assistant working for the rest of the lab. The second is
about privacy.

> **Already had VS Code?** These hold whatever you set long ago, not the
> defaults. **Read** each value rather than assuming it.

### 1 — Python's terminal helper

VS Code tries to be helpful with Python and, later on, that help stops the
assistant from appearing at all. This one is set in writing, because on a fresh
VS Code the switch is not in the settings search yet — it arrives later, with
the Python extension VS Code offers you, and it arrives switched **on**.

1. Press **Ctrl+Shift+P** on Windows, **Cmd+Shift+P** on Mac.
2. Type `settings json` and choose **Preferences: Open User Settings (JSON)**.
3. Add this line just inside the opening `{`, then save with **Ctrl+S** /
   **Cmd+S**:

```json
"python.terminal.activateEnvironment": false,
```


**Check:** the line is in the file, the file is saved, and nothing in it is
underlined in red. VS Code may grey the line out as unknown — that is expected
until the Python extension arrives, and the setting is ready for it.

> **Already had VS Code?** If the line is already there, make sure it says
> `false`. If the file was empty, it should now read `{`, your line, `}`.

> **Why.** From Phase 1 onward your project contains a folder called `.venv`.
> If this setting is on, VS Code types a command into every new terminal it
> opens — including the one the assistant runs in. The assistant loses the race
> and its panel stays blank, with no error to tell you why. It looks exactly
> like the tool being broken, and it is not.

### 2 — Usage reporting

VS Code reports usage data: which commands you ran and which errors you hit. It
has no effect on what the assistant sends.

Close the settings JSON tab first — this one is a different screen.

1. Open **Settings** from the menu bar — Mac: **Code → Preferences →
   Settings** · Windows: **File → Preferences → Settings**.
2. In the search box at the top of that page — not in any popup — type
   `telemetry level`.
3. Set **Telemetry: Telemetry Level** to **off**.


**Check:** the dropdown reads `off`.

---

## Step 6 — Download the lab and open it

This is Rule 1 of `docs/privacy.md` in practice: the assistant reads the
folder you open, and the lab's `opencode.json` tells it never to look outside
it. Open the right one now, before there is an
assistant to read anything.

1. If VS Code has reopened a folder from some earlier work, close it:
   **File → Close Folder**. If you already had VS Code, that folder is your own
   work — this step is the one that matters most for you.
2. Download `unipd-ai-lab.zip` from
   **https://github.com/renatomerotti/unipd-ai-labs/releases/latest/download/unipd-ai-lab.zip**. Leave it in
   `Downloads` — you do not need to move it anywhere.
3. Unzip it where it is. **Mac:** double-click it. **Windows:** right-click it,
   choose **Extract All**, and accept the folder it offers. Double-clicking on
   Windows only *looks* inside the zip, and files copied out of that view arrive
   empty.
4. In VS Code: **File → Open Folder**, then `Downloads` → **`unipd-ai-lab`** →
   **Open**.
5. The folder opens in **Restricted Mode**, and a blue bar across the top says
   so. Click **Manage** in that bar, then **Yes, I trust the authors**. Do this
   now: Restricted Mode disables every extension, so the one Step 7 installs
   would load, show nothing, and give you no error to work from. VS Code does
   not ask you first — the bar is the only thing it shows you, and it is easy
   to read past.
6. In the sidebar, right-click **`README.md`** and choose **Open Preview**. It
   shows the file as a formatted page instead of raw text, and it is how you
   read every `.md` file in this course. A file you have already opened as
   text has a button for it at the top right of the editor, **Open as
   Preview** — its name shows when you hover over it. Shortcut: **⇧⌘V** on
   Mac, **Ctrl+Shift+V** on Windows.





That one folder is the whole project. Everything is at the top level — here in
the order VS Code lists them, folders first, so you can read it straight down
your sidebar:

```text
unipd-ai-lab/
├── docs/           what we are building, and why — written for you
├── later-tests/    phases 2, 3 and 4 — the assistant moves one in per phase
├── specs/          exactly how it must behave — written for the assistant
├── templates/      the page layout, the table's legend, the chart and the
│                   scoreboard, ready-made
├── tests/          test_phase_1.py — how Phase 1 gets checked
├── .gitignore      what never leaves your machine
├── opencode.json   the assistant's rules: stay in this folder, leave your app
│                   running. You will not edit it
├── pyproject.toml  what the project needs. You will not edit it
├── README.md       start here — what you are building, and what is asked of you
├── start.py        starts the app and prints its address — ready-made
└── stop.py         stops the app started by start.py — ready-made
```

There is no application here yet — you build that. What is here is the brief for
it, and the split is the point: `docs/` is written for you, `specs/` is written
for the assistant. `docs/README.md` lists every document beside the question it
answers, and `docs/methodology.md` explains why a project starts with these files
rather than with code — which is also the answer to *what do I do when I start
one of my own from nothing*.

**Check:** the folder `unipd-ai-lab` is at the top of the sidebar, with the eleven
items above under it and no application code. **If you can see anything you
recognise from the rest of your life, you have opened the wrong folder.** Close
it and open
`unipd-ai-lab`. The blue **Restricted Mode** bar is gone — if it is still
there, step 5 has not been done, and nothing you install will run.

---

## Step 7 — Install the OpenCode extension

This is what puts an AI assistant inside your editor.

1. In VS Code, click the **Extensions** icon in the left bar — four small
   squares.
2. Search for **opencode**.
3. Several extensions have similar names, and two are published by **SST**.
   Pick **opencode** — the one that says *opencode for VS Code* underneath, not
   *OpenCode Beta* — then click **Install**.


**Check:** with any file open — `README.md` will do — a square **OpenCode**
icon appears at the top right of the editor. It does not appear in the left bar.


---

## Step 8 — Connect the backup, then choose DeepSeek

Connect OpenRouter now so the backup is ready if the first model reaches a limit.

1. Click the square **OpenCode** icon at the top right of the editor. A tab
   named **opencode** opens. If a **What's new** screen opens, press **ok**.
2. Type `/connect` and press **Enter**.
3. Type `openrouter` — the whole word. Check **OpenRouter** is highlighted,
   then press **Enter**.
4. Paste the application programming interface (API) key from **Step 3** and press **Enter**.
5. Type `/models` and press **Enter**.
6. Under **OpenCode**, choose **DeepSeek V4.1 Flash Free** and press **Enter**.
   If a **Select variant** list opens, choose **Default** and press **Enter**.

**Check:** the bottom line reads `DeepSeek V4.1 Flash Free OpenCode`.
OpenRouter stays connected for **North Mini Code (free)**, the second model.
DeepSeek itself needs no account and no key. If it cannot answer, follow the
fallback order under **Your daily allowance**, below.

---

## Step 9 — Install uv

`uv` runs Python programs. It fetches Python itself, so you never install
Python separately, and it needs no administrator rights.

1. In VS Code's menu bar, click **Terminal → New Terminal**. A panel opens at
   the bottom of the VS Code window. **Use only this terminal** — never the
   separate Terminal app on your computer, which starts in the wrong folder.
2. Look at the line you type on. It must end in `unipd-ai-lab %` (Windows:
   `unipd-ai-lab>`). If it does not, you are not in VS Code's terminal: go back
   to step 1.
3. Paste the line for your operating system, and press **Enter**.

**Mac:**

```bash
curl -LsSf https://astral.sh/uv/0.13.1/install.sh | sh
```

**Windows:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.13.1/install.ps1 | iex"
```

Then type `exit`, press **Enter**, and **open a new terminal exactly as in step
1**, so it notices the new tool.

**Check:**

```bash
uv --version
```

It should print a version number, in a terminal whose line still ends in
`unipd-ai-lab`. Every command from here on runs in this folder. If it says
*command not found*, see Troubleshooting below.

---

## Step 10 — Ask the assistant one question

The last check. In OpenCode, send exactly this:

```text
Introduce yourself in one sentence: which model are you, and who made you?
```

**Check:** any answer shows that the selected model can reply. Compare what it says with the model name on the line at the bottom of the
tab: **if they differ, the bottom line is right** — a model cannot reliably
tell which model it is. One step left. That reply also used
requests from your daily allowance — which is worth understanding, and is
explained below.

---

## Step 11 — Prove the assistant can read your project

The last setup step. The assistant is about to build your project from the files
Step 6 gave you; before it changes anything, prove that it can read them.

1. Check that the folder at the top of the VS Code sidebar is `unipd-ai-lab`. If
   it is not, open that folder again as in **Step 6**.
2. In the **opencode** tab, paste this prompt and press **Enter**. It shows as
   **[Pasted ~6 lines]** — that is normal.

```text
Read docs/prd.md, docs/tech-stack.md and specs/central-bank-game/tasks.md.

Do not write any code yet. Reply with:
1. In one sentence, what the application lets its user do.
2. The five phase names, in order.
3. The command used to run the application.
```

**Check:** its three answers match these. The wording can differ; the content
cannot.

| Question | The right answer |
|---|---|
| What the application lets you do | Act as the central bank, setting the policy rate to bring inflation down to its target |
| The five phases | 1 The application runs · 2 The economy you inherited · 3 Set a policy rate, and meet the lag · 4 Chart, score, and your opponent · 5 Beat the rule |
| The run command | `uv run start.py` |

A list that does not match these five phases, a different project, or
`python app.py` means the answer does not match the files. Do step 1 again,
then send the prompt once more.

---

## Setup is done. Here is how the numbering works from here

Two sets of numbers, and only two. You have just finished the first set.

| | Where | Numbers |
|---|---|---|
| **Setup steps** | this file | 1 to 11 — done once, today |
| **Lab steps** | `prompts/` | 1 to 5 — the lab itself |

**Each lab step builds the phase with the same number.**

```text
prompts/01-the-app-runs.md         Step 1  builds  Phase 1
prompts/02-the-economy.md          Step 2  builds  Phase 2
prompts/03-set-a-policy-rate.md    Step 3  builds  Phase 3
prompts/04-score-and-rule.md       Step 4  builds  Phase 4
prompts/05-beat-the-rule.md        Step 5  your own rule
```

So "Step 3" and "Phase 3" are the same piece of work, and you never have to
translate between them. When you ask for help, say **setup step** or **lab
step** — that is the only ambiguity left.

**Start with `prompts/01-the-app-runs.md`.**

---

## Before you leave a machine that is not yours

**Skip this on your own laptop.** On any other machine, do it at the end of
every session. Otherwise the next person to sit down gets your key.

1. In the **opencode** tab, type `/connect` and press **Enter**.
2. Type `openrouter` — the whole word. Check **OpenRouter** is highlighted, then
   press **Enter**.
3. The line **● OpenRouter** is highlighted, and the bottom says
   **delete ctrl+d**. Press **Ctrl+D** (Ctrl on a Mac too).
4. Sign out of OpenRouter in the browser, and close the window.

**OpenCode closed?** Type `opencode` in that tab and press Enter, then check again.
**Deleting the folder does not remove the key.**

**Check:** type `/connect` and `openrouter` again — **OpenRouter** has no ✓
beside it.

**If you forget, or you are not sure:** go to
**https://openrouter.ai/keys** from any machine and delete the key. It stops
working immediately, and you can make another.

---

## Your daily allowance

Start with **DeepSeek V4.1 Flash Free (OpenCode)**. Its free quota is not
published. If it stops, use **North Mini Code (free) on OpenRouter**, then
**GLM-5.3-Flash Free (OpenCode)**, then ask the instructor.

OpenRouter's free allowance is per account and resets daily; changing to another
free model on OpenRouter does not reset it. OpenCode's two named models belong to the
same provider: do not assume they have separate allowances.
OpenRouter's limits: **https://openrouter.ai/docs/api-reference/limits**.

### One instruction can cost several requests

The assistant may read files, write code, run tests and fix failures before it
answers. A precise instruction saves requests.

### If the screen says "Free limit reached"

Click **dismiss**. Never **subscribe**: this lab uses free models only
(**Row 2's rules**). After dismiss, this line may remain under your prompt:

> You've used today's free messages. They reset at 9:00 PM. Upgrade to OpenCode Go → /connect · Switch model → /models

**Type `/models`, never `/connect`, at this point.** Here the message offers
`/connect` for the paid OpenCode Go upgrade. Step 8 used `/connect` to connect
OpenRouter; that is a different job. Use the free-model switch below.

### If a model stops

On OpenRouter you may see:
`Error: Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day`

**Do not add credits.** A rebuild can use a whole day's OpenRouter requests:
**ask for a checkpoint first**.

1. Read the last test line. If it already shows the total your step expects,
   return to that step's check.
2. Otherwise, type `/models` in the **opencode** tab and press **Enter**.
3. If you were on DeepSeek, choose **North Mini Code (free)** under
   **OpenRouter**. If OpenRouter stopped, choose **GLM-5.3-Flash Free** under
   **OpenCode**. Choose **Default** if a variant list opens.
4. Send this:

```text
The previous model stopped before it finished. Continue the last task from where
it stopped: check what is already done, do only what is still missing, then run
uv run pytest -q.

If the app is not running, run uv run start.py once; otherwise never start,
stop or restart it. Never run pkill or kill, and never send requests to it.
```

If GLM also cannot finish, tell the instructor. If the assistant repeats itself,
press **Esc** twice before switching. Keep Row 2's rules and the training switch
from Step 2 in force. Your work remains in your project files.

---

## Changing model

You can change model at any time in OpenCode's settings. Reasons you might:

* The one you picked is slow or gives poor answers.
* It stopped being free — free offers are promotional and come and go.

Changing models within one provider does not promise a fresh allowance. Your project files keep your work.

---

## Troubleshooting

**`uv: command not found` after installing it**
Close the terminal completely and open a new one. On Windows, if it still
fails, quit VS Code completely and open it again — its terminals can keep the
old settings until VS Code itself restarts. If it still fails after that, try
`winget install --id=astral-sh.uv -e` instead, and restart VS Code once more.

**Windows blocks the PowerShell command**
Some managed laptops refuse it. Try the `winget` command above. If that also
fails, ask — and work with a neighbour for this session rather than losing it.

**The assistant's panel is blank, or its terminal shows nothing**
Almost always the Python setting from Step 5. Open the settings JSON as in
Step 5 and check that `"python.terminal.activateEnvironment": false` is there.
Then close VS Code and open it again — the setting only applies
to terminals opened after it. If the panel is still blank, close every
assistant terminal, reload the window, and open the panel once.

**No free models appear, or every free model is refused**
Training stays off (Step 2), so only providers that do not train will accept
your requests. Try another free model from the list. If none answers, tell the
instructor — do not turn training back on.

**OpenCode says the key is invalid**
Almost always a copy-paste problem: a missing character, or a space at the end.
Delete the key on OpenRouter, make a new one, and paste it carefully.

**`Address already in use` when starting the app**

Almost always your *own* app still running from earlier. Press **Ctrl+C** in the
terminal where it is running — click inside the terminal first, not the browser;
**Ctrl** on a Mac too, not Cmd. No terminal shows it running? Tell the
instructor. Do **not** close programs by force: a forced close can stop other
programs as well, your browser among them.

Do **not** ask the assistant to move the app to a different port. It costs a
request, and then the addresses on your screen stop matching everyone else's.

**The assistant answers, but very slowly**
Free models are shared. Try a different free model, or wait a moment. This does
not consume extra allowance.

**Nothing works and you are behind**
Say so. Losing the session matters more than losing the step.
