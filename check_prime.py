# input a number and print prime or not prime

num = int(input("Number: "))

check = ""

for i in range(2, num):
    print("dividing by:", i)
    if (num % i) == 0:
        check = "not prime"
        break
    else:
        check = "prime"

print(check)