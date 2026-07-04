# Local Security Audit Tool

A **local-only, defensive** command-line tool that scans folders on *your own computer*
for common beginner-level security mistakes — and prints a report telling you what to fix.

It only ever **reads** your files. It never edits, deletes, uploads, or transmits anything.

> Built as a learning project by a beginner, to learn how real software works —
> one small, well-understood step at a time.

---

## What it checks for

| Check | What it looks for | Why it matters |
|-------|-------------------|----------------|
| Exposed `.env` files | `.env` files sitting in a project | `.env` files often hold passwords/keys and should never be shared or committed |
| Possible secrets | Text that looks like an API key, token, or password inside files | Secrets accidentally left in code are one of the most common real-world leaks |
| Risky file permissions | Files readable/writable by everyone | Overly open permissions let other users on the machine read sensitive data |
| Suspicious filenames | Names like `password.txt`, `backup.sql`, `id_rsa` | These often contain sensitive data you didn't mean to leave lying around |
| Outdated / unpinned dependencies | A `requirements.txt` with no fixed versions | Unpinned or old dependencies are a common source of vulnerabilities |
| Security checklist | Presence of `.gitignore`, no committed secrets, etc. | Basic hygiene that prevents the most common beginner mistakes |

---

## Scope & safety (please read)

This tool is **strictly defensive** and intentionally limited:

- It **only scans folders you point it at** on your own machine.
- It is **read-only** — it never modifies, deletes, or moves files.
- It does **not** scan other people's systems, networks, or websites.
- It contains **no** exploitation, brute-forcing, credential theft, malware, or network attacks.
- It sends **no** data anywhere — everything stays on your computer.

If a feature can't be done safely and locally, it does not belong in this project.

---

## How it works

```
You type:  python audit.py ./my-folder
                    │
                    ▼
        ┌───────────────────────┐
        │   audit.py (entry)    │  the file you run
        └───────────────────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │   Scanner logic       │  walks the folder,
        │                       │  reads each file (read-only)
        └───────────────────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │   Security checks     │  one rule at a time
        └───────────────────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │   Findings (a list)   │  collect what was flagged
        └───────────────────────┘
                    │
                    ▼
          Prints a report to your terminal
```

---

## Project structure

You start with a single `audit.py` file and grow into this shape over time.
Items marked *(later)* are added in specific roadmap phases, not up front.

```
security-audit-tool/
├── README.md            this file
├── ROADMAP.md           the learning path
├── .gitignore           files git should ignore            (later)
├── requirements.txt     list of dependencies               (later)
├── audit.py             THE FILE YOU RUN — start here
├── checks/              one file per check                 (later phase)
│   ├── env_files.py
│   ├── secrets.py
│   └── permissions.py
└── sample_target/       fake dummy files to test on safely
    ├── .env             pretend secrets (never real ones)
    └── notes.txt
```

---

## Requirements

- Python 3.10 or newer
- A terminal
- No third-party libraries required for the early phases (added only when needed)

---

## Usage

> Coming as the project is built. The first runnable version arrives in Phase 1 of the roadmap.

Planned command:

```
python audit.py ./sample_target
```

---

## Roadmap

See **ROADMAP.md** for the full, phase-by-phase build plan.
Each phase introduces at most one or two new concepts.

---

## License

Personal learning project. Use at your own risk, on systems you own.
