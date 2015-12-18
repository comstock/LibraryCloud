#!/bin/bash

#
# Run from within a directory of JPG images to produce a webpage with all of the images embedded.
#

# generate list of JPG files in current directory
ls -1 *.jpg  > filelist.txt

# If index.html exists, rename it so we can build a new one
if [ -e ./index.html ]
then
mv index.html "index_"$SECONDS".html"
fi

# remove any existing index.html file
# rm index.html

echo "<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>BIll Rules!</title>
</head>
</body>
" >> index.html

# TEST #while read line; do echo "$line"; done < filelist.txt

while read line; do echo "<a href=\"./$line.html\"><img src=\"$line\" alt=\"[$line]\" width=\"800\" /></a></br></br>
" >> index.html; done < filelist.txt

echo "</body><hr /></html>" >> index.html

## Build individual web pages for individual images

while read line; do echo "<html><head><title>$line</title></head><body><img src=\"$line\" /></body></html>" > $line.html;done < filelist.txt

