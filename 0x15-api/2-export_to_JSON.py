#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    USER_ID = argv[1]
    usereq = requests.get("{}users/{}".format(url, USER_ID)).json()
    USERNAME = usereq["username"]
    todoreq = requests.get("{}todos?userId={}".format(url, USER_ID)).json()
    file_name = "{}.json".format(USER_ID)
    display = {USER_ID: []}
    with open(file_name, "w") as f:
        for user in todoreq:
            data = {"task": user.get("title"),
                    "completed": user.get("completed"),
                    "username": USERNAME}
            display.get(USER_ID).append(data)
        json.dump(display, f)
