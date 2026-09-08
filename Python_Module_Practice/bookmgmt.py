catalog = [
    {
        "id": 1,
        "title": "Python Programming",
        "author": "John Zelle",
        "genre": "Technical",
        "price": 650.00,
        "copies": 15
    },
    {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert Martin",
        "genre": "Technical",
        "price": 950.00,
        "copies": 8
    }
]


# ============================================================
# MENU
# ============================================================

def menu():
    show_menu = '''
          1. Add Book
          2. View Catalog
          3. Search Books
          4. Update Details
          5. Delete Book
          6. Save to File
          7. Load from File
          8. Exit
    '''

    print("\n" + "=" * 55)
    print("        BOOK CATALOG MANAGEMENT SYSTEM")
    print("=" * 55)
    print(show_menu)

    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        choice = -1

    return choice


# ============================================================
# ADD BOOK
# ============================================================

def add_book_entry(catalog: list[dict], next_id: int) -> int:

    # Title
    title = input("Enter Book Title: ").strip()

    while title == "":
        print("Title cannot be empty.")
        title = input("Enter Book Title: ").strip()

    # Author
    author = input("Enter Book Author: ").strip()

    while author == "":
        print("Author name cannot be empty.")
        author = input("Enter Book Author: ").strip()

    # Genre
    genre = input("Enter Book Genre: ").strip()

    while genre == "":
        print("Genre cannot be empty.")
        genre = input("Enter Book Genre: ").strip()

    # Price
    while True:
        try:
            price = float(input("Enter Book Price: "))

            if price > 0:
                break

            print("Price must be greater than 0.")

        except ValueError:
            print("Invalid price. Please enter a number.")

    # Copies
    while True:
        try:
            copies = int(input("Enter Book Copies: "))

            if copies >= 0:
                break

            print("Copies cannot be negative.")

        except ValueError:
            print("Copies must be an integer.")

    # Create book
    book = {
        "id": next_id,
        "title": title,
        "author": author,
        "genre": genre,
        "price": price,
        "copies": copies
    }

    # Add to catalog
    catalog.append(book)

    print(f"\nBook added successfully with ID {next_id}.")

    # Increment ID
    next_id += 1

    return next_id


# ============================================================
# DISPLAY CATALOG
# ============================================================

def render_catalog(catalog: list[dict]) -> None:

    if len(catalog) == 0:

        print("\nCatalog is empty.")

    elif len(catalog) == 1:

        book = catalog[0]

        print("\n" + "=" * 35)
        print("           BOOK DETAILS")
        print("=" * 35)

        print(f"ID      : {book['id']}")
        print(f"Title   : {book['title']}")
        print(f"Author  : {book['author']}")
        print(f"Genre   : {book['genre']}")
        print(f"Price   : {book['price']:.2f}")
        print(f"Copies  : {book['copies']}")

        print("=" * 35)

    else:

        print("\n" + "-" * 90)

        print(
            f"{'ID':<5}"
            f"{'Title':<25}"
            f"{'Author':<20}"
            f"{'Genre':<20}"
            f"{'Price':<12}"
            f"{'Copies':<8}"
        )

        print("-" * 90)

        for book in catalog:

            print(
                f"{book['id']:<5}"
                f"{book['title']:<25}"
                f"{book['author']:<20}"
                f"{book['genre']:<20}"
                f"{book['price']:<12.2f}"
                f"{book['copies']:<8}"
            )

        print("-" * 90)


# ============================================================
# SEARCH BOOKS
# ============================================================

def query_books(catalog: list[dict], search_term: str) -> list[dict]:

    results = []

    search_term = search_term.lower().strip()

    for book in catalog:

        # Search by ID
        if search_term.isdigit():

            if book["id"] == int(search_term):
                results.append(book)

        # Search by title or author
        else:

            if (
                search_term in book["title"].lower()
                or search_term in book["author"].lower()
            ):
                results.append(book)

    return results


# ============================================================
# UPDATE BOOK
# ============================================================

def modify_book_details(catalog: list[dict], book_id: int) -> bool:

    for book in catalog:

        if book["id"] == book_id:

            # New price
            while True:

                try:
                    new_price = float(
                        input("Enter new Price: ")
                    )

                    if new_price > 0:
                        break

                    print("Price must be greater than 0.")

                except ValueError:
                    print("Invalid price.")

            # New copies
            while True:

                try:
                    new_copies = int(
                        input("Enter new copies: ")
                    )

                    if new_copies >= 0:
                        break

                    print("Copies cannot be negative.")

                except ValueError:
                    print("Copies must be an integer.")

            # Update dictionary
            book["price"] = new_price
            book["copies"] = new_copies

            return True

    return False


# ============================================================
# DELETE BOOK
# ============================================================

def delete_book(catalog: list[dict], book_id: int) -> bool:

    for book in catalog:

        if book["id"] == book_id:

            confirmation = input(
                f"Are you sure you want to delete "
                f"'{book['title']}'? (y/n): "
            ).strip().lower()

            if confirmation == "y":

                catalog.remove(book)

                return True

            return False

    return False


# ============================================================
# SAVE CATALOG TO FILE
# ============================================================

def sync_catalog_to_file(
    filepath: str,
    catalog: list[dict]
) -> None:

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:

        for book in catalog:

            line = (
                f"{book['id']}|"
                f"{book['title']}|"
                f"{book['author']}|"
                f"{book['genre']}|"
                f"{book['price']}|"
                f"{book['copies']}"
            )

            f.write(line + "\n")


# ============================================================
# LOAD CATALOG FROM FILE
# ============================================================

def load_catalog_from_file(
    filepath: str
) -> list[dict]:

    catalog = []

    try:

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:

            for line in f:

                line = line.strip()

                if not line:
                    continue

                parts = line.split("|")

                book = {
                    "id": int(parts[0]),
                    "title": parts[1],
                    "author": parts[2],
                    "genre": parts[3],
                    "price": float(parts[4]),
                    "copies": int(parts[5])
                }

                catalog.append(book)

    except FileNotFoundError:

        print("File does not exist.")

    return catalog


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    global catalog

    # Current IDs are 1 and 2
    next_id = 3

    while True:

        choice = menu()

        match choice:

            # ------------------------------------------------
            # 1. ADD BOOK
            # ------------------------------------------------

            case 1:

                next_id = add_book_entry(
                    catalog,
                    next_id
                )

            # ------------------------------------------------
            # 2. VIEW CATALOG
            # ------------------------------------------------

            case 2:

                render_catalog(catalog)

            # ------------------------------------------------
            # 3. SEARCH BOOKS
            # ------------------------------------------------

            case 3:

                search_term = input(
                    "Search for the Book: "
                )

                results = query_books(
                    catalog,
                    search_term
                )

                if len(results) == 0:
                    print("No books found.")
                else:
                    render_catalog(results)

            # ------------------------------------------------
            # 4. UPDATE DETAILS
            # ------------------------------------------------

            case 4:

                try:

                    book_id = int(
                        input("Enter the Book ID: ")
                    )

                    success = modify_book_details(
                        catalog,
                        book_id
                    )

                    if success:
                        print("Book details updated successfully.")
                    else:
                        print("Book ID not found.")

                except ValueError:

                    print("Book ID must be an integer.")

            # ------------------------------------------------
            # 5. DELETE BOOK
            # ------------------------------------------------

            case 5:

                try:

                    book_id = int(
                        input("Enter the Book ID: ")
                    )

                    success = delete_book(
                        catalog,
                        book_id
                    )

                    if success:
                        print("Book deleted successfully.")
                    else:
                        print("Book not found or deletion cancelled.")

                except ValueError:

                    print("Book ID must be an integer.")

            # ------------------------------------------------
            # 6. SAVE TO FILE
            # ------------------------------------------------

            case 6:

                filepath = input(
                    "Enter the File Path: "
                ).strip()

                try:

                    sync_catalog_to_file(
                        filepath,
                        catalog
                    )

                    print("Catalog saved successfully.")

                except OSError as e:

                    print(f"Error saving file: {e}")

            # ------------------------------------------------
            # 7. LOAD FROM FILE
            # ------------------------------------------------

            case 7:

                filepath = input(
                    "Enter the File Path: "
                ).strip()

                loaded_catalog = load_catalog_from_file(
                    filepath
                )

                if loaded_catalog:

                    catalog = loaded_catalog

                    # Make next ID one greater than largest existing ID
                    next_id = max(
                        book["id"]
                        for book in catalog
                    ) + 1

                    print("Catalog loaded successfully.")

                else:

                    print("No catalog loaded.")

            # ------------------------------------------------
            # 8. EXIT
            # ------------------------------------------------

            case 8:

                print("Exiting program...")
                break

            # ------------------------------------------------
            # INVALID CHOICE
            # ------------------------------------------------

            case _:

                print(
                    "Invalid choice. "
                    "Please enter a number from 1 to 8."
                )


# ============================================================
# PROGRAM START
# ============================================================

main()