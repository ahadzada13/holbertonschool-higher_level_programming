#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the X-Request-Id
variable found in the header of the response using requests.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    # headers.get() metodu lüğətdən açarı tapmaq üçün ən təhlükəsiz yoldur
    print(r.headers.get('X-Request-Id'))
