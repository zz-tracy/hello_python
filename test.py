import validators

print(validators.email('someone@example.com'))

a = 5
b = 3
st = 'a大于b' if a > b else 'a 不大于b'
print(st)

print('a大于b') if a > b else print('a 不大于b')

st = print('crazyit'), 'a 大于b' if a > b else 'a不大于b'
print(st)

st = print('crazyit'); x = 20 if a > b else 'a不大于b'
print(st)
print(x)
