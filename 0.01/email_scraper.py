# -*- coding: utf-8 -*-
"""Email Scraper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SYZwaIrD8GWtIx9STZr0c7vVCFzVMRsN

## **Basic Email scraper**

Import required modules
"""

import re
from urllib.request import urlopen

"""Setting the url you want to scrape for emails"""

def pickurl():
    global url
    url = input("Enter a url you want to scrape for emails: ")
pickurl()

#Connect to url
page = urlopen(url)
page

"""Decoding the raw html of the given url (Supports (utf-8 & cp1252))"""

html_bytes = page.read()
try:
  html = html_bytes.decode("utf-8")
except UnicodeDecodeError:
  html = html_bytes.decode("cp1252")
if html == "":
  print("Decoding failed.")
  exit()
print(html)

"""Using the re module to find emails inside the raw html"""

line = html
match = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', line)
for i in match:
    print(i)

"""(Optional) Save all emails to a .csv file"""

#Save emails to a file (Optional)
if i != "":
    global save_file
    save_file = input("Do you want to save emails to a file, y/n.")
    if save_file.lower() == "y":
        global save_as
        save_as = input("Pick file name: ")
        with open("{}.csv".format(save_as), "w") as f:
            for i in match:
                f.write(i + "\n")