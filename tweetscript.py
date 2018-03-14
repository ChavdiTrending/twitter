
from twitter import *
import json
config = {}
execfile("config.py", config)
twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


#-----------------------------------------------------------------------
# retrieve global trends.
# other localised trends can be specified by looking up WOE IDs:
#   http://developer.yahoo.com/geo/geoplanet/
# twitter API docs: https://dev.twitter.com/rest/reference/get/trends/place
#-----------------------------------------------------------------------
dicto = {}
idarr = [1,23424848,2295412]
for i in idarr:
	results = twitter.trends.place(_id = i) #1 is for global trending

	for location in results:
		for trend in location["trends"]:
			dicto[trend["name"]] = trend['url']
			
jsonDict = {}
jsonDict['links'] = dicto
with open('Tweetlinks.json', 'w') as outfile:  
    json.dump(jsonDict, outfile)
