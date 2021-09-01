# write an algorithm to input two numbers find if first number is divisible by second number

numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

# if the remainder is zero => numbers are divisible

remainder = numerator % denominator

divisibility = remainder == 0

print(divisibility)
