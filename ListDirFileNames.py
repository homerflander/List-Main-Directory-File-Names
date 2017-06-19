import os
import sys

if len(sys.argv) is not 2:#takes in one argument for output textfile.
    sys.exit("Error, script needs one command-line argument. (output.txt File)")

list=""

dirList = os.listdir("./")
for filename in dirList:
    list=list+filename+"\n"

print("Now writing the following list of file names to %s" %sys.argv[1])
print(list)

FILEOUT = open(sys.argv[1], 'w')
FILEOUT.write(list)
FILEOUT.close()
