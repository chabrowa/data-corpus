
import urllib2
import json
import csv
import numpy

from db import createDB
from db import downloadData
from db import getCollection
from db import downloadCsvs
from db import createHeadersCollection

from stats import averageResources

collection  = getCollection('packages')
headers     = getCollection('headers')

createHeadersCollection(collection, headers)
#downloadCsvs(collection, headers)
# averageResources(collection)
# createDB(collection)
