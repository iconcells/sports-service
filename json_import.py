import json
import requests
import bolo
from subprocess import call

with open("test.json") as data_file:
    data = [json.loads(line) for line in data_file]

    #number = next(data_file).strip()
# call('ls')

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

print json.dumps(todos, sort_keys=True,
				indent=4, separators=(',', ': '))




