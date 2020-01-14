import json
from pprint import pprint

with open('ingredient-data.json', 'r') as f:
    json_data = json.load(f)

tmps = json_data
result = []
cnt = 1
ingredients_idx = []

for tmp in tmps:
    ingredient_tmp = {}
    ingredient_tmp ['name'] = tmp['name']
    ingredient_tmp['fields'] = {
        'oily': tmp['oily'],
        'dry': tmp['dry'],
        'sensitive': tmp['sensitive']
    }

    ingredients_idx.append(tmp['name'])
    result.append(ingredient_tmp)
    cnt += 1

with open('ingredients_data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
