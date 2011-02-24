#!/usr/bin/env python
import os
import sys
from PIL import Image


def create_predicate(out, im, color):
    """
    Generate the body for a function that returns a boolean with the given
    image.
    """
    width, height = im.size
    out.write('switch (x) {\n')
    for x in range(0, width):
        out.write('case %d:\n' % x)
        out.write('switch (y) {\n')
        has_pixel = False
        for y in range(0, height):
            p = im.getpixel((x, y))
            if p[:3] == color:
                has_pixel = True
                out.write('case %d:\n' % y)
        if has_pixel:
            out.write('return true;\n')
        out.write('default:\n')
        out.write('return false;\n')
        out.write('}\n')
    out.write('default:\n')
    out.write('return false;\n')
    out.write('}\n')


def preprocess(out, im, name):
    """
    Preprocesses the image.
    """
    out.write('var %s = function () { return this; };\n' % name)
    out.write('%s.prototype.in_wall = function(x, y) {\n' % name)
    create_predicate(out, im, (0, 0, 0))
    out.write('};\n')
    # end
    out.write('%s.prototype.reached_end = function(x, y) {\n' % name)
    create_predicate(out, im, (0x86, 0x83, 0xFF))
    out.write('};\n')


def main():
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: %s <image>\n' % sys.argv[0])
        sys.exit(1)
    filename = sys.argv[1]
    try:
        im = Image.open(filename)
        # The name of the image is turned into the class name.
        name = os.path.basename(filename).split('.')[0]
        name = name[0].upper() + name[1:]
        out = sys.stdout
        preprocess(out, im, name)
    except Exception as e:
        sys.stderr.write('Error loading file: %s\n' % filename)
        sys.stderr.write('%s\n' % str(e))
        sys.exit(2)


if __name__ == '__main__':
    main()
