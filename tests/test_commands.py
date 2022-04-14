from typing import Callable, List

from click import Command, Group
from stactools.testing.cli_test import CliTestCase

from stactools.browse.commands import browse_command


class CommandsTest(CliTestCase):
    def create_subcommand_functions(self) -> List[Callable[[Group], Command]]:
        return [browse_command]

    def test_help(self) -> None:
        result = self.run_command("browse --help")
        self.assertEqual(result.exit_code, 0)
