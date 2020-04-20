#! python

import praw

private_subreddit = 'YOUR PRIVATE SUBREDDIT'
reddit = praw.Reddit(client_id='SETUP A REDDIT DEVELOPER ACCOUNT',
                     client_secret='SETUP A REDDIT DEVELOPER ACCOUNT',
					 user_agent='python:reddit-saved-posts-achiver:0.1',
					 username='REDDIT USER NAME',
                     password='REDDIT PASSWORD')

savedlist =  []
for p in reddit.user.me().saved(limit=None):
#	print(p)
	savedlist.append(p)

#savedlist = reddit.user.me().saved(limit=None)
savedlist.reverse()

#for pst in savedlist:
#	print(pst)

for post in savedlist:#reddit.user.me().saved(limit=None):
	#print(str(post))
	#print(str(post.subreddit.display_name))
	
	if hasattr(post, 'title'):	
		post_name = str(post.title)
	else:
		print('skipped ' +'----------------------------------------------------------------------------------' +str(post.permalink))
		continue
		#post_name = '----------------------------------------------------------------------------------'
		
	if hasattr(post, 'url'):	
		post_url = str(post.url)
	else:
		print('skipped ' +'----------------------------------------------------------------------------------' +str(post.permalink))
		continue
		#post_url = '==================================================================================='	
		
	print(post_name + "   " + post_url)

	#try:
	#	semi = post_name.index(':')
	#	post_name = post_name[semi+2:]
	#except Exception:
	#	pass

	sub = str(post.subreddit.display_name)
	package = '[' + sub + ']' + ' ' + post_name
	link = post.permalink
	print (package + "    " + link)
	
	if len(package) > 299 :
		print ("post too long.. SKIPPED ============================")
		continue
	
	submission = reddit.subreddit(private_subreddit).submit( package, url = post_url)
	submission.reply('[Original Post](https://www.reddit.com'+link+') on [/r/'+sub+'](https://www.reddit.com/r/' +sub+ ')')
	
	#remove this line if you want to keep the post saved on your account.
	post.unsave()

print('done! press enter to exit.')