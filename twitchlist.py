import json
import urllib2
from pprint import pprint

url = "https://api.twitch.tv/kraken/search/streams?q=dota2"
data = json.load(urllib2.urlopen(url))

#pprint(data)


streams= data["streams"]
games = [];
for i,var in enumerate(streams):
	games.append((streams[i]["channel"]["views"],streams[i]["channel"]["status"].encode('ascii','ignore'),streams[i]["channel"]["url"].encode('ascii','ignore')))

#print(games)
games.sort(reverse=True)

for var in games:
	print "Views: " + str(var[0]) + " | Status: " + var[1] + " |Stream: " + var[2] + " \n"