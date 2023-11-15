# Работа с JSON: добавить супергероев (2+) и отсортировать всех супергероев по возрасту, результат работы - новый JSON (superhero_new.json) с отсортированными данными.
import json
import operator
def append_json():
    new_data = {"name": "Ivan", "age": 19, "secretIdentity": "Dan Juk", "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]}, {"name": "Vera", "age": 80, "secretIdentity": "Dan", "powers": ["Radiation resistance"]}
    with open('SuperHero.json', encoding='utf8') as file:
        read_json = file.read()
        data = json.loads(read_json)
        data['members'] += new_data
        with open('superhero_new.json', 'w', encoding='utf8') as outfile:
            outfile.write(json.dumps(data, sort_keys=True, ensure_ascii=False,indent=4))

def sort_json():

    with open('superhero_new.json', encoding='utf8') as file:
        read_json = file.read()
        data = json.loads(read_json)
        # sorted(read_json,key=lambda x : x['members'].get['age',0], reverse=True)

    sort_members = sorted(data["members"],key=operator.itemgetter("age"))  
    data["members"] = sort_members

    with open('superhero_new_sorted.json', 'w', encoding='utf8') as outfile:
        outfile.write(json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4))


append_json()
sort_json()

