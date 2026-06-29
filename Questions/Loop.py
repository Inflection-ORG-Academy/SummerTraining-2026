# Write a program to convert a Decimal Number into Binary Number


def convertDecimalToBinary():
    num = int(input("Enter a Number : "))
    # numberSystem = int(input("Choose a Number System : "))
    numberSystem = 10
    binaryNumber = ""


    quotient = num
    while quotient > 0:
        remainder = str(quotient % numberSystem)
        
        binaryNumber = remainder + binaryNumber

        quotient = quotient // numberSystem
    print(binaryNumber)

convertDecimalToBinary()

# Write a Program to print digit of a number

def printEachDigit():
    num = int(input("Enter a Number : "))

    quotient = num
    power = 1
    while quotient > 0:
        # print(quotient)
        digit = quotient % 10
        print(digit)
        print(digit * power)
        power = power * 10
        quotient = quotient // 10

# printEachDigit()
