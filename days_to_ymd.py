# input a number and display no. of uears, months and days
num = int(input("Enter a number: "))

# to get years
years = num // 365

# get the number of days left
num = num % 365 #num = num - (years*365)  use instead num = num % 365
months = num // 30
# gives number of days
num = num % 30 #num = num - (months*30) # use 

# print everything
print("years:", years)
print("month:", months)
print("Days:", num)
