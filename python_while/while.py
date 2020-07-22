# 使用While循环

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


# 设定一个退出值,当用户输入该值时退出程序

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)


# 使用标志

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True   # 标志
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)