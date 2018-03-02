from github import Github
from github_token import GITHUB_TOKEN, user, password

g1 = Github(GITHUB_TOKEN)
g2 = Github(user, password)

user1 = g1.get_user()
user2 = g2.get_user()

print (user2.id)
print (user2.name)
print (user2.login)
print (user2.get_emails())

#For more options see
#http://pygithub.readthedocs.io/en/latest/github_objects/AuthenticatedUser.html
