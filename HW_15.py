# З
# адача №1
# Пользователь будет вводить название и стоимость каждой
# своей покупки за день, до тех пор пока он не напишет
# “стоп”. Ваша задача записать это в json файл в формате:
# {"название" : "яблоко",
#  "стоимость": "200"}


import json

purchases = []

while True:
    name = input("Purchase name (or stop):")
    if name == 'stop':
        break
    price = float(input("Price: "))


    purchase = {"name": name, "price": price}
    purchases.append(purchase)

with open("purchases.json", "w", encoding='utf-8') as file:
    json.dump(purchases, file, indent=2, ensure_ascii=False)

# Задача №2
# Прочитать файл из предыдущего задания и вывести
# стоимость всех покупок за день

with open("purchases.json", 'r', encoding='utf-8') as json_file:
    purchases = json.load(json_file)

total_cost = 0

for purchase in purchases:
    price = int(purchase['price'])
    total_cost += price
print(f"Total cost: {total_cost}")

