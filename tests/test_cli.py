import unittest
from unittest.mock import patch

from digipathos.cli import browser


class CliTests(unittest.TestCase):

    @patch("builtins.input", return_value="invalid_option")
    def test_invalid_command_throws_exception(self, mock_input):
        with self.assertRaises(Exception) as e:
            browser.read_command()
            self.assertEqual(e.message, "Invalid command")


if __name__ == "__main__":
    unittest.main()
