import re
from pymongo import MongoClient

storeJSON = []

myclient = MongoClient("mongodb+srv://TwitterDB:twitterextraction@twittercluster.udioj.mongodb.net/test")
rawDb = myclient["RawDB"]
Collection = rawDb["TestTweet"]
db = myclient["ProcessedDB"]
Collection = db["ProcessedTweet"]
TextDB = myclient['TextDB']
TextCollection = TextDB['TextCollection']

x = Collection.find()
tweetList = []
dictBow = {}
dictTrial = {}
countPositive = 0
countNegative = 0
countNeutral = 0
tweetCount = 1
positiveList = []
negativeList = []
neutralList = []
dictFinal = {}
positiveWords = open('positive-words.txt', "r")
positiveWords = positiveWords.read()
negativeWords = open('negative-words.txt', "r")
negativeWords = negativeWords.read()
neutralWords = open('neutral-words.txt', "r")
neutralWords = neutralWords.read()

for i in x:

    newRecord = {}
    if 'text' in i:
        textField = i['text']

        textField = re.sub(r'\s+', ' ', textField)
        textField = re.sub(r"http\S+", '', textField)
        textField = re.sub(r"[^a-zA-Z0-9!@',.\$& ]", '', textField)
        textField = re.sub(r'\\u[A-Za-z0-9]{4}', '', textField)
        textField = re.sub(r'&amp', 'and', textField)
        textField = re.sub(r'\\n', ' ', textField)
        textField = re.sub(r'RT', ' ', textField)
        print(textField)
        listTrial = textField.split()

        for x in listTrial:
            if x in positiveWords.split():
                dictFinal['Tweet'] = tweetCount
                dictFinal['message'] = textField
                positiveList.append(x)
                countPositive += 1
                dictFinal['Positive Match'] = positiveList
                if len(positiveList) > len(negativeList) and len(positiveList) > len(neutralList):
                    dictFinal['polarity'] = 'positive'

        for x in listTrial:
            if x in negativeWords.split():
                dictFinal['Tweet'] = tweetCount
                dictFinal['message'] = textField
                negativeList.append(x)
                countNegative += 1
                dictFinal['Negative Match'] = negativeList
            if len(negativeList) > len(positiveList) and len(negativeList) > len(neutralList):
                dictFinal['polarity'] = 'negative'

        for x in listTrial:
            if x in neutralWords.split():
                dictFinal['Tweet'] = tweetCount
                dictFinal['message'] = textField
                neutralList.append(x)
                countNeutral += 1
                dictFinal['Neutral Match'] = neutralList
            if len(neutralList) > len(positiveList) and len(neutralList) > len(negativeList):
                dictFinal['polarity'] = 'neutral'

        print(dictFinal)
        negativeList.clear()
        positiveList.clear()
        neutralList.clear()

        for x in listTrial:
            if x in dictTrial:
                dictTrial[x] += 1
            else:
                dictTrial[x] = 1
            tweetCount += 1
        print(dictTrial)
        dictTrial = {}

        print("Total Number of positive polarities: ")
        print(countPositive)
        print("Total Number of negative polarities: ")
        print(countNegative)
        print("Total Number of neutral polarities: ")
        print(countNeutral)
        if tweetCount >= 2500:
            break

print("Sentimental Analysis completed")
