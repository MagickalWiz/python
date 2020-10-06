def leap_year(y):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        return "yes"
    else:
        return "no"

def number_of_days(m):
    if(m == "1" or m == "3" or m == "5" or m == "7" or m == "8" or m == "12"):
        return "31"
    elif(m == "4" or m == "6" or m == "9" or m == "10" or m == "11"):
        return "30"
    else:
        return "28"

def days_left(d,m,y,dl):
    if(m == 1):
        dl = (dl + 334) + (31 - d)
        if(leap_year(y) == "yes"):
            dl = dl + 1
        print(dl)
    elif(m == 2):
        dl = (dl + 304) + (28 - d)
        if(leap_year(y) == "yes" and d != 29):
            dl = dl + 1
        print(dl)
    elif(m == 3):
        dl = (dl + 267) + (31 - d)
        print(dl)
    elif(m == 4):
        dl = (dl + 245) + (31 - d)
        print(dl)
    elif(m == 5):
        dl = (dl + 214) + (31 - d)
        print(dl)
    elif(m == 6):
        dl = (dl + 184) + (30 - d)
        print(dl)
    elif(m == 7):
        dl = (dl + 153) + (31 - d)
        print(dl)
    elif(m == 8):
        dl = (dl + 122) + (31 - d)
        print(dl)
    elif(m == 9):
        dl = (dl + 91) + (30 - d)
        print(dl)
    elif(m == 10):
        dl = (dl + 61) + (30 - d)
        print(dl)
    elif(m == 11):
        dl = (dl + 31) + (30 - d)
        print(dl)
    elif(m == 12):
        dl = dl + (31 - d)
        print(dl)

dl = 0
print("Please enter a date")
d = int(input("Day: "))
m = int(input("Month: "))
y = int(input("Year: "))
print("Menu:")
print("1) Calculate the number of days in the given month.\n2) Calculate the number of days left in the given year.")
nd = input("")
if(nd == "1"):
    #print(leap_year(y))#debug
    if(leap_year(y) == "yes" and m == 2):
        print(int(number_of_days(m)) + 1)
    elif(leap_year(y) == "no"):
        print(int(number_of_days(m)))
elif(nd == "2"):
    days_left(d,m,y,dl)

else:
    print("Invalid, try again")
