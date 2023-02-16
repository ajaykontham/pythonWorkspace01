
def main():
    #Open / Create a file
    # myfile = open("textFile.txt","w+")

    #Open / edit file
    # myfile = open("textFile.txt","a+")
    #
    # #Write some content into the file
    # for i in range(10):
    #     myfile.write("This is a new text line\n")
    #
    # #Close the file
    # myfile.close()

    # Read the file contents
    myFile = open("textFile.txt","r")
    if myFile.mode == 'r':
        # contents = myFile.read()
        # print(contents)

        fl = myFile.readlines()
        for i in fl:
            print(i)

if __name__ == "__main__":
    main()


