import json


def task() -> float:
    path = './input.json'
    sum = 0
    with open(path) as f:
        json_data = json.load(f)
        for dictionary in json_data:
            itog = dictionary.get('score') * dictionary.get('weight')
            sum += itog
    return round(sum, 3)


print(task())
