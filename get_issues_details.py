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
issues_list = []
for issue in issues:
	issues_list.append(issue)

#Now take a issue object and print its every details
#see https://developer.github.com/v3/issues/
issue = issues_list[5]
print (issue.id)
print (issue.url)
print (issue.title)

#Get the user detals who created the issue
issue_creater = issue.user
print (issue_creater.login)
print (issue_creater.url)
#See the link for more

#Get labels on the issue
labels = issue.labels
print (labels[0].name)

#Get assignee details on the issue
assignee = issue.assignee
print (assignee.login)
print (assignee.url)

#Get assinees details on the issue
#Apply when there are more assignees
assignees = issue.assignees
print (assignees[0].login)
print (assignees[0].url)

#Get milestone of the issue
milestone = issue.milestone
print (milestone)
if milestone is not None:
	print (milestone.description)
	#Get the details of milestone creator
	milestone_creator = milestone.creator
	print (milestone_creator.login)
else:
	pass

#Get pull request to the issue
pr = issue.pull_request
print (pr)
if pr is not None:
	print (pr.url)
else:
	pass

print (issue.created_at)

#Get the repo of the issue
repo = issue.repository
print (repo.name)
print (repo.url)

#Get the owner of the repo
owner = repo.owner
print (owner.login)
