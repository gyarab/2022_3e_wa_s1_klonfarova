from pprint import pprint
import httpx

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=C7F38174BFD9D8FF4C8FE71EC9575ED0?date=23.01.2023"
res = httpx.get(url)
rows = res.text.split("\n")

rows = rows[2:-1]

data = {}

for r in rows:
    cols = r.split("|")
    curr = cols[-2]
    rate = cols[-1]
    amount = cols[-3]
    amount = int(amount)
    rate = rate.replace(",",".")
    rate = float(rate)
    
    if amount > 1:
        rate = rate / amount
    
    data[curr] = rate


y = input("Z CZK na cizí? (ano/ne")
if y == "ano":
    user_amount = input("Částka v CZK: ")
    user_amount = float(user_amount)
    user_curr = input("Převést do měny: ")

    result = user_amount / data[user_curr]
    result = round(result, 2)

    print(f"Výsledek je {result} {user_curr}")
elif y == "ne":
    user_curr = input("Měna: ")
    user_amount = input(f"Zadej castku v {user_curr}: ")

    result = user_amount * data["CZK"]
    result = round(result, 2)

    print(f"Výsledek je {result} CZK")
else:
    print("Chyba")