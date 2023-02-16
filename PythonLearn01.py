# print ("hello World!")

# name = input("Name: ")
# print("Hello ", name)

#Variables

myint = 5
myfloat = 5.5
mystr = "This is a test string"
mybool = True
mylist = [0,1,"two",3,4,"five",4.5, False]
mytuple = (0,1,2)
mydict = {1:"one", 2: "two", "test": "newTest"}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

#redeclaring variables

myint = "Five"
# print(myint)

# Accessing Object items
# print(mylist[6])
# print(mylist[1:3])
# print(mylist[1:9:3])
# print(mydict['test'])


#Reverse
# print(mylist[::-1])

# Adding different data types
# print("String" + str(123))

# Global and local variables

def someFunction():
    global mylist
    print(mylist)
    mylist=[1,2,"three"]
    print(mylist)

# someFunction()
# print(mylist)

# del mylist
# print(mylist)

#Funtion 1: without args
def func1():
    print("This is function 1")

# func1()
# print(func1())
# print(func1)

#Function 2: With args
def func2(arg1,arg2):
    print("Arg1: " + arg1 +"\nArg2: " + arg2)

# func2("Value1", "Val2")

#Function 3: Return a value
def cube(x):
    return x * x * x

# print(cube(3))

#Function 4:
def power(num,x=2):
    result = 1;
    for i in range(x):
        result = result * num
    return result

# print(power(2))
# print(power(2, 3))
# print(power(x=5, num=2))

#Function 5: Multiple args
def multiSum(*args):
    result = 0;
    for x in args:
        result = result + x
    return result

# print(multiSum(5,10, 15));

def main1():
    x, y= 10, 100

    #Conditions

    if x < y :
        result = "x is less than y"
    elif x == y:
        result = "x is equal to y"
    else:
        result = "x is greater than y"
    # print(result)

    #2 Conditional Statement

    result2 = "x is less than y" if x < y else "x is greater or equal to y"
    # print(result2)

    #3 Match Case
    value = 9
    match value:
        case "one":
            result3= 1
        case "two":
            result3= 2
        case "three" | "four":
            result3= (3,4)
        case _:
            result3= -1
        
    # print(result3)

if __name__ == "__main__":
    main1()

# Loops
def main():
    x = 0

    #While Loop
    while(x <= 5):
        # print(x)
        x = x + 1

    #For Loop
    # for x in range(5, 10):
        # print(x)

    #For Loop over a collection
    days = ["sun","mon","tue","wed","thu","fri","sat"]
    # for x in days:
        # print(x)

    # For loop - Break
    for x in range(3,10):
        if(x == 7):
            break
        # print(x)

    #For loop - continue
    for x in range(3,10):
        if x % 2 == 0:
            continue
        # print(x)

    #For loop enumerate
    days=["sun","mon","tue","wed","thu","fri","sat"]
    for i,d in enumerate(days):
        print(i,d)

if __name__ == "__main__":
    main()
        