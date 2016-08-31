#!/bin/python2.7
import praw
import sys
import time
import fileinput

r = praw.Reddit(user_agent='saved_links')
r.login("Midasx", "**********")

added = []
first = True # Set to false for first run

while True:
    for line in fileinput.input('../www/saved.html', inplace=1):
        print line,
        if line.startswith('        <!-- Content goes here -->'):
            count = None if first else 5 # Comment out if for first run
            for submission in r.user.get_saved(limit=count, time='all'):
                if first:
                    added.append(submission)
                if submission not in added:
                    if not hasattr(submission, 'domain'):
                        continue  # Filter out saved comments
                    message = "" if submission.thumbnail != 'nsfw' else "<p style='display: inline; color: red;'>NSFW </p>"
                    sys.stdout.write("        <tr class='content " + submission.subreddit.display_name.lower().encode('utf8') + "'>\n")
                    sys.stdout.write("          <td style='vertical-align: middle; text-align: center'><input style='outline: none;' class='filter' onclick='filter(this);' type='radio' value='" + submission.subreddit.display_name.lower().encode('utf8') + "'/></td>")
                    sys.stdout.write("          <td>" + submission.subreddit.display_name.lower().encode('utf8') + "<br><a href='" + submission.short_link + "'>comments</a></td>\n")
                    sys.stdout.write("          <td>" + message + "<a href='" + submission.url.encode('utf8') + "'>" + submission.title.encode('utf8') + "</a></td>\n")
                    sys.stdout.write("        </tr>\n")
                    added.append(submission)
    first = False
    time.sleep(600)
