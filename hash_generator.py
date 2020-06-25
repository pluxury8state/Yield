import hashlib
import json

def open_file(file_i):
    json_file = None
    with open(str(file_i),encoding='utf8') as file_to_hash:
        json_file = json.load(file_to_hash)
    return json_file

def hash_file(object):

    mas = {}
    counter = 0
    for item in object:
        mas['name'] = item['name']
        hash_object = hashlib.md5(bytes(str(item['link']), encoding='utf8'))
        mas['hash_link'] = hash_object.hexdigest()
        yield mas
        counter += 1
    print(f'всего строк было обработано:{counter}')



file = open_file('new_links.json')

for item in hash_file(file):
    print(item)


