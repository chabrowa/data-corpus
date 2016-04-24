# import csv
# import json
# import numpy
#
# inputFile       = 'pubilc-access-wifi-feb.csv'
# outputFile      = ''
# columnName      = true
# iterator        = 0
# dataMatrix      =
#
# with open(inputFile, 'rb') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',')
#     for row in spamreader:
#         for cell in row:

import urllib2
import json
import csv
import numpy

#fp = urllib2.urlopen('http://data.gov.uk/api/2/rest/package')
#results = json.loads(fp.read())

with open('data.json') as data_file:
    results = json.load(data_file)
#fp.close()

numberOfPackages                = len(results)
sumOfResources                  = 0
sumOfPackagesWthoutResources    = 0
listOfResources                 = [];

for resource in results:
    #fp = urllib2.urlopen('http://data.gov.uk/api/2/rest/package/'+ packageId)
    #resource = json.loads(fp.read())
    print resource["num_resources"]
    listOfResources.append(resource["num_resources"])
    sumOfResources = sumOfResources + resource["num_resources"]
    if resource["num_resources"] == 0:
        sumOfPackagesWthoutResources = sumOfPackagesWthoutResources + 1
    #fp.close()


print "Number of packages on data.gov.uk: " + str(numberOfPackages)
print "Average number of resources per package: " + str(sumOfResources/numberOfPackages)
print "Number of packages withour resources: " + str(sumOfPackagesWthoutResources)
print sumOfResources
print numberOfPackages
