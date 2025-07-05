# 🔄 Auto-Sync Setup Guide

This guide explains how to set up automatic synchronization between your main Annie repository and this documentation repository.

## 🎯 Goal

Whenever code changes in the main Annie repository (https://github.com/Programmers-Paradise/Annie), the documentation in this repository should automatically update.

## 🛠️ Setup Steps

### 1. Configure Repository Dispatch in Main Annie Repo

Add this GitHub Action to your main Annie repository at `.github/workflows/notify-docs.yml`:

```yaml
name: Notify Documentation Repository

on:
  push:
    branches: [main, master]
    paths:
      - "src/**"
      - "examples/**"
      - "README.md"
      - "Cargo.toml"
      - "docs/**"

jobs:
  notify-docs:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger documentation update
        uses: peter-evans/repository-dispatch@v2
        with:
          token: ${{ secrets.DOCS_REPO_TOKEN }}
          repository: Programmers-Paradise/Annie-Docs
          event-type: docs-update
          client-payload: |
            {
              "ref": "${{ github.ref }}",
              "sha": "${{ github.sha }}",
              "repository": "${{ github.repository }}"
            }
```

### 2. Create Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name: "Annie Docs Sync Token"
4. Select these scopes:
   - `repo` (Full control of private repositories)
   - `workflow` (Update GitHub Action workflows)
5. Click "Generate token"
6. Copy the token (you won't see it again!)

### 3. Add Token to Main Repository

1. Go to your main Annie repository
2. Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `DOCS_REPO_TOKEN`
5. Value: Paste the token you created
6. Click "Add secret"

### 4. Test the Setup

1. Make a small change to the main Annie repository (edit README.md)
2. Commit and push to main branch
3. Check the Actions tab in this documentation repository
4. You should see the "Sync Documentation from Annie Repository" workflow running

## 🔧 What Gets Synced

The sync process will automatically update:

- **API Documentation**: Extracted from Python/Rust docstrings
- **Examples**: All files from the `examples/` directory
- **README Content**: Main project information
- **Version Information**: From Cargo.toml
- **Guide Content**: Any documentation in the main repo's `docs/` folder

## 🚨 Troubleshooting

### Sync Not Triggering

1. Check that the `DOCS_REPO_TOKEN` secret exists in the main repo
2. Verify the token has the correct permissions
3. Ensure the workflow file is in the main repository
4. Check the Actions tab for any error messages

### Permission Errors

- Make sure the token has `repo` and `workflow` scopes
- Verify you're using a personal access token, not the default `GITHUB_TOKEN`

### Partial Sync

- Check the workflow logs in the Actions tab
- Ensure all required directories exist in the main repository
- Verify file paths in the sync scripts are correct

## 🔄 Manual Sync

You can manually trigger a sync by:

1. Going to the Actions tab in this repository
2. Selecting "Sync Documentation from Annie Repository"
3. Clicking "Run workflow"
4. Selecting the main branch and clicking "Run workflow"

## 📊 Monitoring

- **Sync Status**: Check the Actions tab for workflow runs
- **Sync Frequency**: Automatic on main repo changes + every 6 hours
- **Logs**: View detailed logs in each workflow run

---

_This automation ensures your documentation stays up-to-date with zero manual effort!_
