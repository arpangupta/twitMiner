import csv
import re
#Code to process the tweets and to get the words vector


def main():
	test =0
class TweetProcessor:
	
	def __init__(self):
	        self.stopwords = []
		self.readStopWords()

	def readStopWords(self):
	    self.stopwords =  open(r'stopwords', 'r').read().splitlines()

	def processTweet(self,tweet):
	    # process the tweets
	 
	    #Convert to lower case
	    tweet = tweet.lower()
	    #Convert www.* or https?://* to URL
	    tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','',tweet)
            tweet = re.sub('(:-\))|(:\)) ',' SMILEY ',tweet)
  	    tweet = re.sub('\\\\[u][0-9]+',' ',tweet)
	    tweet = re.sub('[\\][u][0-9]+',' ',tweet)
	    tweet = re.sub('[\s]([0-9]+\.?[0-9]+)',' NUMBER ',tweet)
	    tweet = re.sub('[\\][\"]',' ',tweet) 
 	    tweet = re.sub('[\\][\']',' ',tweet) 
	    tweet = re.sub('[\"]+',' ',tweet) 
	    tweet = re.sub('[\']+',' ',tweet) 
	    tweet = re.sub('[\?!]+',' ',tweet) 
	    tweet = re.sub('\\\\',' ',tweet) 
	    tweet = re.sub('\(',' ',tweet) 
	    tweet = re.sub('\)',' ',tweet) 
	    tweet = re.sub('&[a-zA-Z]+;',' ',tweet) 
	    tweet = re.sub('[\.]+',' ',tweet)
	    tweet = re.sub('[,]+',' ',tweet)
	    tweet = re.sub('[:]+',' ',tweet)

	    #Remove additional white spaces
	    tweet = re.sub('[\s]+', ' ', tweet)

	    #trim
	    tweet = tweet.strip('\'"')
	    return tweet 

	def getwords(self,sentence):
	    w= sentence.split()
	     
	    #remove all things that are 1 or 2 characters long (punctuation)
	    w= [x for x in w if len(x)>2]
	    #get rid of all stop words
	    w= [x for x in w if not x in self.stopwords]

	    #add bigrams
	    w= w + [w[i]+' '+w[i+1] for i in range(len(w)-1)]
	    
	    #get rid of duplicates by converting to set and back to list

	    #this works because sets dont contain duplicates
	    w= list(set(w))
	     
	    return w

	def sortdict(self,catdict):
		returndict = {}
		count = 1000000
		for w in sorted(catdict, key=catdict.get, reverse=True):
			if(count>0):
  				returndict[w] = catdict[w]
				count = count-1
			else:
				break
		return returndict
		#return sorted(catdict, key=catdict.get, reverse=True)

if __name__ == "__main__":
    main()
