# input a number and print factorial

n = int(input("Number: "))

factorial = 1

for i in range(1, n+1):
    factorial *= n
    n-=1
print(factorial)
