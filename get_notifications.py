from github import Github
from github_token import GITHUB_TOKEN, user, password

g1 = Github(GITHUB_TOKEN)
g2 = Github(user, password)

user = g2.get_user()
notifications = user.get_notifications()
print(notifications)
for notification in notifications:
	print (notification)
