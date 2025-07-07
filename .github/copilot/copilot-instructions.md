# GitHub Copilot Instructions for `Annie-Docs`

This project uses **GitHub Copilot Workspace** with an **MCP (Model Context Protocol)** configuration to enable intelligent automation and assistance.

## What Can Copilot Do Here?

Copilot has access to key project context and can:

- Suggest and file Pull Requests (PRs)
- Update documentation files (`mkdocs.yml`, `README.md`, etc.)
- Assist with changelog and version updates
- Benchmark code using provided scripts
- Align version tags across `Annie` and this documentation repo

---

## Context Copilot Uses

Copilot reads context from:

- `docs/` — all documentation files
- `mkdocs.yml` — configuration for the MkDocs static site
- `scripts/` — scripts like `update-version-info.py` or benchmarks
- `README.md`, `netlify.toml`, etc.

This context is defined in `.github/copilot/mcp.json`.

---

## How to Enable or Update Copilot

### Enable Copilot Workspace

1. Go to **Settings → Copilot** in the GitHub UI for this repo
2. Make sure **GitHub Copilot Workspace** is enabled

> Note: Only repository admins can do this.

---

## Try It Out

Once enabled:

- Use GitHub Copilot Chat (from the GitHub.com interface)
- Ask:  
  > “Update all version tags to match the latest Annie release”
- Or say:  
  > “Open a pull request updating the README to reflect new module structure”

---

## Maintainer Notes

- MCP file lives at: `.github/copilot/mcp.json`
- You can edit it to add more files or context
- After editing, **commit and push** the change:
  
  ```bash
  git add .github/copilot/mcp.json
  git commit -m "Update MCP context"
  git push
