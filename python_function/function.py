# 使用关键字def来定义函数
def greet_user():
    """显示简单的问候语"""
    print('Hello!')


greet_user()


# 向函数传递参数
def greet_userf(username):  # username是形参
    """显示简单的问候语"""
    print('Hello, ' + username.title() + "!")


greet_userf('jesse')  # jesse是实参


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


while True:
    print('\nPlease tell me your name:')
    print("(enter 'q' at any time to quit)")

    f_name = input('First name:')
    if f_name == 'q':  # 定义一个退出条件,避免无限循环
        break

    l_name = input('Last name:')
    if l_name == 'q':  # 定义一个退出条件,避免无限循环
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello, ' + formatted_name + '!')

# 现有字典dict={'a': 24, 'g': 52, 'i':12, 'k':33}请按字典中的value值进行排序?
dict = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
print(dict.items())
print(sorted(dict.items(), key=lambda x: x[1]))

# 请反转字符串'aStr'?
print('aStr'[::-1])


# 传递列表
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 在函数中修改列表
# 首先创建一个列表,其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计, 直到没有未打印的设计为止
# 打印每个设计后,都将其一到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # 模拟根据 设计制作3D打印模型的过程
    print('Printing model: ' + current_design)
    completed_models.append(current_design)

# 显示打印好的所有模型
print('\nThe following models have been printed:')
for completed_model in completed_models:
    print(completed_model)


# 编写两个函数,第一个函数负责处理打印 设计的工作,第二个参数将概述打印了哪些设计
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计, 直到没有未打印的设计为止
    打印每个设计后,都将其移到列表completed_models中
    """
    while  unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程
        print('Printing model: ' + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# 禁止函数修改列表
# 使用function_name(list_name[:])
print_models(unprinted_designs[:], completed_models)

# 列表推导式
print([i % 2 for i in range(10)])
# 和生成器表达式
print((i % 2 for i in range(10)))


# 传递任意数量的实参(*args)
def make_pizza(*toppings):    # *toppings中的星号让Python创建一个名为toppings的空元组,并将受到的所有值都封装到这个元祖中
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 将print()语句替换为一个循环,对列表进行遍历
def make_pizza(*toppings):
    """概述要制作的披萨"""
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 使用任意数量的关键字实参(**kwargs)
# **user_info中的两个星号让Python创建一个名为user_info的空字典,并将收到的所有名称-值对都封装早这个字典中
def build_profile(first, last, **user_info):
    """创建一个字典, 其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location = 'princeton', field='physics')
print(user_profile)