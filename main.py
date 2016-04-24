import urllib2
import json
import csv
import numpy

fp = urllib2.urlopen('http://data.gov.uk/api/2/rest/package')
results = json.loads(fp.read())
fp.close()

f = open("data.json","w")
count = 0
resources =[]

for packageId in results:
    if count < 5:
        fp = urllib2.urlopen('http://data.gov.uk/api/2/rest/package/'+ packageId)
        resource = json.loads(fp.read())
        #f.write(json.dumps(resource))
        resources.insert(-1, resource)
        fp.close()
        count = count + 1

f.write(json.dumps(resources))
f.close()
