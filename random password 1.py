import time, random
print("это програма для генерация поролей")
password = ""
add_password = ""
a = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
b = ["@", "#", "&"]
c = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
for i in range(15):
    add_password = random.choice(a)
    password += add_password
    add_password = random.choice(b)
    password += add_password
    add_password = random.choice(c)
    password += add_password
print()
print("ваш пороль")
print()
print(password)
input()
