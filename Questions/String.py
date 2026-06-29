# Write a function that print each character of given word

def printEachChar():
    word = input("Enter a word : ")

    for char in word:
        print(char)

    # for i in range(len(word)):
    #     print(word[i])

    # i = 0
    # while i <= len(word) - 1:
    #     print(word[i])
    #     i = i + 1

# printEachChar()

# ----------------------------------
# Print Reverse of a word

def printReverseStr():
    word = input("Enter a word : ")

    reverseStr = ""

    i = len(word) - 1
    while i >= 0:
        reverseStr = reverseStr + word[i]
        i = i - 1
    
    return reverseStr

# print(printReverseStr())

# --------------------------------
# Check the given word is pallindrome or not

def pallindromeChecker():
    word = input("Enter a word : ")

    reverseStr = ""
    i = len(word) - 1
    while i >= 0:
        reverseStr = reverseStr + word[i]
        i = i - 1
    print(word, reverseStr)

    if word == reverseStr:
        print("Pallindrome Hai")
    else :
        print("Pallindrome Nahi Hai")

# pallindromeChecker()

# 2nd Methods

def checkPallindrome():
    word = input("Enter a word : ")
    isPallindrome = True
    i = 0
    while i <= len(word)/2:

        if word[i] != word[len(word) - 1 - i]:
            isPallindrome = False
            break
        i = i + 1

    if isPallindrome == True:
        print("Pallindrome Hai")
    else :
        print("Pallindrome Nahi hai")

# checkPallindrome()