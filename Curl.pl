#!/usr/bin/perl
use strict;
use warnings;
use XML::LibXML;
#use XML::XPath;
#use XML::XPath::XMLParser;
use XML::Simple;
use File::Find;

# create object
my $xml = new XML::Simple;

my $xpath=999;

my $series = 'Harvard%20College%20Library%20preservation%20digitization%20pro*';

# WORKS my $curl=`curl http://api.lib.harvard.edu/v2/items.xml?limit=0&title=Harvard%20College%20Library%20preservation%20digitization%20pro*`;

my $curl=`curl http://api.lib.harvard.edu/v2/items.xml?limit=0&title=$series`;

# read XML file
my $node = $xml->XMLin($curl);
print $curl;

#my $zaba = system("curl http://api.lib.harvard.edu/v2/items.xml?limit=0&title=$series");

#say $data;

#my $xp = XML::XPath->new(ioref => *DATA);

#my $count = $xp->('/results/pagination/numFound');

#say $zaba;

#print $node->findvalue( $xpath );

#foreach my $numFound ($data->findnodes('/results/pagination/numFound')) {
#    print $numFound->to_literal, "\n" 
#  }