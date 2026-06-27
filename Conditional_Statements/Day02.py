# Conditional Statement Syntax

# age = 56

# if age >= 18:
#     print("you can Vote")
# else:
#     print("You can not Vote")

# --------------------------

# totalAmount = 51600
# if totalAmount >= 500:
#     print("No Delivery Charge")
# else:
#     print("You have to pay delivery charge")


# ----- if elif else statement ------
# Trafic Rule
# lightColor = "red"

# if lightColor == "red":
#     print("STOP")
# elif lightColor == "yellow":
#     print("READY")
# elif lightColor == "green":
#     print("GO")
# else:
#     print("Invailid Light Color")

# -------------------------------

# age = int(input("Enter your age : ")) 
# isLicense = bool(input("Do you have license : "))

# if age >= 18:
#     if isLicense == True:
#         print("You can drive")
#     else:
#         print("You can not drive")
# else:
#     print("You can not drive")


# -----------------------

# 1 = "Sunday"
# 2 = "Monday"
# 3 = Tuesday
# .....

# num = int(input("Enter a number : "))

# if num == 1:
#     print("Sunday")
# elif num == 2:
#     print("Monday")
# elif num == 3:
#     print("Tuesday")
# elif num == 4:
#     print("Wednesday")
# elif num == 5:
#     print("Thursday")
# elif num == 6:
#     print("Friday")
# elif num == 7:
#     print("Saturday")
# else:
#     print("Wrong Number")

# --------------------
# Check a number is Positive, Negative or Zero

# num = int(input("Enter a number : "))

# if num > 0:
#     print("POSITIVE")
# elif num < 0:
#     print("Negative")
# else:
#     print("ZERO")

# Write a program to check whether a number is divisible by 7.

# num = 15

# remainder = num % 7

# if remainder == 0:
#     print("Divisible")
# else:
#     print("Not Devisible")


# ----------------------------

# num = int(input("Enter a number : "))

# if num % 3 == 0 and num % 5 == 0:
#     print("Number is divisible by 3 and 5")
# else:
#     print("Number is not divisible")

# -------------------------------

# Write a program to calculate electricity bill:
# First 100 units → ₹5/unit
# Next 100 units → ₹7/unit
# Above 200 units → ₹10/unit

units = int(input("Enter units : "))

if units <= 100:
    print(units * 5)
elif units > 100 and units <= 200:
    print(units * 7)
else:
    print(units * 10)
