#!/usr/bin/env python

import cgitb
cgitb.enable()
print "Content-Type: text/html\n\n"

from datetime import datetime
print datetime.now()

print "<h1>BetaWall</h1>"

for i in range(0, 2):
    for j in range(0, 3):
	print "<button>Toggle (%i,%i)</button>" % (j, i)
    print "<br />"
