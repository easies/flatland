#!/usr/bin/env python
import os
import sys
from PIL import Image


def preprocess(out, im, name):
    width, height = im.size
    out.write('var %s = function () { return this; };\n' % name)
    out.write('%s.prototype.in_wall = function(x, y) {\n' % name)
    out.write('switch (x) {\n')
    for x in range(0, width):
        out.write('case %d:\n' % x)
        out.write('switch (y) {\n')
        for y in range(0, height):
            p = im.getpixel((x, y))
            if p == (0, 0, 0):
                out.write('case %d:\n' % y)
        out.write('return true;\n')
        out.write('default:\n')
        out.write('return false;\n')
        out.write('}\n')
    out.write('default:\n')
    out.write('return false;\n')
    out.write('}\n')
    out.write('};\n')


def main():
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: %s <image>\n' % sys.argv[0])
        sys.exit(1)
    filename = sys.argv[1]
    try:
        im = Image.open(filename)
        name = os.path.basename(filename).split('.')[0]
        name = name[0].upper() + name[1:]
        out = sys.stdout
        preprocess(out, im, name)
    except:
        sys.stderr.write('Error loading file: %s\n' % filename)
        sys.exit(2)


if __name__ == '__main__':
    main()
