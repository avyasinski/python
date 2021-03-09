# объявление функции
def is_palindrome(text):
    #text = ''.join(text.strip('.').strip('!').strip('?').lower().split())
    new = ''
    for i in text:
        if i.isalpha() == True:
            new += i.lower()
    print(new)
    if new == new[::-1]:
        return True
    else:
        return False
# считываем данные
txt = 'Gabler Ruby - burrel bag!'

# вызываем функцию
print(is_palindrome(txt))