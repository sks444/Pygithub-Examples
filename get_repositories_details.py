from github import Github
from github_token import GITHUB_TOKEN, user, password

g1 = Github(GITHUB_TOKEN)
g2 = Github(user, password)

user = g2.get_user()

#Get repositories for authenticated user
repositories = user.get_repos()

#Get repositories for an organization
org = g1.get_organization('coala')
repos = org.get_repos()
repos_id_lsit=[]
for repo in repos:
	repos_id_lsit.append(repo.id)

#Get assignees for a repo
repo = org.get_repo('community')
assignees = repo.get_assignees()
assignees_list = []
for assignee in assignees:
	assignees_list.append(assignee)

#Check if an assignee is in list of assignees
has_in_assignees = repo.has_in_assignees(assignees_list[0])
print (has_in_assignees)

#Get branches for a repo
branches = repo.get_branches()
branches_list = []
for branch in branches:
	branches_list.append(branch)

#Get a single branch for a repo
branch = repo.get_branch(branches_list[0])

#Get collaborators for a repo
collaborators = repo.get_collaborators()
collaborators_list = []
for collaborator in collaborators:
	collaborators_list.append(collaborator)

#Check if a collaborator is in collaborators_list
has_in_collaborators = repo.has_in_collaborators(collaborators_list[0])

#Get comments on a repo
comments = repo.get_comments()
comments_id_list = []
for comment in comments:
	comments_id_list.append(comment.id)

#Get a comment by its id
comment = repo.get_comment(comments_id_list[0])

#Get commits to a repo
commits = repo.get_commits()
commits_sha_list = []
for commit in commits:
	commits_sha_list.append(commit.sha)

#Get a single commit by its sha
commit = repo.get_commit(commits_sha_list[0])

#Get comments on a sha
comments = commit.get_comments()

#Get contributors to a repo
contributors = repo.get_contributors()

#Get downloads of a repo
downloads = repo.get_downloads()
downloads_id_list = []
for download in downloads:
	downloads_id_list.append(download.id)

download = repo.download(downloads_id_list[0])

#Get events for a repo
events = repo.get_events()

#Get forks for a repo
forks = repo.get_forks()

#Get issues for a repo
issues = repo.get_issues()
issues_number_list = []
for issue in issues:
	issues_number_list.append(issue.number)

#Get a issue by its number
issue = repo.get_issue(issues_number_list[0])
print(issue)

#Get events of an issue
issue_events = issue.get_events()

#Get comments on a perticular issue
comments = issue.get_comments()

#Get labels on a perticular issue
labels = issue.get_labels()

#Get reactions on a perticular issue
reactions = issue.get_reactions()

#Get comments on all the issues for a repo
issues_comments = repo.get_issues_comments()
issues_comments_id_list = []
for issues_comment in issues_comments:
	issues_comments_id_list.append(issues_comment.id)

#Get issue_comment by its id
issue_comment = issue.get_comment(issues_comments_id_list[0])

#Get reactions on a issue comment
issue_comment_reactions = issue_comment.get_reactions()

#Get events of issues
issues_events = repo.get_issues_events()
issues_events_id_list = []
for issues_event in issues_events:
	issues_events_id_list.append(issues_event.id)

#Get event by its id on issues
issues_event = repo.get_issues_event(issues_events_id_list[0])

#Get labels used in a repo
labels = repo.get_labels()
label_list_name = []
for label in labels:
	label_list_name.append(label.name)

#Get label used in a repo by its name
label = repo.get_label(label_list_name[0])

#Get languages used in a repo
languages = repo.get_languages()
languages_list = []
for language in languages:
	languages_list.append(language)

#Get milestones of a repo
milestones = repo.get_milestones()
milestones_numbers_list = []
for milestone in milestones:
	milestones_numbers_list.append(milestone.number)

#Get sinlge milestone by its number
milestone = repo.get_milestone(milestones_numbers_list[0])

#Get labels on the milestone
milestone_labels = milestone.get_labels()

#Get pull requests for a repo
pulls = repo.get_pulls()
pulls_numbers_list = []
for pull in pulls:
	pulls_numbers_list.append(pull.number)

#Get a pull request by its number
pull = repo.get_pull(pulls_numbers_list[0])

#Get comments on a PR
comments = pull.get_comments()
comments_id_list = []
for comment in comments:
	comments_id_list.append(comment.id)

#Get a single comment on a PR
comment = pull.get_comment(comments_id_list[0])

#Get reactions on that comment
reactions = comment.get_reactions()

#Get commits on a PR
commits = pull.get_commits()

#Get files in a PR
files = pull.get_files()

#Check if a PR is merged
is_merged = pull.is_merged()

#Get the requested reviewers on a PR
requested_reviewers = pull.get_reviewer_requests()

#Get reviews on a PR
reviews = pull.get_reviews()
reviews_id_list = []
for review in reviews:
	reviews_id_list.append(review.id)

#Get single review by its id
review = pull.get_review(reviews_id_list[0])

#Get all the comments of all PR
pulls_comments = repo.get_pulls_comments()

#Get readme of a repo
readme = repo.get_readme()

#Get releases of a repo
releases = repo.get_releases()
releases_id_list = []
for release in releases:
	releases_id_list.append(release.id)

#Get a single release detail by its id
release = repo.get_release(releases_id_list[0])
print (release)

#Get the latest release
latest_release = repo.get_latest_release()
print (latest_release)

#Get stargazers for a repo
stargazers = repo.get_stargazers_with_dates()
#OR
#stargazers = repo.get_stargazers()

#Get code frequency stats for a repo
code_frequency = repo.get_stats_code_frequency()

#Get commit activity stats for a repo
commit_activity = repo.get_stats_commit_activity()

#Get contributors stats for a repo
contributors_stats = repo.get_stats_contributors()

#Get participation stats for a repo
participation_stats = repo.get_stats_participation()

#Get punch card stats for a repo
punch_card_stats = repo.get_stats_punch_card()

#Get subscribers for a repo
subscribers = repo.get_subscribers()

#Get tags of a repo
tags = repo.get_tags()

#Get teams of a repo
teams = repo.get_teams()

#Get watchers of a repo
watchers = repo.get_watchers()

#Get all the repo on Github
repos = g2.get_repos()
repos_id_lsit = []
for repo in repos:
	repos_id_lsit.append(repo.id)

#Get a repo by its id
repo = g2.get_repo(repos_id_lsit[0])
