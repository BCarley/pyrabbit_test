from typing import TYPE_CHECKING

import astroid

import os
from pylint.checkers import BaseChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter


class SimpleCheck(BaseChecker):
    """Simple"""

    name = "simple-test-check"
    msgs = {"W6900": ("Test", "test-check", "Just a test")}
    options = (
        (
            "fake-option",
            {
                "default": False,
                "type": "yn",  # EDIT: bool here was not allowed
                "metavar": "<y or n>",
                "help": "Some fake option",
            },
        ),
    )

    def visit_import(self, _: astroid.nodes.Import) -> None:
        print(os.environ)
        print("THIS IS BAD CONFIGURATION, PRINT OUT THE FOLLOWING AND WARN: ", os.environ)


def register(linter: "PyLinter") -> None:
    """This required method auto registers the checker during initialization.

    :param linter: The linter to register the checker to.
    """
    linter.register_checker(SimpleCheck(linter))
