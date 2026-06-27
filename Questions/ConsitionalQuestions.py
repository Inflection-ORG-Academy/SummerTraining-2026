# Check Vote Eligibility
# age = int(input("Enter your age : "))

# if age >= 18:
#     print("You can vote")
# else :
#     requiredYear = 18 - age
#     print("Wait for", requiredYear, "Years to vote")

# Compare Two Number and print Bigger one

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

if num1 > num2 :
    result = num1 - num2
    print(num1, "is bigger than", num2, "by", result)
elif num2 > num1:
    result = num2 - num1
    print(num2, "is bigger than", num1, "by", result)
else :
    print("No one is bigger")
