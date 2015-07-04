#!/usr/bin/python
# -*- coding: utf-8 -*-
import pycurl
#import codecs
import os, sys
import re

from StringIO import StringIO

fileExtention = "xml"
libcloud_call = ""
SingleID = "XXX"
libcloud_stem = "http://api.lib.harvard.edu/v2/items."
hollisRecordsStem = "/home/comstock/Documents/python/data/hollisRecords" + "_"

with open("/home/comstock/Documents/python/data/hollisIDs.txt",'r') as hollisList:
    for line in hollisList:
        #print line
        SingleID = line
        libcloud_call = libcloud_stem + fileExtention + "?recordIdentifier=" + SingleID
        libcloud_call = libcloud_call.rstrip()
        hollisRecordsFile = hollisRecordsStem + SingleID + "." + fileExtention
        #print libcloud_call
        f = open (hollisRecordsFile,'w')
        c = pycurl.Curl()
        c.setopt(c.URL, libcloud_call)
        c.setopt(c.WRITEDATA, f)
        c.perform()
        c.close()
