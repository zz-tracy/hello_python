# input()函数的工作原理

message = input('Tell me something, and I will repeat it back to you: ')
print(message)


# 将提示消息存储在变量中
prompt = 'If you tell us who you are, we can personalize the messages you see.'
prompt += '\nWhat is your first name? '

name = input(prompt)
print('\nHelllo, ' + name + '!')


# 使用int()获取数值输入,由于使用函数input()时,Python将用户解读为字符串,所以需要使用int()函数获取用户输入的数值
height = input('How tall are you, in inches? ')
height = int(height)

if height >= 36:
    print('\nYou\'re tall enpugh to ride!')
else:
    print('\nYou\'ll be able to ride when you\'re a little older.')


# 求模拟运算符(%),它将两个数相除并返回余数
print(4%3)
print(5%3)
print(6%3)


# 可以通过返回的余数是否为零来判断一个数是奇数还是偶数
number = input('Enter a number, and I\'ll tell you if it\'s even or add: ')
number = int(number)

if number % 2 == 0:
    print('\nThe number ' + str(number) + ' is even')
else:
    print('\nThe number ' + str(number) + ' is odd')