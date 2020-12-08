f = open("inputs.txt", "r")

data = f.read()

def resolve(data):
    count = 0
    idx = 0
    for s in list(data):
        if s == '(':
            count+=1
        if s == ')':
            count-=1
        idx+=1
        if count == -1:
            break
    print('floor == ' + str(count) + ' at position == ' + str(idx))


resolve(data)