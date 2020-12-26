f = open("inputs.txt", "r")

data = f.read()

vowels = 'aeiou'
ignoreList = 'ab,cd,pq,xy'

def validVowelFormat(msg):
    count = 0
    for m in list(msg):
        if m in list(vowels):
            count+=1
        if count == 3:
            return True
    return False

def checkIgnoreList(msg):
    for i in ignoreList.split(','):
        if msg.find(i) != -1:
            return False
    return True

def containsTwice(msg):
    idx = 0
    for m in list(msg):
        if (idx+1 < (len(msg) -1)) and list(msg)[idx+1] == m:
            return True
        if ((idx-1) > 0) and list(msg)[idx-1] == m:
            return True
        idx+=1
    return False


countValid = 0
countInvalid = 0

for d in data.split('\n'):
    if checkIgnoreList(d) and containsTwice(d) and validVowelFormat(d):
        countValid+=1
    else:
        countInvalid+=1

print('valid : ' + str(countValid))
print('invalid : ' + str(countInvalid))