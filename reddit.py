import praw
import time
import sys

def main(subreddit, lim, headfile, donefile):
	user_agent = "testing the PRAW API: /u/random_things_test"
	r = praw.Reddit(user_agent=user_agent)
	headlines_file = headfile
	already_done_file = donefile

	with open(already_done_file, 'r') as fread:
		already_done = fread.read().split('\n')

	headlines = []
	new_ids = []

	while True:
		submissions = r.get_subreddit(subreddit).get_hot(limit=lim)
		for submission in submissions:
			if submission.id not in already_done:
				new_ids.append(submission.id)
				title = submission.title
				headlines.append(title.encode('utf-8'))
		print "Added " + str(len(new_ids)) + " new titles"
		already_done += new_ids
		new_ids.append('')
		with open(headlines_file, 'a') as fopen:
			fopen.write('\n'.join(headlines))
		with open(already_done_file, 'a') as fopen2:
			fopen2.write('\n'.join(new_ids))
		new_ids = []
		time.sleep(3600)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]) # subreddit, limit, headlinesfile, idsfile