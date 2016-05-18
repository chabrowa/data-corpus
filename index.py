
import urllib2
import json
import csv
import numpy

from db import createDB
from db import downloadData
from db import getCollection
from db import downloadCsvs

from stats import averageResources

collection = getCollection()

downloadCsvs(collection)
# averageResources(collection)
# createDB(collection)
