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


def start_account():
    # баланс счета
    try:
        # пытаемся загрузить баланс счета
        with open('account.data', 'r') as f:
            acount = int(f.readline())
    except:
        # ошибка чтения файла, обнуляем значение
        acount = 0
        # print('Файл несуществует: счет создан')

    # список покупок
    try:
        # пытаемся загрузить список покупок
        with open('purchases.data', 'r') as f:
            purchases = json.load(f)
    except:
        # ошибка чтения файла, обнуляем значение
        purchases = {}

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
            # баланс счета
            try:
                # сохраним значение счета в файл
                with open('account.data', 'w') as f:
                    f.write(f'{str(acount)}\n')
            except:
                pass

            # список покупок
            try:
                # сохраним список в файл
                with open('purchases.data', 'w') as f:
                    json.dump(purchases, f)
            except:
                pass
                print('Ошибка записи списка покупок')

            # прервать выполнение
            break
        else:
            print('Неверный пункт меню')
        print()


if __name__ == '__main__':
    start_account()
