from moduli import say_name

print("Введите имя и фамилию: ")
name, surname = input().split()
n = say_name(name, surname)
n()