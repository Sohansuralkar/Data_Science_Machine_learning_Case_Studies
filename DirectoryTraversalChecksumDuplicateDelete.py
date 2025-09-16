import os
import sys
import time
import hashlib            #for checksum library

def CalculateChecksum(path,Blocksize = 1024):
    fobj = open(path,"rb")

    hobj = hashlib.md5()   #sha1 pn use kru shkto   md5 algorithm ahe 

    buffer = fobj.read(Blocksize)
    while(len(buffer)> 0 ):
        hobj.update(buffer)
        buffer = fobj.read(Blocksize)
    fobj.close()
  

    return hobj.hexdigest()   

def directorywatcher(DirectoryName ="Marvellous"):
        flag  = os.path.isabs(DirectoryName)

        if(flag == False):
            DirectoryName = os.path.abspath(DirectoryName)
        flag = os.path.exists(DirectoryName)


        if (flag == False):
            print("path is invalid")
            exit()
        flag = os.path.isdir(DirectoryName)

        if(flag == False):
             print("path is valid but the traget is not a directory")
             exit()


        for FolderName, SubFoldernames, Filenames in os.walk("Marvellous"):

            for fname in Filenames:
                 fname = os.path.join(FolderName,fname)
                 checksum = CalculateChecksum(fname)
                 print("file name :",fname)
                 print("Checksum is :",checksum)
                 print()
      

        timestamp = time.ctime()

        filename = "MarvellousLog%s.log" %(timestamp)
        filename = filename.replace(" ","_")
        filename = filename.replace(":","_")
        print(filename)

        #print(timestamp)

        fobj = open("MarvellousLogSun_Jun__8_19_02_53_2025.log","w")

        Border = "-"*54

        fobj.write(Border)
        fobj.write("This file is Marvellous Automation")
        fobj.write("This file is Marvellous Automation directory cleaner")
        fobj.write(Border+"\n")

        fobj.write(Border+"\n")
        fobj.write("This is created as \n"+timestamp+"\n")
        #fobj.write(timestamp)

def FindDuplicate(DirectoryName ="Marvellous"):
        flag  = os.path.isabs(DirectoryName)

        if(flag == False):
            DirectoryName = os.path.abspath(DirectoryName)
        flag = os.path.exists(DirectoryName)


        if (flag == False):
            print("path is invalid")
            exit()
        flag = os.path.isdir(DirectoryName)

        if(flag == False):
             print("path is valid but the traget is not a directory")
             exit()


        Duplicate = {}

        for FolderName, SubFoldernames, Filenames in os.walk("Marvellous"):

            for fname in Filenames:
                 fname = os.path.join(FolderName,fname)
                 checksum = CalculateChecksum(fname)

                 if checksum in Duplicate:
                      Duplicate[checksum].append(fname)
                      
                 else:
                      Duplicate[checksum] = [fname]

        return Duplicate

def DisplayResult(MyDict):
     Result = list(filter(lambda X: len(X)>1,MyDict.values()))
     print(Result)     
       
def main():
    Border = "-"*54
    print(Border)
    print("______________________________________________")
    print("______________________________________________")
    print("_________________marvellous___________________")
    print(Border)
    
    if(len(sys.argv)== 2):

        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This is apllication is used to perform directory cleaning")
            print("This is directory automation script")

        elif(sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
              print("used given script as ")
              print("Scripname.py NameofDirectory")
              print("please provide valid absolute path")
        else:
             Result = FindDuplicate(sys.argv[1])
             DisplayResult(Result)

    else:
        print("invalid number of command line arguments")
        print("used given flag as:")
        print("--h : used for help")
        print("--u : used for usage")

    
    print(Border)
    print("______________________________________________")
    print("_________Thank u for using our script__________")
    print("_________marvellous infosystem_________________")
  

if __name__ == "__main__":
    main()