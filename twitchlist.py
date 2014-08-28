import json
import urllib2
import os
import re
from pprint import pprint

#A quick python script to grab the top live dota2 streams, display the streams in order of most views to least 
#views, ask the user which stream they want to watch, and then open the stream from the terminal using
#livestreamer. 
#Just run python twitchlist.py
#DEPENDENCY WARNING: livestreamer @ http://livestreamer.readthedocs.org/en/latest/install.html
#for ubuntu: sudo apt-get install livestreamer

  

url = "https://api.twitch.tv/kraken/search/streams?q=dota2"
data = json.load(urllib2.urlopen(url))


streams= data["streams"]
games = [];
for i,var in enumerate(streams):
	games.append((streams[i]["channel"]["views"],streams[i]["channel"]["status"].encode('ascii','ignore'),streams[i]["channel"]["url"].encode('ascii','ignore')))

games.sort(reverse=True)

for i,var in enumerate(games):
	print str(i) + " :|  Views: " + str(var[0]) + " | Status: " + var[1] + " |Stream: " + var[2] + " \n"

numgame = input("Enter the number of the stream you wish to watch: ")
regobj = re.search('twitch.tv/.*', games[numgame][2])
gamelink = regobj.group(0)
command = "livestreamer " + gamelink + " best"
os.system(command)