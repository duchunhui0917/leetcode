n, m = list(map(int, input().split(',')))

m -= 1
def f(n, m):
    if n == 1:
        return 1
    else:
        return (f(n - 1, m) + m - 1) % n + 1


print(f(n, m))
