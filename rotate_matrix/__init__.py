def clockwise(l:list):
    return list(reversed(list(zip(*l))))
def anti_clockwise(l:list):
    for i in range(3):
        l = list(reversed(list(zip(*l))))
    return l