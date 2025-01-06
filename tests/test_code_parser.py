import unittest
from unittest.mock import patch, mock_open
from src.code_parser import CodeParser

class TestCodeParser(unittest.TestCase):

    @patch("os.path.isdir")
    @patch("os.walk")
    @patch("builtins.open", new_callable=mock_open, read_data="def test_function():\n    pass")
    def test_parse_directory(self, mock_open, mock_walk, mock_isdir):
        mock_isdir.return_value = True
        mock_walk.return_value = [
            ("/test", ("subdir",), ("file1.py", "file2.py")),
            ("/test/subdir", (), ("file3.py",))
        ]

        parser = CodeParser()
        parsed_files = parser.parse_directory("/test")

        self.assertEqual(len(parsed_files), 3)
        for ast_node in parsed_files:
            self.assertIsNotNone(ast_node)

    @patch("os.path.isfile")
    @patch("builtins.open", new_callable=mock_open, read_data="def test_function():\n    pass")
    def test_parse_file(self, mock_open, mock_isfile):
        mock_isfile.return_value = True

        parser = CodeParser()
        ast_node = parser.parse_file("/test/file.py")

        self.assertIsNotNone(ast_node)

    def test_extract_functions(self):
        code = """def func1():\n    pass\n\ndef func2():\n    pass"""

        parser = CodeParser()
        ast_node = parser.parse_file = patch("builtins.open", mock_open(read_data=code)).start()
        functions = parser.extract_functions(ast_node)

        self.assertEqual(len(functions), 2)
        self.assertIn("func1", functions)
        self.assertIn("func2", functions)

if __name__ == "__main__":
    unittest.main()
