from __future__ import annotations

import ast

from flake8_assignment_expressions import Plugin


def _results(code: str) -> set[str]:
    tree = ast.parse(code)
    plugin = Plugin(tree)
    return {f"{line}:{col} {msg}" for line, col, msg, _ in plugin.run()}


def test_empty_string():
    assert _results("") == set()


def test_normal_expression_does_not_generate_error():
    assert _results("x = 5 ** 2") == set()


def test_assignment_expression_generates_error():
    errors = _results("if a := bool(2): pass")
    assert errors == {"1:3 ASE101 Line contains assignment expression"}
