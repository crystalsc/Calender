#Lists for the days, months, and how many days are in each month
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
monthName = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
#Part 1
def welcome():
    """
    This function welcomes the user to the service and explains what it does
    """
    print("Welcome to the calender print service!")
    print("This program will print a calender based on the first day you wish the year or month to start.")
#Part 2
def startingService():
    """
    This function finds out if the user wishes to start the service. If not the service ends, if they say yes the service continues.
    """
    startService = str(input("Would you like to start the calender printing service? Yes or No. ")) #Finds out if the user wants to start the calender printing service
    while startService != "Yes" and startService != "No": #Verifies that user enters a valid option
        startService = str(input("Please enter Yes or No with proper capitalization. ")) #Allows user to re-enter their answer if it was not valid
    if startService == "Yes":
        return "Yes"
    else:
        return "No"
#Part 3
def userWantsService(days):
    """
    This function finds out the day that the user wants to start. Based off this, the function returns an abbreviated day
    """
    firstDayOfTheWeek = str(input("What day of the week would you like to start on?\nSunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday: ")) #Finds out what day of the week the user wants to start with
    #Verifies that user enters a valid option
    daysOfTheWeek = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    while firstDayOfTheWeek not in daysOfTheWeek:
        firstDayOfTheWeek = str(input("Please enter a valid day and capitalize the first letter: ")) #Allows user to re-enter their answer if it was invalid
    #Matches indecies between the daysOfTheWeek and the days lists to return the abbreviated day
    findDayOfWeekIndex = daysOfTheWeek.index(firstDayOfTheWeek)
    abbreviatedDay = days[findDayOfWeekIndex]
    return abbreviatedDay
    
#Part 4
def selectDisplayChoice():
    """
    This function asks the user if they want to print a year, a month, or end.
    """
    userChoice = str(input("What would you like to print:\ny: print the entire year\nm: print a month\ne: end\n ")) #Finds out if the user wants to print the year, a specific month, or end.
    while userChoice != "y" and userChoice != "m" and userChoice != "e": #Verifies that the user enters a valid answer
        userChoice = str(input("Please enter y, m, or e. ")) #Allows user to re-enter their answer if it was invalid
    if userChoice == "y":
        return "y"
    elif userChoice == "m":
        return "m"
    else:
        return "e"
def userSelectsM(monthName):
    """
    This function occurs if the user selects m in the selectDisplayChoice function.
    It lets the user pick the month they want to print and returns the name the abbreviated month.
    """
    monthPicked = str(input("What month would you like to print a calender for? ")) #Finds out which month the user wants to print if they select m
    #Verifies that the user selects a valid option
    fullMonths = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    while monthPicked not in fullMonths:
        monthPicked = str(input("Please enter a valid month and capitalize the first letter. ")) #Allows user to re-enter an invalid answer
    findIndex = fullMonths.index(monthPicked) #Returns the abbreviation of the month by matching up the fullMonths and monthName abbreviations
    abbreviatedMonth = monthName[findIndex]
    return abbreviatedMonth

def printMonthName(month): 
    """
    This function prints the name of the month in the middle of the calender
    """
    print("         " + month)
def printDayHeader():
    """
    This function prints the days of the week by looping through the days list
    """
    index = 0
    while index < 7:
        print(days[index], end=' ')
        index += 1
    print()
def printDays(firstDayOfTheWeek, month):
    """
    This function prints the days in each month
    """
    #Prints the spaces before the first day of the month
    #If the first day is a sunday (index of 0 in days list) there are no spaces
    i = 0
    while i<=days.index(firstDayOfTheWeek):
        if i>=1:
            print("   ", end=' ')
        else:
            print("", end='')
        i+=1
    n = 1
    #Prints the dates until the last day in the month
    #If the number is less than 10 there is more space afterwards
    #When the date hits the end of a line (meaning its on a saturday) the calender goes to the next line
    while n<=daysInMonth[monthName.index(month)]:
        if n<10:  
            if (n+i-1) % 7 == 0:
                print(n)
            else:
                print(n,' ', end=' ')
        else:
            if (n+i-1) % 7 == 0:
                print(n)
            else:
                print(n,'', end=' ')
        n+=1
    print()
#Part 5b
def printMonth():
    """
    This function prints out one month if the user picks m
    """
    #prints out the chosen month's name, the days of the week, and the actual dates using lists
    if userChoice == "m":
        month = userSelectsM(monthName)
        printMonthName(month)
        printDayHeader()
        printDays(firstDayOfTheWeek, month)
        print()
#Part 5a
def printYear(firstDayOfTheWeek): 
    """
    This function prints out an entire year by looping through the monthName list
    """
    #first prints out January because it is the starting month where the user picks the first day
    if userChoice == "y":
        printMonthName(monthName[0])
        printDayHeader()
        printDays(firstDayOfTheWeek, monthName[0])
        #Program loops through each month
        m = 1
        while m <= 11:
            printMonthName(monthName[m])#Loops through the monthName list to change to name every month 
            printDayHeader()
            #The start day of each month is based on the end day of the last month to determine the number of indents
            indents = (daysInMonth[monthName.index(monthName[m-1])] + days.index(firstDayOfTheWeek))%7
            newFirstDay = days[indents]
            firstDayOfTheWeek = newFirstDay #Changes the firstDayOfTheWeek to the newFirstDay because the first day changes for every month
            printDays(firstDayOfTheWeek, monthName[m]) #Loops through the daysInMonth list to print the correct number of days in each month                               
            m+=1

def startAnotherService():
    """
    This function finds out if the user wants to start another service if they pick e
    """
    anotherService = str(input("Do you wish to start another calender printing service? "))
    while anotherService != "Yes" and anotherService != "No": #Verifies that the user enters a valid option
        anotherService = str(input("Please enter Yes or No. ")) #User can retype their option if invalid
    return anotherService
   
#Starting Program
"""
This part starts the actual program. 
The first time it goes through it asks if the user wants to start, the first day, and prints the month/year accordingly.
If the user says no to starting/restarting the service it prints good bye.
"""
welcome()
startService = startingService() #Finds out if user wants to start the calender service
#If the user wants to start the calender service, ask what day they want to start and what they want to print
if startService == "Yes":
     firstDayOfTheWeek = userWantsService(days)
     userChoice = selectDisplayChoice()
     printMonth()
     printYear(firstDayOfTheWeek)
     userChoice = selectDisplayChoice() #Asks the user if they want to print a year, a month, or end
     #If the user chooses "e" they're asked if they want to start another program, otherwise a new service starts
     if userChoice == "e":
         startService = startAnotherService()
     else:
         startService == "Yes"
#Does the same thing as the if statement above but changes the order so that selectDisplayChoice() adn userWantsService(days) is not repeated twice in one loop
while startService == "Yes":
    printMonth()
    printYear(firstDayOfTheWeek)
    userChoice = selectDisplayChoice() #Asks the user if they want to print a year, a month, or end
    #If the user chooses "e" they're asked if they want to start another program, otherwise a new service starts
    if userChoice == "e":
         startService = startAnotherService()
         if startService == "Yes": #If the user wants to restart, a display is shown for year, month, or end
             userChoice = selectDisplayChoice()
             firstDayOfTheWeek = userWantsService(days)
    else:
         startService == "Yes"
print("Good bye")
