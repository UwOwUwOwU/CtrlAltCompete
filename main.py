import xlsxwriter
import os
from time import sleep
from datetime import datetime
hclogin = "END0FTH3W0R1D"
hclcount = 1
slcount = 1
kickcounter = 0
offloop = 1
loggoloop = 1
while hclcount == 1:
    if kickcounter < 3:
        hclinput = input("Please enter your application password: ")
        if hclinput == hclogin:
            print("Welcome to Syclone Attendance Tracker")
            time = datetime.now()
            current_time = time.strftime("%H:%M:%S")
            print("The time is " + current_time)
            hclcount = 0
        else:
            print("You have entered the wrong password, please try again.")
            kickcounter = kickcounter + 1
    else:
        print("You have failed too many times, please try again later")
        quit()
kickcounter = 0
while offloop == 1:
    offline = input("Do you wish to use offline mode, or connect to the internet? (OFF/ON) ")
    if offline == "ON" or offline == "on":
        offloop = 0
        while slcount == 1:
            if kickcounter < 3:
                slinput = input("Please enter your school: ")
                slist = {"DPSI-SKET", "RICK-ROLL"}
                if slinput in slist:
                    print("You have chosen institution " + slinput)
                    slcount = 0
                    while loggoloop == 1:
                        print("Please login into your account for " + slinput)
                        loggo = input("Your username: ")
                        passo = input("Your password: ")
                        lodict = {
                            'King Syclone':'Platinum',
                            'Aha Aha': 'Gold'
                        }
                        if lodict[loggo] == passo:
                            print("Welcome to " + slinput + ", " + loggo)
                            loggoloop = 0
                        else:
                            print("Please try again, the account specifed doesn't exist")
                else:
                    print("You have entered an invalid code, please try again.")
                    kickcounter = kickcounter + 1

            else:
                print("You have failed too many times, please try again later")
    elif offline == "OFF" or offline == "off":
        offloop = 0
    else:
        print("You have put an invalid choice, please put the correct one")


workbook = xlsxwriter.Workbook('venv/aylmao.xlsx')
worksheet = workbook.add_worksheet()
row = 1
col = 0
worksheet.write(0, 0, 'Name')
worksheet.write(0, 1, 'Ticket')
worksheet.write(0, 2, 'Age')
worksheet.write(0, 3, 'Attendance')
for item, cost, age in (dict):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    worksheet.write(row, col + 2,  age)
    worksheet.write(row, col + 3, 'No')
    row += 1
workbook.close()

