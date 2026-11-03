# PS2 Exercise 1 — collaboration setup

## Start here

The PS2 setup uses Python 3.12 and a committed lock file. Four platforms are
resolved: macOS Apple Silicon, macOS Intel, Linux x86-64, and Windows x86-64.
Runtime validation is performed on macOS Apple Silicon; other platforms are
dependency-resolved, not runtime-tested. Install Pixi from https://pixi.sh/ .

From the repository root:

```bash
pixi install --locked -e ps2-ex1
pixi run -e ps2-ex1 jupyter
```

Use the Python kernel from that environment. Do not use a global Python or a
teammate's absolute environment path. Other CPU architectures require a team
manifest/lock update first. See [CONTRIBUTING.md](CONTRIBUTING.md) for branches,
reviews, notebook editing, and local-file rules.

## Files and unfinished coursework

- Existing `src/` and `notebooks/`: keep the PS1 work and add type hints in the assigned task PR.
- `.pre-commit-config.yaml`: intentionally EMPTY; the hooks owner completes it.
- `docs/answers.md`: intentionally EMPTY; the explanation owner completes it.
- `.gitignore`: shared local-file policy, submitted in a separate PR.

This preparation does not implement hooks or type hints and does not answer the
exercise questions. Keep the hooks, ignore policy, and type-hint coursework PRs
separate; obtain two non-author approvals. The repository owner merges Ex1 PRs.


## Setup verification

Verified on 2026-11-03 with Python 3.12.16 on macOS Apple Silicon.
Checks passed: headless PNG rendering; course modules and lint/type-check tools import (no assignment checks run); fresh Jupyter kernel executes disposable Python/pandas cell.
Other platforms were lock-resolved only. No coursework analysis, answers,
model training, or Kaggle data download was performed.

## Original repository instructions (retained)

# first_repo
