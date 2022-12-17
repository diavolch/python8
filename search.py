def searching():
    surname = input('Введите фамилию, по которой нужно найти данные: ')
    with open('data.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            res = 0
            if surname in line:
                print(line.strip())
                res += 1
        if res == 0:
            print('Такой записи нет!')
