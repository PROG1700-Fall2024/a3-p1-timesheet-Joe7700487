#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     w0500154
#Student Name:  Joseph Petrash

# function to ask the user for 5 days of hours
def getHours(day):
    # ask for hours for 5 days
    for i in range(5):
        # get input
        hours = int(input("Enter hours worked on Day #{0}: ".format(i + 1)))
        # add input to the list
        day.append(hours)

# function to calculate the average of the list
def getAverage(day):
    # place holder for sum of all in the list
    sum = 0
    # loop over the list and add every item together
    for i in range(len(day)):
        sum = sum + day[i]
    # divide it by the list length
    average = sum / len(day)
    # return average
    return average

# function to get days where hours were under 7
def getSlackedDays(day):
    minHours = 7
    # check every list item
    for i in range(len(day)):
        # check if list item is less than 7
        if day[i] < minHours:
            print("Day #{0}: {1} hours".format(i + 1, day[i]))

# function to return the days where you worked the most amount of hours
def getMaxDays(day):
    # get the maximum value in the list
    maxHours = max(day)
    # declare output
    output = ""
    # check if the highest hour appears just once
    if day.count(maxHours) == 1:
        # if highest hour only appears once, output the one index
        output = str(day.index(max(day)) + 1)
        return "Day {0} where you worked {1} hours.".format(output, maxHours)
    else:
        # if highest hour appears more than once cycle through each item in the list
        for i in range(len(day)):
            # check if list item is equal to the highest hour
            if day[i] == maxHours:
                # add index to the output string
                output = output + str(i + 1) + ", "
        # return the final string
        return "Days {0} where you worked {1} hours each.".format(output, maxHours)

#function to display the final stats
def outputHours(day):
    print("----------------------------------------------------------")
    # print the days with the most hours worked
    print("The most hours worked was on: ")
    print("{0}".format(getMaxDays(day)))
    print("----------------------------------------------------------")
    # print the sum of the list and the average of the list
    print("The total amount of hours worked was: {0}".format(sum(day)))
    print("The average number of hours worked each day was: {0}".format(getAverage(day)))
    print("----------------------------------------------------------")
    # print the days where hours was less than 7
    print("Days you slacked off: ")
    getSlackedDays(day)
    print("----------------------------------------------------------")

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # Init global variables
    day = []
    # get hours
    getHours(day)
    # output hours
    outputHours(day)

    # YOUR CODE ENDS HERE
main()