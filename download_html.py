# -*- coding: utf-8 -*-

import os
import urllib

URL_PATTERN = "http://nycstreets.info/honorStreet.asp?b=%s&letter=%s"
BOROUGHS = ["BX","BK","M","Q","SI"]
LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
OUTPUT_DIR = "html/"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

for b in BOROUGHS:

    boroughDir = OUTPUT_DIR + b + "/"
    if not os.path.exists(boroughDir):
        os.makedirs(boroughDir)

    for l in LETTERS:
        filename = boroughDir + l + ".html"

        if not os.path.isfile(filename):
            url = URL_PATTERN % (b, l)
            print "Downloading %s" % url
            f = urllib.URLopener()
            f.retrieve(url, filename)

print "Done."
