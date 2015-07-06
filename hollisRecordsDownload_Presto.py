#!/usr/bin/python
# -*- coding: utf-8 -*-
import pycurl
#import codecs
import os, sys
import re

from StringIO import StringIO

# Presto docs: https://wiki.harvard.edu/confluence/display/LibraryStaffDoc/Request+bibliographic+information+by+record+ID

fileExtention = "xml"
recordFormat = "mods/" #cite,dc,mods,marc
source = "hollis/" #hollis,via,journal
inputFilename = "/home/comstock/Documents/python/data/ming-qing_sample_records_wMultipleNETholdings.txt"
presto_call = ""
SingleID = "XXX"
presto_stem = "http://webservices.lib.harvard.edu/rest/" #http://webservices.lib.harvard.edu/rest/{record_format}/{source}/{id}
#hollisRecordsStem = "/home/comstock/Documents/python/data/hollisRecords" + "_"
hollisRecordsStem = "/home/comstock/Documents/python/data/output/"

with open(inputFilename,'r') as hollisList:
    for line in hollisList:
        #print line
        SingleID = line
        presto_call = presto_stem + recordFormat + source + SingleID
        SingleID = SingleID.rstrip()
        presto_call = presto_call.rstrip()
        hollisRecordsFile = hollisRecordsStem + SingleID + "." + fileExtention
        #print presto_call
        f = open (hollisRecordsFile,'w')
        c = pycurl.Curl()
        c.setopt(c.URL, presto_call)
        c.setopt(c.WRITEDATA, f)
        c.perform()
        c.close()
