import json

class Model:

    names = {}
    phones = {}

    myfile = open('db_names.txt', mode='r')
    json_data = json.load(myfile)
    names = json_data
    myfile.close()
    

    myfile = open('db_phones.txt', mode='r')
    json_data = json.load(myfile)
    phones = json_data
    myfile.close()
    

        
    def __init__(self, key, value):
        self.key = key
        self.value = value
        Model.names[key] = value
        Model.phones[value] = key

    @staticmethod
    def saveToFile():
        myfile = open('db_names.txt', mode='w')
        json.dump(Model.names, myfile)
        myfile.close()
        myfile = open('db_phones.txt', mode='w')
        json.dump(Model.phones, myfile)
        myfile.close()
        

class View:

    @staticmethod
    def menu():
        x = -1
        while x != '7':
            print('''\n1. Вывод - 1\n2. Добавить - 2 \n3. Удалить - 3 \n4. Поиск по имени - 4 \n5. Поиск по номеру телефона - 5 \n6. Сохранить - 6\n7. Выход - 7 \n''')
            x = input('Введите значение : ')
            if x == '1':
                print('')
                for i in Controller.printOut():
                    print(i[0] + ' ' + i[1])
            elif x =='2':
                print('')
                name = input('Введите имя: ')
                phone_number = input('Введите номер: ')
                Controller.add(name, phone_number)
                print('')
                print("Элемент добавлен")
                print('')
                print('Данные сохранены')
            elif x == '3':
                print('')
                name = input('Введите имя: ')
                Controller.delete(name)
                print('')
                print("Элемент удален")
            elif x == '4':
                key=input('Введите имя: ')
                print('')
                print(Controller.view(key))
            elif x == '5':
                phone=input('Введите номер: ')
                print('')
                print(Controller.phone_view(phone))
            elif x == '6':
                Controller.saving()
                print('')
                print('Данные сохранены')
            elif x == '7':
                Controller.saving()
                print('')
                print('Данные сохранены')
                break

class Controller:

     
    @staticmethod
    def printOut():
        return Model.names.items()

 
    @staticmethod
    def add(name, phone_number):
        Model(name,phone_number)
        Model.saveToFile()
          
 
    @staticmethod
    def delete(name):
        
        this_phone = Model.names[name]
        del Model.names[name]
        del Model.phones[this_phone]
        
        Model.saveToFile()
        
 
    @staticmethod
    def view(name):
        return Model.names[name]

    @staticmethod
    def phone_view(phone):
        return Model.phones[phone]

    @staticmethod
    def saving():
        Model.saveToFile()


View.menu()
