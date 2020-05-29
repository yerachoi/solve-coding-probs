import sys
dataSize = int(input())
# sys.stdin.readline(): faster than input()
dataList = [list(map(int, sys.stdin.readline().split())) for i in range(dataSize)]

for data in dataList:
    # get h, w, n
    # h = height, w = width, n = nth subject
    h, w, n = data

    room = n // h + 1
    if n % h == 0:
        floor = h
        room -= 1
    else:
        floor = n % h
    
    roomNum = floor * 100 + room
    print(roomNum)