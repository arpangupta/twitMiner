import urllib2
import json
import time

validationlist = open(r'test', 'r').read().splitlines()
traininset = []
userids = []
user_id = validationlist[0].split()[1]
max_id = validationlist[0].split()[0]

political = ['USAndHyderabad','WHLive','USAinUK','VP','USNATO' ,'UN','UN_Spokesperson','USUN','whitehouse','USAndKolkata']
sport = [ 'UnitedUpdates', 'usatabletennis','Olympics','TennisAustralia','USOlympic','SportsCenter','usopen','Sports_NDTV','USABadminton','ussoccer','Wimbledon']

politics = {}
sports = {}

for line in validationlist:
	#time.sleep(10)
	
	if(line.split()[1] != user_id and user_id not in userids):
		userids.append(user_id)
		tweetsjson  = urllib2.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&exclude_replies=false&user_id="+user_id+"&max_id="+max_id+"&since_id="+since_id+"&count=200")
		tweets = tweetsjson.read()
		tweets = json.loads(tweets)
		print user_id
		for tweet in tweets:
			if (tweet['user']['screen_name'] in political):
				politics[tweet['id']] = tweet['text'];
			elif (tweet['user']['screen_name'] in sport):
				sports[tweet['id']] = tweet['text'];
		max_id = line.split()[0]
	
	user_id =line.split()[1]
	since_id = line.split()[0]


tweetsjson  = urllib2.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&exclude_replies=false&user_id="+user_id+"&max_id="+max_id+"&since_id="+since_id+"&count=200")
tweets = tweetsjson.read()
tweets = json.loads(tweets)
print user_id
for tweet in tweets:
	if (tweet['user']['screen_name'] in political):
		politics[tweet['id']] = tweet['text'];
	elif (tweet['user']['screen_name'] in sport):
		sports[tweet['id']] = tweet['text'];

print list(set(traininset))
json.dump(politics, open("politicalout", 'wb'),indent = True)
json.dump(sports, open("sportsout", 'wb'),indent = True)

print str(len(politics) + len(sports))

