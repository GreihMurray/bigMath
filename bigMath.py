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

def bigAdd(firstNumber, firstExponent, secondNumber, secondExponent):
    firstNumArray = convertToDecimal(firstNumber, firstExponent)
    secondNumArray = convertToDecimal(secondNumber, secondExponent)
    added = []

    if len(firstNumArray) > len(secondNumArray):
        carryVal = 0
        for i in range (0, len(secondNumArray)):
            print('thing')
            reversedFirstNumArray = reversed(firstNumArray)
            print(reversedFirstNumArray)
            reversedSecondNumArray = reversed(secondNumArray)
            print(reversedSecondNumArray)
            added.append(reversedFirstNumArray[i] + reversedSecondNumArray[i] + carryVal)
            carryVal = carryVal((reversedSecondNumArray[i]+reversedFirstNumArray[i]))

    print(added)

def bigMultiply(number, exponent):
    print("multiply")

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