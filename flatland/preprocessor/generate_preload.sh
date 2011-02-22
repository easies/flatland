#!/bin/sh

for x in `ls data/*.png`; do
    echo "/* @pjs preload=\"$x\"; */"
done
