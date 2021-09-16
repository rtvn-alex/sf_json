import json

rules_dict = {
    'timestamp': 'int',
    'referer': 'string (url)',
    'location': 'string (url)',
    'remoteHost': 'string',
    'partyId': 'string',
    'sessionId': 'string',
    'pageViewId': 'string',
    'eventType': 'string (itemBuyEvent или itemViewEvent)',
    'item_id': 'string',
    'item_price': 'int',
    'item_url': 'string (url)',
    'basket_price': 'string',
    'detectedDuplicate': 'bool',
    'detectedCorruption': 'bool',
    'firstInSession': 'bool',
    'userAgentName': 'string'
}

with open('j_f.json') as f:
    json_dict = json.load(f)[0]


def check_fields(dict1, dict2):
    return set(dict1.keys()) == set(dict2.keys())


def check_if_int(a):
    return type(a) is int


def check_if_bool(a):
    return type(a) is bool


def check_if_string(a):
    return type(a) is str


def check_if_string_url(a):
    return type(a) is str and (a[0:7] == r'http://' or a[0:8] == r'https://')


def check_if_string_item(a):
    return a in ['itemBuyEvent', 'itemViewEvent']


if check_fields(rules_dict, json_dict):
    print('Объект JSON содержит все требуемые поля и не содержит других полей')


def check_values(dict1):
    is_ok = True
    wrong_fields_dict = {}

    for key, value in dict1.items():
        if rules_dict[key] == 'int' and not check_if_int(value):
            is_ok = False
            wrong_fields_dict[key] = f'Значение не является {rules_dict[key]}'
        elif rules_dict[key] == 'string' and not check_if_string(value):
            is_ok = False
            wrong_fields_dict[key] = f'Значение не является {rules_dict[key]}'
        elif rules_dict[key] == 'string (url)' and not check_if_string_url(value):
            is_ok = False
            wrong_fields_dict[key] = f'Значение не является {rules_dict[key]}'
        elif rules_dict[key] == 'string (itemBuyEvent или itemViewEvent)' and not check_if_string_item(value):
            is_ok = False
            wrong_fields_dict[key] = f'Значение не является {rules_dict[key]}'
        elif rules_dict[key] == 'bool' and not check_if_bool(value):
            is_ok = False
            wrong_fields_dict[key] = f'Значение не является {rules_dict[key]}'
    if is_ok:
        return 'Pass'
    else:
        return wrong_fields_dict

print(check_values(json_dict))
# print(check_if_int('a'))

