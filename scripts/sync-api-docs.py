"""
Sync API documentation from the Annie repository.
Extracts docstrings and converts them to markdown documentation.
"""


import ast
from pathlib import Path

import sys


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
                    docs.append({
                        "type": "class",
                        "name": node.name,
                        "docstring": docstring,
                        "methods": []
                    })
                    # Extract methods
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            method_doc = extract_docstring(item)
                            if method_doc:
                                docs[-1]["methods"].append({
                                    "name": item.name,
                                    "docstring": method_doc,
                                    "signature": None,  # TODO: add signature extraction
                                    "params": [],        # TODO: add param extraction
                                    "returns": None,     # TODO: add return type
                                    "errors": [],        # TODO: add error info
                                    "since": None,       # TODO: add since version
                                    "examples": [],      # TODO: add examples
                                    "see_also": [],      # TODO: add cross-references
                                })
        return docs
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return []


def convert_to_markdown(docs, class_name, placeholder=False):
    """Convert extracted documentation to markdown format."""
    if placeholder:
        return f"# {class_name} API Documentation\n\n> Documentation for {class_name} will be available soon.\n"

    md_content = f"# {class_name} API Documentation\n\n"

    for doc in docs:
        if doc["type"] == "class" and doc["name"] == class_name:
            md_content += f"## {doc['name']}\n\n{doc['docstring']}\n\n"

            for method in doc["methods"]:
                md_content += f"### {method['name']}\n\n{method['docstring']}\n\n"
                if method.get("params"):
                    md_content += "**Parameters:**\n\n"
                    for param in method["params"]:
                        md_content += f"- `{param['name']}` ({param.get('type', 'Any')}): {param.get('desc', '')}\n"
                    md_content += "\n"
                if method.get("returns"):
                    md_content += f"**Returns:** `{method['returns']}`\n\n"
                if method.get("errors"):
                    md_content += "**Raises:**\n\n"
                    for err in method["errors"]:
                        md_content += f"- `{err}`\n"
                    md_content += "\n"
                if method.get("since"):
                    md_content += f"**Since:** {method['since']}\n\n"
                if method.get("examples"):
                    md_content += "**Examples:**\n\n"
                    for ex in method["examples"]:
                        md_content += f"```python\n{ex}\n```\n\n"
                if method.get("see_also"):
                    md_content += "**See also:** " + ", ".join(f"`{s}`" for s in method["see_also"]) + "\n\n"
    return md_content


def main():
    """Main sync function."""
    import argparse
    parser = argparse.ArgumentParser(description="Sync API docs from source.")
    parser.add_argument(
        "--source", type=str, default="annie-source",
        help="Path to API source directory (Python or Rust stubs)"
    )
    parser.add_argument(
        "--api-dir", type=str, default="docs/api",
        help="Path to output API docs directory"
    )
    args = parser.parse_args()

    source_path = Path(args.source)
    docs_api = Path(args.api_dir)

    # Ensure API docs directory exists
    docs_api.mkdir(exist_ok=True)

    # Map of API files to generate
    api_mapping = {
        "ann_index.md": "AnnIndex",
        "hnsw_index.md": "PyHnswIndex",
        "threadsafe_index.md": "ThreadSafeAnnIndex",
    }

    # Look for Python files in source
    python_files = list(source_path.rglob("*.py")) if source_path.exists() else []

    for md_file, class_name in api_mapping.items():
        print(f"Syncing {class_name} documentation...")

        all_docs = []
        for py_file in python_files:
            docs = parse_python_file(py_file)
            all_docs.extend(docs)

        placeholder = not bool(all_docs)
        md_content = convert_to_markdown(all_docs, class_name, placeholder=placeholder)

        # Write to file
        output_path = docs_api / md_file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        print(f"✓ Updated {md_file}")


# Entrypoint
if __name__ == "__main__":
    main()
