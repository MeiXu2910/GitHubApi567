# GitHub API 567 - Automated Testing

This project uses Python to fetch repository information and commit counts for a specified GitHub user via the GitHub API. It integrates **GitHub Actions** and **CircleCI** for automated testing.

## 📌 Features
- Retrieve all repository names of a GitHub user
- Fetch the number of commits for each repository
- Automated testing using GitHub Actions & CircleCI

## 🚀 Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/MeiXu2910/GitHubApi567.git
   cd GitHubApi567
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**
   ```bash
   python github_api.py
   ```
   Enter a GitHub username to view repository and commit information.

## 🔍 Testing
**This project includes automated testing via GitHub Actions & CircleCI.**

Run tests manually:
```bash
python -m unittest test_github_api.py
```

## ✅ CI/CD Status
### **GitHub Actions**
![GitHub Actions Status](https://github.com/MeiXu2910/GitHubApi567/actions/workflows/python-app.yml/badge.svg)

### **CircleCI**
[![CircleCI](https://circleci.com/gh/MeiXu2910/GitHubApi567.svg?style=svg)](https://circleci.com/gh/MeiXu2910/GitHubApi567)

## 📄 API Reference
### **Retrieve all repositories of a user**
```
GET https://api.github.com/users/{username}/repos
```
### **Retrieve commit history of a repository**
```
GET https://api.github.com/repos/{username}/{repo}/commits
```

## 📌 Contributing
Pull Requests and Issues are welcome!

# GitHubApi567
## 📦 Deliverables
1. **GitHub Repository URL**:  
   - [GitHubApi567 Repository](https://github.com/MeiXu2910/GitHubApi567)

2. **Implemented Features**:
   - Fetching user repositories from GitHub.
   - Counting commits for each repository.
   - Displaying repository names with commit counts.

3. **Automated Testing Integration**:
   - GitHub Actions & CircleCI status badges.
   - `unittest` framework for validation.
   - Ensures correct API responses and handles errors.

4. **Development Reflections**:
   - Thought process behind designing testable functions.
   - Key considerations and challenges faced during testing.
   - Importance of integrating CI/CD for reliability.

