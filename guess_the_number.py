import random
while True:
    random_number = random.randint(1, 10)
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    error_message = 'Некорректный ввод. Введите число от 1 до 10: '
    number = input('Угадай число от 1 до 10: ')
    while True:
        if number in numbers:
            break
        number = input(error_message)
    number = int(number)
    while number != random_number:
        number = int(number)
        if number < random_number:
            number = input('Слишком маленькое, попробуй ещё: ')
            while number not in numbers:
                number = input(error_message)
        elif number > random_number:
            number = input('Слишком большое, попробуй ещё: ')
            while number not in numbers:
                number = input(error_message)
    print('Ура! Ты угадал, это число -', str(number))
    while True:
        what_to_do = input('Попробуешь ещё? Да/Нет (Y/N): ')
        checks = [what_to_do.lower() == 'y', what_to_do.lower() == 'да', what_to_do.lower() == 'yes']
        if what_to_do.lower() in ('y', 'n', 'да', 'нет', 'no', 'yes'):
            break
        print('Некорректный ввод.')
    if any(checks):
        print('\n')
        continue
    else:
        print('Пока!')
        break