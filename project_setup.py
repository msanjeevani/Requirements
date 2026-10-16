import os

# Define project folder structure for E-Governance Platform
folders = [
    "docs",  # For Word reports and planning documents
    "src",  # Source code modules
    "tests",  # Test cases
    "config",  # Configuration files
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"[Directory Created] {folder}/")

# Create a sample README inside docs
readme_path = os.path.docs = "docs/README.md"
with open("docs/Project_Overview.md", "w") as f:
    f.write("# E-Governance Digital Services Platform\n")
    f.write("## Week 1: Project Planning and Requirements Analysis\n")
    f.write("Author: M. Sanjee Vani\n")
    f.write("Date: 10.10.2026\n")

print(
    "[Success] Project workspace structure initialized successfully for GitHub!"
)