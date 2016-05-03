def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])

    twitterlist = []  # Create list with dictionary
    for line in tweet_file:
        line = line.encode('utf-8')
        twitterlist.append(json.loads(line))
        '''print json.dumps(json.loads(line), indent=4, sort_keys=True)'''
        
    
	count_loc = {}
	for tweet in twitterlist:
		if "entities" in tweet:
		    if "hashtags" in tweet["entities"] and len(tweet["entities"]["hashtags"])>0:
		        	for i in tweet["entities"]["hashtags"]:
		        		tweet_hashtag = i["text"].encode('utf-8')
		        		if tweet_hashtag not in count_loc:
		        			count_loc[tweet_hashtag] = 1
		        		elif tweet_hashtag in count_loc:
		        			count_loc[tweet_hashtag] += 1
    count_loc
    
    lst = []
    for k, v in count_loc.items():
    	lst.append((v,k))
    lst.sort (reverse = True)
    for value, key in lst[:10]:
    	print key, value 	        

	
			
			
if __name__ == '__main__':
	main()		
