# TODO решите задачу
import json


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    sum_of_products = sum(item["score"] * item["weight"] for item in data)
    result = round(sum_of_products, 3)
    return result


print(task())
