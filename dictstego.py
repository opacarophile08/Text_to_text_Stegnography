import pprint

def loadSentenceList():
	sentList=[]
	fp = open("eng_sentences.tsv")
	for line in fp:
		sline = line.split("\t")
		currsentence=sline[2][:len(sline[2])-2]
		sentList.append(currsentence)
	#print(sentList)
	return sentList
	
def constDict(sentList):
	alphabet ="abcdefghijklmnopqrstuvwxyz"
	sentDict={}
	for sen in sentList:
		absstr=""
		for ch in alphabet:
			if ch not in sen:
				absstr+=ch
		#print(absstr)
		if absstr not in sentDict.keys():
			sentDict[absstr]=[]
			sentDict[absstr].append(sen)
		else:
			sentDict[absstr].append(sen)

	pprint.pprint(sentDict)
	
sentList=loadSentenceList()
constDict(sentList)
'''
	    #using dummy file for testing 
	sentdict = {}




for line in fp:
    x = line.split("\t")
    key = x[0]
    val = x[2]   
    c = len(val)-1          #getting the-1 
    sent = val[0:c]
    lst = []
    count =0 
    
    #check if letter is not present in sentence and load to dict
    for letter in alphabet:
        if(letter not in sent):
            #lst.append(sent)
            d[letter].append(sent)

print(d['c'])
'''
