#Imports all modules from the Turtle Library
from turtle import *
screensize(500,500)
speed(0)
#==========================================================================================#
#----------------------------- I N T R O  S C R E E N -------------------------------------#
#==========================================================================================#
def intro():
    penup()
    write("Character Occurence Pie-Chart", False, 'center', font=('Arial', 18, 'normal'))
    sety(ycor()-25)
    write("Coded By:", False, 'center', font=('Arial', 15, 'normal'))
    sety(ycor()-20)
    write("Ayushya Amitabh", False, 'center', font=('Arial', 15, 'normal'))
    sety(ycor()-18)
    write("&", False, 'center', font=('Arial', 12, 'normal'))
    sety(ycor()-18)
    write("Nabil Ahmed Khatri", False, 'center', font=('Arial', 15, 'normal'))
    sety(ycor()-20)
    left(90)
#==========================================================================================#
#--------------------------- M A I N  F U N C T I O N -------------------------------------#
#==========================================================================================#
def main():
    home()
    clear()
    intro()
    #Alphabets - Dictionary containing count of each character that appears
    alphabets = {}

    #dictInsert - Function used to insert new alphabet or increase alphabet count
    #             in given dictionary
    def dictInsert(alphabet, dictionary):
        alphaCount = 0
        alphabet = str(alphabet).lower()
        for key in dictionary:
            if key == alphabet:
                alphaCount = 1
                currVal = int(dictionary[alphabet])
                dictionary[alphabet] = currVal + 1
        if alphaCount == 0:
            dictionary[alphabet] = 1

    #fileName - Storing the file name provided by the user.
    fileName = textinput("File","Enter your file name: (include '.txt')")
    #readerFile - Opens the file provided in read-mode
    readerFile = open(fileName, 'r')

    #Goes through each letter in the given file to fill the 'alphabets' dictionary
    charCount = 0
    for line in readerFile:
        for char in line:
            dictInsert(char,alphabets)
            charCount += 1

    #sortedDictKeys - List to store the keys (same as the keys of the dictionary),
    #                 in ascending order
    sortedDictKeys = []

    #sorting - Function used to sort the generated dictionary in ascending order
    def sorting(dictionary):
        dictValues = []
        for key in dictionary:
            dictValues.append(dictionary[key])
        dictValues.sort(reverse=True)
        for value in dictValues:
            for key in dictionary:
                if dictionary[key] == value:
                    exists = 0
                    for already in sortedDictKeys:
                        if already == key:
                            exists = 1
                    if exists == 0:
                        sortedDictKeys.append(key) 
    #Will now sort the file generated dictionary of alphabets in ascending order
    sorting(alphabets)

    #percentages - New dictionary that will store the keys in and their respective
    #              percentage values
    percentages = {}

    #radius - Radius of the circle to be draw drawn / Radius of the Pie Chart
    radius = 250

    #colors - list of all available colors for the pie chart to shift through
    colors = ['azure',
              'cadet blue',
              'coral',
              'cyan',
              'gold',
              'gray',
              'khaki']
    
    #penup - Lifts up the marking tool in Turtle GUI to avoid making random /
    #        un-intentional marks on the screen
    penup()

    #numOut - Number of characters to be displayed in the pie chart
    #         Takes in a number with limits set to between 1 and the number
    #         of unique keys present in the list 'sortedDictKeys'
    numOut = numinput("Number of Sections", "Enter a number", 1, minval=1, maxval=len(sortedDictKeys))
    #numOut - Makes sure the input provided is interpreted as an integer
    numOut = int(numOut)

    #Will now generate values to be stored in the 'percentages' dictionary
    for i in range(numOut):
        percentages[sortedDictKeys[i]] = 360*(alphabets[sortedDictKeys[i]]/charCount)

    #angletracker - Used to change the heading after each section of the pie chart is drawn
    angletracker = 0

    #partCounter - Useed to select the corresponding color from the 'colors' list
    partCounter = 0

    #percenttracker - Used to calculate what amount is left after the requested
    #                 number of segments have been drawn
    percenttracker = 0

    clear()
    home()
    
    #Will now draw each segment of the Pie Chart
    for i in range(numOut):
        #Choosing Fill Color for current segment
        fillcolor(colors[partCounter])
        #Increments the segment / part counter by 1
        partCounter += 1
        if partCounter == len(colors):
            partCounter = 0
        #Begins Filling and Drawing
        begin_fill()
        #Moves forward by the given radius amount
        forward(radius)
        #Rotates Left 90 degrees
        left(90)
        #Draws half of the segment
        circle(radius,percentages[sortedDictKeys[i]]/2)
        #Creates the String to be displayed next to the segment
        charKey = "'"+sortedDictKeys[i]+"' , "+"%.2f" % (percentages[sortedDictKeys[i]]/360)
        #Adds the percents being covered by this whole segment to the percenttracker
        percenttracker += percentages[sortedDictKeys[i]]/360
        #Turns right 90 degrees
        right(90)
        #Moves 40 units away from the Pie Chart
        forward(40)
        #Writes the above generated string 'charKey' next to the respective segment
        write(charKey, False, align="right",font=("Arial", 10, "normal"))
        #Reverses the steps taken before Writing
        backward(40)
        left(90)
        #Completes the second half of the segment
        circle(radius,percentages[sortedDictKeys[i]]/2)
        #Increments the angletracker by the angle covered by the whole segment
        angletracker += percentages[sortedDictKeys[i]]
        home()
        #Sets new heading using the new value for the angletracker
        setheading(angletracker)
        #Ends Segment
        end_fill()
    #Checks if the user has requested for all the alphabets present to be printed out,
    #If not then, a segment labeled All other letters will be created
    if numOut != len(sortedDictKeys):
        #Calcultes the remaining angle by the subtracting the total angle covered from
        # 360 degrees
        remainsAngle = 360-angletracker
        #Selects the next color in the colors list to fill the new segment with
        fillcolor(colors[partCounter])
        #Begins creating new segments - process is the same as above
        begin_fill()
        forward(radius)
        left(90)
        circle(radius, remainsAngle/2)
        right(90)
        forward(40)
        leftoverPercent = "All other letters, " + "%.2f" % (1 - percenttracker)
        write(leftoverPercent, False, align="right",font=("Arial", 10, "normal"))
        tilt(45)
        backward(40)
        left(90)
        circle(radius, remainsAngle/2)
        home()
        end_fill()
    #Adds message to the bottom of the screen to remind the user of how the next file
    #can be tested
    right(90)
    forward(radius +100)
    write("Click anywhere to exit.", False, 'center', font=('Arial', 15, 'normal'))
    home()
    retry = textinput("Next File?","Yes or No")
    def checkRetry(retryVal):
        if retryVal.lower() == "yes":
            main()
        elif retryVal.lower() == "no":
            bye()
        else :
            retryVal = textinput("Next File?","Invalid Input. Yes or No")
            checkRetry(retryVal)
    checkRetry(retry)
main()
exitonclick()
