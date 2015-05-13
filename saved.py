#!/bin/python2.7
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

r = praw.Reddit(user_agent='saved_links')
r.login("USERNAME", "PASSWORD")

for submission in r.user.get_saved(limit=None, time='all'):
    count = 0
    if not hasattr(submission, 'domain'):
        continue  # Filter out saved comments

    if args['--domain']:
        if args['--domain'].lower() == submission.domain:
            count += 1

    if args['--reddit']:
        if args['--reddit'].lower() == submission.subreddit.display_name.encode('ascii').lower():
            count += 1

    if args['--title']:
        if args['--title'].lower() in submission.title.lower():
            count += 1

    if count == criteria:
        print submission.title.encode('utf-8'), " ", submission.short_link
