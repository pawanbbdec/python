import os
print('current folder')
print(os.getcwd())
print(os.listdir())

print('c drive content ')
os.chdir('c:\\program files')
print(os.getcwd())
print(os.listdir())
address ='c:\\program files\python\python.exe'
if os.path.exists(address):
    print('file exists')
else:
    print('file does not exist')    
