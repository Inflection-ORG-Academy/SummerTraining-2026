# Check a given number is Even or Odd

num = int(input("Enter number : "))

print(type(num))

remainder = num % 2

print("remainder", remainder)

if remainder:
    print(num, "is even")
else :
    print(num, "is odd")

# find Greatest Number

num1 = int(input("Enter first Number : "))
num2 = int(input("Enter second Number : "))

if num1 > num2:
    print(num1, "is greater than", num2)
else:
    if num2 > num1 :
        print(num2, "is grater than", num1)
    else:
        print(num1, "and", num2, "both are equal")




