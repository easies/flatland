#!/usr/bin/env python
import sys


# Read in the template.
f = open('index.html.template', 'r')
s = f.read()
# The list of javascript files are passed as arguments.
scripts = ['<script src="%s"></script>' % x for x in sys.argv[1:]]
# Substitute the placeholder.
s = s.replace('{{{scripts}}}', '  \n'.join(scripts))
# Write out the result
sys.stdout.write(s)
