# 🐍 Python CRUD Practical Master Cheat Sheet

> **Purpose:** A reusable reference for solving Python CRUD / management-system practical questions independently, especially harder questions involving **regex, JSON, CSV, file handling, dictionaries, shallow/deep copy, OOP, exceptions, CLI tables, validation, and SQLite**.
>
> The main goal is not to memorize programs. It is to memorize **patterns** and learn how to translate an English question into a working design.

---

# Table of Contents

1. [The Master Mental Model](#1-the-master-mental-model)
2. [How to Understand Any Practical Question](#2-how-to-understand-any-practical-question)
3. [Standard CRUD Architecture](#3-standard-crud-architecture)
4. [Python Data Structures](#4-python-data-structures)
5. [Dictionary Master Reference](#5-dictionary-master-reference)
6. [List of Dictionaries](#6-list-of-dictionaries)
7. [Shallow Copy vs Deep Copy](#7-shallow-copy-vs-deep-copy)
8. [Strings and Type Conversion](#8-strings-and-type-conversion)
9. [Regex Master Cheat Sheet](#9-regex-master-cheat-sheet)
10. [Regex Validation Patterns](#10-regex-validation-patterns)
11. [JSON File Handling](#11-json-file-handling)
12. [CSV File Handling](#12-csv-file-handling)
13. [Text File Handling](#13-text-file-handling)
14. [Files and Directories](#14-files-and-directories)
15. [OOP for CRUD Projects](#15-oop-for-crud-projects)
16. [Custom Exceptions](#16-custom-exceptions)
17. [Exception Handling](#17-exception-handling)
18. [Input Validation Helpers](#18-input-validation-helpers)
19. [CRUD Patterns](#19-crud-patterns)
20. [Searching, Filtering and Sorting](#20-searching-filtering-and-sorting)
21. [CLI Table Display](#21-cli-table-display)
22. [Dates and Times](#22-dates-and-times)
23. [SQLite for Hard-Level CRUD](#23-sqlite-for-hard-level-crud)
24. [Transactions and Rollback](#24-transactions-and-rollback)
25. [Useful Python Modules](#25-useful-python-modules)
26. [Debugging Strategy](#26-debugging-strategy)
27. [Common Errors and Fixes](#27-common-errors-and-fixes)
28. [Hard-Level Project Architecture](#28-hard-level-project-architecture)
29. [Question-to-Code Translation](#29-question-to-code-translation)
30. [Practical Exam Workflow](#30-practical-exam-workflow)
31. [Testing Checklist](#31-testing-checklist)
32. [Ultimate Emergency Cheat Sheet](#32-ultimate-emergency-cheat-sheet)

---

# 1. The Master Mental Model

Almost every management-system practical can be reduced to:

```text
INPUT
  ↓
VALIDATE
  ↓
CREATE / READ / UPDATE / DELETE
  ↓
STORE DATA
  ↓
DISPLAY RESULT
  ↓
HANDLE ERRORS
```

For persistent applications:

```text
User
 ↓
Menu
 ↓
Function / Class Method
 ↓
Validation
 ↓
Business Logic
 ↓
Data Structure / Database
 ↓
JSON / CSV / SQLite
 ↓
Output
```

## The four CRUD operations

| CRUD | Meaning | Common words in questions |
|---|---|---|
| C | Create | add, insert, register, create |
| R | Read | display, list, view, show, search |
| U | Update | modify, edit, change, update |
| D | Delete | remove, delete, cancel |

**Core idea:** Most "different" management systems use the same CRUD skeleton. What usually changes is the **business logic**.

Examples:

```text
Library    → issue / return
Bank       → deposit / withdraw / transfer
Inventory  → stock in / stock out
Student    → grades / pass-fail
Hospital   → appointment / discharge
Booking    → availability / cancellation
```

---

# 2. How to Understand Any Practical Question

## Step 1 — Identify the entity

Ask:

> What is this system managing?

Examples:

```text
Student Management → students
Library            → books / members / issues
Bank               → accounts / transactions
Inventory          → products
Hospital           → patients / doctors / appointments
```

## Step 2 — Extract all fields

Question:

> Create a student with ID, name, age, email, course and marks.

Translate to:

```python
student = {
    "id": 1,
    "name": "Rahul",
    "age": 21,
    "email": "rahul@example.com",
    "course": "Python",
    "marks": 85
}
```

## Step 3 — Extract operations

Create a list:

```text
ADD
VIEW
SEARCH
UPDATE
DELETE
```

Then look for special operations:

```text
SORT
FILTER
REPORT
CALCULATE
ISSUE
RETURN
TRANSFER
PAY
CANCEL
```

## Step 4 — Extract validation rules

Look for words such as:

```text
must
should
cannot
required
unique
greater than
less than
positive
valid
not empty
```

Convert each rule into code.

Example:

> Amount must be positive.

becomes:

```python
if amount <= 0:
    raise ValueError("Amount must be greater than zero")
```

## Step 5 — Identify storage

Look for:

```text
JSON
CSV
file
SQLite
SQL
database
persistent
save/load
```

## Step 6 — Identify relationships

Examples:

```text
Student → Courses
Customer → Orders
Account → Transactions
Member → Issued Books
Employee → Department
```

Relationships often mean **nested dictionaries/lists or multiple database tables**.

## Step 7 — Identify special requirements

Look for:

```text
regex
OOP
inheritance
custom exception
transaction
rollback
audit log
CSV
JSON
sorting
searching
```

These become separate modules/functions/classes in your solution.

---

# 3. Standard CRUD Architecture

A safe beginner/intermediate structure:

```python
def add_record():
    pass


def view_records():
    pass


def search_record():
    pass


def update_record():
    pass


def delete_record():
    pass


def main():
    while True:
        print_menu()

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            update_record()
        elif choice == "5":
            delete_record()
        elif choice == "6":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
```

## Recommended project structure

For an exam:

```text
project/
│
├── main.py
├── data.json
├── data.csv
└── app.db
```

For a bigger project:

```text
project/
│
├── main.py
├── models.py
├── validators.py
├── storage.py
├── services.py
├── display.py
└── data/
    └── data.json
```

Do not over-engineer a simple practical unless the question asks for it.

---

# 4. Python Data Structures

## List

Ordered, mutable collection.

```python
students = []

students.append(student)
students.remove(student)
students.pop()
```

Access:

```python
students[0]
```

Loop:

```python
for student in students:
    print(student)
```

## Tuple

Ordered and immutable.

```python
student = (1, "Rahul", 21)
```

Useful for fixed collections and many database result rows.

## Set

Stores unique values.

```python
emails = set()
emails.add("a@example.com")
emails.add("a@example.com")
```

Useful for duplicate detection.

## Dictionary

Key-value structure. One of the most important structures for CRUD.

```python
student = {
    "id": 101,
    "name": "Rahul",
    "age": 21
}
```

### Quick comparison

| Structure | Best use |
|---|---|
| List | collection of records |
| Dictionary | one record / key-value data |
| Set | unique values |
| Tuple | fixed/immutable sequence |

Most file-based CRUD apps use:

```text
list + dictionary
```

---

# 5. Dictionary Master Reference

Create:

```python
student = {
    "id": 1,
    "name": "Rahul"
}
```

Access:

```python
student["name"]
```

Safer access:

```python
student.get("name")
student.get("email", "Not Available")
```

Add/update:

```python
student["course"] = "Python"
student["name"] = "Amit"
```

Delete:

```python
del student["course"]
```

Check existence:

```python
if "email" in student:
    print(student["email"])
```

Get keys/values/items:

```python
student.keys()
student.values()
student.items()
```

Loop:

```python
for key, value in student.items():
    print(key, value)
```

## Nested dictionary

```python
student = {
    "id": 1,
    "name": "Rahul",
    "address": {
        "city": "Delhi",
        "state": "Delhi"
    }
}
```

Access:

```python
student["address"]["city"]
```

## Dictionary comprehension

```python
squares = {x: x * x for x in range(1, 6)}
```

Filter into a dictionary:

```python
passed = {
    s["id"]: s["name"]
    for s in students
    if s["marks"] >= 40
}
```

---

# 6. List of Dictionaries

This is the classic file-based CRUD structure.

```python
students = [
    {
        "id": 1,
        "name": "Rahul",
        "age": 21
    },
    {
        "id": 2,
        "name": "Amit",
        "age": 22
    }
]
```

Search:

```python
for student in students:
    if student["id"] == 2:
        print(student)
```

Find by ID:

```python
def find_by_id(data, record_id):
    for record in data:
        if record.get("id") == record_id:
            return record
    return None
```

Use:

```python
record = find_by_id(students, 5)

if record:
    print(record)
else:
    print("Not found")
```

## Generate a new numeric ID

```python
new_id = max(
    (item["id"] for item in data),
    default=0
) + 1
```

## Duplicate check

```python
if any(item["id"] == new_id for item in data):
    print("ID already exists")
```

---

# 7. Shallow Copy vs Deep Copy

Import:

```python
import copy
```

## Assignment: same object

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)  # [1, 2, 3, 4]
```

`a` and `b` refer to the same object.

## Shallow copy

```python
b = copy.copy(a)
```

For a flat structure, changes to the new list do not change the original list.

But nested mutable objects are still shared:

```python
a = [{"name": "Rahul"}]
b = copy.copy(a)

b[0]["name"] = "Amit"

print(a)  # [{'name': 'Amit'}]
```

## Deep copy

```python
b = copy.deepcopy(a)
```

Nested objects are copied too:

```python
a = [{"name": "Rahul"}]
b = copy.deepcopy(a)

b[0]["name"] = "Amit"

print(a)  # [{'name': 'Rahul'}]
```

### Remember

```text
b = a                 → same object
copy.copy(a)          → shallow copy
copy.deepcopy(a)      → independent nested copy
```

## Equality vs identity

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True
print(a is b)  # False
```

```text
==  → same value
is  → same object
```

---

# 8. Strings and Type Conversion

Input always returns a string:

```python
value = input("Enter value: ")
```

Convert:

```python
age = int(input("Age: "))
price = float(input("Price: "))
```

Useful string methods:

```python
name.strip()
name.lower()
name.upper()
name.title()
name.replace("old", "new")
"a,b,c".split(",")
",".join(["a", "b", "c"])
name.startswith("Har")
name.endswith("Garg")
```

Clean user input before storage:

```python
name = name.strip()
email = email.strip().lower()
phone = phone.strip()
```

---

# 9. Regex Master Cheat Sheet

Import:

```python
import re
```

Regex is useful for validating:

```text
Email
Phone
Password
Username
ID formats
PIN codes
Dates
Custom codes
```

## Regex symbols

| Pattern | Meaning |
|---|---|
| `.` | any character except newline by default |
| `^` | start of string |
| `$` | end of string |
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 |
| `{n}` | exactly n |
| `{n,m}` | n to m |
| `[]` | character set |
| `[^...]` | not these characters |
| `()` | capture group |
| `|` | OR |
| `\d` | digit |
| `\D` | non-digit |
| `\w` | word character |
| `\W` | non-word character |
| `\s` | whitespace |
| `\S` | non-whitespace |

## Character sets

```text
[0-9]          digits
[a-z]          lowercase letters
[A-Z]          uppercase letters
[A-Za-z]       letters
[A-Za-z0-9]    letters + digits
```

## Raw strings

Prefer:

```python
pattern = r"^\d{6}$"
```

instead of ordinary strings for many regex patterns.

---

# 10. Regex Validation Patterns

## Email

Basic practical regex:

```python
pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

if re.fullmatch(pattern, email):
    print("Valid")
else:
    print("Invalid")
```

## Indian mobile number

```python
pattern = r"[6-9]\d{9}"

if re.fullmatch(pattern, phone):
    print("Valid")
```

## Indian PIN code

```python
pattern = r"\d{6}"
```

## Username

Example: 3–16 characters, letters/numbers/underscore:

```python
pattern = r"[A-Za-z0-9_]{3,16}"
```

## Strong password

At least 8 characters, uppercase, lowercase, digit and special character:

```python
pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}"
```

Use:

```python
re.fullmatch(pattern, password)
```

## Simple date format DD-MM-YYYY

```python
pattern = r"\d{2}-\d{2}-\d{4}"
```

This checks **format only**, not whether the date is real. Use `datetime.strptime()` for actual date validation.

## `fullmatch`, `search`, `match`

### `re.fullmatch()`

Entire string must match.

Best choice for most input validation.

```python
re.fullmatch(pattern, value)
```

### `re.search()`

Find the pattern anywhere in the string.

```python
re.search(pattern, value)
```

### `re.match()`

Checks from the start of the string.

```python
re.match(pattern, value)
```

## Capture groups

```python
pattern = r"^(\w+)@([\w.-]+)$"
match = re.search(pattern, email)

if match:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
```

```text
group(0) → entire match
group(1) → first capture group
group(2) → second capture group
```

## Find all matches

```python
numbers = re.findall(r"\d+", "Prices: 100, 250, 500")
```

Result:

```python
['100', '250', '500']
```

## Regex substitution

```python
cleaned = re.sub(r"\s+", " ", "Hello     World")
```

Result:

```text
Hello World
```

---

# 11. JSON File Handling

Import:

```python
import json
```

JSON is an excellent choice for small-to-medium file-based CRUD practicals.

## Python → JSON file

```python
data = [
    {"id": 1, "name": "Rahul"}
]

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
```

## JSON file → Python

```python
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```

## `dump` vs `dumps`

```text
dump   → Python object to JSON file
dumps  → Python object to JSON string
```

```python
json.dump(data, file)
json_string = json.dumps(data)
```

## `load` vs `loads`

```text
load   → JSON file to Python object
loads  → JSON string to Python object
```

```python
data = json.load(file)
data = json.loads(json_string)
```

### Memory trick

```text
dump  → file
dumps → string
load  → file
loads → string
```

## Robust JSON load function

```python
FILE = "data.json"


def load_data():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Invalid JSON file.")
        return []
```

## Save function

```python
def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
```

### JSON CRUD flow

```text
load_data()
    ↓
modify list/dictionaries
    ↓
save_data(data)
```

This is the simplest reliable file-based CRUD pattern.

---

# 12. CSV File Handling

Import:

```python
import csv
```

CSV is good for tabular data.

Example:

```text
id,name,age
1,Rahul,21
2,Amit,22
```

## Write CSV using `DictWriter`

```python
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["id", "name", "age"]
    )
    writer.writeheader()
    writer.writerows(data)
```

## Read CSV using `DictReader`

```python
with open("students.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
```

CSV values are normally strings after reading:

```python
age = int(student["age"])
price = float(student["price"])
```

## `reader` vs `DictReader`

`reader`:

```python
for row in csv.reader(file):
    print(row)
```

Example:

```python
['1', 'Rahul', '21']
```

`DictReader`:

```python
reader = csv.DictReader(file)

for row in reader:
    print(row["name"])
```

For management systems, `DictReader` / `DictWriter` is often easier.

## Append CSV

```python
with open("students.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["id", "name", "age"]
    )
    writer.writerow({
        "id": 3,
        "name": "Raj",
        "age": 23
    })
```

---

# 13. Text File Handling

## File modes

| Mode | Meaning |
|---|---|
| `r` | read |
| `w` | write / overwrite |
| `a` | append |
| `x` | create new file |
| `b` | binary mode |
| `+` | read/write combination |

## Write

```python
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
```

## Read all

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

## Read lines

```python
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
```

## Process line by line

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

## Always prefer `with open()`

```python
with open("data.txt", "r") as f:
    data = f.read()
```

The context manager closes the file automatically.

---

# 14. Files and Directories

## `os`

```python
import os
```

Useful calls:

```python
os.path.exists("data.json")
os.path.isfile("data.json")
os.path.isdir("data")
os.makedirs("data", exist_ok=True)
os.remove("data.txt")
```

## `pathlib`

Modern and convenient:

```python
from pathlib import Path

path = Path("data.json")

if path.exists():
    print("Exists")
```

Create folder:

```python
Path("data").mkdir(exist_ok=True)
```

---

# 15. OOP for CRUD Projects

For most CRUD practicals, focus on:

```text
class
object
__init__
self
instance attributes
methods
inheritance
super()
@property
classmethod
staticmethod
custom exceptions
```

## Basic class

```python
class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def display(self):
        print(self.student_id, self.name, self.age)
```

Create object:

```python
s1 = Student(1, "Rahul", 21)
s1.display()
```

## What is `self`?

`self` refers to the current object.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

## Class vs object

```text
class  → blueprint
a1     → actual object / instance
```

## Encapsulation conventions

```python
self._balance
```

Common convention for internal/protected-like use.

```python
self.__balance
```

Name-mangled private-style attribute.

## Property

Useful when you want controlled access to an attribute:

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value
```

## Inheritance

```python
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
```

## Static method

Does not require object/class state:

```python
class Validator:
    @staticmethod
    def is_positive(value):
        return value > 0
```

Use:

```python
Validator.is_positive(10)
```

## Class method

Works with the class:

```python
class Student:
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count
```

---

# 16. Custom Exceptions

When the question explicitly asks for custom exceptions, define them yourself:

```python
class TransactionError(Exception):
    pass
```

Raise:

```python
raise TransactionError("Insufficient balance")
```

Catch:

```python
try:
    perform_transaction()
except TransactionError as e:
    print(e)
```

Multiple custom exceptions:

```python
class AccountNotFoundError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


class InvalidAmountError(Exception):
    pass
```

This makes business-rule errors easier to understand.

---

# 17. Exception Handling

## Common exception hierarchy to know

```text
Exception
├── ValueError
├── TypeError
├── KeyError
├── IndexError
├── FileNotFoundError
├── ZeroDivisionError
├── AttributeError
├── NameError
├── ImportError
├── ModuleNotFoundError
├── PermissionError
└── OSError
```

## What they usually mean

### `ValueError`

Correct data type, invalid value.

```python
int("abc")
```

### `TypeError`

Incompatible/wrong type.

```python
"10" + 5
```

### `KeyError`

Dictionary key does not exist.

```python
student["salary"]
```

Safer:

```python
student.get("salary")
```

### `IndexError`

List index does not exist.

```python
items[100]
```

### `FileNotFoundError`

A requested file does not exist.

### `ZeroDivisionError`

```python
10 / 0
```

### `AttributeError`

An object does not have the attribute you tried to access.

### `NameError`

A variable/name does not exist.

## Full try/except structure

```python
try:
    result = 10 / number
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid value")
else:
    print("Success:", result)
finally:
    print("Operation finished")
```

Remember:

```text
try      → risky operation
except   → handle error
else     → runs if no exception
finally  → runs whether error happened or not
```

## Multiple exceptions

```python
try:
    value = int(input("Number: "))
    result = 100 / value
except (ValueError, ZeroDivisionError):
    print("Invalid input")
```

## Avoid this

```python
try:
    ...
except:
    pass
```

It can hide important bugs.

Prefer:

```python
except ValueError as e:
    print("Invalid value:", e)
```

---

# 18. Input Validation Helpers

These small functions can make your entire CRUD application cleaner.

## Safe integer input

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")
```

## Safe float input

```python
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number.")
```

## Required string

```python
def get_required_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Value cannot be empty.")
```

## Positive number

```python
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Must be greater than zero.")
                continue
            return value
        except ValueError:
            print("Enter a valid number.")
```

## Yes/No input

```python
def get_yes_no(prompt):
    while True:
        value = input(prompt).strip().lower()

        if value in ("yes", "y"):
            return True
        if value in ("no", "n"):
            return False

        print("Enter yes or no.")
```

## Email validator

```python
import re


def is_valid_email(email):
    pattern = r"[\w.-]+@[\w.-]+\.\w+"
    return re.fullmatch(pattern, email) is not None
```

## Phone validator

```python
def is_valid_phone(phone):
    return re.fullmatch(r"[6-9]\d{9}", phone) is not None
```

---

# 19. CRUD Patterns

## CREATE pattern

```text
Get input
    ↓
Validate
    ↓
Check duplicate/constraints
    ↓
Create record
    ↓
Append / INSERT
    ↓
Save / COMMIT
```

Example:

```python
def add_student():
    data = load_data()

    student_id = get_int("ID: ")

    if any(s["id"] == student_id for s in data):
        print("ID already exists")
        return

    name = get_required_string("Name: ")

    student = {
        "id": student_id,
        "name": name
    }

    data.append(student)
    save_data(data)
    print("Student added successfully")
```

## READ pattern

```python
def view_students():
    data = load_data()

    if not data:
        print("No records found")
        return

    for student in data:
        print(student)
```

## SEARCH pattern

```python
def search_student():
    data = load_data()
    student_id = get_int("Enter ID: ")

    for student in data:
        if student["id"] == student_id:
            print(student)
            return

    print("Student not found")
```

## UPDATE pattern

```python
def update_student():
    data = load_data()
    student_id = get_int("Enter ID: ")

    for student in data:
        if student["id"] == student_id:
            new_name = input("New name (Enter to keep old): ").strip()

            if new_name:
                student["name"] = new_name

            save_data(data)
            print("Updated")
            return

    print("Student not found")
```

## DELETE pattern

```python
def delete_student():
    data = load_data()
    student_id = get_int("Enter ID: ")

    for student in data:
        if student["id"] == student_id:
            data.remove(student)
            save_data(data)
            print("Deleted")
            return

    print("Student not found")
```

## Delete using list comprehension

```python
old_length = len(data)

data = [
    student
    for student in data
    if student["id"] != student_id
]

if len(data) < old_length:
    save_data(data)
    print("Deleted")
else:
    print("Not found")
```

## Generic search

```python
def find_record(data, key, value):
    for record in data:
        if record.get(key) == value:
            return record
    return None
```

## Generic delete

```python
def delete_record(data, key, value):
    for record in data:
        if record.get(key) == value:
            data.remove(record)
            return True
    return False
```

## Partial update

For optional changes:

```python
new_value = input("New value: ").strip()

if new_value:
    record["field"] = new_value
```

Do not overwrite valid data with a blank value unless the requirement explicitly says so.

---

# 20. Searching, Filtering and Sorting

## Case-insensitive search

```python
query = input("Search: ").strip().lower()

results = [
    student
    for student in students
    if query in student["name"].lower()
]
```

## Filter by condition

```python
results = [
    s for s in students
    if s["age"] >= 18 and s["marks"] >= 60
]
```

## Sort by name

```python
students.sort(key=lambda x: x["name"])
```

## Sort descending by marks

```python
students.sort(
    key=lambda x: x["marks"],
    reverse=True
)
```

## `sort()` vs `sorted()`

```python
data.sort()
```

Changes original list.

```python
new_data = sorted(data)
```

Returns a new list.

## Lambda

```python
lambda x: x["price"]
```

means:

> Take `x` and return its `price`.

## `map()`

```python
names = list(map(lambda x: x["name"], students))
```

Equivalent simple comprehension:

```python
names = [x["name"] for x in students]
```

## `filter()`

```python
expensive = list(
    filter(
        lambda x: x["price"] > 1000,
        products
    )
)
```

Often easier:

```python
expensive = [x for x in products if x["price"] > 1000]
```

## Aggregation

Total:

```python
total = sum(x["price"] for x in products)
```

Average:

```python
average = sum(x["marks"] for x in students) / len(students)
```

Protect empty lists:

```python
if students:
    average = sum(x["marks"] for x in students) / len(students)
else:
    average = 0
```

Maximum:

```python
highest = max(students, key=lambda x: x["marks"])
```

Minimum:

```python
lowest = min(students, key=lambda x: x["marks"])
```

## `any()` and `all()`

At least one:

```python
if any(s["marks"] > 90 for s in students):
    print("Someone scored above 90")
```

All:

```python
if all(s["marks"] >= 40 for s in students):
    print("Everyone passed")
```

## `enumerate()`

```python
for i, student in enumerate(students, start=1):
    print(i, student)
```

## `zip()`

```python
names = ["A", "B", "C"]
marks = [80, 90, 70]

for name, mark in zip(names, marks):
    print(name, mark)
```

## Set for duplicate detection

```python
seen = set()

for student in students:
    email = student["email"]

    if email in seen:
        print("Duplicate email")

    seen.add(email)
```

---

# 21. CLI Table Display

## Manual table — no external package

```python
def display_students(students):
    print("-" * 50)
    print(f"{'ID':<5}{'Name':<20}{'Age':<10}")
    print("-" * 50)

    for student in students:
        print(
            f"{student['id']:<5}"
            f"{student['name']:<20}"
            f"{student['age']:<10}"
        )

    print("-" * 50)
```

## Alignment

```text
<  → left
>  → right
^  → center
```

## Number formatting

```python
price = 12345.678
print(f"{price:.2f}")
```

Output:

```text
12345.68
```

## Wider table

```python
print(
    f"{'ID':<5}"
    f"{'NAME':<20}"
    f"{'EMAIL':<30}"
    f"{'PRICE':>10}"
)

for item in data:
    print(
        f"{item['id']:<5}"
        f"{item['name']:<20}"
        f"{item['email']:<30}"
        f"{item['price']:>10.2f}"
    )
```

## `tabulate` (only when allowed/installed)

```python
from tabulate import tabulate

print(tabulate(data, headers="keys", tablefmt="grid"))
```

For exams, manual formatting is safer when external packages are not guaranteed.

---

# 22. Dates and Times

Import:

```python
from datetime import datetime, date, timedelta
```

Current date/time:

```python
now = datetime.now()
```

Format:

```python
now.strftime("%d-%m-%Y")
```

Parse:

```python
date_obj = datetime.strptime(
    "09-09-2026",
    "%d-%m-%Y"
)
```

Add one day:

```python
tomorrow = datetime.now() + timedelta(days=1)
```

Important format symbols:

```text
%d → day
%m → month
%Y → 4-digit year
%H → hour
%M → minute
%S → second
```

Example:

```python
"%d-%m-%Y %H:%M:%S"
```

## Actual date validation

Regex checks only shape. For real calendar validation:

```python
try:
    date_obj = datetime.strptime(value, "%d-%m-%Y")
except ValueError:
    print("Invalid date")
```

---

# 23. SQLite for Hard-Level CRUD

When the question says:

```text
database
SQLite
SQL
transactions
audit log
foreign key
accounts
persistent records
```

SQLite is often the natural solution.

Import:

```python
import sqlite3
```

## Connection

```python
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
```

## Create table

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
)
""")

conn.commit()
```

## INSERT

Always use parameterized SQL:

```python
cursor.execute(
    """
    INSERT INTO students (name, age, email)
    VALUES (?, ?, ?)
    """,
    (name, age, email)
)

conn.commit()
```

Avoid building SQL using string concatenation or f-strings with user data.

## SELECT

```python
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
```

One row:

```python
row = cursor.fetchone()
```

## UPDATE

```python
cursor.execute(
    """
    UPDATE students
    SET name = ?, age = ?
    WHERE id = ?
    """,
    (name, age, student_id)
)

conn.commit()
```

## DELETE

```python
cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (student_id,)
)

conn.commit()
```

Note the trailing comma:

```python
(student_id,)
```

That is a one-item tuple.

## Row factory

```python
conn.row_factory = sqlite3.Row
```

Then:

```python
row["name"]
row["age"]
```

instead of numeric indexes.

## Foreign keys

Typical relationship:

```sql
FOREIGN KEY (student_id)
REFERENCES students(id)
```

Useful for:

```text
Customer → Orders
Account → Transactions
Department → Employees
```

---

# 24. Transactions and Rollback

Transaction logic is essential for banking and other multi-step operations.

Example transfer:

```text
Check source account
        ↓
Check destination account
        ↓
Validate amount
        ↓
Check sufficient balance
        ↓
Subtract source
        ↓
Add destination
        ↓
Write audit log
        ↓
COMMIT
```

If anything fails:

```text
ROLLBACK
```

## Generic pattern

```python
try:
    cursor.execute(...)  # step 1
    cursor.execute(...)  # step 2
    cursor.execute(...)  # audit

    conn.commit()

except Exception:
    conn.rollback()
    raise
```

Remember:

```text
commit()   → save transaction
rollback() → undo uncommitted changes
```

## Banking validation order

For a transfer:

```text
1. Source account exists?
2. Destination account exists?
3. Amount is valid?
4. Source != destination?
5. Source has enough balance?
6. Perform all updates inside one transaction.
7. Commit only after all steps succeed.
```

---

# 25. Useful Python Modules

## Most important for CRUD

```python
import json
import csv
import re
import copy
import sqlite3
import os
import logging

from datetime import datetime, date, timedelta
from pathlib import Path
```

## Other useful standard-library modules

```python
import sys
import math
import random
import secrets
```

### What to use when

| Requirement | Module / feature |
|---|---|
| JSON storage | `json` |
| CSV storage | `csv` |
| Regex validation | `re` |
| Deep copy | `copy` |
| Database | `sqlite3` |
| Dates | `datetime` |
| Files/folders | `pathlib`, `os` |
| Logging | `logging` |
| Program exit | `sys` |
| Math utilities | `math` |
| Simple randomness | `random` |
| Security-sensitive random tokens | `secrets` |

---

# 26. Debugging Strategy

When a CRUD program fails, do not randomly change code.

## Step 1 — inspect the type

```python
print(type(data))
```

## Step 2 — inspect the actual value

```python
print(data)
```

## Step 3 — inspect a record

```python
print(record)
print(type(record))
```

## Step 4 — inspect dictionary keys

```python
print(record.keys())
```

## Step 5 — trace important variables

```python
print("DEBUG:", variable)
```

## Step 6 — identify where the data changed

Example:

```text
input
 ↓
conversion
 ↓
validation
 ↓
CRUD function
 ↓
list/dict
 ↓
save
```

Find the first stage where the result is wrong.

## Data type checkpoints

Remember what each layer returns:

```text
input()       → str
int(...)      → int
float(...)    → float
json.load()   → Python objects
csv.DictReader→ dictionaries, usually string values
fetchall()    → list of rows/tuples (or Row objects)
```

Many bugs are simply **type misunderstandings**.

---

# 27. Common Errors and Fixes

## `KeyError: 'id'`

Your dictionary does not have the expected key.

Check:

```python
print(record)
print(record.keys())
```

Safer access:

```python
record.get("id")
```

## `ValueError: invalid literal for int()`

You tried:

```python
int("abc")
```

Use `try/except ValueError`.

## `FileNotFoundError`

The file does not exist.

Handle it:

```python
except FileNotFoundError:
    data = []
```

## `json.JSONDecodeError`

JSON content is invalid, malformed or empty.

```python
except json.JSONDecodeError:
    data = []
```

## `TypeError: list indices must be integers`

You likely did:

```python
data["name"]
```

when `data` is a list.

Maybe you needed:

```python
data[0]["name"]
```

## `IndexError`

You accessed a list index that does not exist.

## `ZeroDivisionError`

Check for an empty list / zero divisor before division.

```python
if values:
    average = sum(values) / len(values)
```

## `AttributeError`

You called an attribute/method that the object does not have.

Check:

```python
print(type(obj))
```

## `NameError`

A variable is not defined or is misspelled.

## `PermissionError`

The operating system denied file access.

---

# 28. Hard-Level Project Architecture

For a more complex project, think in layers:

```text
                  ┌───────────────────┐
                  │       main()      │
                  └─────────┬─────────┘
                            │
                       ┌────▼────┐
                       │   MENU  │
                       └────┬────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
      VALIDATION           CRUD          DISPLAY/REPORTS
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ▼
                     BUSINESS LOGIC
                            │
                            ▼
                       DATA LAYER
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
            JSON           CSV         SQLite
                            │
                            ▼
                     ERROR HANDLING
```

## Separate responsibilities

Instead of one 150-line function:

```python
def add_student():
    ...
```

split into reusable pieces:

```python
def get_student_details():
    ...


def validate_student(student):
    ...


def save_student(student):
    ...
```

Then:

```python
def add_student():
    data = load_data()
    student = get_student_details()
    validate_student(student)
    data.append(student)
    save_data(data)
```

This makes debugging much easier.

---

# 29. Question-to-Code Translation

This is one of the most important practical skills.

## Requirement: "User can add a student."

Think:

```python
def add_student():
    pass
```

## Requirement: "Email must be valid."

Think:

```python
if not is_valid_email(email):
    print("Invalid email")
    return
```

## Requirement: "ID must be unique."

Think:

```python
if find_by_id(data, student_id):
    print("Duplicate ID")
    return
```

## Requirement: "Student can be updated."

Think:

```text
get ID
 ↓
find record
 ↓
if missing → error
 ↓
get new values
 ↓
validate
 ↓
modify
 ↓
save
```

## Requirement: "Withdrawal allowed only when balance is sufficient."

Think:

```python
if amount > balance:
    raise InsufficientBalanceError("Insufficient balance")
```

## Requirement: "Transaction log must be maintained."

Think:

```python
add_transaction(...)
```

## Requirement: "Data must survive program restart."

Think:

```text
JSON / CSV / SQLite
```

### Key language mapping

Whenever a question says:

```text
must
cannot
only if
provided that
required
unique
```

translate it mentally to:

```python
if condition:
    allow
else:
    reject
```

---

# 30. Practical Exam Workflow

When you receive a difficult practical question, **do not start coding immediately**.

## Phase 1 — Extract requirements

Write down:

```text
Entities
Fields
CRUD operations
Special operations
Validation rules
Storage type
Relationships
Exceptions
Output requirements
```

## Phase 2 — Design the data

Example:

```python
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 50000,
        "stock": 10
    }
]
```

## Phase 3 — Build skeleton

```python
def load_data():
    pass


def save_data(data):
    pass


def add():
    pass


def view():
    pass


def search():
    pass


def update():
    pass


def delete():
    pass


def main():
    pass
```

## Phase 4 — Make CRUD work

Implement:

```text
CREATE
READ
SEARCH
UPDATE
DELETE
```

before worrying about cosmetic improvements.

## Phase 5 — Add validation

Add:

```text
required fields
ID uniqueness
numeric ranges
regex
business rules
```

## Phase 6 — Add special business logic

Examples:

```text
deposit
withdraw
transfer
issue book
return book
place order
cancel order
calculate bill
calculate salary
```

## Phase 7 — Add error handling

Use:

```text
try
except
raise
custom exceptions
```

## Phase 8 — Improve presentation

Add:

```text
menus
tables
success messages
error messages
sorting
filtering
statistics
```

## Phase 9 — Test edge cases

Do not stop after the happy path.

---

# 31. Testing Checklist

## CREATE

```text
✓ Valid record
✓ Duplicate ID
✓ Empty required field
✓ Invalid email
✓ Invalid phone
✓ Invalid number
✓ Negative values
✓ Zero values
```

## READ

```text
✓ Records exist
✓ No records
```

## SEARCH

```text
✓ Existing ID
✓ Non-existing ID
✓ Partial name
✓ Upper/lowercase search
```

## UPDATE

```text
✓ Existing ID
✓ Non-existing ID
✓ Valid new data
✓ Invalid new data
✓ Empty optional update
```

## DELETE

```text
✓ Existing ID
✓ Non-existing ID
```

## FILES

```text
✓ File exists
✓ File does not exist
✓ Empty JSON
✓ Corrupt JSON
✓ CSV values converted correctly
```

## DATABASE

```text
✓ Duplicate primary key
✓ Missing foreign key
✓ Failed transaction
✓ Rollback
✓ Commit
```

---

# 32. Ultimate Emergency Cheat Sheet

This is the section to revise immediately before a practical.

```python
# ===============================
# IMPORTANT IMPORTS
# ===============================
import json
import csv
import re
import copy
import sqlite3
import os
import logging

from datetime import datetime, date, timedelta
from pathlib import Path


# ===============================
# DICTIONARY
# ===============================
record = {
    "id": 1,
    "name": "Rahul"
}

record.get("name")
record["name"] = "Amit"
record["email"] = "a@example.com"


# ===============================
# LIST OF DICTS
# ===============================
data = []
data.append(record)

for x in data:
    print(x)


# ===============================
# FIND
# ===============================
found = next(
    (x for x in data if x["id"] == 1),
    None
)


# ===============================
# SORT
# ===============================
data.sort(key=lambda x: x["name"])
data.sort(key=lambda x: x["id"], reverse=True)


# ===============================
# FILTER
# ===============================
result = [
    x for x in data
    if x["id"] > 5
]


# ===============================
# JSON READ
# ===============================
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)


# ===============================
# JSON WRITE
# ===============================
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)


# ===============================
# CSV READ
# ===============================
with open("data.csv", "r", newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f))


# ===============================
# CSV WRITE
# ===============================
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["id", "name"]
    )
    writer.writeheader()
    writer.writerows(data)


# ===============================
# REGEX
# ===============================
if re.fullmatch(r"[6-9]\d{9}", phone):
    print("Valid phone")

if re.fullmatch(r"[\w.-]+@[\w.-]+\.\w+", email):
    print("Valid email")

numbers = re.findall(r"\d+", text)
cleaned = re.sub(r"\s+", " ", text)


# ===============================
# SAFE INPUT
# ===============================
try:
    value = int(input("Number: "))
except ValueError:
    print("Invalid number")


# ===============================
# CUSTOM EXCEPTION
# ===============================
class MyError(Exception):
    pass

raise MyError("Something went wrong")


# ===============================
# COPY
# ===============================
b = copy.copy(a)
b = copy.deepcopy(a)


# ===============================
# DATE
# ===============================
now = datetime.now()
formatted = now.strftime("%d-%m-%Y")
d = datetime.strptime("09-09-2026", "%d-%m-%Y")


# ===============================
# SQLITE
# ===============================
conn = sqlite3.connect("app.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

conn.commit()
conn.rollback()


# ===============================
# CLI TABLE
# ===============================
print(f"{'ID':<5}{'NAME':<20}{'AGE':<5}")
print("-" * 30)

for x in data:
    print(
        f"{x['id']:<5}"
        f"{x['name']:<20}"
        f"{x.get('age', ''):<5}"
    )


# ===============================
# MAIN
# ===============================
if __name__ == "__main__":
    main()
```

---

# 🧠 The Most Important Problem-Solving Formula

When you see a new practical, mentally ask:

```text
QUESTION
   ↓
WHAT AM I MANAGING?
   ↓
WHAT ARE THE FIELDS?
   ↓
WHAT ARE THE OPERATIONS?
   ↓
WHAT VALIDATION IS REQUIRED?
   ↓
WHERE IS THE DATA STORED?
   ↓
WHAT BUSINESS RULES EXIST?
   ↓
WHAT CAN GO WRONG?
   ↓
HOW SHOULD THE OUTPUT LOOK?
```

Then implement:

```text
1. Data structure
2. Load
3. Save
4. Input validation
5. CREATE
6. READ
7. SEARCH
8. UPDATE
9. DELETE
10. Business operations
11. Exceptions
12. Display/reporting
13. Testing
```

---

# 🔥 The Most Important Patterns to Memorize

Do **not** try to memorize hundreds of complete projects.

Memorize these reusable patterns:

```text
List of dictionaries
        ↓
CRUD functions
        ↓
Validation helpers
        ↓
Regex validation
        ↓
JSON/CSV persistence
        ↓
Exception handling
        ↓
Search/filter/sort
        ↓
CLI table
```

For database problems:

```text
Class / functions
       ↓
Validation
       ↓
SQL CRUD
       ↓
Parameterized queries
       ↓
Transactions
       ↓
Commit / rollback
       ↓
Audit log
```

For every operation, ask:

```text
1. What is the input?
2. What validation is required?
3. Where is the data?
4. What changes?
5. What should the user see?
6. What can fail?
```

If you can answer those six questions, you can usually turn the English requirement into code.

---

# 🏆 Final Practical Strategy

A hard management-system question is usually a familiar pattern wrapped in a new story.

```text
Library
Bank
Student
Employee
Hospital
Inventory
Restaurant
Booking
```

may look very different, but underneath they are frequently built from:

```text
LIST
DICTIONARY
FUNCTIONS
CRUD
VALIDATION
REGEX
JSON / CSV / SQLITE
EXCEPTIONS
OOP BASICS
SEARCH
SORT
FILTER
DISPLAY
```

The **story changes**.

The **programming patterns mostly stay the same**.

Your goal in the practical is therefore:

> **Convert the story into data + operations + rules + storage + errors.**

Once you can do that, you are no longer trying to remember a specific "Student Management System" or "Library Management System". You are building the required system from reusable Python patterns.
