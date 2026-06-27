# bill = 920
# totalPerson = 4

# tip = bill * 5/100

# totalAmountToPay = bill + tip

# print("Tip :", tip)
# print("Total Amount :", totalAmountToPay)

# print("Per Person Amount to Pay", totalAmountToPay/4)


# Calculate Percentage

obtained = 400
total = 500

percentage = obtained * 100/total

print(percentage)

# Print Distace

speed = 12
time = 10

distance = speed * time
print(distance)

# -----------------------------
# Area of Circle

radius = 5

# areaOfCircle = 3.14 * radius * radius
areaOfCircle = 3.14 * radius ** 2
print(areaOfCircle)

# --------------------------------
l = 10
b = 5
areaOfRectangle =  l * b

print(areaOfRectangle)
# --------------------------

amount = 9999
taxPercentage = 18

print(amount + amount * taxPercentage/100)

# -------------------------


num = 465

digit = num % 10  # 5
print("digit :",digit)

quointent = int(num / 10)
# print("quointent :", quointent)


digit = quointent % 10
print("digit :",digit) # 6
quointent = int(quointent / 10)
# print("quointent :", quointent)

digit = quointent % 10
print("digit :",digit) # 4
# --------------------------

"""
    console.log('Hello')
"""

name = input("Enter Name : ")
age = int(input("Enter Age : "))
isPresent = bool(input("isDeapakPresent : "))

print(type(name))
print(type(age))
print(type(isPresent))