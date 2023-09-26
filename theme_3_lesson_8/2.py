def rearrange_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

n = int(input())
arr = list(map(int, input().split()))

rearrange_array(arr)

for num in arr:
    print(num, end=" ")
