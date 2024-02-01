n = (int(input()))
first = n % 2  == 0
second = n < 0 and n % 3 == 0
if first or second:
    print("YES")
else:
    print("NO")
pass