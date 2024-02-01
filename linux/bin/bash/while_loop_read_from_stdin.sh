#!/bin/sh

# Iterate over stdin
ls -1 | while read f; do echo "$f"; done
