# -*- encoding: utf-8 -*-

# python3.6+ 运行此脚本

import urllib.request
import json
import base64

# Jenkins URL和API Token
username = "admin"
api_url = 'http://172.16.5.108:8082'
api_token = '11989fb125a0640799409326072ce1e7fa'
job_name = 'test'


api_endpoint = f"{api_url}/api/json"
auth_string = f"{username}:{api_token}"
request = urllib.request.Request(api_endpoint)
base64_auth = base64.b64encode(auth_string.encode('ascii')).decode('ascii')
request.add_header(f"Authorization", f"Basic {base64_auth}")
response = urllib.request.urlopen(request)
jobs = json.load(response)
for job in jobs["jobs"]:
    job_name = job["name"]
    job_url = job["url"]
    
    # API endpoint to get job details
    job_api_endpoint = f"{api_url}/job/{job['name']}/api/json"
    request = urllib.request.Request(job_api_endpoint)
    request.add_header(f"Authorization", f"Basic {base64_auth}")
    response = urllib.request.urlopen(request)
    job_details = json.load(response)
    if job_details["name"] == job_name:
        print(job_details)


# Get the latest build number
# latest_build_url = f"{api_url}/job/{job_name}/lastBuild/api/json"
# req = urllib.request.Request(latest_build_url)
# auth_string = f"{username}:{api_token}"
# base64_auth = base64.b64encode(auth_string.encode('ascii')).decode('ascii')
# req.add_header(f"Authorization", f"Basic {base64_auth}")
# response = urllib.request.urlopen(req)
# data = json.load(response)
# latest_build_number = data['number']

# Get the list of running builds
# running_builds_url = f"{api_url}/queue/api/json"
# req = urllib.request.Request(running_builds_url)
# req.add_header(f"Authorization", f"Basic {base64_auth}")
# response = urllib.request.urlopen(req)
# data = json.load(response)
# items = data['items']

# Stop all builds that are not the latest build
# for item in items:
#     print(item)
#     if item['task']['name'] == job_name and item['executable']['number'] != latest_build_number:
#         stop_build_url = f"{api_url}/queue/item/{item['id']}/cancelQueue"
#         req = urllib.request.Request(stop_build_url, method='POST')
#         req.add_header("Authorization", f"Basic {base64_auth}")
#         response = urllib.request.urlopen(req)
#         # print(f"Build {item['executable']['number']} has been aborted.")
#         print(response)