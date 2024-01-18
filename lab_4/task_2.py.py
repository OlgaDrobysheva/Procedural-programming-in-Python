import json

INPUT_FILE = "input.json"


# TODO решите задачу
def task(json_file) -> float:
    with open(json_file, 'r') as file:
        json_data = json.load(file)
    sum_of_products = 0
    for record in json_data:
        score = float(record.get('score', 0))
        weight = float(record.get('weight', 0))
        product = score * weight
        sum_of_products += product
    rounded_sum = round(sum_of_products, 3)
    return rounded_sum


print(task(INPUT_FILE))
