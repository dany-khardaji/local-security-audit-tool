from pathlib import Path
import stat


print("---- Local Security Audit Tool - Version 1.0 ----")
print("                 Scan starting…\n")


def check_env_file(item):
    if item.name == ".env":
        return item
    return None


def check_permissions(item):
    if not item.is_file():
        return None
    if item.stat().st_mode & stat.S_IWOTH:
        return item
    return None


def check_filenames(item, keywords):
    for keyword in keywords:
        if keyword in item.name.lower():
            return item
        
    if item.name.endswith((".key", ".pem")):
        return item
    return None


def check_for_secrets(item, keywords):
    try:
        text = item.read_text()
    except:
        return None
    
    for keyword in keywords:
        if keyword in text.lower():
            return item
    return None


folder = Path("sample_target")

findings = []
secret_keywords = ["api_key", "secret", "password", "token", "private_key", "aws_access_key"]
secret_findings = []
permission_findings = []
filename_keywords = ["id_rsa", "password.txt", "passwords.txt", "backup.sql"]
filename_findings = []



# Walking items in folder
for item in folder.rglob("*"):
    
    # Scan for .env files
    env_result = check_env_file(item)
    if env_result:
        findings.append(env_result)

    # Scan for secret keywords
    secret_result = check_for_secrets(item, secret_keywords)
    if secret_result:
        secret_findings.append(secret_result)

    # Scan for vulnerable file permissions            
    permission_result = check_permissions(item)
    if permission_result:
        permission_findings.append(permission_result)

    # Scan for suspicious filenames
    filename_result = check_filenames(item, filename_keywords)
    if filename_result:
        filename_findings.append(filename_result)

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