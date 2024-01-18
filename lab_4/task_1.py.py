# TODO импортировать необходимые модули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
data = []


def task(csv_file, json_file) -> None:
    ...  # TODO считать содержимое csv файла
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
