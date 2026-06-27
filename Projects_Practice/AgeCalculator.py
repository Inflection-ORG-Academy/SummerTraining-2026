from datetime import date

dobDay = int(input("Enter Date : "))
dobMonth = int(input("Enter Month : "))
dobYear = int(input("Enter Year : "))

today = date.today() # 2026-06-27

age = today.year - dobYear
# print(today.month)

# if (today.month, today.day) < (dobMonth, dobDay):
#     age = age - 1

print("You are", age, "years old")
