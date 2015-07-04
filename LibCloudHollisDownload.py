#!/usr/bin/python
# -*- coding: utf-8 -*-
import pycurl
#import codecs
import os, sys
import re

from StringIO import StringIO

fileExtention = "xml"
libcloud_call = ""
#fileNameStem = "HYL_gazeteers"
SingleID = ""
libcloud_stem = "http://api.lib.harvard.edu/v2/items."
hollisRecords = "/home/comstock/Documents/python/data/hollisRecords.xml"

with open("/home/comstock/Documents/python/data/hollisIDs.txt",'r') as hollisList:
    for line in hollisList:
        # print line
        singleID = line
        libcloud_call = libcloud_stem + fileExtention + "?recordIdentifier=" + singleID
        libcloud_call = libcloud_call.rstrip()

        #print libcloud_call
        f = open (hollisRecords,'w')
        c = pycurl.Curl()
        c.setopt(c.URL, libcloud_call)
        c.setopt(c.WRITEDATA, f)
        c.perform()
        c.close()
