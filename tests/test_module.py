import unittest

import stactools.browse


class TestModule(unittest.TestCase):
    def test_version(self) -> None:
        self.assertIsNotNone(stactools.browse.__version__)
