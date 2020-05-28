fixCost, varCost, price = map(int, input().split())

if price <= varCost:
    print(-1)
else:
    intersect = fixCost / (price - varCost)
    breakeven = int(intersect) + 1
    print(breakeven)
