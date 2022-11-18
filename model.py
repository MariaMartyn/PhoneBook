

def printDict():
    data = open('phonebook.txt', encoding = 'utf-8')
    base = data.read().split('\n')[:-1]
    data.close()
    dict = {}
    for i in base:
        key = i.split(':') [0]
        value = i.split('т.')[1:]
        dict[key] = value
    return dict


def findPhoneNumber(surname):
    dict = printDict()
    a = 0
    if surname in dict:
        a = f"Телефонный номер:  {dict.get(surname)}"
    else:
        a ='Такой фамилии нет в справочнике'
    return a




