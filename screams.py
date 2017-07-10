import os
import sys
import time
data = raw_input()

platform = sys.platform

if "linux" in platform:
        
        for x in data:
                if x == " ":
                   time.sleep(0.2)
                else:
                        os.system("play " + x + ".wav")

if "darwin" in platform:
        
        for x in data:
                if x == " ":
                   time.sleep(0.2)
                else:
                        os.system("afplay " + x + ".wav")

if "win" in platform:
        import winsound
        
        for x in data:
                if x == " ":
                   time.sleep(0.2)
                else:
                        winsound.PlaySound(x + ".wav", winsound.SND_FILENAME)

print "song complete"
