import argparse
from pathlib import Path

from checks.env_files import check_env_file
from checks.permissions import check_permissions
from checks.filenames import check_filenames
from checks.secrets import check_for_secrets
from checks.dependencies import check_dependencies


# Function to print scan findings
def print_findings(findings, none_message, detected_message):
    if not findings:
        print(none_message)
    else:
        for finding in findings:
            print(f"{detected_message}: {finding}")


# Read the target folder from the command line
parser = argparse.ArgumentParser(description="Scan a folder for security issues")
parser.add_argument("target", help="the folder to scan")
args = parser.parse_args()


print("---- Local Security Audit Tool - Version 1.0 ----")
print("                 Scan starting…\n")

# Set the target folder to scan
folder = Path(args.target)
 
# Initialize lists to hold findings for each check
env_findings = []
secret_keywords = ["api_key", "secret", "password", "token", "private_key", "aws_access_key"]
secret_findings = []
permission_findings = []
filename_keywords = ["id_rsa", "password.txt", "passwords.txt", "backup.sql"]
filename_findings = []
dependency_findings = []


# Walking items in folder
for item in folder.rglob("*"):

    # Skip .git directory to avoid false positives
    if ".git" in item.parts:
        continue

    # Scan for .env files
    env_result = check_env_file(item)
    if env_result:
        env_findings.append(env_result)

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
print_findings(env_findings, "No exposed .env files found.", "Exposed .env file detected")
print_findings(secret_findings, "No secrets found.", "Possible secret detected")
print_findings(permission_findings, "No vulnerable file permissions found.", "Vulnerable file permission detected")
print_findings(filename_findings, "No vulnerable filenames found.", "Vulnerable filename detected")
print_findings(dependency_findings, "No flagged dependencies found.", "Dependency with no version specifier detected")




