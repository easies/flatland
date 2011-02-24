#!/bin/sh

# Generates the Processing.js preload directives.
for x in `ls data/*.png`; do
    echo "/* @pjs preload=\"$x\"; */"
done
