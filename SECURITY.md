# Security Policy

## Supported Versions

We actively support the following versions of Annie documentation:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| Main    | :white_check_mark: |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability in the Annie documentation repository, please follow these steps:

### 🔒 Private Disclosure

**DO NOT** open a public issue for security vulnerabilities.

Instead, please:

1. **Email us directly** at: [security@programmers-paradise.com](mailto:security@programmers-paradise.com)
2. **Use GitHub Security Advisories**: Go to the [Security tab](https://github.com/Programmers-Paradise/Annie-Docs/security/advisories) and click "Report a vulnerability"

### 📝 What to Include

When reporting a vulnerability, please include:

- **Description** of the vulnerability
- **Steps to reproduce** the issue
- **Potential impact** of the vulnerability
- **Suggested fix** (if you have one)
- **Your contact information** for follow-up

### ⏱️ Response Timeline

- **Initial response**: Within 48 hours
- **Status update**: Within 7 days
- **Resolution timeline**: Depends on severity, typically 14-30 days

### 🔐 Security Measures

Our documentation repository implements:

- **Automated security scanning** with CodeQL
- **Dependency vulnerability checking** with safety and bandit
- **Regular security updates** via automated workflows
- **Access controls** on repository settings and secrets

### 🏆 Recognition

We appreciate security researchers who help keep our documentation safe. With your permission, we'll acknowledge your contribution in:

- Repository security advisories
- Project documentation
- Security hall of fame (if applicable)

### 📋 Security Best Practices for Contributors

When contributing to this repository:

- **Keep dependencies updated** - Use the automated dependency update PRs
- **Follow secure coding practices** - Scripts are scanned with bandit and semgrep
- **Don't commit secrets** - Use environment variables and GitHub secrets
- **Review security warnings** - Address any CodeQL findings

### 🔗 Related Security Resources

- [Annie Main Repository Security](https://github.com/Programmers-Paradise/Annie/security)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)
- [MkDocs Security Considerations](https://www.mkdocs.org/)

---

**Thank you for helping keep the Annie documentation secure!** 🛡️
