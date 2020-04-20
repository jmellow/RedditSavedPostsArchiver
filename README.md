# RedditSavedPostsArchiver
Takes saved reddit posts and puts them in a private subreddit. This gets around the limits reddit has on recalling saved posts.
its also a good way to share saved posts with people you TRUST with your saved posts :)

this is a "works for me" solution, take care to make a test account if you are concerned about losing data.

STEPS:
1. you will obviously need python and use pip or something to install praw

2. FOLLOW THESE INSTRUCTIONS TO GET YOUR client_id and client_secret
https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example
https://www.reddit.com/prefs/apps

3. Remember to change these values:
private_subreddit = 'YOUR PRIVATE SUBREDDIT'
client_id='SETUP A REDDIT DEVELOPER ACCOUNT'
client_secret='SETUP A REDDIT DEVELOPER ACCOUNT'
username='REDDIT USER NAME'
password='REDDIT PASSWORD'


NOTES:
1. after running the program, maybe remove username password from the file, so its not sitting there with your log in creds, unless you dont care.

2. this python app will unsave posts that have been added to the private subreddit
just put a # before post.unsave() if you want to keep those
	#remove this line if you want to keep the post saved on your account.
	post.unsave()