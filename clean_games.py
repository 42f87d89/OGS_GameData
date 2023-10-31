import json
from datetime import datetime, date
from sys import argv

filename = argv[1]

file = open(filename,'r')
output = open(filename.split('.')[0] + '_clean' + '.json', 'w')

data = json.load(file)

clean_games = []

for game in data:
    clean_game = {}
    players = game['players']
    black = players['black']
    white = players['white']

    clean_game['black_id'] = black['id']
    clean_game['black_username'] = black['username']
    clean_game['black_rating'] = game['historical_ratings']['black']['ratings']['overall']['rating']
    clean_game['white_id'] = white['id']
    clean_game['white_username'] = white['username']
    clean_game['white_rating'] = game['historical_ratings']['white']['ratings']['overall']['rating']

    clean_game['id'] = game['id']
    clean_game['width'] = game['width']
    clean_game['ranked'] = game['ranked']
    clean_game['handicap'] = game['handicap']
    clean_game['tournament'] = game['tournament']
    clean_game['black_lost'] = game['black_lost']
    clean_game['white_lost'] = game['white_lost']
    clean_game['started'] = str(game['started']).split('.')[0]
    if(game['ended'] != None):
        clean_game['ended'] = str(game['ended']).split('.')[0]
    else:
        clean_game['ended'] = None
    clean_games.append(clean_game)

sorted_games = sorted(clean_games, key=lambda g: datetime.strptime(g['started'], "%Y-%m-%dT%H:%M:%S"))

output.write(json.dumps(sorted_games, indent=4))

file.close()
output.close()
