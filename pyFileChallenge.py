#List the file name in the directory
#list the total files byte size
#Create a results folder
#Create a results.txt file that lists

import os
from os import path
import shutil

def main():

    fsize=0
    for x in os.listdir():
        if path.isfile(x):
            fsize += fsize + path.getsize(x)
    print(fsize)

    # src = path.realpath("textFile.txt")
    # rootDir, filename = path.split(src)
    # print(rootDir)
    if not path.exists("results"):
        os.mkdir("results")
    if not path.exists("results/results.txt"):
        resFile = open("results/results.txt", "w+")
        if resFile.mode == "w+":
            resFile.write("Total Byte Count: " +  str(fsize) + "\n")
            resFile.write("File List" + "\n")
            resFile.write("______________" + "\n")
            for x in os.listdir():
                if path.isfile(x):
                    resFile.write(x + "\n")
            resFile.close()


    # pathNew = path.join(rootDir,"results")
    # resultsFilePath = path.join(pathNew,"results.txt")
    # if not path.exists(pathNew):
    #     os.mkdir(pathNew)
    # if not path.exists(resultsFilePath):
    #     open(resultsFilePath, "w+")
    #
    # if path.exists(resultsFilePath):
    #     resultsFile = open(resultsFilePath,"a+")
    #     resultsFile.write("Total Byte Count: " +  str(fsize) + "\n")
    #     resultsFile.write("======================" + "\n")
    #     for x in os.listdir():
    #         if path.isfile(x):
    #             resultsFile.write(x + "\n")
    #     resultsFile.close()
os.re
if __name__ == "__main__":
    main()