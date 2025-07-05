"""
Sync API documentation from the Annie repository.
Extracts docstrings and converts them to markdown documentation.
"""

import ast
from pathlib import Path


def extract_docstring(node):
    """Extract docstring from an AST node."""
    if (
        isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef))
        and node.body
        and isinstance(node.body[0], ast.Expr)
        and isinstance(node.body[0].value, ast.Constant)
        and isinstance(node.body[0].value.value, str)
    ):
        return node.body[0].value.value
    return None


def parse_python_file(file_path):
    """Parse Python file and extract API documentation."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        tree = ast.parse(content)
        docs = []

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                docstring = extract_docstring(node)
                if docstring:
                    docs.append(
                        {
                            "type": "class",
                            "name": node.name,
                            "docstring": docstring,
                            "methods": [],
                        }
                    )

                    # Extract methods
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            method_doc = extract_docstring(item)
                            if method_doc:
                                docs[-1]["methods"].append(
                                    {"name": item.name, "docstring": method_doc}
                                )

        return docs
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return []


def convert_to_markdown(docs, class_name):
    """Convert extracted docs to markdown format."""
    md_content = f"# {class_name}\n\n"

    for doc in docs:
        if doc["type"] == "class" and doc["name"].lower() == class_name.lower():
            md_content += f"{doc['docstring']}\n\n"

            if doc["methods"]:
                md_content += "## Methods\n\n"
                for method in doc["methods"]:
                    md_content += f"### `{method['name']}`\n\n"
                    md_content += f"{method['docstring']}\n\n"

    return md_content


def main():
    """Main sync function."""
    annie_source = Path("annie-source")
    docs_api = Path("docs/api")

    if not annie_source.exists():
        print("Annie source directory not found")
        return

    # Ensure API docs directory exists
    docs_api.mkdir(exist_ok=True)

    # Look for Python files in Annie source
    python_files = list(annie_source.rglob("*.py"))

    # Map of API files to generate
    api_mapping = {
        "ann_index.md": "AnnIndex",
        "hnsw_index.md": "PyHnswIndex",
        "threadsafe_index.md": "ThreadSafeAnnIndex",
    }

    for md_file, class_name in api_mapping.items():
        print(f"Syncing {class_name} documentation...")

        # Find relevant Python files
        all_docs = []
        for py_file in python_files:
            docs = parse_python_file(py_file)
            all_docs.extend(docs)

        # Generate markdown
        md_content = convert_to_markdown(all_docs, class_name)

        # Write to file
        output_path = docs_api / md_file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        print(f"✓ Updated {md_file}")


if __name__ == "__main__":
    main()
