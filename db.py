import pymongo
import urllib2
import json
import csv
import numpy


def getCollection ():
    from pymongo import MongoClient
    client = MongoClient()

    db = client['data-gov-uk-packages']
    return db['packages']

def createDB (collection):
    for i in range(0, 103):
        with open('data/data' + str(i) + '.json') as data_file:
            results = json.load(data_file)
            for package in results:
                collection.insert_one(package)
    print collection.count()

def downloadData ():
    count = 0
    numberOfPackagesPerFile = 300
    resources =[]
    fp = urllib2.urlopen('http://data.gov.uk/api/2/rest/package')
    results = json.loads(fp.read())
    fp.close()

    for packageId in results:
        if count%numberOfPackagesPerFile == 0:
            f = open("data/data" + str(count/numberOfPackagesPerFile) + ".json","w")

        fp = urllib2.urlopen('http://data.gov.uk/api/2/rest/package/'+ packageId)
        resource = json.loads(fp.read())
        resources.insert(count%numberOfPackagesPerFile, resource)
        fp.close()

        if count%numberOfPackagesPerFile == numberOfPackagesPerFile-1:
            f.write(json.dumps(resources))
            resources =[]
            f.close()

        count = count + 1
