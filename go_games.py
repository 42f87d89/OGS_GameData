import requests
import json
from datetime import date
from sys import argv

results = []
uid = str(argv[1])
url = 'https://online-go.com/api/v1/players/'+uid+'/games/'
page = requests.get(url).content
data = json.loads(page)
username_url = 'https://online-go.com/api/v1/players/' + str(uid)
username_page = requests.get(username_url).content
username = json.loads(username_page)['username']
while url != None:
    if 'next' in data:
        url = data['next']
    else:
        url = None
    if 'results' not in data:
        continue
    for game in data['results']:
        if game['players']['black']['username'] == username:
            print(game['historical_ratings']['black']['ratings']['overall']['rating'])
        else:
            print(game['historical_ratings']['white']['ratings']['overall']['rating'])
    results = results + data['results']
    if url == None:
        break
    page = requests.get(url).content
    data = json.loads(page)

f = open(username + str(date.today()) + ".json", 'w')
f.write(json.dumps(results, indent=4))
f.close()
