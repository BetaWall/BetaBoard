#!/usr/bin/env python

import cgitb
cgitb.enable()
print "Content-Type: text/plain\n\n"

from datetime import datetime
print datetime.now()
