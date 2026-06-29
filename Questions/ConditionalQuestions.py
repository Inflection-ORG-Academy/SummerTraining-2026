# Check Vote Eligibility
# age = int(input("Enter your age : "))

# if age >= 18:
#     print("You can vote")
# else :
#     requiredYear = 18 - age
#     print("Wait for", requiredYear, "Years to vote")

# Compare Two Number and print Bigger one

# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))

# if num1 > num2 :
#     result = num1 - num2
#     print(num1, "is bigger than", num2, "by", result)
# elif num2 > num1:
#     result = num2 - num1
#     print(num2, "is bigger than", num1, "by", result)
# else :
#     print("No one is bigger")



# Write a program to determine the type of roots of a quadratic equation using the discriminant:
# Real and distinct
# Real and equal
# Imaginary

def findDiscriminant():

    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))
    c = int(input("Enter a number : "))

    d = b ** 2 - 4 * a *c
    print(d)
    if d > 0:
        print("Real and distinct")
    elif d == 0:
        print("Real and equal")
    else :
        print("Imaginary")

# findDiscriminant()