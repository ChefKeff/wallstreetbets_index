import requests
import json

f = open('secrets.json')
credentials = json.load(f)
print(credentials)

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth(credentials['api1'], credentials['api2'])

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': credentials['user'],
        'password': credentials['password']}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'bigbotman/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get("https://oauth.reddit.com/r/wallstreetbets/search/?q=flair%3Adaily%20discussion&restrict_sr=1",
                   headers=headers)
