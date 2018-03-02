from github import Github
from github_token import GITHUB_TOKEN, user, password

g1 = Github(GITHUB_TOKEN)
g2 = Github(user, password)

#Get events for a repo
org = "coala"
organization = g2.get_organization(org)
repo = organization.get_repo("community")
repo_events = repo.get_network_events()
for network_event in network_events:
	print (network_event)

#Get events for a org
org = "coala"
organization = g2.get_organization(org)
org_events = organization.get_events()
for org_event in org_events:
	print (org_event)
