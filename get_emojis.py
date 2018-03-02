from github import Github
from github_token import GITHUB_TOKEN, user, password

g1 = Github(GITHUB_TOKEN)
g2 = Github(user, password)

#Lists all the emojis available to use on GitHub
#https://developer.github.com/v3/emojis/

emojis = g1.get_emojis()

for emoji in emojis:
	print (emoji)