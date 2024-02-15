import pprint
import random


def loadSentenceList():
    sentList = []
    fp = open("eng_sentences.tsv")
    for line in fp:
        sline = line.split("\t")
        currsentence = sline[2][:len(sline[2]) - 2]
        sentList.append(currsentence)
    # print(sentList)
    return sentList


def constDict(sentList):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sentDict = {}
    for sen in sentList:
        absstr = ""
        for ch in alphabet:
            if ch not in sen:
                absstr += ch
        # print(absstr)
        if absstr not in sentDict.keys():
            sentDict[absstr] = []
            sentDict[absstr].append(sen)
        else:
            sentDict[absstr].append(sen)

    # pprint.pprint(sentDict)
    return sentDict


# absstr = "abd"
# plaintext = "akash"


def calculateFrequnecy(word):
    f = {}
    for sym in word:
        if sym in f:
            f[sym] += 1
        else:
            f[sym] = 1
    return f

def stegoMessage(plaintext,sentDict):
    selectedSen = []
    textFreq = calculateFrequnecy(plaintext)

    for absstr, vallist in sentDict.items():
        myflag=True
        for sym in plaintext:
            if sym not in absstr:
                continue
            else:
                myflag=False
                break

        if (myflag):
            for sen in vallist:
                senFreq=calculateFrequnecy(sen)
                flag = True

                for ch in plaintext:
                    if textFreq[ch] > senFreq[ch]:
                        flag = False
                        break
                if flag:
                    selectedSen.append(sen)

    if len(selectedSen) == 0:
        return
    #print(selectedSen)
    covertext=random.choice(selectedSen)
    stegokey=[]

    usedIndices = []

    for sym in plaintext:
        currindex=covertext.index(sym)

        while currindex in usedIndices:
            currindex = covertext.index(sym, currindex+1)

        stegokey.append(currindex)
        usedIndices.append(currindex)

    print(stegokey)
    print(covertext)

sentList=loadSentenceList()
sentDict=constDict(sentList)
# plaintext="akash"
plaintext = input("Enter text:")
stegoMessage(plaintext,sentDict)

