#!/bin/sh

for x in `ls data`; do
    echo "/* @pjs preload=\"data/$x\"; */"
done
