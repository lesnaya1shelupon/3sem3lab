from moduli import say_name

if __name__ == '__main__':
    print("Введите имя и фамилию: ")
    (name, surname) = input().split()
    n = say_name(name, surname)
    n()
   
