def is_prime(num):
    flag = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            flag = False
            break
    if num > 1 and flag == True:
        return True
    else:
        return False

# объявление функции
def is_valid_password(password):
    p = password.split(':')
    if len(p) > 3:
        return False
    f1, f2, f3 = False, False, False
    if p[0] == p[0][::-1]:
        f1 = True
    if is_prime(int(p[1])):
        f2 = True 
    if int(p[2]) % 2 == 0:
        f3 = True
    print(f1, f2, f3)
    if f1 == f2 == f3 == True:
        return True
    else:
        return False

# считываем данные
psw = '1221:101:22:22'

# вызываем функцию
print(is_valid_password(psw))