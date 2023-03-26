# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользоиз характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

import function

action = function.get_action()
while action!=0:
    if action==1:
        function.import_data()
        action = function.get_action()
    if action==2:
        function.export_data()
        action = function.get_action()
    if action==3:
        function.print_data()
        print()
        action = function.get_action()
    if action==4:
        print()
        poisk=input("Введите имя или фамилию: ")
        function.find_in_data(poisk)
        action = function.get_action()
    if action==5:
        print()
        new_string=input("Введите имя, фамилию, телефон через пробел: ")
        function.add_data("\n"+new_string)
        action = function.get_action()
    if action==6:
        function.rewrite_data()
        action = function.get_action()
    



