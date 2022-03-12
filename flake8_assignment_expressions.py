from __future__ import annotations

import ast
import importlib.metadata
from typing import Any, Generator, Type

ASE101 = "ASE101 Line contains assignment expression"


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors: list[tuple[int, int, str]] = []

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        self.errors.append((node.lineno, node.col_offset, ASE101))
        self.generic_visit(node)


class Plugin:
    name = __name__
    version = importlib.metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col, msg in visitor.errors:
            yield line, col, msg, type(self)
