#!/bin/sh
echo "Recording sound for $1 seconds to $2 file"
arecord -f cd -t raw -d $1 | oggenc - -r -o $2
#arecord -c 1 -f S16_LE -t wav -d $1 | oggenc - -r -R 16000 -o $2
echo "Recording finished"
