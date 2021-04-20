n = int(input())
hn = n // 2
for i in range(n):
    for j in range(n):
        if i == j or i + j == n:
            print(0)
        elif i < hn < j:
            print(1)
        elif i < j < hn:
            print(2)
        elif j < i < hn:
            print(3)
        elif j < hn < i:
            print(4)
        elif j < hn < i:
            print(5)
        elif hn < j < i:
            print(6)
        elif hn < i < j:
            print(7)