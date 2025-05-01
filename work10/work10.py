def open_file(name, mode):
    try:
        f = open(name, mode, encoding='utf-8')
    except Exception as e:
        print(f"Помилка при відкритті файлу {name}: {e}")
        return None
    else:
        print(f"Файл {name} відкрито")
        return f

file_name = "question.txt"
file = open_file(file_name, "w")

if file:
    file.write("Прізвище: Городецький\n")
    file.write("Питання: Як називається  програмний пакет, який виконує код Python?\n")
    file.close()
    print(f"Файл {file_name} закрито")
