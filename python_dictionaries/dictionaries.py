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


# 嵌套:将一系列字典存储在列表中, 或将列表作为值存储在字典中

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = ['alien_0', 'alien_1', 'alien_2']

for alien in aliens:
    print(alien)

# 使用range()方法自动生成一些列数字
# 创建一个空列表用来存储生成的数字
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in alien[:5]:    # 显示前五个生成的信息
    print(alien)
print('...')

# 显示创建了多少个数字
print('Toal number of aliens: ' + str(len(aliens)))


# 字典中存储列表

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print('\n' + name.title() + '\'s favorite languages are: ')
    for language in languages:
        print('\t' + language.title())


# 在字典中存储字典

users = {
    'asinstein' :  {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}


for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())