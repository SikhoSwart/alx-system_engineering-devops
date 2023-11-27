#!/usr/bin/python3
"""
Extend task #0's script to export data in the CSV format.
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    USER_ID = argv[1]
    usereq = requests.get("{}users/{}".format(url, USER_ID)).json()
    USERNAME = usereq["username"]
    todoreq = requests.get("{}todos?userId={}".format(url, USER_ID)).json()
    file_name = "{}.csv".format(USER_ID)
    with open(file_name, "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for user in todoreq:
            writer.writerow([USER_ID, USERNAME, user.get("completed"),
                             user.get("title")])
