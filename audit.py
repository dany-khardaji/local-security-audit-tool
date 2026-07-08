from pathlib import Path
import stat


print("---- Local Security Audit Tool - Version 1.0 ----")
print("                 Scan starting…\n")


folder = Path("sample_target")

findings = []
secret_keywords = ["api_key", "secret", "password", "token", "private_key", "aws_access_key"]
secret_findings = []
permission_findings = []
filename_keywords = ["id_rsa", "password.txt", "passwords.txt", "backup.sql"]
filename_findings = []

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
        if mode & stat.S_IWOTH:
            permission_findings.append(item)

        # Scan for suspicious filenames
        for keyword in filename_keywords:
            if keyword in item.name.lower():
                filename_findings.append(item)
                break

        if item.name.endswith((".key", ".pem")):
             filename_findings.append(item)


# Reports results for each check
if not findings:
    print("No exposed .env files found.")
else:
    for finding in findings:
        print(f"Exposed .env file detected: {finding}")

if not secret_findings:
    print("No secrets found.")
else:
    for finding in secret_findings:
        print(f"Possible secret detected: {finding}")

if not permission_findings:
    print("No vulnerable file permissions found.")
else:
    for finding in permission_findings:
        print(f"Vulnerable file permission detected: {finding}")

if not filename_findings:
    print("No vulnerable filenames found.")
else:
    for finding in filename_findings:
        print(f"Vulnerable filename detected: {finding}")