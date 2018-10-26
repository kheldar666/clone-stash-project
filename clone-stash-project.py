#!/usr/local/bin/python3
import os
import stashy
import getpass

url = input("Enter the URL of BitBucket Server: ")
username = input("Enter your Username: ")
password = getpass.getpass(prompt='Enter your Password: ', stream=None)
projectkey = input("Enter Project Key: ")

stash = stashy.connect(url, username, password)
for repo in stash.projects[projectkey].repos.list():
    for url in repo["links"]["clone"]:
        if (url["name"] == "ssh"):
            os.system("git clone %s" % url["href"])
            break
