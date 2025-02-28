import unittest
from unittest.mock import patch
from github_api import get_user_repos, get_repo_commits, fetch_github_repos

class TestGitHubAPI(unittest.TestCase):

    @patch('github_api.requests.get')
    def test_get_user_repos(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        repos = get_user_repos("mockuser")
        self.assertEqual(len(repos), 2)
        self.assertEqual(repos[0]["name"], "repo1")

    @patch('github_api.requests.get')
    def test_get_repo_commits(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"sha": "123abc"}, {"sha": "456def"}]
        commit_count = get_repo_commits("mockuser", "repo1")
        self.assertEqual(commit_count, 2)

    @patch('github_api.requests.get')
    def test_fetch_github_repos(self, mock_get):
        def mock_side_effect(url):
            if "repos" in url:
                return unittest.mock.Mock(status_code=200, json=lambda: [{"name": "repo1"}, {"name": "repo2"}])
            elif "commits" in url:
                return unittest.mock.Mock(status_code=200, json=lambda: [{"sha": "123abc"}, {"sha": "456def"}])
            return unittest.mock.Mock(status_code=404, json=lambda: {"message": "Not Found"})

        mock_get.side_effect = mock_side_effect
        result = fetch_github_repos("mockuser")
        self.assertEqual(len(result), 2)
        self.assertIn("Repo: repo1 Number of commits: 2", result)

if __name__ == "__main__":
    unittest.main()

