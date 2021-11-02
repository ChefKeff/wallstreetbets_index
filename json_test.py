import json

f = open('response_test.json', 'r')
json = json.load(f)

if json[0]['kind'] == 'Listing':
    json_data = json[0]['data']

print(json_data['children'][0]['data']['selftext'])