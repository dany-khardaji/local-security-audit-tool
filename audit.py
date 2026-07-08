from pathlib import Path
import stat

print("---- Local Security Audit Tool - Version 1.0 ----")
print("                 Scan starting…\n")



folder = Path("sample_target")

findings = []

secret_keywords = ["api_key", "secret", "password", "token", "private_key", "aws_access_key"]
secret_findings = []

permission_findings = []

# Main scan loop runs every security check on each file
for item in folder.rglob("*"):
    if item.name == ".env":    
        findings.append(item)

    if item.is_file():
        try:
            text = item.read_text()
        except:
            continue
        # Scan text for any secret keyword, break on first match
        for keyword in secret_keywords:
            if keyword in text.lower():
                secret_findings.append(item)
                break
        # Scan for vulnerable file permissions            
        mode = item.stat().st_mode
        if mode & stat.S_IROTH:
            permission_findings.append(item)



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

if not permission_findings:
    print("No vulnerable file permissions found.")
else:
    for finding in permission_findings:
        print(f"Vulnerable file permissions found in: {finding}")
