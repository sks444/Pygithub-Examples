from github import Github
from github_token import GITHUB_TOKEN, user, password

g1 = Github(GITHUB_TOKEN)
g2 = Github(user, password)

print (g1.get_last_api_status_message())
print (g1.get_api_status_messages())
print (g1.get_api_status())

#print (g2.get_last_api_status_message())
#print (g2.get_api_status_messages())
#print (g2.get_api_status())
