from math import ceil, sqrt

x = int(input())

# solve n * (n+1) / 2 = x for n using the quadratic formula
# and get only the ceiled positive value
# as the level must be positive
level = ceil((-1 + sqrt(1 + 8 * x)) / 2)

# index of the wanted fraction in level =  
# diff between x and the sum upto the prev level
# (need to subtract 1 to make the index start from 0)
frac_idx = int((x - ((level-1) * level / 2)) - 1)

numer_list = list(range(1, level+1))
denom_list = list(reversed(numer_list))
numer_denom_list = list(zip(numer_list, denom_list))

# if level is odd, count upward
if level % 2 == 1:
    numer_denom_list.reverse()

numer, denom = numer_denom_list[frac_idx]
frac = '{numer}/{denom}'.format(numer=numer, denom=denom)
print(frac)
