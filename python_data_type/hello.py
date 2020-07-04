# 修改字符串的大小写
name = 'ada lovelace'
print(name.title())    #首字母大写

name = 'Ada Lovelace'
print(name.upper())    #大写
print(name.lower())    #小写

# 合并(拼接)字符串
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print(full_name)

# 使用制表符或换行符来添加空白
print('\tpython')    #制表符
print('languages:\nPython\nC\nJavaScript')    #换行符
print('Languages:\n\tPython\n\tC\n\tJavascript')    #组合使用


#删除空白
favorite_language = ' python '
print(favorite_language.rstrip())    # 删除末尾空白
print(favorite_language.lstrip())    # 删除首部空白
print(favorite_language.strip())    #删除首尾空白

