name = input('what is your name=>')
print(name)
print(f'lenght:{len(name)}')

cl_name = name.string() #remove leading and traling whitespace or chars
print(cl_name)
print(f'length:{len(cl_name)}')

secret_msg ='0000000000000000LA00000'
print(secret_msg.strip('0'))
print(secret_msg.lstrip('0'))
print(secret_msg.rstrip('0'))