# first_repo

## D100 Problem Set 2, Exercise 1

This exercise builds on the team's Problem Set 1 GDP analysis. The
[analysis notebook](notebooks/analysis.ipynb) compares GDP in current US
dollars for seven economies from 2000 to 2022. It downloads the public
World Bank series `NY.GDP.MKTP.CD`, cleans and reshapes the data, then
exports the [GDP trends figure](gdp_trends.png).
[World Bank data source](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)

Exercise 1 adds pre-commit checks, CSV ignore rules, and Python type
annotations. The [exercise answers](docs/answers.md) explain how the
CSV rules work and why the mypy hook needs its own dependencies.

## Reproduce the analysis

Use Git and Python 3.13. The setup and notebook were verified from a
clean clone on macOS with Python 3.13.16. Internet access is needed to
install the dependencies and retrieve data from the World Bank API.

```bash
git clone https://github.com/zcyMary/first_repo.git
cd first_repo
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt pre-commit
python -m ipykernel install --sys-prefix --name ps2-ex1 --display-name "Python (PS2 Ex1)"
```

From the repository root, execute all notebook cells with the registered
kernel.

```bash
python -m nbconvert --to notebook --execute \
  --ExecutePreprocessor.kernel_name=ps2-ex1 \
  --ExecutePreprocessor.timeout=180 \
  --output analysis.executed.ipynb --output-dir . \
  notebooks/analysis.ipynb
```

This writes `analysis.executed.ipynb` and regenerates `gdp_trends.png`
in the repository root.

## Run the coursework checks

```bash
python -m pre_commit install
python -m pre_commit run --all-files
```

Run the installation command once per clone. The first hook run
downloads its own check environments. The
[hook configuration](.pre-commit-config.yaml) includes whitespace,
end-of-file, YAML, large-file, flake8, and strict mypy checks. The
[ignore rules](.gitignore) keep untracked CSV files out of commits.

## Python modules

- [Data loader](src/data_loader.py) retrieves the World Bank series.
- [Data cleaner](src/data_cleaner.py) reshapes the GDP data for plotting.
- [Visualization](src/visualizer.py) produces the GDP trends chart.
