# 简单的if语句

age = 19
if age >= 18:
    print('You are old enough to vote!')

# if-else 语句

age = 17
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registerd to vote yet?')
else:
    print('Sorry, you are too young to vote.')
    print('Please register to vote as soon as you turn 18!')

# if-elif-else结构：仅适用于只有一个条件满足的情况,遇到通过了的测试后,python就跳过余下的测试

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print('Your admission cost is $' + str(price) + '.')


# 使用多个elif代码块：

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print('Your admission cost is $' + str(price) + '.')

# 省略else代码块

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >=65:
    price = 5

print('Your admission cost is $' + str(price) + '.')