import json
from datetime import datetime, date
from sys import argv

filename = argv[1]
file = open(filename ,'r')
output = open(filename.split('.')[0].split('_')[0] + '.csv', 'w')

data = json.load(file)

for game in data:
    if game['width'] != 19:
        continue
    if not game['ranked']:
        continue
    if game['handicap'] != 0:
        continue
    if game['tournament'] != None:
        continue
    if(game['black_username'] == argv[2]):
        output.write(str(game['black_rating'])+', '+str(game['started']))
    else if(game['white_username'] == argv[2]):
        output.write(str(game['white_rating'])+', '+str(game['started']))
    else:
        exit()
    output.write('\n')

file.close()
output.close()
