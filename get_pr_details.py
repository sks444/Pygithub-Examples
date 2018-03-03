from github import Github
from github_token import GITHUB_TOKEN, user, password

g1 = Github(GITHUB_TOKEN)
g2 = Github(user, password)

org = g1.get_organization('coala')
repo = org.get_repo('community')

#Get pull requests for a repo
pulls = repo.get_pulls()
pulls_numbers_list = []
for pull in pulls:
	pulls_numbers_list.append(pull.number)

#Get a pull request by its number
pull = repo.get_pull(pulls_numbers_list[0])

#Get pull request details
#see https://developer.github.com/v3/pulls/
#for more options
print (pull.url)
print (pull.issue_url)
print (pull.number)

#For getting details of
#assignee, labels and milestone
#see get_issues_details.py

print (pull.created_at)
print (pull.updated_at)
print (pull.merged_at)

#Get the head details of the pr
head = pull.head
print (head.label)
print (head.sha)

#Get the user for the head
user = head.user
print (user.login)
print (user.url)

#Get the repo of the head
repo = head.repo
print (repo.id)
print (repo.owner)
print (repo.name)
print (repo.url)

#Get the base of the pr
base = pull.base
print (base.label)
print (base.sha)

#Get the user for the base
#Similar to head

#Get the creator of the pr
user = pull.user
print (user.login)
