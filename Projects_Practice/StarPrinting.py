# *
# **
# ***
# ****
# *****


# count = 1
# while count <= 5:
    
#     num = 1
#     while num <= count:
#         print("*", end=" ")
#         num = num + 1
#     print("")
#     count = count + 1

# ----------------------------

# count = 5
# while count >= 2:
    
#     num = 1
#     while num <= count:
#         print("*", end=" ")
#         num = num + 1
#     print("")
#     count = count - 1

# ---------------------------------

# count = 1
# while count <= 5:
#     num = 1
#     while num <= 5 - count:
#         print(" ", end="")
#         num = num + 1

#     k = 1
#     while k <= count:
#         print("*", end="")
#         k = k + 1
    
#     print("")
#     count = count + 1

# ------------------------------------------

# i = 1
# while i <= 5:

#     k = 1
#     while k <= 5 - i:
#         print(" " , end="")
#         k = k + 1

#     j = 1
#     while j <= i:
#         print("*", end="")
#         j = j + 1
#     print("")
#     i = i + 1


# i = 1
# while i <= 5:

#     j = 1
#     while j <= 2* i - 1:
#         print(j, end="")
#         j = j + 1
#     i = i + 1
#     print("")



# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# num = int(input("Enter a number : "))

# i = 1
# while i <= num:

#     j = 1
#     while j <= num:
#         if i == 1 or i == 5 or j == 1 or j == 5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#         j = j + 1

#     print("")
#     i = i + 1

# * * * * *
# *       
# *       
# *       
# * * * * *

num = int(input("Enter a number : "))

i = 1
while i <= num:

    j = 1
    while j <= num:
        if i == 1 or j == 1 or j == 5 or i == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j = j + 1

    print("")
    i = i + 1







