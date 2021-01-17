import requests
from time import sleep
import json

TOKEN = "INSERT_YOUR_TOKEN_HERE"

def uploadViaPresignedURL(input_csv):
	r = requests.post("https://api2.dropbase.io/v1/pipeline/generate_presigned_url", data={'token': TOKEN})

	if (r.status_code != 200):
		print(r.status_code)
		print(r.json())

	presigned_url = r.json()["upload_url"]
	job_id = r.json()["job_id"]

	r = requests.put(presigned_url, data=open(input_csv, "rb"))

	if (r.status_code != 200):
		print(r.status_code)
		print(r.json())

	return [job_id, presigned_url]

def databaseQuery():
	REST_API_Link = "INSERT_YOUR_REST_API_LINK_HERE"
	TABLE = "INSERT_YOUR_TABLE_HERE"
	KEY = "INSERT_YOUR_REST_AUTHORIZATION_KEY_HERE"

	r = requests.get(REST_API_Link + '/' + TABLE, headers={"Authorization": KEY})

	return json.loads(r.text)

def getStatus(job_id):
	r = requests.get("https://api2.dropbase.io/v1/pipeline/run_pipeline", data={ "job_id":job_id })

	while (r.status_code == 202):
		print(r.json())
		time.sleep(1)
		r = requests.get("https://api2.dropbase.io/v1/pipeline/run_pipeline", data={ "job_id":job_id})

	print(r.status_code)

	if (r.status_code != 200):
		print("ERROR")
		print(r.status_code)
		print(r.json())
	else:
		print("SUCCESS")

j = databaseQuery()
file = open("text.json", "w")
json.dump(j, file)
file.close()