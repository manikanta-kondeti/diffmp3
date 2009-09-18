#!/usr/bin/env python

# Simple Script to order ID3-Tags in MP3
# This has nothing to do with normalising the audio data. 
# Copyright 2009 Daniel Bachmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of version 2 of the GNU General Public License as
# published by the Free Software Foundation.
#
import sys,os,glob,operator
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3 

def main():
  if len(sys.argv) < 2:
    print "Error: wrong number of arguments: ", len(sys.argv)-1, " minimal 1 needed" 
    usage()
    sys.exit()
  sys.argv = reduce(operator.add, map(glob.glob, sys.argv))
  for file in sys.argv[1:]:
    if not os.path.exists(file) or not file.endswith(".mp3"):
      print "Error: not a valid MP3 file: ", file 
      sys.exit()
  for file in sys.argv[1:]:
    normalizeMP3Tag(file)  

def normalizeMP3Tag(file):
  writeMP3Tag(file,MP3(file, ID3=EasyID3))

def writeMP3Tag(file, tag):
  m = MP3(file, ID3=EasyID3) 
  try:
    m.add_tags(ID3=EasyID3)
    message = "Added tags to %s" , file
  except mutagen.id3.error:
    message = file, "already had tags"
  #print message
  for s in tag.keys():
    m[s] = tag[s]
  m.save()
  print "Normalized MP3: ", file

def usage():
  print "Usage: python ", sys.argv[0], " <MP3-file>"
  print "  or"
  print "Usage: python ", sys.argv[0], " <MP3-file1> <MP3-file2> ..."

if __name__ == "__main__":
  main()
