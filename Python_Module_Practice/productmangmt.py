# ============================================================
# PRODUCT INVENTORY MANAGEMENT SYSTEM
# ============================================================

# We do not need any external modules for this problem.
# The entire program can be built using basic Python concepts.


# ============================================================
# SAMPLE PRODUCT DATA
# ============================================================

# The inventory is stored as a LIST of DICTIONARIES.
#
# Each dictionary represents ONE product.
#
# Example:
# products[0] gives the first product
# products[0]["name"] gives the name of the first product

products = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "Electronics",
        "price": 55000.0,
        "quantity": 10
    },
    {
        "id": 2,
        "name": "Smartphone",
        "category": "Electronics",
        "price": 20000.0,
        "quantity": 25
    },
    {
        "id": 3,
        "name": "Chair",
        "category": "Furniture",
        "price": 1500.0,
        "quantity": 50
    },
    {
        "id": 4,
        "name": "Notebook",
        "category": "Stationery",
        "price": 50.0,
        "quantity": 200
    },
    {
        "id": 5,
        "name": "Bottle",
        "category": "Accessories",
        "price": 300.0,
        "quantity": 80
    }
]


# ============================================================
# 1. DISPLAY MENU
# ============================================================

def menu():
    """
    Display the menu and return the user's choice.
    """

    print("\n" + "=" * 60)
    print("         PRODUCT INVENTORY MANAGEMENT SYSTEM")
    print("=" * 60)

    print("""
1. Add Product
2. View All Products
3. Search Product
4. Update Product
5. Delete Product
6. Exit
""")

    # input() always returns a string.
    # We convert it to an integer because menu choices
    # are expected to be numbers.
    try:
        choice = int(input("Enter your choice: "))
        return choice

    # If the user enters something like:
    # abc
    # hello
    # one
    # int() will raise ValueError.
    except ValueError:
        print("Invalid choice. Please enter a number.")
        return -1


# ============================================================
# 2. ADD PRODUCT
# ============================================================

def add_product(products, next_id):
    """
    Add a new product to the inventory.

    Parameters:
        products -> list containing all products
        next_id  -> ID to assign to the new product

    Returns:
        next available ID
    """

    # --------------------------------------------------------
    # GET PRODUCT NAME
    # --------------------------------------------------------

    name = input("Enter product name: ").strip()

    # Name cannot be empty.
    # Keep asking until the user provides a valid name.
    while name == "":
        print("Product name cannot be empty.")
        name = input("Enter product name: ").strip()


    # --------------------------------------------------------
    # GET PRODUCT CATEGORY
    # --------------------------------------------------------

    category = input("Enter product category: ").strip()

    # Category cannot be empty.
    while category == "":
        print("Product category cannot be empty.")
        category = input("Enter product category: ").strip()


    # --------------------------------------------------------
    # GET PRODUCT PRICE
    # --------------------------------------------------------

    while True:

        try:
            # Convert input from string to float.
            price = float(input("Enter product price: "))

            # Price must be greater than 0.
            if price > 0:
                break

            print("Price must be greater than 0.")

        # Handles input such as "abc".
        except ValueError:
            print("Price must be a number.")


    # --------------------------------------------------------
    # GET PRODUCT QUANTITY
    # --------------------------------------------------------

    while True:

        try:
            # Convert input from string to integer.
            quantity = int(input("Enter product quantity: "))

            # Quantity can be zero, but cannot be negative.
            if quantity >= 0:
                break

            print("Quantity cannot be negative.")

        except ValueError:
            print("Quantity must be an integer.")


    # --------------------------------------------------------
    # CREATE PRODUCT DICTIONARY
    # --------------------------------------------------------

    product = {
        "id": next_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }


    # --------------------------------------------------------
    # ADD PRODUCT TO LIST
    # --------------------------------------------------------

    products.append(product)


    # --------------------------------------------------------
    # SUCCESS MESSAGE
    # --------------------------------------------------------

    print(
        f"Product added successfully. "
        f"Product ID: {next_id}"
    )


    # Increase ID so the next product gets a unique ID.
    next_id += 1

    return next_id


# ============================================================
# 3. VIEW ALL PRODUCTS
# ============================================================

def view_products(products):
    """
    Display all products in a formatted table.
    """

    # --------------------------------------------------------
    # CHECK IF INVENTORY IS EMPTY
    # --------------------------------------------------------

    if len(products) == 0:
        print("Inventory is empty.")
        return


    # --------------------------------------------------------
    # PRINT TABLE HEADER
    # --------------------------------------------------------

    print("\n" + "-" * 85)

    print(
        f"{'ID':<5}"
        f"{'Name':<25}"
        f"{'Category':<20}"
        f"{'Price':<15}"
        f"{'Quantity':<10}"
    )

    print("-" * 85)


    # --------------------------------------------------------
    # PRINT EVERY PRODUCT
    # --------------------------------------------------------

    for product in products:

        print(
            f"{product['id']:<5}"
            f"{product['name']:<25}"
            f"{product['category']:<20}"
            f"{product['price']:<15.2f}"
            f"{product['quantity']:<10}"
        )


    # Bottom border
    print("-" * 85)


# ============================================================
# 4. SEARCH PRODUCT
# ============================================================

def search_products(products, search_term):
    """
    Search for products using:
        - Product ID
        - OR Product Name

    Returns:
        List of matching products
    """

    # List to store matching products.
    results = []

    # Remove extra spaces and make the search
    # case-insensitive.
    search_term = search_term.strip().lower()


    # --------------------------------------------------------
    # SEARCH THROUGH ALL PRODUCTS
    # --------------------------------------------------------

    for product in products:

        # ----------------------------------------------------
        # SEARCH BY PRODUCT ID
        # ----------------------------------------------------

        # isdigit() checks whether search_term contains
        # only digits.
        #
        # Example:
        # "3".isdigit() -> True
        # "laptop".isdigit() -> False

        if search_term.isdigit():

            # Convert search string to integer.
            if product["id"] == int(search_term):

                results.append(product)


        # ----------------------------------------------------
        # SEARCH BY PRODUCT NAME
        # ----------------------------------------------------

        else:

            # "in" performs substring matching.
            #
            # Example:
            # "lap" in "laptop" -> True

            if search_term in product["name"].lower():

                results.append(product)


    # Return all matching products.
    return results


# ============================================================
# 5. UPDATE PRODUCT
# ============================================================

def update_product(products, product_id):
    """
    Find a product by ID and update:
        - name
        - category
        - price
        - quantity

    Returns:
        True  -> update successful
        False -> product not found
    """

    # --------------------------------------------------------
    # FIND PRODUCT
    # --------------------------------------------------------

    for product in products:

        if product["id"] == product_id:


            # ------------------------------------------------
            # UPDATE NAME
            # ------------------------------------------------

            name = input("Enter new product name: ").strip()

            while name == "":
                print("Product name cannot be empty.")
                name = input(
                    "Enter new product name: "
                ).strip()


            # ------------------------------------------------
            # UPDATE CATEGORY
            # ------------------------------------------------

            category = input(
                "Enter new product category: "
            ).strip()

            while category == "":
                print("Product category cannot be empty.")

                category = input(
                    "Enter new product category: "
                ).strip()


            # ------------------------------------------------
            # UPDATE PRICE
            # ------------------------------------------------

            while True:

                try:

                    price = float(
                        input("Enter new product price: ")
                    )

                    if price > 0:
                        break

                    print("Price must be greater than 0.")

                except ValueError:

                    print(
                        "Price must be a number."
                    )


            # ------------------------------------------------
            # UPDATE QUANTITY
            # ------------------------------------------------

            while True:

                try:

                    quantity = int(
                        input("Enter new product quantity: ")
                    )

                    if quantity >= 0:
                        break

                    print(
                        "Quantity cannot be negative."
                    )

                except ValueError:

                    print(
                        "Quantity must be an integer."
                    )


            # ------------------------------------------------
            # UPDATE DICTIONARY
            # ------------------------------------------------

            product["name"] = name
            product["category"] = category
            product["price"] = price
            product["quantity"] = quantity


            # Update successful.
            return True


    # Product ID was not found.
    return False


# ============================================================
# 6. DELETE PRODUCT
# ============================================================

def delete_product(products, product_id):
    """
    Delete a product using its ID.

    Returns:
        True  -> product deleted
        False -> product not found
    """

    # --------------------------------------------------------
    # SEARCH FOR PRODUCT
    # --------------------------------------------------------

    for product in products:

        if product["id"] == product_id:


            # Display the product before deleting.
            print("\nProduct Found:")
            print(f"ID       : {product['id']}")
            print(f"Name     : {product['name']}")
            print(f"Category : {product['category']}")
            print(f"Price    : {product['price']:.2f}")
            print(f"Quantity : {product['quantity']}")


            # ------------------------------------------------
            # ASK FOR CONFIRMATION
            # ------------------------------------------------

            confirmation = input(
                "Are you sure you want to delete this product? (y/n): "
            ).strip().lower()


            # ------------------------------------------------
            # DELETE PRODUCT
            # ------------------------------------------------

            if confirmation == "y":

                products.remove(product)

                print("Product deleted successfully.")

                return True


            # User did not confirm.
            print("Deletion cancelled.")

            return False


    # Product ID doesn't exist.
    return False


# ============================================================
# 7. MAIN FUNCTION
# ============================================================

def main():

    # next_id contains the ID that will be assigned
    # to the next newly added product.
    #
    # Existing IDs are 1-5,
    # so the next ID is 6.
    next_id = 6


    # --------------------------------------------------------
    # CONTINUOUS MENU LOOP
    # --------------------------------------------------------

    while True:

        # Display menu.
        choice = menu()


        # ----------------------------------------------------
        # MATCH USER'S CHOICE
        # ----------------------------------------------------

        match choice:


            # =================================================
            # OPTION 1: ADD PRODUCT
            # =================================================

            case 1:

                # add_product() returns the next available ID.
                next_id = add_product(
                    products,
                    next_id
                )


            # =================================================
            # OPTION 2: VIEW ALL PRODUCTS
            # =================================================

            case 2:

                view_products(products)


            # =================================================
            # OPTION 3: SEARCH PRODUCT
            # =================================================

            case 3:

                search_term = input(
                    "Enter Product ID or Name: "
                )

                # Search and store results.
                results = search_products(
                    products,
                    search_term
                )


                # Check whether results were found.
                if results:

                    view_products(results)

                else:

                    print("Product not found.")


            # =================================================
            # OPTION 4: UPDATE PRODUCT
            # =================================================

            case 4:

                try:

                    # Convert user input to integer.
                    product_id = int(
                        input("Enter Product ID: ")
                    )


                    # Call update function.
                    success = update_product(
                        products,
                        product_id
                    )


                    # Check whether update succeeded.
                    if success:

                        print(
                            "Product updated successfully."
                        )

                    else:

                        print(
                            "Product ID not found."
                        )


                except ValueError:

                    print(
                        "Product ID must be an integer."
                    )


            # =================================================
            # OPTION 5: DELETE PRODUCT
            # =================================================

            case 5:

                try:

                    # Get product ID.
                    product_id = int(
                        input("Enter Product ID: ")
                    )


                    # Call delete function.
                    success = delete_product(
                        products,
                        product_id
                    )


                    # If the function returned False,
                    # it means the product wasn't found
                    # or deletion was cancelled.
                    if not success:

                        print(
                            "Product ID not found."
                        )


                except ValueError:

                    print(
                        "Product ID must be an integer."
                    )


            # =================================================
            # OPTION 6: EXIT
            # =================================================

            case 6:

                print(
                    "Thank you for using the "
                    "Product Inventory Management System."
                )

                # Stop the while True loop.
                break


            # =================================================
            # INVALID OPTION
            # =================================================

            case _:

                print(
                    "Invalid choice. "
                    "Please enter a number from 1 to 6."
                )


# ============================================================
# START THE PROGRAM
# ============================================================

main()