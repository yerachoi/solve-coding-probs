rise, drop, height = map(int, input().split())

# do not need to account for the drop for the last day
day = (height - drop) / (rise - drop)

# ceil day without math.ceil()
# ref:
# https://stackoverflow.com/questions/57115951/rounding-a-math-calculation-up-without-math-ceil
day_ceil = int(-(-day // 1))

print(day_ceil)