f = open('Day_07/names.txt','r', encoding="utf-8")
data = f.read(6)
print(data)
print(f.readline())
lines = f.readlines()
print(lines)
print(f.tell()) # Tells where my cursor is
f.seek(0)
f.seek(0,0) # whence = 0  begining 1 = current position 2 = end
print(f.tell())
print("-"*80)
print(f.read())
print("-"*80)

f.close()

print("-"*80)

f = open('Day_07/names.txt','r', encoding="utf-8")
print(f.read())
f.close()


print("-" * 80)

with open('Day_07/names.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    print("I am opening file using with:\n" + data)


with open("Day_07/fruits.txt", "w", encoding="utf-8") as f:
    f.writelines(["Apple", "Banana", "Mango"])

print("-"*80)

with open("Day_07/fruits.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)


print("-"*80)

with open("Day_07/fruits.txt", "a", encoding="utf-8") as f:
    result = f.write("Kiwi")

print(result)

with open("Day_07/fruits.txt", "r", encoding="utf-8") as fs:
    for line in fs:
        print(line)

print("-"*80)

lines = [
    "\nApple\n",
    "Banana\n",
    "Mango\n"
]

with open("Day_07/fruits.txt", "a", encoding="utf-8") as f:
    f.writelines(lines)
    f.flush()

with open("Day_07/fruits.txt", "r", encoding="utf-8") as fs:
    for line in fs:
        print(line)
fs.close()

print(f"files closed: {f.closed}")

print("-"*80)

with open("students.txt", "w", encoding="utf-8") as f:
    f.write("Harshit\n")
    f.write("Rahul\n")
    f.write("Aman\n")

with open("students.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())



# csv

print("-"*80)

import csv

with open("Day_07/books.csv", 'r' , encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)



print("-"*80)


data = [
"id,product,price\n",
"1,Chai,18\n",
"2,Chang,19\n"
]

with open("Day_07/products.csv", "w", encoding="utf-8") as f:
    f.writelines(data)

with open("Day_07/products.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row["product"])
        print(row["price"])


print("-"*80)

records = [
    {"id": 1, "product": "Chai", "price": 18.0},
    {"id": 2, "product": "Chang", "price": 19.0}
]

with open("Day_07/products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["id", "product", "price"]
    )

    writer.writeheader()
    writer.writerows(records)

with open("Day_07/products.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print("ID:", row["id"])
        print("Product:", row["product"])
        print("Price:", row["price"])
        print()



with open("Day_07/products.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    print(f"{'ID':<5}{'Product':<15}{'Price':>10}")
    print("-" * 30)

    for row in reader:
        print(f"{row['id']:<5}{row['product']:<15}{row['price']:>10}")




print("-"*80)

import json


datajson = {
    "name": "Harshit",
    "age": 22,
    "skills": ["Python", "SQL"]
}

json_str = json.dumps(datajson)

restored = json.loads(json_str)

json_str1= json.dumps(datajson, indent=10)

restored1 = json.loads(json_str1)
print(restored)
print(restored1)

print("-"*80)

with open("Day_07/order.json", "w", encoding="utf-8") as f:
    json.dump(datajson, f, indent=4)

with open("Day_07/order.json", 'r', encoding="utf-8") as f:
    newdata = json.load(f)


print(newdata)