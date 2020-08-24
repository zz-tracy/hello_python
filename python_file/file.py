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


#
