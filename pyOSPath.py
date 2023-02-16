
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main ():

    #Print the name of the os
    # print(os.name)

    #Check if an item exits
    # print("Item exists", path.exists("textFile.txt"))
    # print("Item is a file:", path.isfile("textFile.txt"))
    # print("Item is a dir:", path.isdir("textFile.txt"))

    # # File path
    # print("Item path:", path.realpath("textFile.txt"))
    # print("Item path and Name:", path.split(path.realpath("textFile.txt")))

    # Modification Time
    t= time.ctime(path.getmtime("textFile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textFile.txt")))

    #Date Modification
    td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textFile.txt"))
    print(td.total_seconds())

if __name__ == "__main__":
    main()