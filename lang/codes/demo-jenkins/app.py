import requests
import json

# Jenkins URL
url = "http://172.16.5.108:8082"

# Jenkins Credentials
username = "admin"
password = "52117e17f9e445a3b449c58d166e262d"

# API endpoint to get all jobs
api_endpoint = url + "/api/json"

# make request with authentication
response = requests.get(api_endpoint, auth=(username, password))

# load response content as json
jobs = json.loads(response.content.decode('utf-8'))
# print(jobs)

# iterate over jobs and get their details
for job in jobs["jobs"]:
    job_name = job["name"]
    job_url = job["url"]
    
    # API endpoint to get job details
    job_api_endpoint = url + "/job/" + job["name"] + "/api/json"
    
    # make request with authentication
    response = requests.get(job_api_endpoint, auth=(username, password))
    
    # load response content as json
    job_details = json.loads(response.content.decode('utf-8'))
    if job_details["name"] == "jenkins-pipeline-test":
        print(job_details)
    # get job's last build details
    # last_build_number = job_details["lastBuild"]["number"]
    # last_build_url = job_details["lastBuild"]["url"]
    
    # # API endpoint to get last build details
    # last_build_api_endpoint = last_build_url + "api/json"
    
    # # make request with authentication
    # response = requests.get(last_build_api_endpoint, auth=(username, password))
    
    # # load response content as json
    # last_build_details = json.loads(response.content.decode('utf-8'))
    
    # # get last build's result
    # last_build_result = last_build_details["result"]
    
    # # print job name, last build number and result
    # print(job_name + ": #" + str(last_build_number) + ", result: " + last_build_result)