import unittest
from unittest.mock import patch, MagicMock
from src.analyzer.lint_checker import LintChecker

class TestLintChecker(unittest.TestCase):

    @patch("subprocess.run")
    def test_analyze_success(self, mock_subprocess_run):
        # Setup mock for subprocess.run
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = "Linting successful"
        mock_result.stderr = ""
        mock_subprocess_run.return_value = mock_result

        # Initialize LintChecker
        checker = LintChecker()

        # Run analyze
        results = checker.analyze("./test_project")

        # Assertions
        self.assertTrue(results["success"])
        self.assertIn("Linting successful", results["output"])
        self.assertEqual(results["errors"], "")
        mock_subprocess_run.assert_called_once_with([
            "flake8", "./test_project"
        ], capture_output=True, text=True, check=True)

    @patch("subprocess.run")
    def test_analyze_failure(self, mock_subprocess_run):
        # Setup mock for subprocess.run
        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_result.stdout = ""
        mock_result.stderr = "Linting errors found"
        mock_subprocess_run.return_value = mock_result

        # Initialize LintChecker
        checker = LintChecker()

        # Run analyze
        results = checker.analyze("./test_project")

        # Assertions
        self.assertFalse(results["success"])
        self.assertIn("Linting errors found", results["errors"])
        self.assertEqual(results["output"], "")
        mock_subprocess_run.assert_called_once_with([
            "flake8", "./test_project"
        ], capture_output=True, text=True, check=True)

    @patch("subprocess.run", side_effect=Exception("Command not found"))
    def test_analyze_exception(self, mock_subprocess_run):
        # Initialize LintChecker
        checker = LintChecker()

        # Run analyze and assert exception handling
        results = checker.analyze("./test_project")

        self.assertFalse(results["success"])
        self.assertIn("Command not found", results["errors"])
        self.assertEqual(results["output"], "")
        mock_subprocess_run.assert_called_once_with([
            "flake8", "./test_project"
        ], capture_output=True, text=True, check=True)

if __name__ == "__main__":
    unittest.main()
