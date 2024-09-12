import csv
import sys

if len(sys.argv) != 4:
    print("Использование: python script.py <путь_к_csv_файлу> <номер_строки> <номер_столбца>")
    sys.exit(1)

csv_file = sys.argv[1]
row_num = int(sys.argv[2])
col_num = int(sys.argv[3])

try:
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    value = data[row_num - 1][col_num - 1]
    print(value)

except FileNotFoundError:
    print(f"Ошибка: Файл '{csv_file}' не найден.")
except IndexError:
    print("Ошибка: Неверный номер строки или столбца.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

#Чтобы использовать эту программу, вам нужно сохранить ее в файл, например, script.py, и запускать из командной строки следующим образом:

#python script.py <путь_к_csv_файлу> <номер_строки> <номер_столбца>


#Где:
#- <путь_к_csv_файлу> - полный путь к CSV-файлу
#- <номер_строки> - номер строки (начиная с 1)
#- <номер_столбца> - номер столбца (начиная с 1)
