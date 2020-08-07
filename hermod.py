import praw
from configparser import SafeConfigParser
from pathlib import Path

user_list = "user_list.txt"
message = "message.txt"

config = SafeConfigParser()
config.read('config.ini')

def login():
	return praw.Reddit(
		username=config.get('user_section', 'username'), 
		password=config.get('user_section', 'password'),
		client_id=config.get('user_section', 'client_id'),
		client_secret=config.get('user_section', 'client_secret'),
		user_agent=config.get('user_section', 'user_agent'))	


if(len(sys.argv)>2):
	reddit = login()		
	if not Path(user_list).is_file():
		with open(user_list, "a") as f:
			comment = reddit.comment(url=config.get('submission_section', 'submission url'))
			comment.refresh()
			for reply in comment.replies:
				f.write(reply.author.name+"\n")

	else: 
		with open(user_list, "r") as f, open("message.txt", "r") as body:
			text = body.read()
			for line in f:
				reddit.redditor(line).message(sys.argv[1], text)

else:
	print("Missing arguments!")
