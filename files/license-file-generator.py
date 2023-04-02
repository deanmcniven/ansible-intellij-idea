#!/usr/bin/env python

import binascii
import codecs
import os
import sys

if len(sys.argv) != 3:
    print("ERROR: Invalid number of parameters!")
    print("Usage: ", sys.argv[0], " <license string> <output file>")
    sys.exit(1)

licensestring=sys.argv[1]
outputfile=sys.argv[2]

with open(outputfile, 'wb') as f:
    f.write(binascii.unhexlify('FFFF'))
    f.write(licensestring.encode('utf-16-le'))

os.chmod(outputfile, 0o644)
