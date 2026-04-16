#!/usr/bin/python3
"""
Uses the GitHub API to display the user id using Basic Authentication
with a personal access token.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    # HTTP Basic Authentication istifadə edirik
    r = requests.get(url, auth=(username, password))
    try:
        print(r.json().get('id'))
    except ValueError:
        print("None")
