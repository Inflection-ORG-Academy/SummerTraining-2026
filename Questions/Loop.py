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

# convertDecimalToBinary()

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

# Find largest nums in given list

def findMaxNumber(numsList = []):
    largestNum = numsList[0]
    i = 1
    while i <= len(numsList) - 1:
        if numsList[i] > largestNum:
            largestNum = numsList[i]
        i = i + 1
    print(largestNum)

# findMaxNumber([4, 7, 10, 45, 6, 8,45, 9,])
# print("------------")
# findMaxNumber([56,86,23,5,6])

# Find Lowest nums in given list

def findLowestNumber(numsList = []):
    smallestNum = numsList[0]

    i = 1
    while i <= len(numsList) - 1:
        if numsList[i] < smallestNum:
            smallestNum = numsList[i]
        i = i + 1
    
    print(smallestNum)


# findLowestNumber([ 7, 10, 4,45, 3, 6, 8, 9,])

# Question --------------------------
# Given an array of positive integers arr[], 
# return the second largest element from the array. 
# If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element. 

def findSecondLargestNum(nums):
    largestNumber = float("-inf") # Negative Infinity
    secondLargestNumber = float("-inf")
    i = 0
    while i <= len(nums) - 1:

        if nums[i] > largestNumber:
            secondLargestNumber = largestNumber
            largestNumber = nums[i]

        elif nums[i] > secondLargestNumber and nums[i] != largestNumber:
            secondLargestNumber = nums[i]

        i = i + 1
    print(secondLargestNumber, largestNumber)

findSecondLargestNum([ 7, 10, 4,45, 3, 6, 18, 45, 9])

findSecondLargestNum([45, 10,45,45, 9])
findSecondLargestNum([45,45,45])