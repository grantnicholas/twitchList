import json
import urllib2
import os
import re
from pprint import pprint

#Twitch API get dota2 streams
url = "https://api.twitch.tv/kraken/search/streams?q=dota2"
data = json.load(urllib2.urlopen(url))


#Sort the json streams and display the stream info to the user
streams= data["streams"]
games = [];
for i,var in enumerate(streams):
	games.append((streams[i]["channel"]["views"],streams[i]["channel"]["status"].encode('ascii','ignore'),streams[i]["channel"]["url"].encode('ascii','ignore')))

games.sort(reverse=True)

for i,var in enumerate(games):
	print str(i) + " :|  Views: " + str(var[0]) + " | Status: " + var[1] + " |Stream: " + var[2] + " \n"


#Ask the user which stream they want to watch and pipe the output to livestreamer
numgame = input("Enter the number of the stream you wish to watch: ")
regobj = re.search('twitch.tv/.*', games[numgame][2])
gamelink = regobj.group(0)
command = "livestreamer " + gamelink + " best"
os.system(command)