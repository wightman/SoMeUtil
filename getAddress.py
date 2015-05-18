#!/usr/bin/python
#
# getAddress.py - Rick Wightman, February 2014
#
# Use GoogleMaps API to get a street address range from a
# 	given postal code. 
#

import urllib2
import urllib
import sys
import xml.etree.ElementTree as ET


iNArg = len(sys.argv)
if iNArg < 2:
	print sys.argv[0],' <postal code>'
	exit(1)
postalCode = sys.argv[1:iNArg]
code = ""
for piece in postalCode:
	code+=piece

uri = 'https://maps.googleapis.com/maps/api/geocode/xml?address='+code+'&sensor=false'


response = urllib2.urlopen(uri)
geoXML = response.read()

root = ET.fromstring(geoXML)
geoLat = root.find("result/geometry/location/lat").text
geoLong = root.find("result/geometry/location/lng").text

uri = 'https://maps.googleapis.com/maps/api/geocode/xml?latlng='+geoLat+','+geoLong+'&sensor=false'

response = urllib2.urlopen(uri)
geoXML = response.read()

root = ET.fromstring(geoXML)
formattedAddress = root.find("result/formatted_address")

print formattedAddress.text

