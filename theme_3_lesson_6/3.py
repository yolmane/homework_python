a = int(input())
b = int(input())
num_str = ""
if a <= b:
    for i in range(a, b+1):
        if i % 2 == 0:
            num_str += f'{i} '
    print(num_str," ")