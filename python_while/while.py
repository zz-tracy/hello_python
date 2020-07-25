# 使用While循环

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


# 设定一个退出值,当用户输入该值时退出程序

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)


# 使用标志

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True   # 标志
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


# 使用break退出循环

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print('I\'d love to go to ' + city.title() + '!')


# 在循环中使用continue

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)


# 避免无限循环

x = 1
while x <= 5:
    print(x)
    x += 1    # 每当x满足循环条件时都进行+1赋值,以避免无限循环


# 使用While循环处理列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)

print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# 删除包含特定值的所有列表元素

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


# 使用用户输入来填充字典

responses = {}

# 设置一个标志,指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入别调查这的名字和回答
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to climb someday? ')

    # 将答卷存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input('Would you like to let another person respond?(yes/ no) ')
    if repeat == 'no':
        polling_active = False

# 调查结束, 显示结果
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name + ' would like to climb ' + response + '.')