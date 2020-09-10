"""文件和异常"""

# 读取整个文件
# 使用with关键字在不需要访问文件后将其关闭
# open（）函数打开文件，并返回一个表示文件的对象
with open(r'C:\Users\hp\Desktop\demo\pi_digits.txt') as file_object:
    contents = file_object.read()  # 使用read（）方法读取文件的全部内容
    print(contents.rstrip())  # 调用rstrip()函数删除末尾的空行

# 文件路径：相对路径和绝对路径
# 相对路径：相对路径让Python到指定的位置去查找，而该位置是相对于当前运行的程序所在目录的
# 在Linux和OS X中
# with open('text_files/filename.txt') as file_onject:

# 在Windows系统中，使用反斜杠（\）
# with open('text_files\filename.txt') as file_object：

# 绝对路径：将文件在计算机中的准确位置告诉Python，这样就不用考虑当前运行的程序存储在什么地方了
# 在Linux和OS X中
# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:

# 在Windows系统中
# file_path = 'C\Users\ehmattes\other_files\text_files\filename.txt'
# with open(file_path) as file_object:
# 注意：可以在单引号前加上r----表示非转义的原始字符串


# 逐行读取
filename = r'C:\Users\hp\Desktop\demo\pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 创建一个包含文件各行内容的列表
filename = r'C:\Users\hp\Desktop\demo\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()  # 使用readlines（）从文件中读取每一行，并将其存储在一个列表中

for line in lines:
    print(line.rstrip())

# 使用文件的内容
filename = r'C:\Users\hp\Desktop\demo\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# 针对一个包含一百万位的大型文件
filename = r'C:\Users\hp\Desktop\demo\pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:52] + '......')
print(len(pi_string))

# 圆周率值中包含你的生日吗？
filename = r'C:\Users\hp\Desktop\demo\pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appear in the first million digits pf pi.')

# 写入文件
filename = r'C:\Users\hp\Desktop\demo\programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('---- + I love programming.')  # wirte()函数会覆盖之前写入的文件

# 写入多行
filename = r'C:\Users\hp\Desktop\demo\programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('---- I love programming.\n')
    file_object.write('---- I love creating new games.\n')

# 附加到文件
filename = r'C:\Users\hp\Desktop\demo\programming.txt'

with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')

# 异常
# 处理ZeroDivisionError异常
# 使用try-except代码块
try:
    print(5 / 0)
except ZeroDivisionError:
    print('You can\'t divide by zero')

# 使用异常避免崩溃
print('Give me two numbers, and I\'ll divide them.')
print('Enter \'q\' to quit.')

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

# else代码块
print('Give me two numbers, and I\'ll divide them.')
print('Enter \'q\' to quit.')

while True:
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You can\'t divide by 0!')
    else:
        print(answer)

# 处理FileNotFoundError异常
filename = r'C:\Users\hp\Desktop\demo\alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + ' does not exist.'
    print(msg)

# 分析文本
filename = r'C:\Users\hp\Desktop\demo\alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + ' does not exist.'
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print('The file ' + filename + 'has about ' + str(num_words) + ' words.')


# 使用多个文件
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = 'Sorry, the file ' + filename + ' does not exist.'
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + 'has about ' + str(num_words) + ' words.')


# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
# for filename in filenames:
#     count_words(filename)


# pass语句
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        pass
    except:
        pass  # pass语句充当占位符，提醒你在程序的某个地方什么都没有做，以后也许要在这里做些什么
    else:
        pass


# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
# for filename in filenames:
#     count_words(filename)

# 存储数据
# 使用json.dump()和json.load()

import json


numbers = [2, 3, 4, 5, 6, 7, 12]

filename = r'C:\Users\hp\Desktop\demo\numbers.json'
with open(filename, 'w') as f_obj:
    # 使用json.dump()函数将数字列表存储到文件numbers.json中
    json.dump(numbers, f_obj)


# 使用json.load()函数将这个列表读取到内存中
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)



# 保存和读取用户生成的数据
username = input('What is your name? ')

filename = r'C:\Users\hp\Desktop\demo\username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print('We\'ll remember you when you come back, ' + username + '!')


# 使用json.load()存储在username.json中的信息读取到变量username中
with open(filename) as f_obj:
    username = json.load(f_obj)
    print('Welcome back, ' + username + '!')


# 使用try--except--else保存和读取用户生成的数据
filename = r'C:\Users\hp\Desktop\demo\username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input('What is your name? ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print('We\'ll remember you when you come back, ' + username + '!')
else:
    print('Welcome back, ' + username + '!')




