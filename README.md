# reddit-headline-bot
Bot to scrape headlines from a subreddit

Example Usage:

python reddit.py showerthoughts 1000 headlines.txt used_ids.txt

Pulls top 1000 headlines (reddit API's limit per request) every hour that haven't already been seen, saves the headline text to headlines.txt and the Reddit id's associated with them to used_ids.txt. The only requirement is that headlines.txt and used_ids.txt already exist (can be empty).
