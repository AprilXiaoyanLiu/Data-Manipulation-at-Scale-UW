import json
import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    twitterlist = []  # Create list with dictionary
    for line in tweet_file:
    	line = line.encode('utf-8')
    	twitterlist.append(json.loads(line)) 
    
    scores = {} # initialize an empty dictionary
    for line in sent_file:
    	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    	scores[term] = int(score)  # Convert the score to an integer.
    
    sent_score = {}
    count_number = {}
    for i in range(len(twitterlist)):
    	if "text" in twitterlist[i]:
    		tweetword = twitterlist[i]["text"].split()
    		sentscore = 0
    		for word in tweetword:
    			word = word.encode('utf-8')
    			if word in scores:
    				sentscore = sentscore + scores[word]
    		for word in tweetword:	
    			word = word.encode('utf-8')
    			if word not in scores:
    				if word not in sent_score:
    					sent_score[word] = sentscore
    					count_number[word] = 1
    				elif word in sent_score:
    					sent_score[word] = sentscore + sent_score[word]
    					count_number[word] = count_number[word] + 1
    				
	d = {}
	for key, val in sent_score.items():
		d[key] = float(val)/count_number[key]
    		
    for k, v in d.items():
    	print k, float(v)
    
    		
    
if __name__ == '__main__':
	main()