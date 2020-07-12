# 访问字典中的值

alien = {'color': 'green'}
print(alien['color'])


# 向字典中添加键-值对

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 修改字典中的值

alien_0 = {'color': 'green'}
print('The alien is ' + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + '.')

# 删除键值-对

alien_0 = {'color': 'green', 'opions': 5}
print(alien_0)

del alien_0['opions']
print(alien_0)


# 遍历字典

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print('\nkey: ' + key)
    print('value: ' + value)


# 遍历字典中的所有键

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_language.keys():
    print(name.title())

for name in favorite_language:  # 遍历字典时,会默认遍历所有的键,所以不需要加keys()输出效果一样
    print(name.title())


# 使用sorted()方法按顺序遍历字典中所有的键

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_language.keys()):
    print(name.title() + ', thank you for taking the poll')


# 遍历字典中所有的值:


favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for language in favorite_language.values():
    print(language.title())


# 使用集合set()方法找出列表中独一无二的元素

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for language in set(favorite_language.values()):
    print(language.title())