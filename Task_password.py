password = input("Введите пароль: ")

try:
    password[0]
    int(password)/0
except IndexError:
    print("Вы ввели пустой пароль")
except ZeroDivisionError:
    print("Ваш пароль состоит только из цифр")
except ValueError:
    print("Требования к паролю соблюдены")