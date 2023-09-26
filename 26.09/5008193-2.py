#Strike
n = int(input())
sequence = list(map(int, input().split()))

count_strike = 0
current_strike = 0
strikes = []

for i in range(1, n):
    if sequence[i] == sequence[i-1] + 1:
        current_strike += 1
    else:
        count_strike += 1
        strikes.append(current_strike + 1)
        current_strike = 0

count_strike += 1
strikes.append(current_strike + 1)

print(count_strike)
print(' '.join(map(str, strikes)))

