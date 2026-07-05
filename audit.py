from pathlib import Path

print("Local Security Audit Tool - Version 1.0")
print("Scan starting…")

# Scans the fake test folder (can't leak real secrets while testing)
folder = Path("sample_target")

findings = []
for item in folder.rglob("*"):
    if item.name == ".env":
        findings.append(item)

if not findings:
    print("No exposed .env files found.")
else:
    for finding in findings:
        print(f"Exposed .env file detected: {finding}")


