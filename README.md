This project was made out of frustration for not being able to manage my saved links on reddit very easily. I wanted to be able to create a list of all of the videos that I had enjoyed, but this was not possible as there was no way to search by domain. 

The script saved.py, allows you to search by multiple critera, title, domain, and sub-reddit to look for a saved post, or posts. The webpage.py script will generate an HTML file that contains all your saved posts and then allows you to filter them by sub-reddit. You can see mine at http://owen.cymru/saved.html. 

Usage for saved.py:

    Usage:
      savedLinks [options]
    Options:
      -t, --title TITLE     Search for links based on link title
      -d, --domain DOMAIN   Search for links from a certain domain
      -r, --reddit REDDIT   Search for links based on subreddit
    
To run the webpage.py script just run:

    python webpage.py > output.html
  
Remember to edit the scripts to contain your reddit credentials!
