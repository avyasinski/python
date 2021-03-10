# объявление функции
def convert_to_python_case(text):
    l = []
    result = ''
    for i in range(len(text)):
        if text[i].isupper():
            l.append(i)
    l.append(len(text))
    for i in range(len(l) - 1):
        result += text[l[i]:l[i + 1]].lower()
        result += '_'
    return result.rstrip('_')

    '''
    result = ''
    for i in range(len(text)):
        if text[i].isupper():
            result += '_' + text[i:].lower()
            print(result)
        else:
            print('suck')
    return result
    '''

# считываем данные
txt = 'ThisIsCamelCased'

# вызываем функцию
print(convert_to_python_case(txt))