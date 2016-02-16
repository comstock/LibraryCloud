#!/usr/bin/python
# -*- coding: utf-8 -*-
# Reads a TEXT format JHOVE report and reduces it to two elements: Filename (aka, RepresentationInformation) and validation status
#
# Note: Using first version of JHOVE. See: http://jhove.sourceforge.net/
#
# # Using the following command, a full JHOVE output report generated for each examined file, and all reports concatenated into a single text file
# java -jar ./JhoveApp.jar -h text ~/anyDIR/CharlieHebdo/* > ./CharlieHebdoPictures_JHOVE_TXT_20160216.txt
#
# I eliminated LONG file paths by running the output through the following SED script
# s/\/run\/user\/1000\/gvfs\/smb-share:server=pentos-smb.ad.dil.harvard.edu,share=jellyPlanet\/TEST\/COMSTOCK\/CharlieHebdo//g;
#

import os, sys
import re

inputFilename = "/home/comstock/Documents/python/data/CH_input.txt"
f = open("/home/comstock/Documents/python/data/CH_output.txt", 'w')

with open(inputFilename,'r') as jhove_audit_list:
    for line in jhove_audit_list:
        #line = line.rstrip()
        if re.findall('RepresentationInformation*', line) :
            #print line
            f.write(line)
        elif re.findall('Status\:*', line) :
            #print line
            f.write(line)
            f.write("\n")
f.close()
