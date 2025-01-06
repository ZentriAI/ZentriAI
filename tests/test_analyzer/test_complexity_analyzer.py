import unittest
from unittest.mock import patch, mock_open
from src.analyzer.complexity_analyzer import ComplexityAnalyzer

class TestComplexityAnalyzer(unittest.TestCase):

    @patch("os.path.exists")
    @patch("os.path.isdir")
    @patch("os.walk")
    @patch("builtins.open", new_callable=mock_open, read_data="def test_function():\n    pass")
    @patch("radon.visitors.ComplexityVisitor.from_code")
    def test_analyze_directory(self, mock_visitor, mock_open, mock_walk, mock_isdir, mock_exists):
        mock_exists.return_value = True
        mock_isdir.return_value = True
        mock_walk.return_value = [
            ("/test", ("subdir",), ("file1.py", "file2.py")),
            ("/test/subdir", (), ("file3.py",))
        ]
        mock_visitor.return_value = MagicMock(functions=[
            MagicMock(name="func1", complexity=5, type="function"),
            MagicMock(name="func2", complexity=8, type="function")
        ])

        analyzer = ComplexityAnalyzer()
        results = analyzer.analyze("/test")

        self.assertEqual(len(results), 3)
        for file, functions in results.items():
            for func in functions:
                self.assertIn("name", func)
                self.assertIn("complexity", func)
                self.assertIn("type", func)

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data="def test_function():\n    pass")
    @patch("radon.visitors.ComplexityVisitor.from_code")
    def test_analyze_file(self, mock_visitor, mock_open, mock_exists):
        mock_exists.return_value = True
        mock_visitor.return_value = MagicMock(functions=[
            MagicMock(name="func1", complexity=5, type="function")
        ])

        analyzer = ComplexityAnalyzer()
        results = analyzer.analyze("/test/file.py")

        self.assertEqual(len(results), 1)
        self.assertIn("/test/file.py", results)
        self.assertEqual(len(results["/test/file.py"]), 1)
        self.assertEqual(results["/test/file.py"][0]["name"], "func1")
        self.assertEqual(results["/test/file.py"][0]["complexity"], 5)
        self.assertEqual(results["/test/file.py"][0]["type"], "function")

if __name__ == "__main__":
    unittest.main()
