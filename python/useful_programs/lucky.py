#!/usr/bin/python3
# This program opens google search results in a new tab
# This program search google for the command line argument passed and opens the links in the results in a new tab

import sys,webbrowser,requests,bs4,time

if(len(sys.argv) < 2):
    print("Usage: ./lucky.py [search term]")
    sys.exit()

# Print googling statement while the page download
print("Googling.....");

# searching google and getting the page
res = requests.get("https://www.google.com/search?q="+" ".join(sys.argv[1:]))
res.raise_for_status();

#  Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,"lxml");

#  Open a browser tab for each result. 
# this is a selector for the results that basically means get all the links which are inside the kCrYT class
links = soup.select('.kCrYT > a');

# if the user results are less than 6 then use the length of the links and max_pages
max_pages = min(6, len(links))

for i in range(max_pages):
    # used to prevent duplicate results
    if(links[i].get('href')[:40] == links[i+1].get('href')[:40]):
        continue

    webbrowser.open("https://www.google.com"+links[i].get('href'))
