# Method to reverse all elements in a list
# Accepts a list as an argument and returns the reversed version of that list
def reverseList(passedIn):
    reversedList = []
    for i in reversed(passedIn):
        reversedList.append(i)
    return reversedList

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = ""):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

# Can be used to print results from other methods
# Accepts list as argument
def printResults(passedIn):
    for i in passedIn:
        print(i, end="")
    print(" ")


# Converts number and exponent to a list which represents the numerical value
def convertToDecimal(number, exponent):
    numArray = []

    # Appends all values in the given number while skipping the period (.)
    for digit in number:
        if (digit == '.'):
            continue
        else:
            numArray.append(int(digit))
    # Appends the correct number of 0s to match the exponent given
    for i in range(0, (int(exponent) - (len(numArray) - 1))):
        numArray.append(0)

    return numArray


# Used in addition and multiplication to determine what value will be carried over
def carryVal(number):
    stringNum = str(number)

    if (len(stringNum) > 1):
        firstDigit = stringNum[0]

        if (firstDigit == '1'):
            return 1
        elif (firstDigit == '2'):
            return 2
        elif (firstDigit == '3'):
            return 3
        elif (firstDigit == '4'):
            return 4
        elif (firstDigit == '5'):
            return 5
        elif (firstDigit == '6'):
            return 6
        elif (firstDigit == '7'):
            return 7
        elif (firstDigit == '8'):
            return 8
        elif (firstDigit == '9'):
            return 9
    else:
        return 0


# Adapted version of bigAdd which is called by bigMultiply
def bigAdder(firstNum, secondNum):
    added = []
    result = []

    # Determines which list is longer and performs the computations accordingly
    if len(firstNum) > len(secondNum):
        carriedVal = 0
        # Since the second list is shorter, its length is used to limit the for loop
        for i in range(0, len(secondNum)):
            holdingVal = int(firstNum[i]) + int(secondNum[i]) + int(carriedVal)

            # If holdingVal is two digits or longer, adds only the last digit, otherwise adds the entirety
            if (len(str(holdingVal)) > 1):
                added.append(int(str(holdingVal)[1]))
            else:
                added.append(holdingVal)
            # Calls carryVal to determine the value which is carried to the next iteration of the loop
            carriedVal = carryVal((int(secondNum[i]) + int(firstNum[i])))
        # Appends anything from the first list which would not have been used in the computations
        for i in range(len(secondNum), len(firstNum)):
            added.append(int(firstNum[i]) + carriedVal)
            carriedVal = 0
    elif len(firstNum) < len(secondNum):
        carriedVal = 0
        # Since the first list is shorter, it is used to limit the for loop
        for i in range(0, len(firstNum)):
            holdingVal = int(firstNum[i]) + int(secondNum[i]) + int(carriedVal)

            # If holdingVal is more than one digit, only adds last digit. otherwise adds entire number
            if (len(str(holdingVal)) > 1):
                added.append(int(str(holdingVal)[1]))
            else:
                added.append(holdingVal)

            # Calls carriedVal to calculate the value that will be carried to the next iteration
            carriedVal = carryVal((secondNum[i] + firstNum[i]))
        # Appends anything from the second list which would not have been used for the calculation
        for i in range(len(firstNum), len(secondNum)):
            added.append(secondNum[i] + carriedVal)
            carriedVal = 0
    return added


# Used to perform addition
# Accepts two numbers and their exponents
def bigAdd(firstNumber, firstExponent, secondNumber, secondExponent):
    # Converting the numbers and exponents to corresponding lists
    firstNumList = convertToDecimal(firstNumber, firstExponent)
    secondNumList = convertToDecimal(secondNumber, secondExponent)
    added = []
    result = []
    # Reverses the lists for use in calculations
    reversedFirstNumList = reverseList(firstNumList)
    reversedSecondNumList = reverseList(secondNumList)

    # Determines which list is longer and performs calculations accordingly
    if len(firstNumList) > len(secondNumList):
        carriedVal = 0
        # Uses shorter list to limit for loop
        for i in range(0, len(secondNumList)):
            holdingVal = reversedFirstNumList[i] + reversedSecondNumList[i] + carriedVal

            # If holdingVal is more than one digit, adds only the last digit, otherwise adds the entire thing
            if (len(str(holdingVal)) > 1):
                added.append(int(str(holdingVal)[1]))
            else:
                added.append(holdingVal)

            # Calls carriedVal to determine the value carried over to the next iteration
            carriedVal = carryVal((reversedSecondNumList[i] + reversedFirstNumList[i]))
        # Adds anything from the longer list which wasnt used in calculations
        for i in range(len(secondNumList), len(firstNumList)):
            added.append(reversedFirstNumList[i] + carriedVal)
            carriedVal = 0
    elif len(firstNumList) < len(secondNumList):
        carriedVal = 0
        # uses shorter list to limit for loop
        for i in range(0, len(firstNumList)):
            holdingVal = reversedFirstNumList[i] + reversedSecondNumList[i] + carriedVal

            # If holdingVal is multiple digits, adds just the last one, otherwise adds entire thing
            if (len(str(holdingVal)) > 1):
                added.append(int(str(holdingVal)[1]))
            else:
                added.append(holdingVal)

            # Calls carriedVal to determine the value carried over to the next iteration
            carriedVal = carryVal((reversedSecondNumList[i] + reversedFirstNumList[i]))
        # Any values from the longer list that werent used in calculations are appended here
        for i in range(len(firstNumList), len(secondNumList)):
            added.append(reversedSecondNumList[i] + carriedVal)
            carriedVal = 0

    # Reverses the result list so it is the right way around
    result = reverseList(added)

    # Sends the results to printResults method
    printResults(result)


# Used for multiplication
# Accepts two numbers and their exponents
def bigMultiply(firstNumber, firstExponent, secondNumber, secondExponent):
    # Converts the numbers and exponents to their corresponding lists
    firstNumList = convertToDecimal(firstNumber, firstExponent)
    secondNumList = convertToDecimal(secondNumber, secondExponent)

    currentValue = []
    holdToAdd = []
    result = []
    incrementer = 0
    carriedVal = 0
    spotInList = 0
    increment = 0

    # Reverses lists for use in computations
    reversedFirstNumList = reverseList(firstNumList)
    reversedSecondNumList = reverseList(secondNumList)

    # Performs calculations based on which list is longer
    if len(reversedFirstNumList) > len(reversedSecondNumList):
        printProgressBar(0, len(reversedSecondNumList), prefix='Progress:', suffix='Complete', length=50)

        # Multiplies each digit in the shorter list by each digit in the longer list before moving on to the next digit
        for digit in reversedSecondNumList:
            printProgressBar(increment + 1, len(reversedSecondNumList), prefix='Progress:', suffix='Complete', length=50)
            increment += 1
            spotInList = 0
            currentValue = []
            carriedVal = 0
            # Actually performing the calculations
            for otherDigit in reversedFirstNumList:
                stringMultiplied = str((otherDigit * digit) + carriedVal)
                currentValue.append(stringMultiplied[len(stringMultiplied) - 1])
                heldVal = (otherDigit * digit) + carriedVal

                # If at the end of the calculation, append the entire result, otherwise just the last digit
                if (spotInList == len(reversedFirstNumList) - 1):
                    carriedVal = heldVal
                    currentValue.append(int(str(heldVal)[0]))
                else:
                    carriedVal = int(str(heldVal)[0])

                spotInList = spotInList + 1

            # Used to add extra 0s to the end of the list (Magic zeros from elementary math)
            for i in range(0, incrementer):
                currentValue.insert(0, 0)
            # Used to add the result of each iteration of the outer for loop together
            holdToAdd = bigAdder(currentValue, holdToAdd)
            incrementer = incrementer + 1
        # Reverses the list so it is the right way around
        result = reverseList(holdToAdd)
        # Sends the result to printResults
        printResults(result)
    elif len(reversedFirstNumList) < len(reversedSecondNumList):
        printProgressBar(0, len(reversedFirstNumList), prefix='Progress:', suffix='Complete', length=50)
        # Multiplies each digit of the shorter list by each digit in the longer list before moving on
        for digit in reversedFirstNumList:
            printProgressBar(increment + 1, len(reversedFirstNumList), prefix='Progress:', suffix='Complete', length=50)
            increment += 1
            spotInList = 0
            currentValue = []
            carriedVal = 0
            # Actually performs the calculations
            for otherDigit in reversedSecondNumList:

                stringMultiplied = str((otherDigit * digit) + carriedVal)
                currentValue.append(stringMultiplied[len(stringMultiplied) - 1])
                heldVal = (otherDigit * digit) + carriedVal

                # If at the end of the iteration, adds entire result to list, otherwise only adds last element
                if (spotInList == len(reversedSecondNumList) - 1):
                    carriedVal = heldVal
                    currentValue.append(int(str(heldVal)[0]))
                else:
                    carriedVal = int(str(heldVal)[0])

                spotInList = spotInList + 1
            # Used to add extra 0s to the end of the list (Magic zeros from elementary math)
            for i in range(0, incrementer):
                currentValue.insert(0, 0)

            # Used to add the results of each iteration
            holdToAdd = bigAdder(currentValue, holdToAdd)
            incrementer = incrementer + 1
        # Reverses result so it is the right way around
        result = reverseList(holdToAdd)
        # Sends result to printResults
        printResults(result)


# Determines if the first number is greater than the second
# Accepts two numbers and two exponents
def isGreaterThan(firstNumber, firstExponent, secondNumber, secondExponent):
    #Converting numbers and exponents to lists
    firstNumList = convertToDecimal(firstNumber, firstExponent)
    secondNumList = convertToDecimal(secondNumber, secondExponent)

    result = False

    #If one is longer than the other, it is greater (Negatives not quite accounted for)
    if (len(firstNumList) > len(secondNumList)):
        result = True
    elif (len(secondNumList) > len(firstNumList)):
        result = False
    #Goes through element by element to determine which is greater
    else:
        for i in range(0, len(firstNumList)):
            if (firstNumList[i] > secondNumList[i]):
                result = True
                break
            elif (secondNumList[i] > firstNumList[i]):
                result = False
                break
            else:
                continue
    # Sends result to printResults
    printResults(result)

# Determines if the first number is less than the second
# Accepts two numbers and two integers
def isLessThan(firstNumber, firstExponenet, secondNumber, secondExponent):
    #Converting numbers and exponents to lists
    firstNumList = convertToDecimal(firstNumber, firstExponenet)
    secondNumList = convertToDecimal(secondNumber, secondExponent)

    result = True

    # If one list is shorter, it is less than (Not quite accounting for negatives)
    if (len(firstNumList) > len(secondNumList)):
        result = False
    elif (len(secondNumList) > len(firstNumList)):
        result = True
    # Goes element by element to see which is less than
    else:
        for i in range(0, len(firstNumList)):
            if (firstNumList[i] > secondNumList[i]):
                result = False
                break
            elif (secondNumList[i] > firstNumList[i]):
                result = True
                break
            else:
                continue
    # Sends result to printResults
    printResults(result)

# Determines if the numbers are equal
# Accepts two numbers and two exponents
def isEqual(firstNumber, firstExponenet, secondNumber, secondExponent):
    #Converts numbers and exponents to corresponding lists
    firstNumList = convertToDecimal(firstNumber, firstExponenet)
    secondNumList = convertToDecimal(secondNumber, secondExponent)

    result = True

    # If the lists are not the same size, sets result to False
    if(len(firstNumList) > len(secondNumList)):
        result = False
    elif(len(secondNumList) > len(firstNumList)):
        result = False
    else:
        # Checks each element, if any are not equal sets result to false and breaks
        for i in range(0, len(firstNumList)):
            if(firstNumList[i] != secondNumList[i]):
                result = False
                break

    # Calls print results and passes the result
    printResults(result)

# Main method, takes numbers and exponents via terminal along with desired operation
def main():
    while (True):
        print("Please enter first number (Without exponent): ")
        firstNumber = input()
        print("Please enter first exponenet: ")
        firstExponent = input()

        print("Please enter second number (Without exponent): ")
        secondNumber = input()
        print("Please enter second exponenet: ")
        secondExponent = input()

        print("Choose operation (0. Quit, 1. Addition, 2. Multiplication, 5. Greater Than, 6. Less Than): ")
        operation = input()

        # Depending on operation, calls appropriate function
        if (operation == '1'):
            bigAdd(firstNumber, firstExponent, secondNumber, secondExponent)
        elif (operation == '2'):
            bigMultiply(firstNumber, firstExponent, secondNumber, secondExponent)
        elif (operation == '5'):
            isGreaterThan(firstNumber, firstExponent, secondNumber, secondExponent)
        elif (operation == '6'):
            isLessThan((firstNumber, firstExponent, secondNumber, secondExponent))
        elif (operation == '0'):
            break
        else:
            print("Please enter a valid option")

# Calls main method to start program
if __name__ == '__main__':
    main()
