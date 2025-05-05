#Городецький А.Ю.
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
    file.write("Питання: Як називається програмний пакет, який виконує код Python?\n")
    file.close()
    print(f"Файл {file_name} закрито")

file = open_file(file_name, "r")

#Коваль А.М.
if file:
    lines = file.readlines()
    file.close()

    full_text = "".join(lines)
    full_text += "Відповідь: Інтерпретатор Python (наприклад, CPython)\n"
    full_text += "Прізвище: Коваль\n"

    answer_file_name = "answer.txt"
    answer_file = open_file(answer_file_name, "w")
    if answer_file:
        answer_file.write(full_text)
        answer_file.close()
        print(f"Результат записано у файл {answer_file_name}")

