# 可通过索引访问列表
# 索引从0开始而不是1开始

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])


# 通过重新给列表索引赋值来修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)


# 使用append()方法在列表末尾添加元素

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# 使用insert(index, '')方法在列表的任意位置插入元素

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)


# 使用del语句删除元素

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# 使用pop()方法删除列表末尾元素

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# 使用pop(index)方法删除列表任何位置的元素

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(first_owned.title())

# 使用remove()方法根据值删除元素

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)


# 使用sort()对列表进行永久性排序

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)    # 向sort()方法内传递reverse=True参数即可实现将列表中的元素按着字母相反的顺序排序
print(cars)

# 使用函数sorted()对列表进行临时排序

cars = ['bmw', 'audi', 'toyota', 'subaru']

print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)


# 使用reverse()倒着打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)


# 使用列表的长度

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))


# 使用for循环遍历列表

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


# 使用range()函数生成一系列数字

for value in range(1,5):
    print(value)

# 使用range()函数创建数字列表

numbers = list(range(1,6))
print(numbers)

# 使用range()函数指定步长

even_numbers = list(range(1,11,2))
print(even_numbers)

# 创建一个列表,其中包含前10个整数的平方

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)


# 数字列表的简单统计计算

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


# 列表解析

squares = [value**2 for value in range(1, 11)]
print(squares)


# 切片

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])    # 打印列表中前三个元素
print(players[:4])    # 打印前四个元素
print(players[2:])    # 打印第三个元素到最后一个元素
print(players[-3:])    # 打印倒数三个元素
print(players[:])    # 打印所有元素


# 元祖: 元组使用圆括号来标识, 使用索引来访问其元素

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 通过重新给元祖变量赋值来修改元祖
dimensions = (200, 5)
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)

