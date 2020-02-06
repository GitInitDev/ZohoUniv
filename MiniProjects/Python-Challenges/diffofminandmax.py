def diffMinMax(start, stop):
    a = [x for x in range(start, stop + 1)]
    print(a)
    b = min(a)
    c = max(a)
    print("The difference between", b, "and", c, "is :", c - b)


start = int(input('Enter the start point :'))
stop = int(input('Enter the stop point :'))
diffMinMax(start, stop)
