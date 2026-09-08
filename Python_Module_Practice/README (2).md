# Python Management Systems — Master Cheat Sheet

> A practical, exam-focused reference for solving **management-system questions** and many other beginner/intermediate Python lab problems.
>
> Focus: **lists, dictionaries, functions, loops, conditions, CRUD, validation, exceptions, menus, file handling, JSON, CSV, SQLite basics, regex, and problem-solving patterns**.
>
> **Not covered deeply:** OOP and Pickle, since those were excluded from the practicals you shared.

---

# 0. THE MASTER APPROACH

When you receive a new Python management-system question, do **not** start coding immediately.

Use this sequence:

```text
1. Read the problem
       ↓
2. Identify the DATA structure
       ↓
3. Identify the FIELDS
       ↓
4. Identify the CRUD operations
       ↓
5. Identify VALIDATION rules
       ↓
6. Identify SEARCH rules
       ↓
7. Identify FILE / DATABASE requirements
       ↓
8. Write small FUNCTIONS
       ↓
9. Build the MENU / CONTROLLER
       ↓
10. Test every operation
```

For most management systems, the architecture is:

```text
                    main()
                      |
                    menu()
                      |
        +-------------+-------------+
        |             |             |
       CREATE        READ          SEARCH
        |             |             |
      append       display        results
        |             |             |
        +-------------+-------------+
                      |
                    UPDATE
                      |
                    DELETE
                      |
               SAVE / LOAD
```

---

# 1. FIRST THING: IDENTIFY THE DATA MODEL

Most lab management systems use:

```python
items = [
    {
        "id": 1,
        "name": "Example",
        "category": "Demo",
        "price": 100.0,
        "quantity": 10
    },
    {
        "id": 2,
        "name": "Another",
        "category": "Demo",
        "price": 200.0,
        "quantity": 5
    }
]
```

This is:

```text
list
  ├── dictionary
  ├── dictionary
  ├── dictionary
  └── ...
```

### What does each level mean?

```python
items[0]
```

= first dictionary

```python
items[0]["name"]
```

= first item's name

```python
items[0]["price"]
```

= first item's price

### General pattern

```python
records = [
    {
        "id": 1,
        "field1": value,
        "field2": value
    }
]
```

When the question says:

> Store records in a list of dictionaries

this is the pattern to use.

---

# 2. COMMON MANAGEMENT-SYSTEM FIELDS

Typical examples:

## Product

```python
{
    "id": 1,
    "name": "Laptop",
    "category": "Electronics",
    "price": 55000.0,
    "quantity": 10
}
```

## Student

```python
{
    "id": 1,
    "name": "Aarav",
    "course": "Python",
    "marks": 88.5,
    "grade": "A"
}
```

## Employee

```python
{
    "id": 1,
    "name": "Rahul",
    "department": "IT",
    "salary": 50000.0
}
```

## Book

```python
{
    "id": 1,
    "title": "Python Programming",
    "author": "John Zelle",
    "price": 650.0,
    "copies": 15
}
```

The **same CRUD architecture** works for all of them.

---

# 3. CRUD — THE CORE OF MANAGEMENT SYSTEMS

CRUD means:

```text
C = Create
R = Read
U = Update
D = Delete
```

## CREATE

Usually:

```python
records.append(record)
```

## READ

Usually:

```python
for record in records:
    print(record)
```

## UPDATE

Usually:

```python
record["name"] = new_name
record["price"] = new_price
```

## DELETE

Usually:

```python
records.remove(record)
```

### Memorize this

```text
Create → append()
Read   → loop / display
Update → modify dictionary
Delete → remove()
```

---

# 4. AUTO-GENERATED ID

Most questions say:

> ID should be automatically generated.

Use:

```python
next_id = 1
```

When adding:

```python
record = {
    "id": next_id,
    ...
}
```

Then:

```python
next_id += 1
```

### Example

```text
next_id = 1
add record → ID 1
next_id = 2

add record → ID 2
next_id = 3
```

### Important

If your add function receives `next_id` and increments it:

```python
def add_record(records, next_id):
    ...
    return next_id + 1
```

the caller must save the returned value:

```python
next_id = add_record(records, next_id)
```

Otherwise the outside variable will not change.

---

# 5. HOW TO WRITE FUNCTIONS

A management system becomes much easier if each operation is a function.

Basic structure:

```python
def function_name(parameters):
    # logic
    return result
```

Typical functions:

```python
def add_record(records, next_id):
    pass

def view_records(records):
    pass

def search_records(records, search_term):
    pass

def update_record(records, record_id):
    pass

def delete_record(records, record_id):
    pass

def menu():
    pass

def main():
    pass
```

---

# 6. TYPE ANNOTATIONS

You may see:

```python
def add_record(records: list[dict], next_id: int) -> int:
```

Meaning:

```text
records → expected list of dictionaries
next_id → expected integer
-> int  → function returns an integer
```

Another example:

```python
def calculate_grade(marks: float) -> str:
```

means:

```text
marks → float
return → string
```

These annotations improve readability. They are not a replacement for validation.

---

# 7. INPUT() ALWAYS RETURNS A STRING

This is one of the biggest exam traps.

```python
x = input("Enter number: ")
```

Even if the user enters:

```text
10
```

`x` is:

```python
"10"
```

not:

```python
10
```

Therefore:

```python
age = int(input("Age: "))
```

```python
price = float(input("Price: "))
```

---

# 8. TYPE CONVERSION

## String → Integer

```python
number = int("10")
```

## String → Float

```python
price = float("99.50")
```

## Number → String

```python
text = str(100)
```

### Common errors

```python
int("abc")
```

→ `ValueError`

```python
float("hello")
```

→ `ValueError`

Use `try/except`.

---

# 9. THE UNIVERSAL VALIDATION PATTERN

This pattern is extremely important:

```python
while True:
    try:
        value = ...

        if valid_condition:
            break

        print("Invalid value.")

    except ValueError:
        print("Invalid input.")
```

Think:

```text
ASK
 ↓
CONVERT
 ↓
VALIDATE
 ↓
 ┌──────────────┐
 │              │
VALID          INVALID
 │              │
break          repeat
```

---

# 10. STRING VALIDATION

If a field cannot be blank:

```python
name = input("Enter name: ").strip()

while name == "":
    print("Name cannot be empty.")
    name = input("Enter name: ").strip()
```

## Why `.strip()`?

Input:

```text
"   Laptop   "
```

becomes:

```text
"Laptop"
```

It also lets you correctly detect:

```text
"     "
```

as an empty value after stripping.

---

# 11. NUMERIC VALIDATION

## Positive price

```python
while True:
    try:
        price = float(input("Enter price: "))

        if price > 0:
            break

        print("Price must be greater than 0.")

    except ValueError:
        print("Price must be a number.")
```

## Non-negative quantity

```python
while True:
    try:
        quantity = int(input("Enter quantity: "))

        if quantity >= 0:
            break

        print("Quantity cannot be negative.")

    except ValueError:
        print("Quantity must be an integer.")
```

## Range validation

```python
while True:
    try:
        marks = float(input("Enter marks: "))

        if 0 <= marks <= 100:
            break

        print("Marks must be between 0 and 100.")

    except ValueError:
        print("Marks must be a number.")
```

---

# 12. CHAINED COMPARISON

This:

```python
0 <= marks <= 100
```

means:

```python
0 <= marks and marks <= 100
```

Examples:

```python
0 <= 50 <= 100     # True
0 <= 150 <= 100    # False
```

Useful for marks, percentages, age ranges, etc.

---

# 13. FINDING A RECORD BY ID

The most reusable management-system pattern:

```python
for record in records:
    if record["id"] == record_id:
        # record found
```

Example:

```python
for product in products:
    if product["id"] == product_id:
        print(product)
        break
```

---

# 14. RETURN TRUE / FALSE PATTERN

Very useful for update and delete functions.

```python
def update_record(records, record_id):

    for record in records:

        if record["id"] == record_id:

            # perform update

            return True

    return False
```

Meaning:

```text
Found → perform operation → True
Not found → False
```

Caller:

```python
success = update_record(records, record_id)

if success:
    print("Updated successfully.")
else:
    print("Record not found.")
```

---

# 15. SEARCH BY ID OR TEXT

This is a common requirement.

```python
def search_records(records, search_term):

    results = []

    search_term = search_term.strip().lower()

    for record in records:

        if search_term.isdigit():

            if record["id"] == int(search_term):
                results.append(record)

        else:

            if search_term in record["name"].lower():
                results.append(record)

    return results
```

---

# 16. CASE-INSENSITIVE SEARCH

Convert both sides to lowercase:

```python
search_term = search_term.lower()
```

and:

```python
record["name"].lower()
```

Example:

```python
"lap" in "laptop"
```

→ `True`

```python
"PYTHON".lower()
```

→ `"python"`

---

# 17. SUBSTRING SEARCH WITH `in`

```python
"py" in "python"
```

→ `True`

```python
"john" in "john zelle"
```

→ `True`

This is useful for partial search.

---

# 18. EXACT MATCH VS SUBSTRING MATCH

## Exact

```python
record["name"].lower() == search_term
```

Matches only the entire value.

## Substring

```python
search_term in record["name"].lower()
```

Can match part of the value.

Example:

```text
Search: "lap"

Laptop
```

substring = match

exact = no match

Read the question carefully to determine which one is required.

---

# 19. `isdigit()`

```python
"123".isdigit()
```

→ `True`

```python
"abc".isdigit()
```

→ `False`

Useful for deciding:

```text
numeric input → search by ID
text input    → search by name/title/etc.
```

---

# 20. LIST METHODS YOU SHOULD KNOW

## append

```python
items.append(value)
```

Add at the end.

## remove

```python
items.remove(value)
```

Remove matching value.

## pop

```python
items.pop()
```

Remove last element.

```python
items.pop(0)
```

Remove index 0.

## insert

```python
items.insert(0, value)
```

Insert at position.

## len

```python
len(items)
```

Number of elements.

## sort

```python
items.sort()
```

Sort list.

## reverse

```python
items.reverse()
```

Reverse list.

---

# 21. DICTIONARY OPERATIONS

Suppose:

```python
product = {
    "id": 1,
    "name": "Laptop",
    "price": 50000
}
```

## Read

```python
product["name"]
```

## Update

```python
product["price"] = 55000
```

## Add new key

```python
product["quantity"] = 10
```

## Remove key

```python
del product["quantity"]
```

## Check key

```python
if "price" in product:
```

## Get safely

```python
product.get("price")
```

or:

```python
product.get("price", 0)
```

---

# 22. LOOPING THROUGH A LIST

```python
for product in products:
    print(product)
```

For dictionaries:

```python
for key, value in product.items():
    print(key, value)
```

Keys:

```python
product.keys()
```

Values:

```python
product.values()
```

---

# 23. FORMATTED TABLES

Common pattern:

```python
print(
    f"{'ID':<5}"
    f"{'Name':<25}"
    f"{'Price':<12}"
)
```

Then:

```python
for product in products:
    print(
        f"{product['id']:<5}"
        f"{product['name']:<25}"
        f"{product['price']:<12.2f}"
    )
```

### Important formatting

```python
:<10
```

Left-align in 10 spaces.

```python
:>10
```

Right-align in 10 spaces.

```python
:^10
```

Center in 10 spaces.

```python
:.2f
```

Two decimal places.

Example:

```python
f"{55000:.2f}"
```

→ `55000.00`

---

# 24. EMPTY LIST CHECKS

These all work:

```python
if len(records) == 0:
```

```python
if not records:
```

```python
if records:
```

The last one means:

> list contains at least one item

Example:

```python
results = []

if results:
    print("Found")
else:
    print("Not found")
```

---

# 25. `break`, `continue`, `return`

## break

Stops the current loop.

```python
for x in numbers:
    if x == 5:
        break
```

## continue

Skip current iteration.

```python
for x in numbers:
    if x < 0:
        continue

    print(x)
```

## return

Ends the function and optionally sends a value back.

```python
def square(x):
    return x * x
```

---

# 26. MENU-DRIVEN PROGRAM

Typical pattern:

```python
while True:

    choice = menu()

    if choice == 1:
        ...
    elif choice == 2:
        ...
    elif choice == 3:
        ...
    elif choice == 4:
        ...
    elif choice == 5:
        ...
    elif choice == 6:
        break
    else:
        print("Invalid choice.")
```

---

# 27. `match/case`

Alternative to `if/elif`:

```python
match choice:

    case 1:
        ...

    case 2:
        ...

    case 3:
        ...

    case 6:
        break

    case _:
        print("Invalid choice.")
```

`case _` = default case.

Use whichever the question/instructor accepts.

---

# 28. MENU FUNCTION

A clean pattern:

```python
def menu():

    print("""
1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Exit
""")

    try:
        choice = int(input("Enter choice: "))
        return choice

    except ValueError:
        print("Choice must be an integer.")
        return -1
```

---

# 29. MAIN FUNCTION

Use `main()` to control the application:

```python
def main():

    records = []
    next_id = 1

    while True:

        choice = menu()

        match choice:

            case 1:
                next_id = add_record(records, next_id)

            case 2:
                view_records(records)

            case 3:
                ...

            case 6:
                break


main()
```

This separates:

```text
data + functions + controller
```

and keeps the code easier to debug.

---

# 30. CREATE FUNCTION TEMPLATE

Use this whenever asked to add something:

```python
def add_record(records, next_id):

    # 1. Get input
    name = input("Enter name: ").strip()

    # 2. Validate
    while name == "":
        print("Name cannot be empty.")
        name = input("Enter name: ").strip()

    # 3. More fields...
    # 4. Build dictionary

    record = {
        "id": next_id,
        "name": name
    }

    # 5. Add to list
    records.append(record)

    # 6. Increment ID
    next_id += 1

    # 7. Return new ID
    return next_id
```

---

# 31. READ FUNCTION TEMPLATE

```python
def view_records(records):

    if not records:
        print("No records found.")
        return

    for record in records:
        print(record)
```

For table output, replace the simple print with formatted columns.

---

# 32. SEARCH FUNCTION TEMPLATE

```python
def search_records(records, search_term):

    results = []

    search_term = search_term.strip().lower()

    for record in records:

        if search_term in record["name"].lower():
            results.append(record)

    return results
```

Adapt the searchable fields according to the question.

---

# 33. UPDATE FUNCTION TEMPLATE

```python
def update_record(records, record_id):

    for record in records:

        if record["id"] == record_id:

            new_name = input(
                "Enter new name: "
            ).strip()

            while new_name == "":
                print("Name cannot be empty.")
                new_name = input(
                    "Enter new name: "
                ).strip()

            record["name"] = new_name

            return True

    return False
```

---

# 34. DELETE FUNCTION TEMPLATE

```python
def delete_record(records, record_id):

    for record in records:

        if record["id"] == record_id:

            confirmation = input(
                "Delete this record? (y/n): "
            ).strip().lower()

            if confirmation == "y":

                records.remove(record)

                return True

            return False

    return False
```

---

# 35. IMPORTANT: DON'T RETURN FALSE INSIDE THE LOOP TOO EARLY

Wrong:

```python
for record in records:

    if record["id"] == record_id:
        return True

    return False
```

This checks only the first element.

Correct:

```python
for record in records:

    if record["id"] == record_id:
        return True

return False
```

The `return False` belongs **after the loop**.

---

# 36. FILE HANDLING — BASIC

## Write

```python
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
```

## Read entire file

```python
with open("data.txt", "r", encoding="utf-8") as f:
    data = f.read()
```

## Read one line

```python
with open("data.txt", "r", encoding="utf-8") as f:
    line = f.readline()
```

## Read all lines

```python
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
```

## Iterate through lines

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)
```

---

# 37. FILE MODES

```text
"r" → read
"w" → write / overwrite
"a" → append
"x" → create only if file doesn't exist
```

### Very important

```python
open("file.txt", "w")
```

can replace existing content.

```python
open("file.txt", "a")
```

adds to the end.

---

# 38. `with open(...)`

Prefer:

```python
with open("file.txt", "r", encoding="utf-8") as f:
    ...
```

Why?

Python automatically closes the file after the block.

---

# 39. TEXT-FILE SERIALIZATION

For a pipe-delimited question:

```text
1|Laptop|Electronics|55000|10
```

Save:

```python
line = (
    f"{product['id']}|"
    f"{product['name']}|"
    f"{product['category']}|"
    f"{product['price']}|"
    f"{product['quantity']}"
)

f.write(line + "\n")
```

Load:

```python
line = line.strip()
parts = line.split("|")
```

Then:

```python
product = {
    "id": int(parts[0]),
    "name": parts[1],
    "category": parts[2],
    "price": float(parts[3]),
    "quantity": int(parts[4])
}
```

---

# 40. `strip()` vs `split()`

## strip

Removes surrounding whitespace:

```python
"  hello  ".strip()
```

→ `"hello"`

## split

Breaks a string into a list:

```python
"a|b|c".split("|")
```

→

```python
["a", "b", "c"]
```

---

# 41. JSON — VERY IMPORTANT

First:

```python
import json
```

JSON is excellent when the question asks to save a list of dictionaries.

---

# 42. `json.dump()` — SAVE

```python
with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4)
```

Think:

```text
Python object
     ↓
 json.dump()
     ↓
JSON file
```

`indent=4` makes it readable.

---

# 43. `json.load()` — LOAD

```python
with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)
```

Think:

```text
JSON file
     ↓
 json.load()
     ↓
Python object
```

---

# 44. `dump` VS `dumps`

## dump

Writes directly to a file:

```python
json.dump(data, f)
```

## dumps

Creates a JSON string:

```python
text = json.dumps(data)
```

Similarly:

## load

Reads from a file:

```python
data = json.load(f)
```

## loads

Reads JSON from a string:

```python
data = json.loads(text)
```

### Memory trick

```text
dump  = file
dumps = string

load  = file
loads = string
```

---

# 45. JSON ERROR HANDLING

```python
try:

    with open("students.json", "r", encoding="utf-8") as f:
        students = json.load(f)

except FileNotFoundError:

    print("File does not exist.")

except json.JSONDecodeError:

    print("Invalid or corrupted JSON.")
```

## Difference

`FileNotFoundError`:

> The file doesn't exist.

`JSONDecodeError`:

> The file exists, but its JSON is invalid.

---

# 46. JSON SAVE TEMPLATE

```python
def save_to_json(filepath, records):

    try:

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                records,
                f,
                indent=4
            )

        print("Saved successfully.")

    except OSError as e:

        print(f"Error saving file: {e}")
```

---

# 47. JSON LOAD TEMPLATE

```python
def load_from_json(filepath):

    try:

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:

            records = json.load(f)

        return records

    except FileNotFoundError:

        print("File does not exist.")

    except json.JSONDecodeError:

        print("Invalid JSON.")

    return []
```

---

# 48. CSV BASICS

If a question asks for CSV:

```python
import csv
```

Write:

```python
with open("products.csv", "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow(
        ["id", "name", "price"]
    )

    writer.writerow(
        [1, "Laptop", 55000]
    )
```

Read:

```python
with open("products.csv", "r", newline="", encoding="utf-8") as f:

    reader = csv.reader(f)

    for row in reader:
        print(row)
```

Dictionary-based CSV:

```python
with open("products.csv", "w", newline="", encoding="utf-8") as f:

    fieldnames = ["id", "name", "price"]

    writer = csv.DictWriter(
        f,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerow({
        "id": 1,
        "name": "Laptop",
        "price": 55000
    })
```

---

# 49. SQLITE BASICS

Only use this when the question explicitly asks for SQLite/database storage.

```python
import sqlite3
```

Connect:

```python
conn = sqlite3.connect("products.db")
```

Cursor:

```python
cursor = conn.cursor()
```

Create table:

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL,
        quantity INTEGER
    )
""")
```

Insert:

```python
cursor.execute(
    """
    INSERT INTO products
    (name, price, quantity)
    VALUES (?, ?, ?)
    """,
    ("Laptop", 55000, 10)
)
```

Save transaction:

```python
conn.commit()
```

Read:

```python
cursor.execute("SELECT * FROM products")

rows = cursor.fetchall()
```

Close:

```python
conn.close()
```

### Important SQL CRUD mapping

```text
CREATE TABLE → database structure
INSERT       → Create
SELECT       → Read
UPDATE       → Update
DELETE       → Delete
```

### SQL security rule

Use placeholders:

```python
cursor.execute(
    "SELECT * FROM products WHERE id = ?",
    (product_id,)
)
```

Do not build SQL with unsafe string concatenation.

---

# 50. REGEX — MASTER CHEAT SHEET

Regex = **Regular Expression**.

Use:

```python
import re
```

Regex is useful when the question asks you to validate or extract patterns such as:

```text
email
phone number
PIN code
username
password
ID format
date
specific text pattern
```

---

# 51. MOST IMPORTANT REGEX SYMBOLS

```text
.       any character except newline
^       beginning of string
$       end of string
*       zero or more
+       one or more
?       zero or one
{n}     exactly n
{n,m}   n to m
[]      character set
[^]     negated character set
()      capturing group
|       OR
\d      digit
\D      non-digit
\w      word character
\W      non-word character
\s      whitespace
\S      non-whitespace
```

---

# 52. CHARACTER CLASSES

## Digits

```regex
\d
```

Equivalent to:

```regex
[0-9]
```

Example:

```python
re.search(r"\d", "abc123")
```

---

## Letters

```regex
[a-zA-Z]
```

Only ASCII letters.

---

## Lowercase letters

```regex
[a-z]
```

## Uppercase

```regex
[A-Z]
```

---

# 53. QUANTIFIERS

## `*`

Zero or more:

```regex
a*
```

Matches:

```text
""
"a"
"aa"
"aaa"
```

## `+`

One or more:

```regex
a+
```

Does not match empty string.

## `?`

Zero or one:

```regex
a?
```

## `{5}`

Exactly five:

```regex
\d{5}
```

## `{3,10}`

Between 3 and 10:

```regex
\d{3,10}
```

---

# 54. `^` AND `$`

These are extremely important for validation.

```regex
^...$
```

means:

> The entire string must follow the pattern.

Example:

```regex
^\d{6}$
```

means exactly six digits.

Examples:

```text
123456 → valid
12345  → invalid
1234567 → invalid
abc123 → invalid
```

---

# 55. REGEX FOR INDIAN PIN CODE

Simple six-digit PIN:

```python
pattern = r"^\d{6}$"
```

Check:

```python
match = re.fullmatch(pattern, pin)
```

---

# 56. REGEX FOR SIMPLE PHONE NUMBER

10 digits:

```python
pattern = r"^\d{10}$"
```

This validates length and digits only.

---

# 57. REGEX FOR EMAIL

A common practical-level pattern:

```python
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
```

Example:

```python
email = "user@example.com"

if re.fullmatch(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
```

### Breakdown

```regex
^[a-zA-Z0-9._%+-]+
```

username

```regex
@
```

literal @

```regex
[a-zA-Z0-9.-]+
```

domain

```regex
\.
```

literal dot

```regex
[a-zA-Z]{2,}$
```

top-level domain

---

# 58. REGEX FOR USERNAME

Example: 3–15 characters, letters/numbers/underscore:

```python
pattern = r"^[A-Za-z0-9_]{3,15}$"
```

---

# 59. REGEX FOR STRONGER PASSWORD

A common educational pattern requiring:

- at least 8 characters
- uppercase
- lowercase
- digit
- special character

```python
pattern = (
    r"^(?=.*[A-Z])"
    r"(?=.*[a-z])"
    r"(?=.*\d)"
    r"(?=.*[^A-Za-z0-9])"
    r".{8,}$"
)
```

### New regex concept: lookahead

```regex
(?=.*[A-Z])
```

means:

> Somewhere ahead, an uppercase letter must exist.

Similarly:

```regex
(?=.*\d)
```

means:

> Somewhere ahead, a digit must exist.

---

# 60. `re.search()`

Searches anywhere in the string:

```python
match = re.search(pattern, text)
```

Good for:

> Find this pattern somewhere.

---

# 61. `re.match()`

Checks from the beginning of the string.

```python
match = re.match(pattern, text)
```

---

# 62. `re.fullmatch()`

Checks the entire string.

```python
match = re.fullmatch(pattern, text)
```

For validation, `fullmatch()` is often the clearest choice.

---

# 63. `re.findall()`

Returns all matches:

```python
numbers = re.findall(r"\d+", text)
```

Example:

```python
text = "There are 20 books and 5 pens."

numbers = re.findall(r"\d+", text)
```

Result:

```python
["20", "5"]
```

---

# 64. CAPTURE GROUPS

Parentheses capture parts of a match:

```python
pattern = r"(\d{4})-(\d{2})-(\d{2})"
```

For:

```text
2026-09-09
```

Groups:

```text
group(1) → 2026
group(2) → 09
group(3) → 09
```

The full match:

```python
match.group(0)
```

---

# 65. REGEX SEARCH / VALIDATION TEMPLATE

```python
import re

pattern = r"your_pattern_here"

value = input("Enter value: ").strip()

if re.fullmatch(pattern, value):
    print("Valid")
else:
    print("Invalid")
```

Or:

```python
match = re.search(pattern, value)

if match:
    print("Found")
else:
    print("Not found")
```

---

# 66. F-STRINGS

Use:

```python
name = "Harshit"
age = 20

print(f"Name: {name}, Age: {age}")
```

Formatting:

```python
price = 55000

print(f"{price:.2f}")
```

Alignment:

```python
print(f"{name:<20}")
print(f"{name:>20}")
print(f"{name:^20}")
```

---

# 67. COMMON STRING METHODS

```python
text.strip()
text.lower()
text.upper()
text.title()
text.replace("a", "b")
text.split(",")
",".join(items)
text.startswith("A")
text.endswith(".")
text.isdigit()
text.isalpha()
text.isalnum()
```

---

# 68. `split()` VS `join()`

Split:

```python
"a,b,c".split(",")
```

→

```python
["a", "b", "c"]
```

Join:

```python
",".join(["a", "b", "c"])
```

→

```text
a,b,c
```

---

# 69. `any()` AND `all()`

## any

True if at least one item is true:

```python
if any(x > 100 for x in numbers):
    print("Found")
```

## all

True if every item is true:

```python
if all(x >= 0 for x in numbers):
    print("All valid")
```

---

# 70. `min()`, `max()`, `sum()`

```python
numbers = [10, 20, 30]
```

```python
min(numbers)  # 10
max(numbers)  # 30
sum(numbers)  # 60
```

Useful for management systems.

Example:

```python
highest_mark = max(
    student["marks"]
    for student in students
)
```

---

# 71. FIND NEXT ID AFTER LOADING DATA

Useful after loading from JSON/file:

```python
next_id = max(
    record["id"]
    for record in records
) + 1
```

For an empty list, use a safe version:

```python
if records:
    next_id = max(
        record["id"]
        for record in records
    ) + 1
else:
    next_id = 1
```

---

# 72. LIST COMPREHENSION

Basic:

```python
squares = [x * x for x in numbers]
```

Filtered:

```python
positive = [
    x for x in numbers
    if x > 0
]
```

Management-system example:

```python
technical = [
    product
    for product in products
    if product["category"] == "Electronics"
]
```

You do not have to use comprehensions in every exam. Normal loops are often easier to debug.

---

# 73. `enumerate()`

When you need both index and value:

```python
for index, item in enumerate(items):
    print(index, item)
```

Example:

```python
for i, product in enumerate(products, start=1):
    print(i, product["name"])
```

---

# 74. `range()`

```python
for i in range(5):
    print(i)
```

Outputs:

```text
0 1 2 3 4
```

```python
for i in range(1, 6):
```

Outputs:

```text
1 2 3 4 5
```

---

# 75. NESTED LOOPS

Useful when processing tables or multiple records:

```python
for student in students:

    for value in student.values():
        print(value)
```

Don't use nested loops unnecessarily.

---

# 76. COMMON CALCULATION PATTERNS

## Average

```python
average = sum(numbers) / len(numbers)
```

Protect against empty list:

```python
if numbers:
    average = sum(numbers) / len(numbers)
```

## Percentage

```python
percentage = (obtained / total) * 100
```

## Total price

```python
total = price * quantity
```

## Discount

```python
discount_amount = price * discount / 100
final_price = price - discount_amount
```

---

# 77. CALCULATE-GRADE PATTERN

```python
def calculate_grade(marks):

    if marks >= 85:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 50:
        return "C"

    else:
        return "F"
```

General lesson:

> Put reusable business rules into a separate function.

---

# 78. DO NOT DUPLICATE BUSINESS LOGIC

Bad:

```python
# add function
if marks >= 85:
    grade = "A"

# update function
if marks >= 85:
    grade = "A"
```

Better:

```python
def calculate_grade(marks):
    ...
```

Then everywhere:

```python
grade = calculate_grade(marks)
```

This reduces mistakes.

---

# 79. EXCEPTION HANDLING MASTER PATTERN

```python
try:
    risky_operation()

except ValueError:
    print("Invalid value.")

except FileNotFoundError:
    print("File not found.")

except json.JSONDecodeError:
    print("Invalid JSON.")

except OSError as e:
    print(f"File error: {e}")
```

Use the **specific exception** when possible.

Avoid:

```python
except:
```

unless there is a very strong reason.

---

# 80. COMMON BUILT-IN EXCEPTIONS

## ValueError

Wrong value for conversion/operation.

```python
int("abc")
```

## TypeError

Wrong type used.

```python
"5" + 2
```

## IndexError

Invalid list index.

```python
items[100]
```

## KeyError

Missing dictionary key:

```python
student["unknown"]
```

## FileNotFoundError

Missing file.

## JSONDecodeError

Invalid JSON.

---

# 81. DEBUGGING: READ THE ERROR

When Python reports:

```text
NameError
```

Think:

> Did I misspell or forget to define a variable?

```text
TypeError
```

Think:

> Am I using the wrong type?

```text
ValueError
```

Think:

> Is the value invalid for this conversion?

```text
KeyError
```

Think:

> Does this dictionary key exist?

```text
IndexError
```

Think:

> Is my list index outside the list?

---

# 82. INDENTATION

Python uses indentation to define blocks.

Correct:

```python
if age >= 18:
    print("Adult")
```

Incorrect:

```python
if age >= 18:
print("Adult")
```

Remember:

```text
def
if
elif
else
for
while
try
except
match
case
```

all create blocks where indentation matters.

---

# 83. THE BIG `return` INDENTATION TRAP

Wrong:

```python
for record in records:

    if record["id"] == record_id:
        update_record()

    return True
```

This may return `True` after checking only the first record.

Correct:

```python
for record in records:

    if record["id"] == record_id:
        update_record()
        return True

return False
```

---

# 84. VARIABLE NAMES TO AVOID

Avoid overriding useful built-ins:

```python
str
list
dict
id
input
sum
max
min
```

For example, don't do:

```python
str = input(...)
```

Use:

```python
search_term = input(...)
```

Don't do:

```python
list = []
```

Use:

```python
records = []
```

---

# 85. FUNCTIONS SHOULD HAVE ONE CLEAR JOB

Good:

```python
calculate_grade()
```

does grade calculation.

```python
search_students()
```

does searching.

```python
save_to_json()
```

does saving.

Avoid giant functions that do everything.

---

# 86. REUSABLE MANAGEMENT-SYSTEM SKELETON

This is the template you can adapt to many questions:

```python
# DATA
records = [
    {
        "id": 1,
        "name": "Example"
    }
]


# CREATE
def add_record(records, next_id):
    pass


# READ
def view_records(records):
    pass


# SEARCH
def search_records(records, search_term):
    pass


# UPDATE
def update_record(records, record_id):
    pass


# DELETE
def delete_record(records, record_id):
    pass


# MENU
def menu():
    pass


# CONTROLLER
def main():

    next_id = 2

    while True:

        choice = menu()

        match choice:

            case 1:
                next_id = add_record(
                    records,
                    next_id
                )

            case 2:
                view_records(records)

            case 3:
                ...

            case 4:
                ...

            case 5:
                ...

            case 6:
                break

            case _:
                print("Invalid choice.")


main()
```

---

# 87. HOW TO CONVERT A WORD PROBLEM INTO CODE

Suppose the question says:

> Create a Product Inventory Management System. Each product contains ID, name, category, price, quantity.

Translate:

```text
Product
  ↓
dictionary

Many products
  ↓
list of dictionaries
```

Question says:

> Add product.

Translate:

```python
products.append(product)
```

Question says:

> Auto-generate ID.

Translate:

```python
next_id
```

Question says:

> Price must be greater than zero.

Translate:

```python
if price > 0:
```

Question says:

> Quantity cannot be negative.

Translate:

```python
if quantity >= 0:
```

Question says:

> Search by ID or name.

Translate:

```python
if search_term.isdigit():
    # ID search
else:
    # name search
```

Question says:

> Update by ID.

Translate:

```python
for product in products:
    if product["id"] == product_id:
```

Question says:

> Delete after confirmation.

Translate:

```python
confirmation = input("(y/n): ").strip().lower()

if confirmation == "y":
    products.remove(product)
```

---

# 88. EXAM STRATEGY: READ THE MARKS

If the question gives marks such as:

```text
Menu = 8
CRUD = 8
Search = 6
Validation = 3
Exception handling = 3
```

do not spend 40 minutes polishing output.

Prioritize:

```text
1. Required data structure
2. All required functions
3. CRUD
4. Search
5. Validation
6. Exception handling
7. Menu
8. Formatting/polish
```

Get the functionality working first.

---

# 89. EXAM STRATEGY: REQUIREMENT CHECKLIST

Before submitting, scan the question and tick each requirement:

```text
[ ] Data structure correct?
[ ] All fields present?
[ ] ID auto-generated?
[ ] Add works?
[ ] View works?
[ ] Search works?
[ ] Update works?
[ ] Delete works?
[ ] Menu repeats?
[ ] Exit works?
[ ] Invalid menu input handled?
[ ] String validation?
[ ] Numeric validation?
[ ] ValueError handled?
[ ] File requirement completed?
[ ] Correct file mode?
[ ] Correct JSON/CSV/text format?
```

---

# 90. TESTING STRATEGY

Do not test only the happy path.

Test:

## Normal

```text
Add valid product
Search valid product
Update valid product
Delete valid product
```

## Boundary

```text
price = 0
quantity = 0
marks = 0
marks = 100
```

## Invalid

```text
price = -5
quantity = -1
marks = 101
marks = abc
ID = abc
name = ""
```

## Missing

```text
search ID that doesn't exist
delete ID that doesn't exist
update ID that doesn't exist
```

---

# 91. BOOLEAN LOGIC CHEAT SHEET

```python
and
```

Both must be true.

```python
or
```

At least one must be true.

```python
not
```

Reverses truth value.

Example:

```python
if price > 0 and quantity >= 0:
```

Example:

```python
if name == "" or category == "":
```

---

# 92. COMPARISON OPERATORS

```text
==  equal
!=  not equal
>   greater
<   smaller
>=  greater or equal
<=  smaller or equal
```

Don't confuse:

```python
=
```

assignment

with:

```python
==
```

comparison.

---

# 93. ASSIGNMENT VS COMPARISON

```python
x = 10
```

means:

> put 10 into x

```python
x == 10
```

means:

> is x equal to 10?

---

# 94. COMMON MANAGEMENT-SYSTEM QUESTIONS

Be prepared for:

```text
Product Management
Student Management
Employee Management
Library Management
Inventory Management
Banking Management
Hospital Management
Course Management
Book Management
Movie Management
Customer Management
Order Management
Hotel Management
```

The architecture is usually almost identical.

Only the **fields and business rules** change.

---

# 95. ADAPTING THE TEMPLATE

## Product

```python
id, name, category, price, quantity
```

## Student

```python
id, name, course, marks, grade
```

## Employee

```python
id, name, department, salary
```

## Book

```python
id, title, author, genre, price, copies
```

## Customer

```python
id, name, email, phone
```

The CRUD logic remains almost the same.

---

# 96. WHEN THE QUESTION HAS BUSINESS LOGIC

Separate the rule into a function.

Examples:

```python
calculate_grade()
calculate_discount()
calculate_tax()
calculate_salary()
calculate_total()
calculate_status()
```

Pattern:

```python
def business_rule(value):
    if condition:
        return result
    ...
```

Then call it during create/update.

---

# 97. BUSINESS-RULE SYNCHRONIZATION

If one field depends on another, update them together.

Example:

```python
student["marks"] = marks
student["grade"] = calculate_grade(marks)
```

Example:

```python
order["quantity"] = quantity
order["total"] = quantity * order["price"]
```

Never update the source field without updating dependent fields.

---

# 98. DEFAULT VALUES

Sometimes a field needs a default:

```python
status = "Active"
```

or:

```python
quantity = 0
```

Then:

```python
record = {
    "id": next_id,
    "status": "Active"
}
```

Read the question carefully before inventing defaults.

---

# 99. OPTIONAL FIELDS

If a field is optional:

```python
phone = input("Phone (optional): ").strip()
```

Do not apply non-empty validation unless the question requires it.

---

# 100. `None`

`None` means no value / absence of a value.

```python
result = None
```

Check:

```python
if result is None:
```

Use `is None`, not normally `== None`.

---

# 101. `is` VS `==`

Use:

```python
==
```

for value comparison.

Use:

```python
is None
```

for checking `None`.

---

# 102. SHALLOW MENTAL MODEL OF DATA FLOW

For a management system:

```text
INPUT
 ↓
VALIDATE
 ↓
CONVERT
 ↓
BUILD / FIND / MODIFY
 ↓
STORE IN LIST
 ↓
DISPLAY / SAVE
```

If you are stuck, ask:

> Which step am I missing?

---

# 103. WHEN YOU ARE STUCK: THE 7 QUESTIONS

Ask yourself:

```text
1. What is my main list?
2. What does one dictionary look like?
3. What does the user need to enter?
4. What must be validated?
5. How do I find the record?
6. What should happen to the record?
7. What should the function return?
```

This solves a huge percentage of lab questions.

---

# 104. COMMON BUG: FORGETTING TO APPEND

You build:

```python
product = {
    "id": next_id,
    ...
}
```

but forget:

```python
products.append(product)
```

Result:

> Product never actually enters the inventory.

---

# 105. COMMON BUG: FORGETTING TO STORE RETURN VALUE

Wrong:

```python
add_product(products, next_id)
```

when the function returns the next ID.

Correct:

```python
next_id = add_product(
    products,
    next_id
)
```

---

# 106. COMMON BUG: STRING ID VS INTEGER ID

Wrong:

```python
product_id = input("ID: ")
```

Then:

```python
product["id"] == product_id
```

This compares:

```text
1 == "1"
```

which is false.

Correct:

```python
product_id = int(input("ID: "))
```

---

# 107. COMMON BUG: CALLING `.lower()` WITHOUT ASSIGNING

Wrong:

```python
search_term.lower()
```

Strings are immutable; this does not change the variable.

Correct:

```python
search_term = search_term.lower()
```

---

# 108. COMMON BUG: ONLY CHECKING FIRST RECORD

Wrong:

```python
for record in records:

    if record["id"] == record_id:
        ...

    return False
```

Correct:

```python
for record in records:

    if record["id"] == record_id:
        ...

return False
```

---

# 109. COMMON BUG: RETURN INSIDE LOOP TOO EARLY

Wrong:

```python
for record in records:
    return record
```

This returns the first record only.

Put `return` after the desired condition.

---

# 110. COMMON BUG: INPUT WITHOUT VALIDATION

Risky:

```python
price = float(input("Price: "))
```

If the user enters:

```text
abc
```

the program crashes.

Safer:

```python
try:
    price = float(input("Price: "))
except ValueError:
    print("Invalid price.")
```

For repeated validation, combine with `while True`.

---

# 111. COMMON BUG: MANUAL BUSINESS-RULE FIELDS

If the question says:

> Grade is calculated automatically

Do NOT:

```python
grade = input("Enter grade: ")
```

Instead:

```python
grade = calculate_grade(marks)
```

---

# 112. COMMON BUG: SAVE/LOAD MISMATCH

If saving uses JSON:

```python
json.dump(...)
```

loading should use:

```python
json.load(...)
```

If saving uses a custom pipe format:

```text
id|name|price
```

loading must use:

```python
split("|")
```

The write format and read format must agree.

---

# 113. COMMON BUG: LOADED DATA NOT ASSIGNED

Wrong:

```python
json.load(f)
```

Correct:

```python
records = json.load(f)
```

Otherwise you may read the file but ignore the returned Python object.

---

# 114. COMMON BUG: OVERWRITING DATA UNEXPECTEDLY

```python
open("file.txt", "w")
```

overwrites the file.

Use:

```python
"a"
```

when you need append behavior.

Always follow the exact requirement.

---

# 115. MENU + FUNCTION CALL MAP

Think:

```text
1 → add function
2 → view function
3 → search function
4 → update function
5 → delete function
6 → save function
7 → load function
8 → exit
```

For a new question, make this map first.

---

# 116. EXAM CODING ORDER

A very reliable order:

```text
STEP 1 → import modules
STEP 2 → sample data
STEP 3 → helper/business-rule functions
STEP 4 → add
STEP 5 → view
STEP 6 → search
STEP 7 → update
STEP 8 → delete
STEP 9 → save/load if required
STEP 10 → menu
STEP 11 → main
STEP 12 → test
```

Why?

Because each function builds on simpler concepts.

---

# 117. IF TIME IS VERY SHORT

Write the minimum working architecture first:

```python
records = []


def add_record(...):
    ...


def view_records(...):
    ...


def search_records(...):
    ...


def update_record(...):
    ...


def delete_record(...):
    ...


def main():
    while True:
        ...
```

Get the skeleton running.

Then fill validation and formatting.

Do not spend 20 minutes on table borders before CRUD works.

---

# 118. PRACTICAL TEST: MINIMUM VIABLE PROGRAM

The program should at least:

```text
start
 ↓
menu
 ↓
add
 ↓
view
 ↓
search
 ↓
update
 ↓
delete
 ↓
exit
```

Then add defensive handling.

---

# 119. CLEAN CODE CHECKLIST

Before finishing:

```text
[ ] Meaningful variable names
[ ] Functions have clear responsibilities
[ ] No unnecessary imports
[ ] No duplicate business logic
[ ] No accidental global variables
[ ] Correct indentation
[ ] Correct return placement
[ ] Input converted to correct type
[ ] Invalid input handled
[ ] Empty list handled
[ ] Not-found cases handled
```

---

# 120. MASTER ONE-PAGE MEMORY SHEET

If you only have a few minutes before the exam, memorize this:

```python
# DATA
records = [
    {
        "id": 1,
        "name": "Example",
        "price": 100.0
    }
]


# VALIDATION
while True:
    try:
        value = float(input("Enter value: "))

        if value > 0:
            break

    except ValueError:
        print("Invalid input.")


# FIND
for record in records:
    if record["id"] == record_id:
        ...


# CREATE
record = {
    "id": next_id,
    "name": name
}
records.append(record)
next_id += 1


# SEARCH
search_term = search_term.strip().lower()

for record in records:
    if search_term in record["name"].lower():
        ...


# UPDATE
record["name"] = new_name


# DELETE
records.remove(record)


# SUCCESS / FAILURE
return True
return False


# TEXT FILE SAVE
with open("data.txt", "w", encoding="utf-8") as f:
    f.write(line + "\n")


# TEXT FILE LOAD
with open("data.txt", "r", encoding="utf-8") as f:
    line = f.readline()


# JSON SAVE
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(records, f, indent=4)


# JSON LOAD
with open("data.json", "r", encoding="utf-8") as f:
    records = json.load(f)


# JSON ERRORS
except FileNotFoundError:
    ...

except json.JSONDecodeError:
    ...


# REGEX
import re

if re.fullmatch(r"^\d{10}$", value):
    print("Valid")


# MENU
while True:
    choice = menu()

    match choice:
        case 1:
            ...
        case 2:
            ...
        case 3:
            ...
        case _:
            print("Invalid choice.")
```

---

# 121. FINAL MASTER STRATEGY

When you get **ANY new management-system question**, extract these things from the statement:

```text
DATA
→ What does one record look like?

FIELDS
→ What keys does the dictionary have?

CREATE
→ What inputs are required?

VALIDATION
→ What values are allowed?

READ
→ What should be displayed?

SEARCH
→ Search by what fields?
→ Exact or substring?
→ Case-sensitive or insensitive?

UPDATE
→ Which fields can change?

DELETE
→ Is confirmation required?

BUSINESS LOGIC
→ Any grade/discount/status/total calculation?

PERSISTENCE
→ Text / JSON / CSV / SQLite?

ERRORS
→ Which inputs/files can fail?

MENU
→ What are the options?

ID
→ Is it auto-generated?

RETURNS
→ Should functions return True/False/list/next_id?
```

Then translate each requirement into a function.

---

# 122. GOLDEN RULE

Do not think:

> "I need to write a 300-line program."

Think:

```text
I need:
1 data structure
+ 5–10 small functions
+ 1 menu
+ 1 main loop
```

That's all.

Most "different" management-system questions are the **same machine wearing different clothes**.

```text
Product Management
Student Management
Library Management
Employee Management
Inventory Management

          ↓

same CRUD architecture
same validation patterns
same search patterns
same menu
same exception handling
```

Only the fields and business rules change.

---

# 123. FINAL EXAM MANTRA

```text
READ THE REQUIREMENTS
        ↓
IDENTIFY THE DATA
        ↓
BUILD THE DICTIONARY
        ↓
WRITE CRUD FUNCTIONS
        ↓
ADD VALIDATION
        ↓
ADD SEARCH
        ↓
ADD BUSINESS LOGIC
        ↓
ADD FILE/DATABASE LAYER
        ↓
CONNECT WITH MENU
        ↓
TEST EDGE CASES
```

If you can follow that sequence, you are far less likely to get stuck when the question changes from **Product** to **Student**, **Library**, **Employee**, **Inventory**, or another similar management system.
