#!/usr/bin/python3
# Python script that fetches https

import urllib.request


def fetcher():
    """fetcher"""
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format("b" "'OK'"))
        print("\t- utf8 content: {}".format("OK"))


if __name__ == "__main__":
    fetcher()
