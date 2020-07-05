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
