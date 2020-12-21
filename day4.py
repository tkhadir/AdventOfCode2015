import hashlib

key = 'bgvyzdsv'
print('key secret == ' + key)
mineNumber = 0
result = ''
complete = False

while not complete:
    result = hashlib.md5((key + str(mineNumber)).encode())
    complete = result.hexdigest().startswith('000000')
    if not complete:
        mineNumber+=1

print('found mine number == ' + str(mineNumber))
print(result.hexdigest())