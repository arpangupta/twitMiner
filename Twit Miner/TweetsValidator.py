import json
import re
import csv
from TweetsProcessor import TweetProcessor

def main():
	print""

class Validator:
	def __init__(self):
		self.sportswords = json.load(open("sportswords"))
		self.politicswords = json.load(open("politicswords"))
	
		self.sportshashtags = json.load(open("sportshashtags"))
		self.politicshashtags = json.load(open("politicshashtags"))
	
		self.sportsmentions = json.load(open("sportsmentions"))
		self.politicsmentions = json.load(open("politicsmentions"))
		self.tweetprocessor = TweetProcessor()

	def validateToFile(self,infile,outfile,a,b,c):
		sportstweets = json.load(open("sportstrainingset"))
		politicstweets = json.load(open("politicstrainingset"))
		trainingset= open(infile, 'r').read().splitlines()
		text_file = open(outfile, "w")
		for line in trainingset:
			tweetid = line[:line.find(' ')]
			tweet = line[line.find(' ')+2:-1]
			tweet = self.tweetprocessor .processTweet(tweet)
			words= self.tweetprocessor .getwords(tweet)
			totalsportsweight = 0.0
			totalpoliticsweight = 0.0
			sportwordweight = 0.0
			politicwordweight = 0.0

			for word in words:
				if(word != ''):	
					if(word[0] == '#' and len(word.split())<2):
						sportwordweight = self.sportshashtags.get(word,0.0)  +1.0
						politicwordweight = self.politicshashtags.get(word,0.0) +1.0
						if(sportwordweight!=0 or sportwordweight!=0):
							totalsportsweight += a*(sportwordweight / (sportwordweight +politicwordweight))
							totalpoliticsweight += a*(politicwordweight / (sportwordweight +politicwordweight))
					elif(word[0] == '@' and len(word.split())<2):
						sportwordweight = self.sportsmentions.get(word,0.0) +1.0
						politicwordweight = self.politicsmentions.get(word,0.0) +1.0
						if(sportwordweight!=0 or sportwordweight!=0):
							totalsportsweight += b*(sportwordweight / (sportwordweight +politicwordweight))
							totalpoliticsweight += b*(politicwordweight / (sportwordweight +politicwordweight))
					else:
						sportwordweight = self.sportswords.get(word,0.0) +1.0
						politicwordweight = self.politicswords.get(word,0.0) +1.0
						if(sportwordweight!=0 or sportwordweight!=0):
							totalsportsweight += c*sportwordweight / (sportwordweight +politicwordweight)
							totalpoliticsweight += c*politicwordweight / (sportwordweight +politicwordweight)

			if (totalsportsweight > totalpoliticsweight):
				text_file.write("%s Sports\n"%tweetid)
				if(tweet not in sportstweets):
					sportstweets.append(tweet)
				#print tweetid+ " Sports"
			else:
				text_file.write("%s Politics\n"%tweetid)
				if(tweet not in politicstweets):
					politicstweets.append(tweet)
				#print tweetid+ " Politics"

			#for w in sorted(sportswords, key=sportswords.get, reverse=True):
		  		#print w, sportswords[w]
			#	a =1

		text_file.close()
		json.dump(sportstweets, open("sportstrainingset", 'wb'),indent = True)
		json.dump(politicstweets, open("politicstrainingset", 'wb'),indent = True)
if __name__ == "__main__":
    main()

