import requests

def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

def get_repo_commits(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return len(response.json())

def fetch_github_repos(username):
    repos = get_user_repos(username)
    if repos is None:
        return "Error fetching repositories"
    result = []
    for repo in repos:
        repo_name = repo['name']
        commit_count = get_repo_commits(username, repo_name)
        if commit_count is None:
            commit_count = "Error fetching commits"
        result.append(f"Repo: {repo_name} Number of commits: {commit_count}")
    return result
