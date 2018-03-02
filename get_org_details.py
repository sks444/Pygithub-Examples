from github import Github
from github_token import GITHUB_TOKEN, user, password

g1 = Github(GITHUB_TOKEN)
g2 = Github(user, password)

#Get org object
org = g1.get_organization('coala')
print(org)

#Get issues assigned to you in an org
issues = org.get_issues()
for issue in issues:
	print(issue)

#Get members of an org
members = org.get_members()
members_list = []
for member in members:
	members_list.append(member)

#Check if a user is in members
has_in_members = org.has_in_members(members_list[0])
print (has_in_members)

#Get public members
public_members = org.get_public_members()
public_members_list = []
for public_member in public_members:
	public_members_list.append(public_member)

#Check if a user in public memebr
has_in_public_members = org.has_in_public_members(public_members_list[0])
print (has_in_public_members)

#Get repos for an org
repos = org.get_repos()
repos_lsit=[]
for repo in repos:
	repos_lsit.append(repo)

#GEt teams for an org
teams = org.get_teams()
teams_list=[]
for team in teams:
	teams_list.append(team)
