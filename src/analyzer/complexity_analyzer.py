import os
import radon.complexity as radon_complexity
from radon.visitors import ComplexityVisitor

class ComplexityAnalyzer:
    def __init__(self):
        pass

    def analyze(self, target_path):
        """
        Analyze the cyclomatic complexity of the Python files in the target path.

        :param target_path: Path to the directory or file to analyze.
        :return: Dictionary with complexity results.
        """
        if not os.path.exists(target_path):
            raise FileNotFoundError(f"Target path {target_path} does not exist.")

        results = {}
        if os.path.isdir(target_path):
            for root, _, files in os.walk(target_path):
                for file in files:
                    if file.endswith(".py"):
                        file_path = os.path.join(root, file)
                        results[file_path] = self._analyze_file(file_path)
        elif target_path.endswith(".py"):
            results[target_path] = self._analyze_file(target_path)
        else:
            raise ValueError("Target path must be a Python file or directory containing Python files.")

        return results

    def _analyze_file(self, file_path):
        """
        Analyze the cyclomatic complexity of a single Python file.

        :param file_path: Path to the Python file.
        :return: List of functions/methods with their complexity scores.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                code = f.read()

            visitor = ComplexityVisitor.from_code(code)
            return [
                {
                    "name": item.name,
                    "complexity": item.complexity,
                    "type": item.type
                }
                for item in visitor.functions + visitor.methods
            ]
        except Exception as e:
            print(f"Error analyzing file {file_path}: {e}")
            return []

if __name__ == "__main__":
    analyzer = ComplexityAnalyzer()

    # Example: Analyze complexity of a local directory or file
    target = "./example_project"
    complexity_results = analyzer.analyze(target)

    for file, results in complexity_results.items():
        print(f"File: {file}")
        for item in results:
            print(f"  - {item['name']} (Type: {item['type']}, Complexity: {item['complexity']})")
