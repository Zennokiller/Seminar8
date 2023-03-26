# Запрос действия
def get_action():
    print("Какое действие вы хотите совершить?")
    print("1 - импорт")
    print("2 - экпорт")
    print("3 - вывести справочник на экран")
    print("4 - поиск по справочнику")
    print("5 - ввод данных в справочник")
    print("6 - редактирование данных")
    print("0 - выход")
    return int(input())

def import_data(): # 1 - импорт данных
    import_file = input("Введите имя файла: ")
    f = open(import_file, "r")
    data = f.readlines()
    f.close
    f = open("data.txt", "a")
    f.writelines("\n")
    f.writelines(data)
    f.close



    print("Импорт данных произведен")


def export_data(): # 2 - экспорт данных
    f = open("data.txt", "r")
    data = f.readlines()
    f.close
    export_file = input("Введите имя файла: ")
    f = open(export_file, "w")
    f.writelines(data)
    f.close
    print("Экпорт данных произведен")



def print_data(): #3 - выводит справочник на экран
    f = open("data.txt", "r")
    for line in f:
        print(line.strip())
    f.close

def find_in_data(poisk): #4 - выводит найденные записи по ключевику
    f = open("data.txt", "r")
    bool = False
    for line in f:
        a = list(line.strip().split())
        if a[0]==poisk or a[1]==poisk:
            bool = True
            print(a)
    if bool==False:
        print("Данные не найдены")
    f.close

def add_data(new_string): # 5 - добавление данных в справочник
    f = open("data.txt", "a")
    f.writelines(new_string)
    f.close

def del_record(num_record): # функция удаляет из спавочника (файла) запись с нужным номером, нумерация с 1
    f = open("data.txt", "r")
    data = f.readlines()
    f.close
    i=0
    for t in data:
        i+=1
        if i==num_record:
            data.remove(t)
    f = open("data.txt", "w")
    f.writelines(data)
    f.close

def rewrite_data(): # 6 - редактирование данных
    f = open("data.txt", "r+")
    i=0
    print("Весь справочник")
    for line in f:
        a = list(line.strip().split())
        i+=1
        print(str(i)+"  "+str(a))
    f.close
    del_record(int(input("Введите номер записи для радактирования: "))) #удаляем запись
    add_data("\n"+input("Введите имя, фамилию, телефон через пробел: ")) # добавляем запись


    


    


