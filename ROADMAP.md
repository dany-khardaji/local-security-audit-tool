# Roadmap — Local Security Audit Tool

This is the build plan. We follow it **one phase at a time**, in order.

**Rules for this roadmap:**
- Each phase teaches **at most one or two new concepts**.
- You write the code yourself; the mentor explains, reviews, and hints.
- A phase is done only when every box in its **"Done when"** list is checked.
- Never move to the next phase until the current one runs and you understand *why* it works.

Legend: 🧠 = new concept · 🛠️ = what you build · ✅ = done when

---

## Phase 0 — Setup (no code yet)

**Goal:** Create the project and a safe place to test it.

- 🧠 What a project folder is
- 🧠 What `git` and a repository are (version history for your code)
- 🧠 What a "safe test target" is (dummy files, so you never test on real secrets)

- 🛠️ Create the `security-audit-tool/` folder
- 🛠️ Add `README.md` and `ROADMAP.md`
- 🛠️ Run `git init` to start tracking history
- 🛠️ Create a `sample_target/` folder with fake files (a fake `.env`, a `notes.txt`)

- ✅ The folder exists with README and ROADMAP inside
- ✅ `git status` runs without error
- ✅ `sample_target/` contains at least two harmless dummy files

---

## Phase 1 — The skeleton ("hello, audit")

**Goal:** A script you can actually run from the terminal.

- 🧠 Running a `.py` file from the terminal
- 🧠 The `print()`-driven program flow (start → work → finish)

- 🛠️ Create `audit.py` that prints a banner and "Scan starting…"
- 🛠️ Run it with `python audit.py`

- ✅ Typing `python audit.py` prints your banner
- ✅ You can explain what "running a script" means in your own words

---

## Phase 2 — Walking a folder

**Goal:** Make the tool *see* files.

- 🧠 The filesystem as a tree of folders and files
- 🧠 `pathlib` — Python's tool for finding and listing files

- 🛠️ Take a folder path and list every file inside it (including subfolders)
- 🛠️ Print each file path it finds

- ✅ Running the tool on `sample_target/` lists all its files
- ✅ You understand the difference between a file and a folder in code

---

## Phase 3 — First real check: exposed `.env` files

**Goal:** Turn "listing files" into "flagging problems."

- 🧠 Comparing filenames to a rule
- 🧠 Collecting results in a **list of findings**

- 🛠️ For each file, check if it's named `.env`; if so, record a finding
- 🛠️ Print all findings at the end

- ✅ The tool flags the fake `.env` in `sample_target/`
- ✅ You understand what a "finding" is and why we collect them in a list

---

## Phase 4 — Scanning file contents for secrets

**Goal:** Look *inside* files, not just at their names.

- 🧠 Reading a file's contents in Python
- 🧠 Simple pattern detection (start with keyword matching, regex comes later)

- 🛠️ Read each text file and flag lines that look like a secret
      (e.g. contain `API_KEY`, `password=`, `secret`)
- 🛠️ Record the file and line number as a finding

- ✅ The tool flags a fake secret you planted in `sample_target/`
- ✅ You can explain why reading file contents is riskier and slower than reading names

---

## Phase 5 — Risky file permissions

**Goal:** Check *how exposed* a file is, not just what's in it.

- 🧠 What file permissions are (who can read/write/execute a file)
- 🧠 Reading permissions with `os.stat` / `pathlib`

- 🛠️ Flag files that are world-readable or world-writable
- 🛠️ Add these to findings

- ✅ The tool reports at least one permission finding on a test file
- ✅ You can read a permission string like `rw-r--r--` and say what it means

---

## Phase 6 — Suspicious filenames + refactor

**Goal:** Add more rules *and* clean up repeated code.

- 🧠 Rule lists (a list of patterns to check against)
- 🧠 Refactoring: moving repeated logic into its own function

- 🛠️ Flag risky names (`password.txt`, `id_rsa`, `backup.sql`, etc.)
- 🛠️ Move each check into its own clearly named function

- ✅ The tool flags a suspicious filename in `sample_target/`
- ✅ Your `audit.py` has one function per check, not one giant blob

---

## Phase 7 — Outdated / unpinned dependencies

**Goal:** Introduce the idea of dependencies safely and simply.

- 🧠 What a dependency is and what `requirements.txt` is
- 🧠 Pinned vs unpinned versions (`requests` vs `requests==2.31.0`)

- 🛠️ If a `requirements.txt` exists, flag any dependency with no pinned version
- 🛠️ (Checking for *known-vulnerable* versions is an advanced feature for much later)

- ✅ The tool flags an unpinned dependency in a test `requirements.txt`
- ✅ You can explain why unpinned dependencies are risky

---

## Phase 8 — Organize into modules

**Goal:** Grow from one file into a clean structure.

- 🧠 What a module and a package are in Python
- 🧠 `import` — using code from another file

- 🛠️ Move each check into `checks/` (e.g. `checks/env_files.py`)
- 🛠️ Have `audit.py` import and run them

- ✅ The tool still works exactly the same after the split
- ✅ You can explain why splitting into modules helps as a project grows

---

## Phase 9 — Report, arguments, and polish

**Goal:** Make it feel like a real tool.

- 🧠 Command-line arguments with `argparse` (letting the user pass options)
- 🧠 Writing a report file (plain text or JSON)

- 🛠️ Accept the target folder as a command-line argument
- 🛠️ Print a clean summary and optionally save a report file
- 🛠️ Add a `.gitignore` and finalize the `README.md`

- ✅ `python audit.py ./sample_target --report report.txt` works
- ✅ The output is readable and clearly grouped by check type

---

## After the roadmap (ideas, not commitments)

Only once everything above is solid and understood:

- Add colored output for readability
- Add a "severity" level to each finding (info / warning / critical)
- Write your first automated tests
- Package it so you can run it as a single command

Keep it defensive. Keep it local. Keep it understood.
