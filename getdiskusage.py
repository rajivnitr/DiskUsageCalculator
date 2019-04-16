import subprocess
import sys
import os
import json

def getdiskusage(path):

    
    if os.path.exists(path):
        filePathandSize={}
        listingOfFiles=[]
        FinalListOfFileAndSize={}

        p = subprocess.Popen( 'ls ' + str(sys.argv[1]), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            
            script= "du "+ str(sys.argv[1])+"/"+str(line.decode('ascii')).strip('\n') + " | awk '{print($1)}'"
            proc = subprocess.Popen(script, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
            output = proc.communicate()[0]
            filePathandSize[str(sys.argv[1])+"/"+str(line.decode('ascii')).strip('\n')]=int.from_bytes(output, byteorder='big')
            listingOfFiles.append(filePathandSize)
            filePathandSize={}
            FinalListOfFileAndSize["Files"]=listingOfFiles
            retval = p.wait()
            
        jsonreponse=json.dumps(FinalListOfFileAndSize, ensure_ascii=False)
        return jsonreponse

if __name__== "__main__":
    
    result= getdiskusage(str(sys.argv[1]))
    if str(result)=='None':
        print("Enter correct directory path")
    else:
        print(result)
