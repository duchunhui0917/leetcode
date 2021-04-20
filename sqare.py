def func(x):
    return (A * x ** 3) / 3 + x ** 2 / 2 + B * x


n = int(input())
for i in range(n):
    A, B, C, D = [int(i) for i in input().split(' ')]
    print(abs(func(D) - func(C)))
