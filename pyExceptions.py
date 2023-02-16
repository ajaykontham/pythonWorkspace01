
try:
    x = 10 / 0
except:
    print("There is an exception")


try:
    num = input("Provide a value to divide:")
    print(10/int(num))
except ZeroDivisionError as e:
    print("You can not divide by Zero")
except ValueError as e:
    print("Please provide a valid number")
    print(e)
finally:
    print("This code runs")


