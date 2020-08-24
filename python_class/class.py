# 创建Dog类
class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + ' rolled over!')


# 根据类创建实例
my_dog = Dog('willie', 6)

print('My dog\'s name is ' + my_dog.name.title() + '.')
print('My dog is ' + str(my_dog.age) + 'years old.')

# 调用方法
my_dog.sit()
my_dog.roll_over()

# 创建多个实例
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print('My dog\'s name is ' + my_dog.name.title() + '.')
print('My dog is ' + str(my_dog.age) + ' years old.')
my_dog.sit()

print('\nYour dog\'s name is ' + your_dog.name.title() + '.')
print('Your dog is ' + str(your_dog.age) + 'years old.')
your_dog.sit()


# 给属性指定默认值
class Car():

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())

# 修改属性的值
my_new_car.odometer_reading = 23
print(my_new_car.read_odometer())


# 通过方法修改属性的值
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage

    # 通过方法对属性的值进行递增
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# 继承
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage

    # 通过方法对属性的值进行递增
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        # super()是一个特殊函数，帮助Python将父类和子类关联起来
        super().__init__(make, model, year)
        # 给子类定义属性
        self.battery_size = 70
        self.battery = Battery()

    # 给子类定义方法
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print('This car has a ' + str(self.battery_size) + '-kwh battery.')

    # 重写父类方法：即该方法要与重写的父类方法同名，这样Python将不会考虑父类的方法
    def fill_gas_tank(self):
        """电动车漆没有邮箱"""
        print('This car doesn\'t need a gas tank!')


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print('This car has a ' + str(self.battery_size) + '-kwh battery.')


my_tesla = ElectricCar('tesla', 'model\'s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.describe_battery()

# 导入类
# from module_name import Class_name

# 从一个模块中导入多个类
# from module_name import Class_name1, Class_name2, Class_name3...


# 导入整个模块
# import module_name
# 然后使用module_name.Class() 访问需要的类


# 导入模块中的所有类
# from module_name import *
