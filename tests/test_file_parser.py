import unittest
from utils.file_parser import parse_file
import tempfile


class TestFileParser(unittest.TestCase):
    def test_parse_valid_csv(self):
        csv_data = "Player1,Player2\n0,0\n1,1\n3,2\n"
        with tempfile.NamedTemporaryFile(suffix=".csv", mode="w+", delete=True) as temp_file:
            temp_file.write(csv_data)
            temp_file.seek(0)
            parsed_data = parse_file(temp_file.name)
        self.assertEqual(len(parsed_data), 3)
        self.assertEqual(parsed_data.iloc[0].to_dict(), {"Player1": 0, "Player2": 0})

    def test_parse_empty_csv(self):
        csv_data = "Player1,Player2\n"
        with tempfile.NamedTemporaryFile(suffix=".csv", mode="w+", delete=True) as temp_file:
            temp_file.write(csv_data)
            temp_file.seek(0)
            parsed_data = parse_file(temp_file.name)
        self.assertEqual(len(parsed_data), 0)

    def test_invalid_file_format(self):
        with self.assertRaises(ValueError):
            parse_file("invalid_file.txt")


if __name__ == "__main__":
    unittest.main()
