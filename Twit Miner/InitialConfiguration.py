from TweetsClassifier import Classifier
from TweetsValidator import Validator
from TweetsProcessor import TweetProcessor
import json
#This code should be executed during the inital configuration / starting up 

def main():
	#has to be executed only once
	addTrainingToTweets() 
	a =7
	b =5.8
	c =1.3
	print "Please Be patient while we make things ready will take around 2 mins"
	classify = Classifier()
	classify.categorisetweets()
	validate = Validator() 
	validate.validateToFile(r'validation.txt','Outputvalidation.txt',a,b,c)
	for i in range(5):
		cleanUpTrainingSet(a,b,c,"sports")
		cleanUpTrainingSet(a,b,c,"politics")
		classify = Classifier()
		classify.categorisetweets()
		validate = Validator() 
		validate.validateToFile(r'test.txt','OutputTest.txt',a,b,c)
		
		print str((i+1)*100/5) +"% complete"
	print "Awesome you are done.\nNow you can run RunTwitMiner.py as many time you want :) \nNote the inpu file for the program should be in validation.txt and you will get the output in OutputTest.txt"

def cleanUpTrainingSet(a,b,c,cat):
	#this code will cleanup training set with previous training to eliminate confusion.
	#This code has to executed only once and is done in the above
	tweetprocessor = TweetProcessor()
	sportswords = json.load(open("sportswords"))
	politicswords = json.load(open("politicswords"))
	
	sportshashtags = json.load(open("sportshashtags"))
	politicshashtags = json.load(open("politicshashtags"))

	sportsmentions = json.load(open("sportsmentions"))
	politicsmentions = json.load(open("politicsmentions"))
	tweets = json.load(open(cat+"trainingset"))
	for actualtweet in tweets:
		tweet = tweetprocessor.processTweet(actualtweet)
		words= tweetprocessor.getwords(tweet)
		totalsportsweight = 0.0
		totalpoliticsweight = 0.0
		sportwordweight = 0.0
		politicwordweight = 0.0
		for word in words:
			if(word != ''):	
				if(word[0] == '#' and len(word.split())<2):
					sportwordweight = sportshashtags.get(word,0.0)  +1.0
					politicwordweight = politicshashtags.get(word,0.0) +1.0
					if(sportwordweight!=0 or sportwordweight!=0):
						totalsportsweight += a*(sportwordweight / (sportwordweight +politicwordweight))
						totalpoliticsweight += a*(politicwordweight / (sportwordweight +politicwordweight))
				elif(word[0] == '@' and len(word.split())<2):
					sportwordweight = sportsmentions.get(word,0.0) +1.0
					politicwordweight = politicsmentions.get(word,0.0) +1.0
					if(sportwordweight!=0 or sportwordweight!=0):
						totalsportsweight += b*(sportwordweight / (sportwordweight +politicwordweight))
						totalpoliticsweight += b*(politicwordweight / (sportwordweight +politicwordweight))
				else:
					sportwordweight = sportswords.get(word,0.0) +1.0
					politicwordweight = politicswords.get(word,0.0) +1.0
					if(sportwordweight!=0 or sportwordweight!=0):
						totalsportsweight += c*sportwordweight / (sportwordweight +politicwordweight)
						totalpoliticsweight += c*politicwordweight / (sportwordweight +politicwordweight)
		if (cat == "politics" and totalsportsweight > totalpoliticsweight):
			tweets.remove(actualtweet)
		if (cat == "sports" and totalsportsweight < totalpoliticsweight):
			tweets.remove(actualtweet)
	json.dump(tweets, open(cat + "trainingset", 'wb'),indent = True)

def addTrainingToTweets():
	trainingset= open(r'training.txt', 'r').read().splitlines()
	tweetprocessor = TweetProcessor()
	sportstweets = []
	politicstweets = []
	for line in trainingset:
		sportindex = line.find(" ")+9
		if line.split()[1] == 'Sports':
			sportstweets.append(tweetprocessor.processTweet(line[sportindex:-1]))

	for line in trainingset:
		politicsindex = line.find(" ")+11
		if line.split()[1] == 'Politics':
			politicstweets.append(tweetprocessor.processTweet(line[politicsindex:-1]))

	json.dump(sportstweets, open("sportstrainingset", 'wb'),indent = True)
	json.dump(politicstweets, open("politicstrainingset", 'wb'),indent = True)

if __name__ == "__main__":
    main()
