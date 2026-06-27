# Function Declaration
def printEachChar(str):
    for char in str:
        print(char)

# Function Calling / function execuation / function invocation
printEachChar("aman")
print("-----------")
printEachChar("Deepankar")
print("-----------")
printEachChar("Vijay Kumar")

# addition of two digit

def sum(num1, num2):
    result = num1 + num2
    print(result)

sum(4, 6)
sum(14, 16)

def converText():
    inputText = str(input("Enter something : "))
    choice = int(input("Please Type 1 for Upper, 2 for Lower, 3 for capitilize, 4 for title : "))
    
    if choice == 1:
        print(inputText.upper())
    elif choice == 2:
        print(inputText.lower())
    elif choice == 3:
        print(inputText.capitalize())
    elif choice == 4:
        print(inputText.title())
    else:
        print("Select right choice")

converText()