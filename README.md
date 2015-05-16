This project was made out of frustration for not being able to manage my saved links on reddit very easily. I wanted to be able to create a list of all of the videos that I had enjoyed, but this was not possible as there was no way to search by domain. 

The script saved.py, allows you to search by multiple critera, title, domain, and sub-reddit to look for a saved post, or posts. The webpage.py script will add all of your saved links to an HTML template, then update the file every 10 minutes to include any new additions; this has a bonus benefit of being able to store more than the 1000 saved links that reddit allows you.

You can see mine at [owen.cymru/saved](http://owen.cymru/saved)

Usage for saved.py:

    Usage:
      savedLinks [options]
    Options:
      -t, --title TITLE     Search for links based on link title
      -d, --domain DOMAIN   Search for links from a certain domain
      -r, --reddit REDDIT   Search for links based on subreddit
    
To run the webpage.py script just run:

    python webpage.py
  
Remember to edit the scripts to contain your reddit credentials, and for the website.py change the path to the HTML template. 
