import urllib2
import json
import csv
import numpy

fp = urllib2.urlopen('http://data.gov.uk/api/2/rest/package')
results = json.loads(fp.read())
fp.close()

count = 0
numberOfPackagesPerFile = 300
resources =[]

for packageId in results:
    if count%numberOfPackagesPerFile == 0:
        print "count: " + str(count/numberOfPackagesPerFile) + " i am making new file"
        f = open("data/data" + str(count/numberOfPackagesPerFile) + ".json","w")


    fp = urllib2.urlopen('http://data.gov.uk/api/2/rest/package/'+ packageId)
    resource = json.loads(fp.read())
    #f.write(json.dumps(resource))
    resources.insert(count%numberOfPackagesPerFile, resource)
    fp.close()

    if count%numberOfPackagesPerFile == numberOfPackagesPerFile-1:
        print "count: " + str(count) + " i am closing the file"
        f.write(json.dumps(resources))
        resources =[]
        f.close()

    count = count + 1
