from pymongo import MongoClient
from collections import Counter

myclient = MongoClient("mongodb+srv://TwitterDB:twitterextraction@twittercluster.udioj.mongodb.net/test")
reuterDb = myclient["ReuterDb"]
Collection = reuterDb["Reuters"]
x = Collection.find()
canadaCount = 0
canadaList = []
canadaFrequencyList = []
dictCanada = {}
rainCount = 0
coldCount = 0
hotCount = 0
N = 0
for c, i in enumerate(x):
    if 'text' in i:
        textField = i['text']
        titleField = i['titleSgm']

        finalList = titleField.split() + textField.split()

        if 'Canada' in finalList:
            print('\n')
            print(f'Article#{c}')
            canadaCount += 1
            canadaFrequency = Counter(finalList)
            canadaList.append(canadaFrequency['Canada'])
            canadaList.sort()
            canadaWordCount = len(finalList)
            relativeFrequency = canadaFrequency["Canada"] / canadaWordCount

            print(f'Total words in the article: {canadaWordCount}')
            print(f'Frequency of Canada in Article#{c}: {canadaFrequency["Canada"]}')
            print(f'Relative Frequency: {relativeFrequency}')

            canadaFrequencyList.append(relativeFrequency)
            canadaFrequencyList.sort()

            if canadaFrequency["Canada"] == canadaList[len(canadaList) - 1]:
                articleNumberOccurrence = c
                temp1 = canadaList[len(canadaList) - 1]
            if canadaFrequencyList[len(canadaFrequencyList) - 1] == relativeFrequency:
                articleNumberHRF = c
                temp2 = canadaFrequencyList[len(canadaFrequencyList) - 1]
            if articleNumberHRF == c:
                title = titleField
                text = textField

print('\n')
print(f'Article#{articleNumberOccurrence} has highest occurrence of word "Canada" with frequency {temp1}')
print(f'Article#{articleNumberHRF} has Highest Relative Frequency of word "Canada" with title :{title} ')
print(f'and Highest Relative Frequency :{temp2}')
