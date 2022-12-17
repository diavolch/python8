def input_data():
    input_choise = int(input(
        'Как вам удобно внести данные:\n'
        '1. через запятую\n'
        '2. построчно\n'
        'Выбираю вариант ввода под номером: '
    ))
    if input_choise == 1:
        data = input('Введите через запятую Фамилию, Имя, Отчество, Телефон, Описание: \n').split(',')
    elif input_choise == 2:
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        middle_name = input('Введите отчество: ')
        phone = input('Введите телефон: ')
        description = input('Введите описание: ')
        data = [surname, name, middle_name, phone, description]
    else:
        data[0] = -1
        ('Такого варианта нет!')
    return data

def write_to_db(data):
    if data[0] == -1:
        input_data()
    else:
        s, n, m_n, ph, desc = data
        with open('data.txt','a') as file:
            file.write(f'{s}, {n}, {m_n}, {ph}, {desc}\n')

