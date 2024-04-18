#!/bin/sh

# Iterate over lines (like xargs -L1)
for f in $(ls -1); do echo "$f"; done
