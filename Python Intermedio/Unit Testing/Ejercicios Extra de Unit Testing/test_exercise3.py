import unittest
from unittest.mock import mock_open, patch

from exercise3 import read_lines


class TestReadLines(unittest.TestCase):
    
    def test_returns_expected_lines_from_mocked_file(self):
        # Arrange
        mocked_content = "linea 1\nlinea 2\nlinea 3\n"
        with patch("builtins.open", mock_open(read_data=mocked_content)) as mocked_file:
            # Act
            result = read_lines("fake_path.txt")

        # Assert
        mocked_file.assert_called_once_with("fake_path.txt", "r")
        self.assertEqual(result, ["linea 1\n", "linea 2\n", "linea 3\n"])

    def test_raises_file_not_found_error_when_file_does_not_exist(self):
        # Arrange
        with patch("builtins.open", side_effect=FileNotFoundError):
            # Act & Assert
            with self.assertRaises(FileNotFoundError):
                read_lines("missing_file.txt")


if __name__ == "__main__":
    unittest.main()
