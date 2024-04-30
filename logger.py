from data_create import name_data, surname_data, phone_data, address_data

def read_file1():
    with open('File1.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j:i+1]))
                    j = i
    return data_first_list 

def read_file2():
    with open('File2.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        data_second_list = []
        j = 0
        for i in range(len(data_second)):
            if data_second[i] == '\n' or i == len(data_second) - 1:
                    data_second_list.append(''.join(data_second[j:i+1]))
                    j = i
    return data_second_list 

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
                    f"1 вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 вариант: \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант "))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('File1.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('File2.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('File1.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range (len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))

    print('Вывожу данные из 2 файла: \n')
    with open('File2.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

def delete_data():
    data_first_list = read_file1()
    data_second_list = read_file2()
    var = int(input(f"В каком файле удалить данные\n 1 - в файле 1 (построчный) \n 2 - в файле 2 (данные в одну строку через ;)"))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))
    var2 = str(input('Введите фамилию или имя человека, чьи данные нужно удалить '))
    if var == 1:
        data_first_list = list(filter(lambda x: not(var2) in x, data_first_list))
        with open('File1.csv', 'w') as f:
            f.write(''.join(data_first_list))
    elif var == 2:
        data_second_list = list(filter(lambda x: not(var2) in x, data_second_list))
        with open('File2.csv', 'w') as f:
            f.write(''.join(data_second_list))
    print("Удалено")

def change_data():
    data_first_list = read_file1()
    data_second_list = read_file2()
    
    var = int(input(f"В каком файле изменить данные\n 1 - в файле 1 (построчный) \n 2 - в файле 2 (данные в одну строку через ;)"))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))
    var2 = str(input('Введите фамилию или имя человека, чьи данные нужно изменить '))
    if var == 1:
        record_to_change = list(filter(lambda x: (var2) in x, data_first_list))
        if len(record_to_change) == 0:
            print('Запись не найдена')
            return
        print('Введите новые значения для записи: ')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        changed_record = f"{name} \n{surname} \n{phone} \n{address} \n \n"
        changed_index = data_first_list.index(record_to_change[0])
        data_first_list[changed_index] = changed_record
        with open('File1.csv', 'w') as f:
            f.write(''.join(data_first_list))
    elif var == 2:
        record_to_change = list(filter(lambda x: (var2) in x, data_second_list))
        if len(record_to_change) == 0:
            print('Запись не найдена')
            return
        print('Введите новые значения для записи: ')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        changed_record = f"{name} \n{surname} \n{phone} \n{address} \n \n"
        changed_index = data_second_list.index(record_to_change[0])
        data_second_list[changed_index] = changed_record
        with open('File2.csv', 'w') as f:
            f.write(''.join(data_second_list))
    print("Данные изменены")

