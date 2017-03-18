# -*- coding: utf-8 -*-

import os
import urllib2

URL_PATTERN = "http://nycstreets.info/honorStreet.asp?b=%s&letter=%s"
BOROUGHS = ["BX","BK","M","Q","SI"]
LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
OUTPUT_DIR = "html/"
ENCODING = "ISO-8859-1"
OVERWRITE = True

def downloadUrl(url, filename):
    print "Downloading %s" % url
    req = urllib2.urlopen(url)
    content = req.read()
    ucontent = unicode(content, ENCODING)
    with open(filename, 'w') as f:
        f.write(ucontent.encode('utf-8'))

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

for b in BOROUGHS:

    boroughDir = OUTPUT_DIR + b + "/"
    if not os.path.exists(boroughDir):
        os.makedirs(boroughDir)

    for l in LETTERS:
        filename = boroughDir + l + ".html"
        if not os.path.isfile(filename) or OVERWRITE:
            url = URL_PATTERN % (b, l)
            downloadUrl(url, filename)

print "Done."
