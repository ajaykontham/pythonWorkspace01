
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar

def main():

    # DATE OBJECTS
    # today = date.today()
    # print(today)
    # print(datetime.today())
    # print("Date components:", today.day, today.month, today.year)
    # print("Today's weekday # is", today.weekday())

    #DATETIME objects
    # now = datetime.now()
    # today = datetime.today()
    # print(now)
    # print(today)
    # currentTimeNow = datetime.time(datetime.now())
    # print(currentTimeNow)

    #Formatting Dates and Times
    # now = datetime.now()
    # print(now.strftime("The current year is %Y"))
    # # %a: Day of the week(3) %A:Day of the week(Full)
    # # %b: Month(3) %B: Month(Full)
    # # %d: Day of the month %D: current date ; %y: Year(2) %Y: Year(4)
    # print(now.strftime("%A, %d %B, %Y"))
    # print(now.strftime("Locale Date and Time: %c"))
    # print(now.strftime("Locale Date: %x"))
    # print(now.strftime("Locale Time: %X"))
    # print (now.strftime("Current Time: %I:%M:%S %p"))
    # print (now.strftime("24 Hour Time: %H:%M"))


    # print(timedelta(days=365, hours=5, minutes=1))
    # now = datetime.now()
    # print("Today:", now)
    # print("One year from now", str(now + timedelta(days=365)))
    # print("In 2 weeks and 3 days, it will be", str(now + timedelta(weeks=2,days=3)))
    # print("In 20 days, it will be", str(now + timedelta(days=20)))

    ## TimeDelta
    # today = date.today();
    # afd = date(today.year,4,1)
    # if afd < today:
    #     print("April Fools day already went by", (today - afd).days,"days")
    #     afd = afd.replace(afd.year + 1, afd.month, afd.day)
    #     print("April Fools day will come in", str((afd-today).days),"days")

    # c = calendar.TextCalendar(calendar.SUNDAY)
    # str = c.formatmonth(2022,1,0,0)
    # print(str)

    #HTML Calendar
    # hc = calendar.HTMLCalendar(calendar.SUNDAY)
    # strHC = hc.formatmonth(2022,1)
    # print(strHC)

if __name__ == "__main__":
    main()