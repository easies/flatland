#!/usr/bin/env python
import sys


if len(sys.argv) < 2:
    sys.stdout.write('Usage: %s <test_script> [dependencies]\n')
    sys.exit(1)

# Read in the template.
f = open('test.html.template', 'r')
s = f.read()
# The list of javascript files are passed as arguments.
test_script = sys.argv[1]
dependencies = ' '.join(sys.argv[2:])
# Substitute the placeholders.
s = s.replace('{{{dependencies}}}', dependencies)
s = s.replace('{{{test_script}}}', test_script)
# Write out the result
sys.stdout.write(s)
