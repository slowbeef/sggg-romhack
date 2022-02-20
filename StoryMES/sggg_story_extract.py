#!/usr/bin/python

'''
The MES file starts with file pointers to each string start. We start at 0, and
subtract the following byte from it to get a list of lengths to read. We do
this until we hit zero, EOF (error) or maybe until we reach where the first pointer
was.
'''

import struct
import re

filename = 'files/STORY00.MES'

lengthCount = 0
lineLengths = []
lines = []

with open(filename, 'rb') as file:
    offset = struct.unpack('<I', file.read(4))[0]
    length = 0

    while True:
        nextOffset = struct.unpack('<I', file.read(4))[0]
        if nextOffset == 0:
            break

        nextLength = nextOffset - offset

        if nextLength > 0:
            lineLengths.append(nextOffset - offset)
        offset = nextOffset

    for lineLength in lineLengths:
        section = file.read(lineLength)
        section = re.sub(br'((?:@[a-z]{1,2}\d*){1,4})', br'\n \1 --- ', section)
#        section = re.sub(br'@', br'\n', section)
        print section.decode("shift-jis").encode("utf-8")

        print ""


'''
import re
import csv
import os
import sys
import argparse


with open(filename, 'rb') as f:
    encodedMESbytes = f.read()

japaneseLines = []

# This is ridiculous, I alraedy have all the pointers at the start.
# This gets the ones with no metadata, I guess.
japaneseLines = japaneseLines + re.findall(br'\x00{5}([^\x00].*?)\x00', encodedMESbytes)

#This regex gets the metadata too
#encodedLine = re.findall(br'(.@[a-z](?:@[a-z]\d+)+)(.*?).@', encodedMESbytes)
japaneseLines = japaneseLines + re.findall(br'@[a-z](?:@[a-z]\d+)+(.*?)@', encodedMESbytes)

for line in japaneseLines:
    print line
'''
