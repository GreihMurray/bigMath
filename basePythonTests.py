import bigMath
import time

start = time.clock()
numberOne = bigMath.convertToDecimal('1.234', '500000')
numberTwo = bigMath.convertToDecimal('1.234', '500000')
num = ''
num2 = ''

for digit in numberOne:
    num += str(digit)

for digit in numberTwo:
    num2 += str(digit)

num = int(num)
num2 = int(num2)


ans = num * num2
end = time.clock()

print((end-start)*1000)