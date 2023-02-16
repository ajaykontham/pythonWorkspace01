
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("textFile.txt"):
        # Get the path to the file in the current directory

        src = path.realpath("textFile.txt")

        # Backup copy by appending "bak" to the name
        # dest = src + ".bak"
        # shutil.copy(src, dest)

        # Rename original file
        # os.rename("textFile.txt.bak", "textFileBackup.txt")

        # Put things into a ZIP archive
        # rootDir, tail = path.split(src)
        # shutil.make_archive("archivePy", "zip",rootDir)

        # More control over ZIP file

        with ZipFile("test.zip", "w") as newzip:
            newzip.write("textFile.txt")
            newzip.write("textFileBackup.txt")


if __name__ == "__main__":
    main()