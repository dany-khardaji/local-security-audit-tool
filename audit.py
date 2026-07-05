from pathlib import Path

print("Local Security Audit Tool - Version 1.0")
print("Scan starting…")

folder = Path("sample_target")
for item in folder.rglob("*"):
    print(item)