import json

json_data = '''
{
"name":"Jan Kot",
"age":30,
"city":"Gdańsk",
"is_student":"False",
"last_ids":[23,67,224],
"address":{
        "street": "Złota",
        "local_nb":"6/46"
    }
}
'''

print(json_data)
print(type(json_data))

try:
    data_dict = json.loads(json_data)
    print("Parsowanie JSON zakończone sukcesem:\n")
    #wyświetlenie danych

    print(f"Imię i nazwisko: {data_dict['name']}\n"
          f"wiek: {data_dict['age']}\n"
          f"miasto: {data_dict['city']}\n"
          f"czy jest studentem? ({data_dict['is_student']})\n"
          f"id zamówień: {data_dict['last_ids']}\n"
          f"ulica: {data_dict['address']['street']}\n"
          f"numer lokalu: {data_dict['address']['local_nb']}")

    json_d = json.dumps(data_dict,indent=4)
    with open("zamowienia.json","w",encoding="utf-8") as f:
        f.write(json_d)
except json.JSONDecodeError as e:
    print(f"Błąd parsowania: {e}")
