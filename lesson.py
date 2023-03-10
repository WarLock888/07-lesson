import os
import shutil
import sys

from victory import start_victory
from account import start_account


def file_dir_copy(filedirname1, filedirname2):
    if os.path.exists(filedirname1):
        if os.path.isdir(filedirname1):
            shutil.copytree(filedirname1, filedirname2)  # dir
        else:
            shutil.copy(filedirname1, filedirname2)  # file


def show_dirs(current_dir):
    oslist = os.listdir(current_dir)
    dirlist = list(filter(lambda x: os.path.isdir(x), oslist))
    return dirlist


def show_files(current_dir):
    oslist = os.listdir(current_dir)
    filelist = list(filter(lambda x: not os.path.isdir(x), oslist))
    return filelist


def save_lines(filename, value):
    try:
        with open(filename, 'w') as f:
            # запись списка
            f.writelines(value)
    except:
        pass


def main():
    print('Wellcome to console FileManager!')
    # print(os.getcwd())
    # exit()

    while True:
        print('-------------')
        print('1. создать папку')
        print('2. удалить (файл/папку)')
        print('3. копировать (файл/папку)')
        print('4. просмотр содержимого рабочей директории')
        print('5. сохранить содержимое рабочей директории в файл')
        print('6. посмотреть только папки')
        print('7. посмотреть только файлы')
        print('8. просмотр информации об операционной системе')
        print('9. создатель программы')
        print('10. играть в викторину')
        print('11. мой банковский счет')
        print('12. смена рабочей директории')
        print('13. выход')
        print('-------------')

        choice = input('Выберите пункт меню ')
        if choice == '1':  # создать папку
            dirname = input('Введите имя папки которую создать: ')
            if not os.path.exists(dirname):
                os.mkdir(dirname)
        elif choice == '2':  # удалить (файл/папку)
            filedirname = input('Введите имя файла/папки которую удалить: ')
            if os.path.exists(filedirname):
                if os.path.isdir(filedirname):
                    shutil.rmtree(filedirname)  # dir shutil.rmtree() deletes a directory and all its contents.
                else:
                    os.remove(filedirname)  # file
        elif choice == '3':  # копировать (файл/папку)
            filedirname1 = input('Введите имя файла/папки которую копировать: ')
            filedirname2 = input('Введите имя файла/папки в которую копировать: ')
            file_dir_copy(filedirname1, filedirname2)  # copy file or dir
        elif choice == '4':  # просмотр содержимого рабочей директории
            oslist = os.listdir(os.getcwd())
            print(oslist)
        elif choice == '5':  # сохранить содержимое рабочей директории в файл
            # формируем список файлов
            filelist = show_files(os.getcwd())
            filelist = f'files: {", ".join(filelist)}'
            # формируем список директорий
            dirlist = show_dirs(os.getcwd())
            dirlist = f'dirs: {", ".join(dirlist)}'
            # запись в файл списков
            save_lines('listdir.txt', [f'{filelist}\n', f'{dirlist}\n'])
        elif choice == '6':  # посмотреть только папки
            dirlist = show_dirs(os.getcwd())
            print(dirlist)
        elif choice == '7':  # посмотреть только файлы
            filelist = show_files(os.getcwd())
            print(filelist)
        elif choice == '8':  # просмотр информации об операционной системе
            sysinfo = f'My OS is {sys.platform} ({os.name})'
            print(sysinfo)
        elif choice == '9':  # создатель программы
            name = 'WarLock888'
            info = f'Program created by {name}'
            print(info)
        elif choice == '10':  # играть в викторину
            start_victory()
        elif choice == '11':  # мой банковский счет
            start_account()
        elif choice == '12':  # смена рабочей директории
            dirname = input('Введите имя директории на которую менять рабочую директорию: ')
            if os.path.exists(dirname):
                os.chdir(dirname)
            else:
                print(f'Ошибка. Нет такой директории.')
        elif choice == '13':  # выход
            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    main()
