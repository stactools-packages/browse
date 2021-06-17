from stactools.testing import CliTestCase

from stactools.browse.commands import browse_command


class CommandsTest(CliTestCase):
    def create_subcommand_functions(self):
        return [browse_command]

    def test_help(self):
        result = self.run_command(["browse", "--help"])
        self.assertEqual(result.exit_code, 0)
