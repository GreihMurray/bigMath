def reverseList(passedIn):
    reversedList = []
    for i in reversed(passedIn):
        reversedList.append(i)
    return reversedList

def printResults(passedIn):
    for i in passedIn:
        print(i, end="")
    print(" ")

def convertToDecimal(number, exponent):
    numArray = []

    for digit in number:
        if (digit == '.'):
            continue
        else:
            numArray.append(int(digit))
    for i in range(0, (int(exponent) - (len(numArray) - 1))):
        numArray.append(0)

    return numArray

def carryVal(number):
    stringNum = str(number)

    if(len(stringNum) > 1):
        firstDigit = stringNum[0]

        if(firstDigit == '1'):
            return 1
        elif(firstDigit == '2'):
            return 2
        elif(firstDigit == '3'):
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

def bigAdder(firstNum, secondNum):
    added = []
    result = []

    if len(firstNum) > len(secondNum):
        carriedVal = 0
        for i in range (0, len(secondNum)):
            added.append(int(firstNum[i]) + int(secondNum[i]) + int(carriedVal))
            carriedVal = carryVal((int(secondNum[i])+int(firstNum[i])))
        for i in range (len(secondNum), len(firstNum)):
            added.append(int(firstNum[i]) + carriedVal)
            carriedVal = 0
    elif len(firstNum) < len(secondNum):
        carriedVal = 0
        for i in range (0, len(firstNum)):

            added.append(int(firstNum[i]) + int(secondNum[i]) + int(carriedVal))
            carriedVal = carryVal((secondNum[i]+firstNum[i]))
        for i in range (len(firstNum), len(secondNum)):
            added.append(secondNum[i] + carriedVal)
            carriedVal = 0
    return added

def bigAdd(firstNumber, firstExponent, secondNumber, secondExponent):
    firstNumList = convertToDecimal(firstNumber, firstExponent)
    secondNumList = convertToDecimal(secondNumber, secondExponent)
    added = []
    result = []

    if len(firstNumList) > len(secondNumList):
        carriedVal = 0
        for i in range (0, len(secondNumList)):
            reversedFirstNumList = reverseList(firstNumList)
            reversedSecondNumList = reverseList(secondNumList)

            added.append(reversedFirstNumList[i] + reversedSecondNumList[i] + carriedVal)
            carriedVal = carryVal((reversedSecondNumList[i]+reversedFirstNumList[i]))
        for i in range (len(secondNumList), len(firstNumList)):
            added.append(reversedFirstNumList[i] + carriedVal)
            carriedVal = 0
    elif len(firstNumList) < len(secondNumList):
        carriedVal = 0
        for i in range (0, len(firstNumList)):
            reversedFirstNumList = reverseList(firstNumList)
            reversedSecondNumList = reverseList(secondNumList)

            added.append(reversedFirstNumList[i] + reversedSecondNumList[i] + carriedVal)
            carriedVal = carryVal((reversedSecondNumList[i]+reversedFirstNumList[i]))
        for i in range (len(firstNumList), len(secondNumList)):
            added.append(reversedSecondNumList[i] + carriedVal)
            carriedVal = 0

    result = reverseList(added)

    printResults(result)

def bigMultiply(firstNumber, firstExponent, secondNumber, secondExponent):
    firstNumList = convertToDecimal(firstNumber, firstExponent)
    secondNumList = convertToDecimal(secondNumber, secondExponent)

    currentValue = []
    holdToAdd = []
    result = []
    incrementer = 0
    carriedVal = 0

    reversedFirstNumList = reverseList(firstNumList)
    reversedSecondNumList = reverseList(secondNumList)

    if len(reversedFirstNumList) > len(reversedSecondNumList):
        for digit in reversedSecondNumList:
            for otherDigit in reversedFirstNumList:
                stringMultiplied = str((otherDigit * digit) + carriedVal)
                currentValue.append(stringMultiplied[len(stringMultiplied)-1])
                carriedVal = carryVal(otherDigit * digit)

            for i in range(0, incrementer):
                currentValue.append(0)

            holdToAdd = bigAdder(currentValue, holdToAdd)
            print("HoldToAdd", holdToAdd)
            incrementer = incrementer + 1
        result = reverseList(holdToAdd)
        printResults(result)
def main():
    while(True):
        print("Please enter first number (Without exponent): ")
        firstNumber = input()
        print("Please enter first exponenet: ")
        firstExponent = input()

        print("Please enter second number (Without exponent): ")
        secondNumber = input()
        print("Please enter second exponenet: ")
        secondExponent = input()

        print("Choose operation (0. Quit, 1. Addition, 2. Multiplication): ")
        operation = input()

        if(operation == '1'):
            bigAdd(firstNumber, firstExponent, secondNumber, secondExponent)
        elif(operation == '2'):
            bigMultiply(firstNumber, firstExponent, secondNumber, secondExponent)
        elif(operation == '0'):
            break
        else:
            print("Please enter a valid option")

if __name__ == '__main__':
    main()