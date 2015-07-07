#!/usr/bin/python
# -*- coding: utf-8 -*-
import pycurl
#import codecs
import os, sys
import re
import time

from StringIO import StringIO

fileExtention = "xml"
inputFilename = "/home/comstock/Documents/python/data/HYL_rubbings._20150707_hollis_ids.tsv"
libcloud_call = ""
SingleID = "XXX"
libcloud_stem = "http://api.lib.harvard.edu/v2/items."
#hollisRecordsStem = "/home/comstock/Documents/python/data/hollisRecords" + "_"
hollisRecordsStem = "/home/comstock/Documents/python/data/output/libCloud/"

with open(inputFilename,'r') as hollisList:
    for line in hollisList:
        #print line
        SingleID = line
        libcloud_call = libcloud_stem + fileExtention + "?recordIdentifier=" + SingleID
        SingleID = SingleID.rstrip()
        libcloud_call = libcloud_call.rstrip()
        hollisRecordsFile = hollisRecordsStem + SingleID + "." + fileExtention
        #print libcloud_call
        f = open (hollisRecordsFile,'w')
        c = pycurl.Curl()
        c.setopt(c.URL, libcloud_call)
        c.setopt(c.WRITEDATA, f)
        c.perform()
        time.sleep(.300) # Added this brief pause to prevent timeouts. Not sure it is necessary.
        c.close()
