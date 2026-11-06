# PS2 Exercise 1 answers

## Does the CSV ignore rule work?

Yes. The `*.csv` rule ignores new, untracked CSV files. In a disposable
repository using this project's `.gitignore`, `git check-ignore -v` matched
an untracked example CSV against `*.csv`. A second CSV was committed before
adding the rule and still appeared in `git ls-files` afterwards.

Git continues to track files that are already in its index. To keep a
previously tracked CSV on disk while removing it from future commits, use
`git rm --cached -- path/to/file.csv` and commit the index change.

[Git documentation on ignore rules](https://git-scm.com/docs/gitignore)

## Why does the mypy hook need additional dependencies?

Pre-commit runs the mypy hook in its own virtual environment. Packages and
type stubs installed in the project's Conda environment are therefore
separate from what the hook can see. The hook's `additional_dependencies`
installs the listed packages and stubs in the hook environment.

For example, `pandas-stubs` supplies type information for the pandas
objects our functions use. Making that information available to the hook
lets mypy check those types consistently. `--ignore-missing-imports`
suppresses missing-import diagnostics, while a missing library or stub
can still leave mypy treating imported values as `Any`.

[mypy hook documentation](https://github.com/pre-commit/mirrors-mypy#using-mypy-with-pre-commit)
