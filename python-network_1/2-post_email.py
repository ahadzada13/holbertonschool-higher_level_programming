#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter,
and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Parametrləri lüğət (dict) formatında hazırlayırıq
    values = {'email': email}
    
    # Məlumatı URL formatına salırıq (email=hr@holbertonschool.com)
    # və sonra bayt (bytes) formatına çeviririk
    data = urllib.parse.urlencode(values).encode('ascii')
    
    # Sorğunu hazırlayırıq və göndəririk
    request = urllib.request.Request(url, data)
    
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
