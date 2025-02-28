import unittest
from github_api import get_user_repos, get_repo_commits, fetch_github_repos

class TestGitHubAPI(unittest.TestCase):
    def test_get_user_repos(self):
        repos = get_user_repos("octocat")
        self.assertIsInstance(repos, list)

    def test_get_repo_commits(self):
        commits = get_repo_commits("octocat", "Hello-World")
        self.assertIsInstance(commits, int)

    def test_fetch_github_repos(self):
        result = fetch_github_repos("octocat")
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()
