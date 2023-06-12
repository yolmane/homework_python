mike_inv = a = int(input())
ivan_inv = b = int(input())
min_inv = x = int(input())
if a >= x and b >= x:
    print("2")
elif a >= x and b < x:
    print("Mike")
elif a < x and b >= x:
    print("Ivan")
elif (a < x and b < x) and (a + b) >= x:
    print("1")
else:
    print("0")
