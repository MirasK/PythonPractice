from math import ceil
print("YES-1    NO-0")
a = 0
b = 99
n = 0

while(1):
    print("Is it bigger?", ceil((a + b)/ 2))
    x = input()
    n = ceil((a + b)/ 2)

    if x == "0":
        b = n - 1
    if x == "1":
        a = n
    if a == b :
        n += 1
        print(n)
        break
