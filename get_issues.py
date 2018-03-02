from github import Github
from github_token import GITHUB_TOKEN, user, password

g1 = Github(GITHUB_TOKEN)
g2 = Github(user, password)

user = g2.get_user()

#List all issues assigned to the authenticated
#user across all visible repositories including 
#owned repositories, member repositories, 
#and organization repositories
issues = user.get_issues()
for issue in issues:
	print (issue)
