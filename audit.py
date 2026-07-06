from pathlib import Path


print("Local Security Audit Tool - Version 1.0")
print("Scan starting…")


folder = Path("sample_target")
findings = []
secret_findings = []

# Main scan loop runs every security check on each file
for item in folder.rglob("*"):
    if item.name == ".env":    
        findings.append(item)
    if item.is_file():
        try:
            text = item.read_text()
        except:
            continue
        if "API_KEY" in text:
            secret_findings.append(item)


# Reports results for each check
if not findings:
    print("No exposed .env files found.")
else:
    for finding in findings:
        print(f"Exposed .env file detected: {finding}")

if not secret_findings:
    print("No secrets found in file contents.")
else:
    for finding in secret_findings:
        print(f"Possible secret found in: {finding}")