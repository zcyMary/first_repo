# PS2 Exercise 1 — collaboration setup

<!-- PS2_FINAL_TEAM_PLAN_START -->
## PS2 最终分工与前置顺序

本组完成第 1、2、3、5 题。A-E 为成员占位，确认后替换姓名。第 1、5 题沿用 PS1 的 Conda；第 2、3 题使用 Pixi，各题不要求统一环境工具。

### 仓库与环境

| 题目 | 小组仓库 | 环境安排 |
| --- | --- | --- |
| 第1题 | [first_repo](https://github.com/zcyMary/first_repo) | 沿用 PS1 的 Conda，补充检查工具 |
| 第2题 | [Smoking](https://github.com/starries-creator/ps_2_ex2_smoking_is_bad) | Pixi，环境名 `smoke` |
| 第3题 | [NBA](https://github.com/starries-creator/ps_2_ex3_database) | 沿用老师的 Pixi 配置，Python 3.12，环境名 `nba` |
| 第5题 | [Titanic](https://github.com/starries-creator/ps1_ex4_nb_to_repo_forked) | 沿用 Conda，Python 3.13.16、pandas 2.3 |

### 成员分工

| 成员 | 第1题 | 第2题 | 第3题 | 第5题 |
| --- | --- | --- | --- | --- |
| **A** | pre-commit、flake8、mypy 配置 | 变量分布图与解释 | 洞见① | 整合报告及 README |
| **B** | 忽略规则、CSV 跟踪验证 | **优先配置环境**，完善锁文件、README、nbstripout | 洞见② | 年龄、票价分析 |
| **C** | 第一组函数类型标注 | 数据清理、TODO、总体生存率 | **准备数据与表结构**，完成打包及加载模块解释 | 家庭变量分析 |
| **D** | 第二组函数类型标注 | 分组生存率比较＋整合 notebook | 洞见③ | 性别、舱位分析 |
| **E** | mypy 依赖验证，结合 B 的结果回答两问 | 年龄分组敏感性检查 | 洞见④＋整合 notebook | 缺失值与变量可用性 |

### 前置顺序

- **第1题**：配置、标注可并行；最终类型检查等 A 配好工具。hooks、忽略规则、类型标注分别开 PR，各安排两名非作者 review。
- **第2题**：**B 环境 → C 数据准备 → A/D/E 分析 → D 整合**。提交前各自在本机装好 hook。
- **第3题**：**C 数据与表结构 → 四条洞见并行**；打包同步进行，整合前完成导入验证。warm-up 按单元格共同认领。
- **第5题**：**各自确认原 Conda 环境可用 → B/C/D/E 并行分析 → A 整合**。报告≤500词，不含图；README 补充可视化说明，同时保留原项目说明。

### 交付与协作

各作者交齐自己的代码、必要图表和简短解释；第3题每条洞见还需包含查询和相关函数。整合者负责接入、复跑和统一格式。通过分支和 PR 协作，开工前划清函数、文件和 notebook 修改范围。

作业占位文件和原 notebook 中的 TODO 由对应成员完成；本次只同步分工及操作说明，不预填分析、答案或报告。
<!-- PS2_FINAL_TEAM_PLAN_END -->

## Start here

For PS2, each member should activate their own PS1 Conda environment. The
existing `requirements.txt` lists pandas, wbgapi, matplotlib, and jupyter;
it does not specify a Python version. From the repository root, install the
project dependencies and the tools needed for the assigned checks:

```bash
python -m pip install -r requirements.txt
python -m pip install pre-commit flake8 mypy
```

Select the corresponding environment's notebook kernel. See
[CONTRIBUTING.md](CONTRIBUTING.md) for collaboration rules.

<details>
<summary>Optional historical Pixi setup</summary>

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

</details>

## Files and unfinished coursework

- Existing `src/` and `notebooks/`: keep the PS1 work and add type hints in the assigned task PR.
- `.pre-commit-config.yaml`: intentionally EMPTY; the hooks owner completes it.
- `docs/answers.md`: intentionally EMPTY; the explanation owner completes it.
- `.gitignore`: shared local-file policy, submitted in a separate PR.

This preparation does not implement hooks or type hints and does not answer the
exercise questions. Keep the hooks, ignore policy, and type-hint coursework PRs
separate; obtain two non-author approvals. The repository owner merges Ex1 PRs.


## Setup verification (Pixi only)

The following records the earlier Pixi setup, not a verification of the
default Conda workflow.

Verified on 2026-11-03 with Python 3.12.16 on macOS Apple Silicon.
Checks passed: headless PNG rendering; course modules and lint/type-check tools import (no assignment checks run); fresh Jupyter kernel executes disposable Python/pandas cell.
Other platforms were lock-resolved only. No coursework analysis, answers,
model training, or Kaggle data download was performed.

## Original repository instructions (retained)

# first_repo
