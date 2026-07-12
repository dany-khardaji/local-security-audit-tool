# local-security-audit-tool
**Version 1.0**
This is a local-only command-line tool that scans a folder for common security mistakes such as exposed secrets, sensitive files and risky permissions. Intended for use before you push your code to GitHub.

## Why I built it
Wanted a tool to make sure that I don't accidentally commit any secrets or sensitive information. This tool will help me scan my project directory before pushing to GitHub.

## What it checks for
- Exposed `.env` files
- Secrets in file contents (keyword-based)
- World-writable file permissions
- Suspicious filenames (`id_rsa`, `.key`, etc.)
- Unpinned dependencies in `requirements.txt`

## Known Limitations
- False positives are possible - It flags keywords in any file so even unintended matches may be flagged.
- Keyword matching NOT pattern matching - Can miss real secrets with unusual names or patterns.
- Catches common mistakes NOT all possible mistakes - This is a simple tool for beginner level security auditing.
- Permission check is Mac/Linux ONLY - Won't behave as expected on Windows.

## How to use it
1. Make sure you have Python3 installed.
2. Open a terminal and run the following command:

```bash
python3 audit.py <folder>
```
Example (test folder):
```bash
python3 audit.py sample_target
```

## Built with
- Python3 (standard library only and no external dependencies)
- pathlib, stat, argparse modules for file system operations and command-line argument parsing
