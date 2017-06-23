import os
import sys

if len(sys.argv) is not 2:#takes in one argument for output textfile.
    sys.exit("Error, script needs one command-line argument. (output.txt File)")

list=""#set up output name list
start=0#start of python script location string
end=len(sys.argv[0])#end of python script location string
#print(start)
#print(end)

#find python script name
while(sys.argv[0].find("/",start,end)!=-1):
    #print(sys.argv[0].find("/",start,end))
    start=sys.argv[0].find("/",start,end)+1

#create file name list excluding python script name
dirList = os.listdir("./")
for filename in dirList:
    if(filename!=sys.argv[0][start:end]):
        list=list+filename+"\n"

print("Now writing the following list of file names to %s" %sys.argv[1])
print(list)

#open output text file and write the file name list. Then close output file.
FILEOUT = open(sys.argv[1], 'w')
FILEOUT.write(list)
FILEOUT.close()
