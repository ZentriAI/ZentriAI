import os
import ast

class CodeParser:
    def __init__(self):
        self.parsed_files = []

    def parse_directory(self, directory_path):
        """
        Recursively parse Python files in a directory.

        :param directory_path: Path to the directory to parse.
        :return: List of parsed AST nodes.
        """
        if not os.path.isdir(directory_path):
            raise ValueError(f"Invalid directory path: {directory_path}")

        self.parsed_files = []
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    self.parsed_files.append(self.parse_file(file_path))

        return self.parsed_files

    def parse_file(self, file_path):
        """
        Parse a single Python file to generate an AST.

        :param file_path: Path to the Python file.
        :return: AST node.
        """
        if not os.path.isfile(file_path):
            raise ValueError(f"Invalid file path: {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                code = f.read()
            return ast.parse(code, filename=file_path)
        except (SyntaxError, UnicodeDecodeError) as e:
            print(f"Failed to parse {file_path}: {e}")
            return None

    def extract_functions(self, ast_node):
        """
        Extract all function definitions from an AST node.

        :param ast_node: The AST node to extract functions from.
        :return: List of function names.
        """
        if not ast_node:
            return []

        return [
            node.name for node in ast.walk(ast_node) if isinstance(node, ast.FunctionDef)
        ]

if __name__ == "__main__":
    parser = CodeParser()

    # Example: Parse a directory and extract function names from all Python files
    directory_path = "./example_project"
    parsed_nodes = parser.parse_directory(directory_path)

    for node in parsed_nodes:
        if node:
            functions = parser.extract_functions(node)
            print(f"Functions found: {functions}")
