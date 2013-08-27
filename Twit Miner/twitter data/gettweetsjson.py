import urllib2
import json
import time
def puttweetstofile(cat ):
	twitternames = open(cat, 'r').read().splitlines()
	traininset = []
	for name in twitternames:
		#time.sleep(10)
		tweetsjson  = urllib2.urlopen('https://api.twitter.com/1/statuses/user_timeline.json?screen_name='+ name +'&count=200')
		tweets = tweetsjson.read()
		tweets = json.loads(tweets)
		print name
		
		for tweet in tweets:
			traininset.append(tweet['text'])
	print len(traininset)
	json.dump(traininset, open(cat + "trainingset", 'wb'),indent = True)


puttweetstofile('sports')
puttweetstofile('politics')
