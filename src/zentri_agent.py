import os
import json
from src.analyzer.lint_checker import LintChecker
from src.analyzer.complexity_analyzer import ComplexityAnalyzer
from src.integrations.github_connector import GitHubConnector
from src.integrations.gitlab_connector import GitLabConnector

class ZentriAgent:
    def __init__(self):
        self.analyzers = [
            LintChecker(),
            ComplexityAnalyzer()
        ]
        self.integrations = {
            "github": GitHubConnector(),
            "gitlab": GitLabConnector()
        }

    def analyze_code(self, target_path):
        if not os.path.exists(target_path):
            raise FileNotFoundError(f"Target path {target_path} does not exist.")

        results = {}
        print(f"Starting analysis on: {target_path}")

        for analyzer in self.analyzers:
            analyzer_name = analyzer.__class__.__name__
            print(f"Running {analyzer_name}...")
            results[analyzer_name] = analyzer.analyze(target_path)

        print("Analysis completed.")
        return results

    def fetch_and_analyze(self, repo_url, platform="github"):
        if platform not in self.integrations:
            raise ValueError(f"Unsupported platform: {platform}")

        connector = self.integrations[platform]
        print(f"Fetching repository from {repo_url} using {platform} connector...")
        local_path = connector.clone_repo(repo_url)

        print("Repository fetched. Starting analysis...")
        return self.analyze_code(local_path)

if __name__ == "__main__":
    agent = ZentriAgent()

    # Example: Analyze a local project
    local_results = agent.analyze_code("./example_project")
    print(json.dumps(local_results, indent=4))

    # Example: Fetch and analyze a GitHub repository
    # Uncomment the following lines to test fetching and analyzing a remote repo
    # repo_results = agent.fetch_and_analyze("https://github.com/example/repo.git", platform="github")
    # print(json.dumps(repo_results, indent=4))
