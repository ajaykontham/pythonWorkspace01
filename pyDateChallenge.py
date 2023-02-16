
import datetime
from datetime import date
from datetime import datetime
import calendar

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def printWeekday():
    print("Which day of the week do you want to count?")
    for x in days:
        print(str(days.index(x)) + ": ",x)
    return input("Or 'exit' to close : ")

def numberOfDays(year,month):
    numberOfDays = 0
    for x in calendar.monthcalendar(year,month):
        if x[1] != 0:
            numberOfDays = numberOfDays + 1
    return numberOfDays

def main():
    run = True
    while run:
        weekday = printWeekday()
        if weekday.isdigit() and int(weekday) < len(days):
            try:
                yearVal = int(input("Enter Year: "))
                monthVal = int(input("Enter Month: "))
                numberOfDaysVal = numberOfDays(yearVal,monthVal)

                print("\n-----------START-----------")
                print("There are", numberOfDaysVal,days[int(weekday)],"in the", monthVal,"th month of year",yearVal)
                print("-----------END----------- \n")
            except ValueError as e:
                print(e)
                print("Please enter a valid error!")
        elif weekday.isdigit() and int(weekday) > len(days):
            print("Enter a valid weekday!")
        elif weekday.isalnum() and weekday != "exit":
            print("Enter a valid weekday value!")
        elif weekday == "exit":
            run = False

if __name__ == "__main__":
    main()