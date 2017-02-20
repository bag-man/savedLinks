"""
Usage:
  savedLinks [options]

Options:
  -t, --title TITLE     Search for links based on link title
  -d, --domain DOMAIN   Search for links from a certain domain
  -r, --reddit REDDIT   Search for links based on subreddit
"""

from docopt import docopt
import praw
import sys

if __name__ == "__main__":
    args = docopt(__doc__)

criteria = sum(1 for v in args.values() if v is not None)

if criteria == 0:
    sys.exit(__doc__)

r = praw.Reddit(user_agent='savedSearch',
                client_id='OkDyg4-hOs-TbQ',
                client_secret='**************',
                username='Midasx',
                password='**************',)

for post in r.redditor('Midasx').saved(limit=None):
    count = 0
    if not hasattr(post, 'domain'):
        continue  # Filter out saved comments

    if args['--domain']:
        if args['--domain'].lower() == post.domain:
            count += 1

    if args['--reddit']:
        subreddit = post.subreddit.display_name.encode('ascii').lower()
        if args['--reddit'].lower() == subreddit:
            count += 1

    if args['--title']:
        if args['--title'].lower() in post.title.lower():
            count += 1

    if count == criteria:
        print(post.shortlink, " ", post.title)
