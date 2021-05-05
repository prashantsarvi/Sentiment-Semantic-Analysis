from math import log10
from pymongo import MongoClient

myclient = MongoClient("mongodb+srv://TwitterDB:twitterextraction@twittercluster.udioj.mongodb.net/test")
reuterDb = myclient["ReuterDb"]
Collection = reuterDb["Reuters"]
x = Collection.find()
canadaCount = 0
canadaList = []
rainCount = 0
coldCount = 0
hotCount = 0
N = 0
for c, i in enumerate(x):
    if 'text' in i:
        textField = i['text']
        titleField = i['titleSgm']

        if 'Canada' in textField or 'Canada' in titleField:
            canadaCount += 1
        if 'rain' in textField or 'rain' in titleField:
            rainCount += 1
        if 'cold' in textField or 'cold' in titleField:
            coldCount += 1
        if 'hot' in textField or 'hot' in titleField:
            hotCount += 1
    N += 1
print('\n')
print(f"Total news Articles: {N}")
print('\n')
print(f"Number of documents containing the word 'Canada': {canadaCount}")
print(f"Number of documents containing the word 'rain': {rainCount}")
print(f"Number of documents containing the word 'cold': {coldCount}")
print(f"Number of documents containing the word 'hot': {hotCount}")
print('\n')

IDFC = log10(N / canadaCount)
print(f"Term frequency-inverse document frequency of 'Canada': {IDFC}")

IDFR = log10(N / rainCount)
print(f"Term frequency-inverse document frequency of 'rain': {IDFR}")

IDFCO = log10(N / coldCount)
print(f"Term frequency-inverse document frequency of 'cold': {IDFCO}")

IDFH = log10(N / hotCount)
print(f"Term frequency-inverse document frequency of 'hot': {IDFH}")
