n = int(input())

temp = n - 1
level = 0

while temp >= 0:
    if temp - level * 6 <= 0:
        break
    else:
        temp -= level * 6
        level += 1

dist = level + 1

print(dist)
