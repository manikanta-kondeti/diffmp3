## What is diffmp3? ##
With the script, it is possible to compare MP3 files.
Shows diff summary of MP3-file-comparison.
Compares binary MP3-Files and shows diffffernces
in ID3-Tags.

## Usage ##
It is a simple and easy console command, with
just two parameters:
```
python diffmp3.py MP3-File MP3-File2 
```

  * It compares the Files, possible output is:
    1. files are exactly the same
    1. Audio-Data is identical, but Tags differ!
      * Output like:
```
Audio-Data in Files 01 a hard day's night.mp3 and example.mp3 is identical, but Tags differ!
--- 2009-09-17 15:21:09 01 a hard day's night.mp3
+++ 2009-09-17 15:58:48 example.mp3
  MPEG 1 layer 3, 128000 bps, 44100 Hz, 153.39 seconds (audio/mp3)
  album=A Hard Days Night
  artist=The Beatles
- date=1964
?         ^
+ date=1963
?         ^
  genre=Rock
  title=01 a hard day's night
  tracknumber=1

```
    1. Both audio-data and tags differ!



## Requirements ##
Installation of **Mutagen** Library required:
  * http://code.google.com/p/mutagen/ - Python multimedia tagging library
  * Installation of Python 2.5.x or higher (tested on 2.6.2)
  * should be OS-independent (tested on Windows XP and Mac OS X Leopard)

You can browse the source [here](http://code.google.com/p/diffmp3/source/browse/trunk/diffmp3.py)