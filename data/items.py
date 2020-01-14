import json
from pprint import pprint

with open('ingredients_data.json', 'r', encoding='utf-8') as f:
    ingredients_data = json.load(f)

with open('item-data.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

tmps = json_data
result = []

for tmp in tmps:
    # 성분 str => list로 변환
    ingredients_list = tmp['ingredients'].split(',')
    skin_types = ['oily', 'dry', 'sensitive']
    point = [0, 0, 0] # oily, dry, seneitive 순으로

    for ingredient in ingredients_list:
        for info in ingredients_data:
            if info['name'] == ingredient:
                for idx, skin_type in enumerate(skin_types):
                    if info['fields'][skin_type] == 'X':
                        point[idx] -= 1
                    elif info['fields'][skin_type] == 'O':
                        point[idx] += 1
                break

    # 딕셔너리 생성
    item_tmp = {}
    item_tmp['model'] = 'item.item'
    item_tmp['pk'] = tmp['id']
    item_tmp['fields'] = {
        'imageId': tmp['imageId'],
        'name': tmp['name'],
        'price': int(tmp['price']),
        'gender': tmp['gender'],
        'category': tmp['category'],
        'monthlySales': tmp['monthlySales'],
        'ingredients': tmp['ingredients'],
        'oily_point': point[0],
        'dry_point': point[1],
        'sensitive_point': point[2]

    }
    result.append(item_tmp)

with open('items_data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
