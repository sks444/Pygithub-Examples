from github import Github
from github_token import GITHUB_TOKEN, user, password

g1 = Github(GITHUB_TOKEN)
g2 = Github(user, password)

#https://developer.github.com/v3/repos/hooks/
hooks = g1.get_hooks()

names = []
for hook in hooks:
	names.append(hook.name)

#get a single hook
for name in names:
	print(g1.get_hook(name))
