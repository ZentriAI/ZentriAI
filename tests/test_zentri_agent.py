import unittest
from unittest.mock import patch, MagicMock
from src.zentri_agent import ZentriAgent

class TestZentriAgent(unittest.TestCase):

    @patch("src.zentri_agent.LintChecker")
    @patch("src.zentri_agent.ComplexityAnalyzer")
    def test_analyze_code(self, MockComplexityAnalyzer, MockLintChecker):
        # Setup mock analyzers
        lint_checker_instance = MockLintChecker.return_value
        lint_checker_instance.analyze.return_value = {"lint": "ok"}

        complexity_analyzer_instance = MockComplexityAnalyzer.return_value
        complexity_analyzer_instance.analyze.return_value = {"complexity": "low"}

        # Initialize ZentriAgent
        agent = ZentriAgent()

        # Run analyze_code
        results = agent.analyze_code("./test_project")

        # Assert analyzers were called and results match
        MockLintChecker.assert_called_once()
        MockComplexityAnalyzer.assert_called_once()
        self.assertIn("LintChecker", results)
        self.assertIn("ComplexityAnalyzer", results)
        self.assertEqual(results["LintChecker"], {"lint": "ok"})
        self.assertEqual(results["ComplexityAnalyzer"], {"complexity": "low"})

    @patch("src.zentri_agent.GitHubConnector")
    def test_fetch_and_analyze(self, MockGitHubConnector):
        # Setup mock GitHub connector
        github_instance = MockGitHubConnector.return_value
        github_instance.clone_repo.return_value = "./cloned_repo"

        # Mock analyze_code
        with patch.object(ZentriAgent, "analyze_code", return_value={"mock_analysis": "success"}) as mock_analyze_code:
            # Initialize ZentriAgent
            agent = ZentriAgent()

            # Run fetch_and_analyze
            results = agent.fetch_and_analyze("https://github.com/example/repo.git")

            # Assert GitHubConnector and analyze_code were called
            MockGitHubConnector.assert_called_once()
            github_instance.clone_repo.assert_called_once_with("https://github.com/example/repo.git")
            mock_analyze_code.assert_called_once_with("./cloned_repo")

            # Assert results
            self.assertEqual(results, {"mock_analysis": "success"})

if __name__ == "__main__":
    unittest.main()
