# 使用关键字def来定义函数
def greet_user():
    """显示简单的问候语"""
    print('Hello!')
greet_user()


# 向函数传递参数
def greet_userf(username):    # username是形参
    """显示简单的问候语"""
    print('Hello, ' + username.title() + "!")


greet_userf('jesse')    # jesse是实参


# 传递实参
# 位置实参(位置实参要与形参的位置对应)
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print('\nI have a ' + animal_type + '.')
    print('My' + animal_type + '\'s name is ' + pet_name.title() + '.')


describe_pet('hamster', 'harry')
# 调用函数多次
describe_pet('dog', 'willie')

# 关键字参数
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print('\nI have a ' + animal_type + '.')
    print('My' + animal_type + '\'s name is ' + pet_name.title() + '.')


describe_pet(animal_type='hamster', pet_name='harry')


# 默认值(可以给每个形参指定默认值,在调用函数中给形参提供了实参时,python将使用指定的实参值;否则,将使用形参的默认值)
# 注意:在使用默认值时,在形参列表中必须先列出没有默认值的形参,再列出有默认值的形参
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print('\nI have a ' + animal_type + '.')
    print('My' + animal_type + '\'s name is ' + pet_name.title() + '.')


describe_pet(pet_name='willie')


# 返回值(return语句将值返回到调用函数的代码行.可以返回一个或一组值)
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 让实参变成可选的
# 通过将可选的实参对应的形参设置一个默认值等于空字符串
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + '' + middle_name + '' + last_name
    else:
        full_name = first_name + '' + last_name
    return full_name


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# 返回字典
def build_person(first_name, last_name):
    """返回一个字典,其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


# 新增可选形参age
def build_person(ffirst_name, last_name, age=''):
    """返回一个字典, 其中包含有关一个人的信息"""
    person = {'first': ffirst_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)


# 结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + '' + last_name
    return full_name.title()

while  True:
    print('\nPlease tell me your name:')
    print("(enter 'q' at any time to quit)")

    f_name = input('First name:')
    if f_name == 'q':    # 定义一个退出条件,避免无限循环
        break

    l_name = input('Last name:')
    if l_name == 'q':    # 定义一个退出条件,避免无限循环
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello, ' + formatted_name + '!')