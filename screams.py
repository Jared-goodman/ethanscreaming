import os
import sys

data = raw_input()

platform = sys.platform

if "linux" in platform:
        
        for x in data:

                os.system("play " + x + ".wav")

if "darwin" in platform:
        
        for x in data:

                os.system("afplay " + x + ".wav")

if "win" in platform:
        import winsound
        
        for x in data:

                winsound.PlaySound(x + ".wav", winsound.SND_FILENAME)

print "song complete"
