# input number of terms from the userand dispay the first n terms of the series 1^1, 2^2, 3^3 ...

loops = int(input("Terms: "))

for num in range(1,loops+1):
    print(num**num)
