#!/bin/sh

for x in `ls data/*.png`; do
    echo "/* @pjs preload=\"data/$x\"; */"
done
