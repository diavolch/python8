def searching():
    surname = input('Введите фамилию, по которой нужно найти данные: ')
    with open('data.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            if surname in line:
                print(line.strip())
