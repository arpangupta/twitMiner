import urllib2
import json
import time

validationlist = open(r'test', 'r').read().splitlines()
traininset = []
userids = []

for line in validationlist:
	#time.sleep(10)
	user_id =line.split()[1]
	if(user_id  not in userids):
		userids.append(user_id )
		tweetsjson  = urllib2.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?user_id="+str(user_id)+"&count=200")
		tweets = tweetsjson.read()
		tweets = json.loads(tweets)
		print user_id 
		for tweet in tweets:
		#	if (tweet['user']['screen_name']) in political):
		#		text_file.write(tweet['id'] +' Politics ' +tweet['text']) )
				traininset.append(tweet['user']['screen_name'])	



print list(set(traininset))
#json.dump(traininset, open(cat + "trainingset", 'wb'),indent = True)



