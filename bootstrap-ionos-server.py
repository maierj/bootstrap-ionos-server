#!/usr/bin/env python3

import requests
import os
import json

base_url = "https://cloudpanel-api.ionos.com/v1"

def main():
    server_name = os.environ["IONOS_SERVER_NAME"]
    ssh_public_key = os.environ["IONOS_SSH_PUBLIC_KEY"]
    api_key = os.environ["IONOS_API_KEY"]

    request_headers = {
        "Content-Type": "application/json",
        "X-Token": api_key
    }

    request_body = {
        "name": server_name,
        "server_type": "cloud",
        "hardware": {
            "vcore": 1,
            "cores_per_processor": 1,
            "ram": 1,
            "hdds": [
                {
                    "is_main": True,
                    "size": 20
                }
            ]
        },
        "appliance_id": "B0E9BF5BA7B56EAA027582A0784357B3",
        "datacenter_id": "4EFAD5836CE43ACA502FD5B99BEE44EF",
        "ssh_password": False,
        "rsa_key": ssh_public_key,
        "user_data_content_type": "sh",
        "power_on": True
    }

    response = requests.post("%s/servers" % base_url, headers=request_headers, data=json.dumps(request_body))

    print("Received response: %s" % response.text)


if __name__ == "__main__":
    main()
