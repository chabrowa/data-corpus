import pymongo
import urllib2
import json
import csv
import numpy
import wget
import os


def getCollection (collectionName):
    from pymongo import MongoClient
    client = MongoClient()

    db = client['data-gov-uk-packages']
    return db[collectionName]

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

def createHeadersCollection (collection, headers):
    for package in collection.find():
        newObject = {
            "_id" : package['_id'],
    	    "owner_org" : package['owner_org'],
            "id" : package['id'],
            "num_resources" : package['num_resources'],
            "resources" : []
        }
        #db.products.insert( { _id: 10, item: "box", qty: 20 } )
        for resource in package['resources']:
            if resource['format'] == 'CSV':
                newObject['resources'].append({
                    "resource_group_id" : resource['resource_group_id'],
                    "id" : resource['id'],
                    "description": resource['description'],
                    "format": resource['format'],
                    "url": resource['url'],
                })
        headers.insert_one(newObject)

def downloadCsvs (collection, headers):
    startDerectory = os.getcwd()
    os.chdir(startDerectory+ '/CSVs')
    for package in collection.find():
        for resource in package['resources']:
            if resource['format'] == 'CSV':

                try:
                    wget.download(resource['url'])
                    print ''
                except:
                    pass

    os.chdir(startDerectory)

def validateCsv ():
    f=os.popen("ls -l")
    for i in f.readlines():
        print "myresult:",i,
