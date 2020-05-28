n = int(input())

if n % 5 == 0:
    count = n // 5

else:
    quot = n // 5
    rem = n % 5
    
    while quot >= 0:
        if (quot == 0) and (rem % 3 != 0):
            count = -1
            break
        elif rem % 3 == 0:
            count = quot + (rem // 3)
            break
        else:
            quot -= 1
            rem += 5
            
print(count)
