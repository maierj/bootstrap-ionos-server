#!/usr/bin/env python3

import requests
import os

base_url = "https://cloudpanel-api.ionos.com/v1"


def main():
    api_key = os.environ["IONOS_API_KEY"]

    request_headers = {
        "Content-Type": "application/json",
        "X-Token": api_key
    }

    servers_response = requests.get("%s/servers" % base_url, headers=request_headers)
    print("GET Status Code: %d" % servers_response.status_code)

    servers_response_object = servers_response.json()

    for server in servers_response_object:
        delete_response = requests.delete("%s/servers/%s" % (base_url, server["id"]), headers=request_headers)
        print("DELETE Status Code: %d" % delete_response.status_code)


if __name__ == "__main__":
    main()
