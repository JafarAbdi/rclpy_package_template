# Developers Guide

To make sure you have the latest repos:

```bash
cd $COLCON_WS/src/{{ cookiecutter.project_name | snakecase }}
git checkout main
git pull origin main
cd $COLCON_WS/src
vcs import < {{ cookiecutter.project_name | snakecase }}/{{ cookiecutter.project_name | snakecase }}.repos
rosdep install --from-paths . --ignore-src -y
```

## Setup pre-commit

pre-commit is a tool to automatically run formatting checks on each commit, which saves you from manually running clang-format (or, crucially, from forgetting to run them!).

Install pre-commit like this:

```bash
pip3 install pre-commit
```

Run this in the top directory of the repo to set up the git hooks:

```bash
pre-commit install
```

## Testing and Linting

To test the pacakges in {{ cookiecutter.project_name | snakecase }}, use the following command with [colcon](https://colcon.readthedocs.io/en/released/).

```bash
export TEST_PACKAGES="PROJECT_PACKAGE_NAMES"
colcon build --packages-up-to ${TEST_PACKAGES}
colcon test --packages-select ${TEST_PACKAGES}
colcon test-result
```
