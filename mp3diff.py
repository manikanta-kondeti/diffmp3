import sys,os,filecmp,difflib,shutil,tempfile,time

from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3 


def main():
  if len(sys.argv) <> 3:
    print "wrong number of arguments: ", len(sys.argv)-1, " expected 2" 
    usage()
    sys.exit()
  file1 = sys.argv[1]
  file2 = sys.argv[2]
  if not os.path.exists(file1) or not file1.endswith(".mp3"):
    print "Error: first parameter is not a valid MP3 file: ", file1 
    usage()
    sys.exit()
  if not os.path.exists(file2) or not file2.endswith(".mp3"):
    print "Error: second parameter is not a valid MP3 file: ", file2 
    usage()
    sys.exit()
  # normalize both tracks
  temp1 = tempfile.mktemp()
  temp2 = tempfile.mktemp()
  shutil.copy (file1, temp1)
  shutil.copy (file2, temp2)
  normalizeMP3Tag(temp1)
  normalizeMP3Tag(temp2)

  tag1 = MP3(file1, ID3=EasyID3)
  tag2 = MP3(file2, ID3=EasyID3)
  

  if filecmp.cmp(temp1, temp2):
    print "Files %s and %s are identical" % (file1,file2)
  else:
    writeMP3Tag(temp2, tag1)
    if filecmp.cmp(temp1, temp2):
      print "Audio-Data in Files %s and %s is identical, but Tags differ!" % (file1,file2)
      diff = difflib.ndiff(tag1.pprint().splitlines(1), tag2.pprint().splitlines(1))
      print "--- %s %s" % (time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getmtime(file1))),file1)
      print "+++ %s %s" % (time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getmtime(file2))),file2)
      print ''.join(diff),
    else:
      print "Files %s and %s differ in Tags and Audio!" % (file1,file2)
  os.remove(temp1)
  os.remove(temp2)
  
def normalizeMP3Tag(file):
  writeMP3Tag(file,MP3(file, ID3=EasyID3))

def writeMP3Tag(file, tag):
  m = MP3(file, ID3=EasyID3) 
  #try:
  #  m.add_tags(ID3=EasyID3)
  #  message = "Added tags to %s" , file
  #except mutagen.id3.error:
  #  message = file, "already had tags"
  #print message
  for s in tag.keys():
    m[s] = tag[s]
  m.save()

def usage():
  print "Usage: python ", sys.argv[0], " <MP3-file1> <MP3-file2>"

if __name__ == "__main__":
  main()

