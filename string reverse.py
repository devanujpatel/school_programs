# print reverse of a string

s = input("Enter a string: ")

nl = 0 - len(s)
l = -1

rev = ""

for ch in range(len(s)+1):
    rev += s[l]
    l -= 1
    if nl == l+1:
        break

print(rev)
