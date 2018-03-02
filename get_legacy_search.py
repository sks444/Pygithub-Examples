from github import Github
from github_token import GITHUB_TOKEN, user, password

g1 = Github(GITHUB_TOKEN)
g2 = Github(user, password)

repo_keyword = "coala"

#Find repo by legacy search according to keyword
legacy_search_repos = g2.legacy_search_repos(repo_keyword)
for legacy_search_repo in legacy_search_repos:
	print(legacy_search_repo)

#Find users by legacy search
user_keyword = "sks444"
legacy_search_users = g2.legacy_search_users(user_keyword)
for legacy_search_user in legacy_search_users:
	print(legacy_search_user)

#Find users by email using legacy search
email = "krishnasingh.ss30@gmail.com"
legacy_search_user_by_email = g2.legacy_search_user_by_email(email)
print (legacy_search_user_by_email)

#Find issues by legacy search
keyword = "import data model"
org = "coala"
organization = g2.get_organization(org)
repo = organization.get_repo("community")
legacy_search_issues = repo.legacy_search_issues(keyword)
for legacy_search_issue in legacy_search_issues:
	print(legacy_search_issue)
