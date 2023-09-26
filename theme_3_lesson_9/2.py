list1 = []
list2 = []

n = int(input("Введите количество чисел в первом списке: "))
print("Введите числа первого списка:")
for _ in range(n):
    number = int(input())
    list1.append(number)

m = int(input("Введите количество чисел во втором списке: "))
print("Введите числа второго списка:")
for _ in range(m):
    number = int(input())
    list2.append(number)

total_count = len(list1) + len(list2)

print("Общее количество чисел в обоих списках:", total_count)
