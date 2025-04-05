from random import choice

all_symbols = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#-=_&'
lenght = int(input("Введите длину пароля:"))
password = ""

for i in range(lenght):
    password += choice(all_symbols)





sogl = 'qwrtpsdfghjklzxcvbnm'
glas = 'eyuioa'
numbers = '1234567890'
symvol = '!@#$%^&*()_-+='
password = ''
for i in range(5):
    password += choice(sogl) + choice(glas)
for i in range(3):
    password += choice(numbers)
for i in range(2):
    password += choice(symvol)
print(password)
