"""
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

import json


def add_item(purchases, item, expenses):
    purchases = dict(purchases)  # create new object
    purchases[item] = expenses  # add new expenses
    return purchases


def increment_acount(acount, value):
    return acount + value


def decrement_acount(acount, value):
    return acount - value


def load_value(filename, def_value=0):
    try:
        # пытаемся загрузить
        with open(filename, 'r') as f:
            value = int(f.readline())
    except:
        # ошибка чтения файла, берем по умолчанию
        value = def_value
    return value


def save_value(filename, value):
    try:
        # сохраним значение в файл
        with open(filename, 'w') as f:
            f.write(f'{str(value)}\n')
    except:
        pass


def load_dict(filename, def_dict={}):
    try:
        # пытаемся загрузить словарь
        with open(filename, 'r') as f:
            value = json.load(f)
    except:
        # ошибка чтения файла, берем по умолчанию
        value = def_dict
    return value


def save_dict(filename, value):
    try:
        # сохраним словарь в файл
        with open(filename, 'w') as f:
            json.dump(value, f)
    except:
        pass


def start_account():
    # загрузить баланс счета
    acount = load_value('account.data', 0)

    # загрузить список покупок
    purchases = load_dict('purchases.data', {})

    while True:
        print(f'На Вашем счете {acount}')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            refill = int(input('Какую сумму хотите внести?: '))
            acount = increment_acount(acount, refill)
        elif choice == '2':
            expenses = int(input('Какую сумму потратим?: '))
            if expenses > acount:
                print('Не достаточно средств')
            else:
                item = input('Что покупаем?: ')
                purchases = add_item(purchases, item, expenses)
                acount = decrement_acount(acount, expenses)
        elif choice == '3':
            print()
            print('Ваши покупки')
            for k, v in purchases.items():
                print(f'{k} - {v}')
        elif choice == '4':
            # сохранить баланс счета
            save_value('account.data', acount)

            # список покупок
            save_dict('purchases.data', purchases)

            # прервать выполнение
            break
        else:
            print('Неверный пункт меню')
        print()


if __name__ == '__main__':
    start_account()
