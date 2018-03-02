from github import Github
from github_token import GITHUB_TOKEN, user, password

g1 = Github(GITHUB_TOKEN)
g2 = Github(user, password)

#List all templates available to pass
#as an option when creating a repository
gitignore_templates = g1.get_gitignore_templates()
print(gitignore_templates)

for gitignore_template in gitignore_templates:
	name = gitignore_template
	print (name)
	print (g1.get_gitignore_template(name))
