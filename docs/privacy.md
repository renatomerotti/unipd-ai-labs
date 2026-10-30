# Security

Read this before you create an account. It is the
lab's only security briefing: the setup steps and the lab do not repeat it. They
trust you to remember these four rules.

---

## The noticeboard test

> Everything you type into the assistant, and every file in the folder you have
> open, is sent to a model provider. Its handling depends on the model selected. Put nothing there you would not pin to the noticeboard in the corridor.

The good news: the Central Bank Game passes that test by design. The economy is invented, the
numbers are made up, and the random shocks come from a fixed seed so that
everyone gets the identical history. **The lab never needs anything personal**,
so you never have to decide whether something is safe to send. It never is, and
it is never needed.

---

## Rule 1 — Open `unipd-ai-lab`, never a folder above it

The assistant reads files to understand your project. **It can read anything in
the folder you opened in VS Code**, not only the file you are looking at, and
there is no list afterwards of what it sent. Open `Downloads` and it can read
every PDF (Portable Document Format) file, bank statement and attachment you
have ever saved. Open `Documents` and it can read your thesis, your CV
(curriculum vitae) and last year's tax return.

OpenCode can also reach *outside* the folder unless it is told not to. The lab's
`opencode.json` tells it not to — never delete or change that file.

**Where the folder lives matters far less than which folder you open.** A
project on your Desktop is no safer if you then open the Desktop itself. The
whole of this rule is one line:

```text
Downloads/
└── unipd-ai-lab/     ← open this one, and nothing above it
```

The lab arrives as a single folder and that folder *is* the project, so there is
no second folder to choose between and no level to get wrong. `SETUP.md` Step 6
opens it and Step 11 checks it before you load anything.

**The test, any time:** if the VS Code sidebar shows anything you recognise from
the rest of your life, you opened the wrong folder. Close it and open
`unipd-ai-lab`.

> **Keeping your work.** `Downloads` is where the archive lands, and it is fine
> to work there — the assistant only ever sees the folder you opened. But some
> machines empty `Downloads` without asking. If you want your project after the
> course, drag the whole `unipd-ai-lab` folder to wherever you keep your
> coursework when you are done, and open it from there next time.

## Rule 2 — Nothing personal in the chat

Do not paste into the assistant:

* your student number, tax code, address, telephone number or date of birth
* a CV, a thesis draft, or coursework for another module
* real data about **other people** — a classmate, a family member, an interview
  subject. Their information is not yours to hand over.
* anything from a job, an internship or a placement
* passwords, of anything, ever

If you want to try the assistant on your own work, do it after the course, with
an account whose privacy settings you have chosen deliberately. Not here.

## Rule 3 — Your key is a password

The API key (Application Programming Interface key) you make in `SETUP.md`
Step 3 spends your allowance and acts as you.

* **Never** put it in a file, a screenshot, a chat message, an email or a
  repository.
* **Leaked it, or not sure?** Delete it at <https://openrouter.ai/keys> and make
  a new one. Deleting a key you did not need to delete
  costs you nothing.
* **Working in a pair?** Share a screen, not a key. Each of you uses your own
  account — a shared key spends the same OpenRouter backup allowance for both of you.
* **On a lab machine you did not bring?** Remove the key before you leave —
  `SETUP.md`, under **Before you leave a machine that is not yours**.

And give OpenRouter a password you have not used anywhere else.

## Rule 4 — Extensions report on their own

`SETUP.md` Step 5 turns off VS Code's usage reporting. Each extension also ships
a switch of its own, and from outside you cannot tell which one wins. If you add
an extension later, search its settings for `telemetry` and decide for yourself.

---

## "Free" is not free

The first model, **DeepSeek V4.1 Flash Free (OpenCode)**, needs no account and no key. OpenCode describes it and **GLM-5.3-Flash Free (OpenCode)** as zero-retention and no-training models, with content kept **30 days for safety reasons**. The safety exception is why the noticeboard test still applies.

OpenRouter is the backup. **SETUP Step 2 stays off**: OpenRouter's
*Allow free endpoints that train on request data* switch excludes training
providers for those requests. It does not control OpenCode's free models or promise that
requests are never stored for safety.

Follow the four rules above with every model. The lab needs only invented,
non-confidential course material.

- OpenCode's free models’ model terms: <https://opencode.ai/v2/docs/console/models/>
- OpenRouter's terms: <https://openrouter.ai/docs/features/privacy-and-logging>

---

## If you would rather not create an account

DeepSeek, the first model, needs no account or key. Tell the instructor if you
will not set up OpenRouter, the backup, so you have help if the first model
stops. You can also pair with someone or work from the specification by hand.
