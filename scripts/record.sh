#!/bin/sh
echo "Recording sound for $1 seconds to $2 file"
arecord -r 16000 -f S16_LE -d $1 -c 1 -D plughw:0,0 -t wav tmp.wav
oggenc -q 3 -o $2 tmp.wav
rm tmp.wav
echo "Recording finished"
