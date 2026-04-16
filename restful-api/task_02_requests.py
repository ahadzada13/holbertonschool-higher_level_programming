#!/usr/bin/python3
"""
Consuming and processing data from an API using Python requests.
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches and prints titles of all posts from JSONPlaceholder."""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetches posts and saves them into a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    if r.status_code == 200:
        posts = r.json()
        
        # Datanı strukturlaşdırırıq
        structured_data = []
        for post in posts:
            structured_data.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            })

        # CSV faylına yazırıq
        with open('posts.csv', mode='w', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_data)
