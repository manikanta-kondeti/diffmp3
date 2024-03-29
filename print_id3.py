#!/usr/bin/env python

# Simple print ID-Tag of MP3 audio file
# For testing the mutagen library.
# Copyright 2009 Daniel Bachmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of version 2 of the GNU General Public License as
# published by the Free Software Foundation.
#
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3 

import sys
import os

def main():
  if len(sys.argv) <> 2:
    print "wrong number of arguments: ", len(sys.argv)-1, " expected 1" 
    usage()
    sys.exit()
  else:
    if os.path.exists(sys.argv[1]):
      mp3 = sys.argv[1]
    else:
      print "argument is not a valid file: ", sys.argv[1]
      usage()
      sys.exit()
  print mp3tag(mp3)

def mp3tag(file):
  audio = MP3(file, ID3=EasyID3)
  return audio.pprint()

def usage():
  print "Usage: python ", sys.argv[0], " <MP3-file>"

if __name__ == "__main__":
  main()

