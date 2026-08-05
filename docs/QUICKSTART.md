# Quick Start

## 1. Copy the starter kit

```bash
cp -R /path/to/chatgpt-parent-pm/starter-kit/. /path/to/your-project/
cp -R /path/to/chatgpt-parent-pm/validators /path/to/your-project/
```

## 2. Configure the project profile

Set project identity, repository, stack, commands, agent assignments, forbidden operations, and owner-only actions.

## 3. Pin the core

Replace the placeholder repository and commit in `GOVERNANCE_LOCK.json` with the public repository and an exact released commit.

## 4. Create a 0%-weight adoption Goal

Do not count governance installation as product completion.

## 5. Run validation

```bash
python3 validators/validate_install.py .
```

## 6. Commit through a branch and PR

Do not install directly on `main` by default.
