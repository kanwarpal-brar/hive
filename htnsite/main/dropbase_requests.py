import requests
from time import sleep
import json

TOKEN = "3pRbuKcaKskkxmW9EEavpq"

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
	REST_API_Link = "https://query.dropbase.io/8FNdXUrN82TaZDks2p3YLc"
	TABLE = "hive_deploy_table"
	KEY = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhYmFzZUlkIjoiOEZOZFhVck44MlRhWkRrczJwM1lMYyIsImFjY2Vzc1Blcm0iOiJmdWxsIiwidG9rZW5JZCI6Ind1UEZjZE5Lc3JaMURVZ3BQWElzanc3QmpLR0dTdHZqTXpHNjREbndMRGRDbEtiRmxGaDc0OWxLV0t3RXVjbEsiLCJpYXQiOjE2MTA4NzQxMzQsImV4cCI6MTYxMDk2MDUzNCwiaXNzIjoiZHJvcGJhc2UuaW8iLCJzdWIiOiJjcHpUVVJqakhyVHY5amY4bVhtcGZzIn0.UHDIhRCarNhvyINfgSuEV5AD205kLcHsJFuRYyTblCc"

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