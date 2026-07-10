from pathlib import Path

from checks.env_files import check_env_file
from checks.permissions import check_permissions
from checks.filenames import check_filenames
from checks.secrets import check_for_secrets
from checks.dependencies import check_dependencies

print("---- Local Security Audit Tool - Version 1.0 ----")
print("                 Scan starting…\n")


folder = Path("sample_target")

findings = []
secret_keywords = ["api_key", "secret", "password", "token", "private_key", "aws_access_key"]
secret_findings = []
permission_findings = []
filename_keywords = ["id_rsa", "password.txt", "passwords.txt", "backup.sql"]
filename_findings = []
dependency_findings = []


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

    # Flag dependencies with no version specifier
    dependency_result = check_dependencies(item)
    if dependency_result:
        dependency_findings.append(dependency_result)


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

if not dependency_findings:
    print("No flagged dependencies found.")
else:
    for finding in dependency_findings:
        print(f"Dependency with no version specifier detected: {finding}")
