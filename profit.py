profit = int(input())
bonus = 0

if profit > 10e5:
    bonus += (profit - 10e5) * 0.01 + 5e4
    profit = 10e5
if 6e5 < profit <= 10e5:
    bonus += (profit - 6e5) * 0.015 + 3e4
    profit = 6e5
if 4e5 < profit <= 6e5:
    bonus = (profit - 4e5) * 0.03 + 2e4
    profit = 4e5
if 2e5 < profit <= 4e5:
    bonus = (profit - 2e5) * 0.05 + 1.75e4
    profit = 2e5
if 1e5 < profit <= 2e5:
    bonus = (profit - 1e5) * 0.075 + 1e4
    profit = 1e5
if profit <= 1e5:
    bonus = profit * 0.1

print(int(bonus))
