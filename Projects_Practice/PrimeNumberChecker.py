def primeNumberChecker():
    num = int(input("Enter a number : "))

    isDivided = False

    divisbleNum = 2
    while divisbleNum <= num - 1:

        if num % divisbleNum == 0:
            isDivided = True
            break

        divisbleNum = divisbleNum + 1
    
    if isDivided == False:
        print("Prime Hai")
    else :
        print("Prime Nahi Hai")


# primeNumberChecker()



count = 2
while count <= 100:
    num = count

    isDivided = False

    divisbleNum = 2
    while divisbleNum <= num - 1:

        if num % divisbleNum == 0:
            isDivided = True
            break

        divisbleNum = divisbleNum + 1
    
    if isDivided == False:
        print(count, end=", ")

    
    count = count + 1

 