import os
import subprocess

class LintChecker:
    def __init__(self, linter="flake8"):
        self.linter = linter

    def analyze(self, target_path):
        """
        Run linting analysis on the target path.

        :param target_path: Path to the directory or file to analyze.
        :return: Dictionary with linting results.
        """
        if not os.path.exists(target_path):
            raise FileNotFoundError(f"Target path {target_path} does not exist.")

        print(f"Running {self.linter} on {target_path}...")

        try:
            result = subprocess.run(
                [self.linter, target_path],
                capture_output=True,
                text=True
            )
            return {
                "success": result.returncode == 0,
                "output": result.stdout,
                "errors": result.stderr
            }
        except Exception as e:
            print(f"An error occurred while running {self.linter}: {e}")
            return {
                "success": False,
                "output": "",
                "errors": str(e)
            }

if __name__ == "__main__":
    checker = LintChecker()

    # Example: Lint a local directory or file
    target = "./example_project"
    lint_results = checker.analyze(target)

    if lint_results["success"]:
        print("Linting completed successfully:")
        print(lint_results["output"])
    else:
        print("Linting failed with errors:")
        print(lint_results["errors"])
