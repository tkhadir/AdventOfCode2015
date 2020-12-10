f = open("inputs.txt", "r")

data = f.read()

def contains(x, y, c):
    for d in c:
        if d[0] == x and d[1] == y:
            return True
    return False

def countTotal(c1, c2):
    merge= []
    merge= c1
    for d in c2:
        if not contains(d[0], d[1], merge):
            merge.append(d)
    return len(merge)

def move(x, y, d):
    if d == '>':
        x+=1
    if d == '<':
        x-=1
    if d == '^':
        y+=1
    if d == 'v':
        y-=1
    return [x, y]

def addCoords(coords, x, y):
    checked = False
    for c in coords:
        if c[0] == x and c[1] == y:
            checked = True
    if not checked:
        coords.append([x, y])

def solve(data):
    x = 0
    y = 0
    xr = 0
    yr = 0
    coords = []
    robotCoords = []
    count = 0
    coords.append([x, y])
    robotCoords.append([xr, yr])
    for d in list(data):
        if count % 2 == 0:
            x, y = move(x, y, d)
            addCoords(coords, x, y)
        else:
            xr, yr = move(xr, yr, d)
            addCoords(robotCoords, xr, yr)
        count+=1
    print('total houses : ' + str(len(coords)))
    print('total houses robots : ' + str(len(robotCoords)))
    print('total : ' + str(countTotal(coords,robotCoords)))

solve(data)