# flake8_expression_assignments

A flake8 plugin that disallows assignment expressions.

## Installation

`pip install flake8_assignment_expressions`

## Flake8 codes

| Code   | Description                                            |
|--------|--------------------------------------------------------|
| ASE101 | Line contains assignment expression                    |

## Why

Assignment expressions/the walrus operator was introduced in Python 3.8.
If you want to keep assignment expressions out of your own or your companies'
repositories, use this plugin.

This plugin will encourage you to rewrite code like

```python
import os

if environment := os.getenv("ENVIRONMENT"):
    print(f"You are currently on the {environment} environment.")
```

into

```python
import os

environment = os.getenv("ENVIRONMENT")
if environment:
    print(f"You are currently on the {environment} environment.")
```

## Running as a pre-commit hook
See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions.

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/pycqa/flake8
    rev: 4.0.1
    hooks:
    -   id: flake8
        additional_dependencies: [flake8_assignment_expressions]
```
