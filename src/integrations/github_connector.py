import os
import subprocess

class GitHubConnector:
    def __init__(self, clone_dir="./cloned_repos"):
        self.clone_dir = clone_dir
        if not os.path.exists(self.clone_dir):
            os.makedirs(self.clone_dir)

    def clone_repo(self, repo_url):
        """
        Clone a GitHub repository to the local system.

        :param repo_url: The URL of the GitHub repository.
        :return: The local path to the cloned repository.
        """
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        local_path = os.path.join(self.clone_dir, repo_name)

        if os.path.exists(local_path):
            print(f"Repository already cloned at {local_path}.")
            return local_path

        print(f"Cloning repository {repo_url} to {local_path}...")
        try:
            subprocess.run([
                "git", "clone", repo_url, local_path
            ], check=True, capture_output=True)
            print("Clone successful.")
            return local_path
        except subprocess.CalledProcessError as e:
            print(f"Failed to clone repository: {e.stderr}")
            raise

if __name__ == "__main__":
    connector = GitHubConnector()

    # Example: Clone a GitHub repository
    repo_url = "https://github.com/example/repo.git"
    cloned_path = connector.clone_repo(repo_url)
    print(f"Repository cloned to: {cloned_path}")
