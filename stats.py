import pymongo
import urllib2
import json
import csv
import numpy

def averageResources (collection):
    sum = 0.0
    nb = 0.0
    maxNbPackages = 0
    for package in collection.find():
        sum = sum + package['num_resources']
        nb = nb + 1.0
        if package['num_resources'] > maxNbPackages:
            maxNbPackages = package['num_resources']
            packageid = package['id']
    print sum
    print nb
    print sum / nb
    print maxNbPackages
    print packageid
