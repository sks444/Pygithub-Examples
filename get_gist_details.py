from github import Github
from github_token import GITHUB_TOKEN, user, password

g1 = Github(GITHUB_TOKEN)
g2 = Github(user, password)

user = g2.get_user()
gists = user.get_gists()
starred_gists = user.get_starred_gists()
print (starred_gists)

for gist in gists:
	comments = gist.get_comments()
	for comment in comments:
		print (comment.id)
		print (comment.get_comment(comment.id))

for gist in gists:
	print (gist.is_starred())
