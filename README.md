# CDAC PGCP-AI

A structured learning archive for the **CDAC PGCP-AI** program, containing daily notes, assignments, Python exercises, web-development examples, REST APIs, database practice, NumPy work, web scraping, and assessment programs.

This repository is organized as a day-by-day record of the hands-on learning completed during the course. Each `Day_XX` directory contains its own notes and workspace material where available.

## Repository Overview

| Section | Focus |
|---|---|
| `Day_01` | Python introduction, history, philosophy, syntax, data types, variables, operators, input/output |
| `Day_02` | Strings and tuples, immutability, indexing, slicing, sequence operations |
| `Day_03` | Lists, mutability, indexing/slicing, list operations and practice |
| `Day_04` | Dictionaries and exception handling |
| `Day_05` | Functions, scopes, `*args`, `**kwargs`, lambda functions, regular expressions |
| `Day_06` | Object-oriented programming, decorators, inheritance, MRO, polymorphism, encapsulation, dunder methods |
| `Day_07` | File I/O, CSV, JSON, pickle, SQLite and relational-database concepts |
| `Day_08` | Additional Python practice, serialization, database exercises, generators and supporting examples |
| `Day_09` | Web architecture, HTTP/HTTPS, design patterns, Flask, virtual environments, SQLite web applications |
| `Day_10` | REST APIs with Flask, web scraping with Requests/BeautifulSoup, NumPy and image manipulation |

There are **10 course days** in the current archive, with **190 repository paths** in total at the time this README was created.

## Learning Progression

The repository follows a practical progression from Python fundamentals to backend and data-oriented development:

```text
Python Fundamentals
        │
        ▼
Strings / Tuples / Lists / Dictionaries
        │
        ▼
Functions / Exceptions / Regular Expressions
        │
        ▼
Object-Oriented Programming
        │
        ▼
Files / JSON / CSV / Pickle / SQLite
        │
        ▼
Flask Web Applications
        │
        ▼
REST APIs + Web Scraping + NumPy
```

## What You Will Find Here

### Python Fundamentals

The first part of the archive develops core Python skills through explanations and executable exercises, including:

- Variables and data types
- Operators and expressions
- Conditional statements
- `for` and `while` loops
- Strings and tuples
- Lists and list transformations
- Dictionaries
- Functions and argument passing
- Scope and the LEGB rule
- Lambda functions and built-in helpers
- Regular expressions
- Exception handling

The daily workspaces contain small, focused scripts such as printing/input examples, conditionals, loops, string operations, list processing, dictionary practice, and reusable utility functions.

### Object-Oriented Programming

The Day 06 material covers:

- Classes and objects
- Instance vs. class variables
- `self` and object state
- `@classmethod`, `@staticmethod`, and `@property`
- Inheritance
- Multiple inheritance
- Method Resolution Order (MRO)
- `super()`
- Polymorphism and overriding
- Encapsulation and name mangling
- Dunder methods such as `__str__`, `__repr__`, `__add__`, and `__eq__`
- Iteration with `__iter__` and `__next__`

### Data Persistence

Day 07 introduces practical persistence and serialization:

- File streams and context managers
- CSV processing
- JSON serialization
- Pickle serialization
- SQLite
- Python DB-API concepts
- Creating tables, inserting records, reading records, and working with database connections

The repository also contains SQLite databases and examples used during the course, including `emps.sqlite`.

### Flask and Backend Development

The web-development section progresses from basic Flask applications to database-backed applications and REST APIs.

Examples include:

- Flask server setup
- Templates and server-side rendering
- Client/server architecture
- HTTP request/response flow
- MVC/MVT concepts
- Book management applications
- SQLite-backed Flask applications
- RESTful JSON endpoints
- CRUD-oriented API exercises

One Day 10 example implements a simple Books API:

```text
GET  /api/v1/books
POST /api/v1/books
```

The example uses Flask + SQLite and returns JSON responses.

### Web Scraping

The Day 10 scraping exercises use:

- `requests`
- `BeautifulSoup`

The included demonstration fetches quotes from `quotes.toscrape.com`, extracts quote text, author names, and tags, and returns structured Python dictionaries.

When extending these examples, respect a site's terms, robots policy, rate limits, and applicable laws.

### NumPy and Image Processing

The NumPy material introduces array-based numerical computing and demonstrates image manipulation.

The included examples cover operations such as:

- Creating NumPy arrays
- Vectorized arithmetic
- Comparing Python-list and NumPy performance
- Reading image data into arrays
- Grayscale conversion
- Cropping
- Flipping images
- Brightness/color transformations

The repository contains sample output images under the Day 10 NumPy workspace.

## Practice Projects

### Book Management

Several iterations of a Book Management application appear throughout the course.

The exercises demonstrate the evolution from basic Python data handling into file/database-backed applications and Flask-based interfaces.

### Product Inventory Management

The repository contains a standalone Product Inventory Management program with operations for:

- Add product
- View products
- Search by ID or name
- Update product
- Delete product
- Exit

Products are represented as dictionaries inside a list, making this a useful example of applying functions, loops, validation, formatted output, and CRUD-style logic using core Python.

### Grade Management

The `Python_Module_Practice/grade_management.py` project provides a larger menu-driven practice program using structured student records and JSON persistence.

### Assessment Programs

The `practice_assessment_qp/` directory contains practice question papers and a corresponding implementation for the Product Inventory Management System.

## Repository Structure

```text
CDAC-PGCP-AI/
│
├── Day_01/
├── Day_02/
├── Day_03/
├── Day_04/
├── Day_05/
├── Day_06/
├── Day_07/
├── Day_08/
├── Day_09/
├── Day_10/
│
├── Python_Module_Practice/
│   ├── bookmgmt.py
│   ├── grade_management.py
│   ├── productmangmt.py
│   └── supporting practice/readme files
│
├── practice_assessment_qp/
│   ├── Library Book Management System.pdf
│   ├── Product Inventory Management System.pdf
│   ├── Student Grade Management System.pdf
│   └── main.py
│
├── Northwind_Orders.csv
├── Python_Learning_Material.pdf
├── emps.sqlite
├── students.json
├── students.txt
└── transactions.log
```

Each day generally follows a pattern similar to:

```text
Day_XX/
├── Assignment.md
├── Assignment.pdf
├── README.md
├── README.pdf
└── workspace/
    └── exercises, projects, examples and supporting files
```

Not every day contains all of these files; the exact contents vary by session.

## Running the Examples

Most exercises are standalone Python scripts.

### Run a script

```bash
python path/to/example.py
```

For example:

```bash
python Day_01/workspace/ex01_hello.py
```

### Recommended environment

Create a virtual environment before installing third-party packages:

Windows:

```bash
python -m venv .venv
.venv\\Scripts\\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Some individual exercises have their own `requirements.txt` files. Install dependencies from the relevant project directory rather than assuming one global dependency set for the entire archive.

For example, the Day 10 web-scraping examples use Requests and BeautifulSoup, while the Flask API examples use Flask and SQLite.

## Highlights from the Course

### Day 01 — Python Foundations

The first session establishes the language fundamentals:

```python
print("Hello, World!")
```

It then progresses into variables, data types, collections, control flow, operators, input/output, and basic Python development environments.

### Day 06 — OOP

The OOP material moves beyond procedural scripts and introduces class design, inheritance, decorators, MRO, polymorphism, encapsulation, operator overloading, and custom iteration.

### Day 07 — Persistence

Python is connected to real data workflows through files, structured formats, object serialization, and SQLite.

### Day 09 — Flask

The course moves into the web stack: client/server architecture, HTTP, Flask, templates, virtual environments, and database-backed web applications.

### Day 10 — APIs, Scraping and NumPy

The archive then branches into three practical areas:

1. REST API development with Flask
2. Web scraping with Requests and BeautifulSoup
3. Numerical/image processing with NumPy

## Learning Resources Included

The repository also contains course-level resources such as:

- Daily Markdown notes
- Daily PDF notes
- Assignment statements
- Assignment PDFs
- Python learning material
- Concept diagrams
- Sample datasets
- SQLite databases
- Practice assessment papers

The daily `README.md` files are the best place to find detailed explanations for a particular session.

## Data and Generated Files

Some repository files are intentionally used as learning artifacts rather than production datasets, including:

- `Northwind_Orders.csv`
- `emps.sqlite`
- `students.json`
- `students.txt`
- `transactions.log`
- Sample images used by the NumPy exercises

Treat these files as course material and examples, not as production-ready data pipelines.

## Notes on Code Quality

This repository is primarily a **learning archive**, so the code is intentionally varied. Some scripts demonstrate concepts in isolation, while later examples combine them into small applications.

Expect to find:

- Multiple versions of similar exercises
- Educational comments and verbose explanations
- Simplified validation suitable for classroom exercises
- Development configurations such as Flask debug mode in learning examples
- Standalone scripts rather than a single installable Python package

That variation is part of the learning record.

## Suggested Learning Path

For someone using this repository to revise Python and backend fundamentals:

```text
1. Day_01  → Python basics
2. Day_02  → Strings & tuples
3. Day_03  → Lists
4. Day_04  → Dictionaries & exceptions
5. Day_05  → Functions & RegEx
6. Day_06  → OOP
7. Day_07  → Files, serialization & SQLite
8. Day_09  → Flask & web architecture
9. Day_10  → REST APIs, scraping & NumPy
10. Python_Module_Practice → larger practice programs
11. practice_assessment_qp → assessment-style problems
```

## Future Expansion

This repository can naturally grow into a broader AI/ML study archive by adding later coursework and experiments around:

- NumPy and Pandas
- SciPy
- Data visualization
- Exploratory data analysis
- Statistics
- Machine learning
- Deep learning
- Computer vision
- NLP
- Generative AI
- MLOps and deployment

The current foundation already covers many of the Python, data, web, and API skills that support those areas.

## Author

**Harshit Garg**

GitHub: https://github.com/Harshit765G4

## Disclaimer

This repository is a personal learning and coursework archive. Examples are intended for education and practice and should be reviewed, tested, and secured before being reused in production systems.
