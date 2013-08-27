import json
import re
import csv
from TweetsProcessor import TweetProcessor

def main():
	print""

class Classifier:
	def __init__(self):
		self.tweetprocessor = TweetProcessor()	
		self.topsportswords =  open(r'topsportswords', 'r').read().splitlines()
		self.toppoliticswords = open(r'toppoliticswords', 'r').read().splitlines()
		self.topsportshashtags = open(r'topsportshashtags', 'r').read().splitlines()
		self.toppoliticshashtags = open(r'toppoliticshashtags', 'r').read().splitlines()
		self.sportstweets = json.load(open("sportstrainingset"))
		self.politicstweets = json.load(open("politicstrainingset"))
		self.categorisetweets()
		
	def categorisetweets(self):
		politicswords = {}
		sportswords= {}

		politicshashtags = {}
		sportshashtags= {}

		politicsmentions = {}
		sportsmentions= {}
		#Filling in most common words and hash tags
		for word in self.topsportswords:
			sportswords[word] = 10
		for word in self.topsportshashtags:
			sportshashtags[word] = 5
		for word in self.toppoliticswords:
			politicswords[word] = 10
		for word in self.toppoliticshashtags:
			politicshashtags[word] = 5
		#Analyzing the tweets
		for tweet in self.sportstweets:

			tweet = self.tweetprocessor.processTweet(tweet)
			words= self.tweetprocessor.getwords(tweet)
			for word in words:	
				if(word[0] == '#' ):
					sportshashtags[word] = sportshashtags.get(word, 0) +1
				elif(word[0] == '@' ):
					sportsmentions[word] = sportsmentions.get(word, 0) +1
				else:
					sportswords[word] = sportswords.get(word, 0) +1

		for tweet in self.politicstweets:
			tweet = self.tweetprocessor.processTweet(tweet)
			words= self.tweetprocessor.getwords(tweet)
			for word in words:
				if(word[0] == '#' ):
					politicshashtags[word] = politicshashtags.get(word, 0) +1
				elif(word[0] == '@' ):
					politicsmentions[word] = politicsmentions.get(word, 0) +1
				else:
					politicswords[word] = politicswords.get(word, 0) +1
		#Saving the categorised tweets

	
		json.dump(sportswords, open("sportswords", 'wb'))
		json.dump(sportshashtags, open("sportshashtags", 'wb'))

		json.dump(politicswords, open("politicswords", 'wb'))
		json.dump(politicshashtags, open("politicshashtags", 'wb'))

		json.dump(politicsmentions, open("politicsmentions", 'wb'))
		json.dump(sportsmentions, open("sportsmentions", 'wb'))
		

if __name__ == "__main__":
    main()
