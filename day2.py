f = open("inputs.txt", "r")

data = f.read()

def resolve(data):
    count = 0
    for p in data.split('\n'):
        dimensions = p.split('x')
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])
        perimeter = min(((2 * l) + (2 * w)), ((2 * w) + (2 * h)))
        perimeter = min(perimeter, ((2 * l) + (2 * h)))
        total = (l * w * h) + perimeter
        count += total
    print('total square : ' + str(count))
        
resolve(data)