# pattern for
"""
A
AB
ABC
ABCD
"""

ord_a = ord("A")

N = int(input("Enter number of lines: "))

if N <= 26:
    ord_end = ord_a + N

    for i in range(1, N+1):
        for a in range(ord_a, ord_a+i):
            print(chr(a), end="")
        print()


# pattern for
"""
ABCD
ABC
AB
A
"""
ord_a = ord("A")

N = int(input("Enter number of lines: "))

if N <= 26:

    for i in range(N, 0, -1):
        for a in range(ord_a, ord_a+i):
            print(chr(a), end="")
        print()


# pattern for

"""
A
BB
CCC
DDDD
EEEEE
"""

N = int(input("Enter number of lines: "))

_ord =  ord("A")

if N <= 26:

    for i in range(1, N+1):
        for a in range(i):
            print(chr(_ord), end='')
        _ord += 1
        print()

# pattern for:
"""
GGGGGG
FFFFF
EEEE
DDD
CC
B
"""
N = int(input("Enter number of lines: "))

ord_a = ord("A")

_ord =  N + ord_a -1

if N <= 26:

    for i in range(N, 0, -1):
        for a in range(i):
            print(chr(_ord), end='')
        _ord -= 1
        print()
