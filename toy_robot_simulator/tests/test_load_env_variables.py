import os
import unittest
import test_setup
from unittest.mock import patch


class TestEnvVariables(unittest.TestCase):
    @patch('os.environ', {'TABLE_X': '5'})
    def test_env(self):
        self.assertEqual(os.environ.get("TABLE_X"), str(5))

    @patch('os.environ', {})
    def test_invalid_env(self):
        self.assertEqual(os.environ.get("JUNK"), None)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
