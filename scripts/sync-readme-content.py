#!/usr/bin/env python3
"""
Sync README content from the Annie repository.
Extracts relevant sections and updates documentation.
"""

import re
from pathlib import Path


def extract_sections(readme_content):
    """Extract relevant sections from Annie repository README."""
    sections = {}

    # Extract installation section
    install_match = re.search(
        r"## Installation\s*\n(.*?)(?=\n##|\Z)", readme_content, re.DOTALL
    )
    if install_match:
        sections["installation"] = install_match.group(1).strip()

    # Extract usage examples
    usage_match = re.search(
        r"## (?:Usage|Basic Usage|Quick Start)\s*\n(.*?)(?=\n##|\Z)",
        readme_content,
        re.DOTALL,
    )
    if usage_match:
        sections["usage"] = usage_match.group(1).strip()

    # Extract features
    features_match = re.search(
        r"## (?:Features|Key Features)\s*\n(.*?)(?=\n##|\Z)", readme_content, re.DOTALL
    )
    if features_match:
        sections["features"] = features_match.group(1).strip()

    # Extract performance benchmarks
    perf_match = re.search(
        r"## (?:Performance|Benchmarks?)\s*\n(.*?)(?=\n##|\Z)",
        readme_content,
        re.DOTALL,
    )
    if perf_match:
        sections["performance"] = perf_match.group(1).strip()

    return sections


def update_docs_index(sections):
    """Update the main documentation index with synced content."""
    docs_index = Path("docs/index.md")

    if not docs_index.exists():
        print("docs/index.md not found, creating new file")
        return

    # Read current content
    with open(docs_index, "r", encoding="utf-8") as f:
        content = f.read()

    # Update installation section if available
    if "installation" in sections:
        # Replace installation section
        install_pattern = r"(## Installation\s*\n).*?(?=\n##|\n\Z)"
        replacement = f"\\1\n{sections['installation']}\n"
        content = re.sub(install_pattern, replacement, content, flags=re.DOTALL)

    # Update basic usage if available
    if "usage" in sections:
        usage_pattern = r"(## Basic Usage\s*\n).*?(?=\n##|\n\Z)"
        replacement = f"\\1\n{sections['usage']}\n"
        content = re.sub(usage_pattern, replacement, content, flags=re.DOTALL)

    # Update features if available
    if "features" in sections:
        features_pattern = r"(## Key Features\s*\n).*?(?=\n##|\n\Z)"
        replacement = f"\\1\n{sections['features']}\n"
        content = re.sub(features_pattern, replacement, content, flags=re.DOTALL)

    # Write updated content
    with open(docs_index, "w", encoding="utf-8") as f:
        f.write(content)

    print("✓ Updated docs/index.md with synced content")


def update_examples(sections):
    """Update examples documentation."""
    examples_file = Path("docs/examples.md")

    if not examples_file.exists():
        print("Creating new examples.md file")
        content = "# Examples\n\n"
    else:
        with open(examples_file, "r", encoding="utf-8") as f:
            content = f.read()

    # Add performance section if available
    if "performance" in sections:
        if "## Performance" not in content:
            content += f"\n## Performance\n\n{sections['performance']}\n"
        else:
            # Update existing performance section
            perf_pattern = r"(## Performance\s*\n).*?(?=\n##|\n\Z)"
            replacement = f"\\1{sections['performance']}\n"
            content = re.sub(perf_pattern, replacement, content, flags=re.DOTALL)

    with open(examples_file, "w", encoding="utf-8") as f:
        f.write(content)

    print("✓ Updated examples.md")


def main():
    """Main sync function."""
    annie_readme = Path("annie-source/README.md")

    if not annie_readme.exists():
        print("Annie README.md not found")
        return

    # Read Annie repository README
    with open(annie_readme, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Extract relevant sections
    sections = extract_sections(readme_content)

    if not sections:
        print("No relevant sections found in Annie README")
        return

    print(f"Found {len(sections)} sections to sync: {list(sections.keys())}")

    # Update documentation files
    update_docs_index(sections)
    update_examples(sections)

    print("✓ README content sync completed")


if __name__ == "__main__":
    main()
