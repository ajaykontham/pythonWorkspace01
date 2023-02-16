
def palindromeFunc(inValue):
    inputVal = (str(inValue)).lower()

    if not inputVal.isalnum():
        newVal = ""
        for character in inputVal:
            if character.isalnum():
                newVal += character
        inputVal = newVal

    if inputVal.isalnum() and inputVal == inputVal[::-1]:
        print("Palindrome:", True)
    elif inputVal == 'exit':
        exit()
    else:
        print("Palindrome:", False)

# palindromeFunc()

def palindromeWhileFunc():
    run = True
    while(run):
        inputVal = input("Enter value to test for palindrome:")

        if inputVal == 'exit':
            run = False
        else:
            palindromeFunc(inputVal)
            # print("Still running")

palindromeWhileFunc();