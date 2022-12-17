import input_dt as inp
import search
import data_output as d_o

def action_choise():
    print(
        'Действие, которое необходимо совершить: \n'
        '1. Ввод данных\n'
        '2. Поиск данных\n'
        '3. Вывод всех данных')
    action = int(input('Введите номер действия: '))
    if action == 1:
        inp.write_to_db(inp.input_data())
    elif action == 2:
        search.searching()
    elif action == 3:
        d_o.output()
    else:
        print('Такого варианта нет!')

action_choise()