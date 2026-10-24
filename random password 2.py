import random
symbol = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()"
number = int(input("количество цифр: "))
password = ""
for i in range(number):
    password += random.choice(symbol)
print()
print("ваш пороль")
print()
print(password)
input()
