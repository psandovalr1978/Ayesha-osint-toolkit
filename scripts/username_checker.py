# This script checks whether a username exists on multiple social platforms using APIs.
# scripts/username_checker.py
import requests

def check_username(platform, username):
    url = f"https://www.{platform}.com/{username}"
    response = requests.get(url)

    if response.status_code == 404:
        print(f"Username '{username}' is available on {platform}.")
    else:
        print(f"Username '{username}' is already taken on {platform}.")

if __name__ == "__main__":
    platform = input("Enter platform (e.g., github, twitter, instagram): ")
    username = input("Enter username to check: ")
    check_username(platform, username)
