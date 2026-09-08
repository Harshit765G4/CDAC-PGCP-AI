# ============================================================
# STUDENT GRADE & ASSESSMENT MANAGEMENT SYSTEM
# ============================================================

# json is Python's built-in module for working with JSON files.
# We need it for:
#   json.dump() -> save Python data into a JSON file
#   json.load() -> load JSON data back into Python
import json


# ============================================================
# 1. CALCULATE GRADE
# ============================================================

def calculate_grade(marks: float) -> str:
    """
    Calculate the student's grade based on marks.

    Grading rules:
        85 or above -> A
        70 to 84.99 -> B
        50 to 69.99 -> C
        Below 50    -> F

    The function returns the grade as a string.
    """

    # Check highest grade first.
    if marks >= 85:
        return "A"

    # If marks are below 85 but at least 70.
    elif marks >= 70:
        return "B"

    # If marks are below 70 but at least 50.
    elif marks >= 50:
        return "C"

    # Anything below 50 is a fail.
    else:
        return "F"


# ============================================================
# 2. ENROLL STUDENT
# ============================================================

def enroll_student(
    students: list[dict],
    next_id: int
) -> int:
    """
    Add a new student to the students list.

    Parameters:
        students -> list containing student dictionaries
        next_id  -> ID that should be assigned to the new student

    Returns:
        next available ID after adding the student
    """

    # --------------------------------------------------------
    # STEP 1: GET STUDENT NAME
    # --------------------------------------------------------

    name = input("Enter Student Name: ").strip()

    # Keep asking until a non-empty name is entered.
    while name == "":
        print("Name cannot be blank.")
        name = input("Enter Student Name: ").strip()


    # --------------------------------------------------------
    # STEP 2: GET COURSE
    # --------------------------------------------------------

    course = input("Enter Course/Module: ").strip()

    # Keep asking until a non-empty course is entered.
    while course == "":
        print("Course cannot be blank.")
        course = input("Enter Course/Module: ").strip()


    # --------------------------------------------------------
    # STEP 3: GET AND VALIDATE MARKS
    # --------------------------------------------------------

    while True:

        try:
            # input() returns a string,
            # so convert it to float.
            marks = float(
                input("Enter Marks (0-100): ")
            )

            # Marks must be between 0 and 100.
            if 0 <= marks <= 100:
                break

            # This executes if marks are outside the range.
            print("Marks must be between 0 and 100.")

        # Handles values such as:
        # "abc", "hello", "ten"
        except ValueError:
            print("Marks must be a number.")


    # --------------------------------------------------------
    # STEP 4: AUTOMATICALLY CALCULATE GRADE
    # --------------------------------------------------------

    # The user does NOT enter the grade.
    # Our program calculates it.
    grade = calculate_grade(marks)


    # --------------------------------------------------------
    # STEP 5: CREATE STUDENT DICTIONARY
    # --------------------------------------------------------

    student = {
        "id": next_id,
        "name": name,
        "course": course,
        "marks": marks,
        "grade": grade
    }


    # --------------------------------------------------------
    # STEP 6: ADD STUDENT TO MASTER LIST
    # --------------------------------------------------------

    students.append(student)


    # Show success message.
    print(
        f"Student enrolled successfully. "
        f"ID: {next_id}, Grade: {grade}"
    )


    # Return the next available ID.
    #
    # Example:
    # next_id = 6
    # new student gets ID 6
    # return 7
    return next_id + 1


# ============================================================
# 3. DISPLAY / RENDER STUDENTS
# ============================================================

def render_students(students: list[dict]) -> None:
    """
    Display all student records in table format.
    """

    # --------------------------------------------------------
    # EMPTY LIST CHECK
    # --------------------------------------------------------

    if len(students) == 0:

        print("Cohort is empty.")

        # Stop the function here.
        return


    # --------------------------------------------------------
    # PRINT TABLE HEADER
    # --------------------------------------------------------

    print("-" * 90)

    # <5 means left-align inside 5 spaces.
    # <25 means left-align inside 25 spaces.
    print(
        f"{'ID':<5}"
        f"{'Name':<25}"
        f"{'Course':<25}"
        f"{'Marks':<12}"
        f"{'Grade':<8}"
    )

    print("-" * 90)


    # --------------------------------------------------------
    # PRINT EACH STUDENT
    # --------------------------------------------------------

    for student in students:

        print(
            f"{student['id']:<5}"
            f"{student['name']:<25}"
            f"{student['course']:<25}"
            f"{student['marks']:<12.2f}"
            f"{student['grade']:<8}"
        )

    print("-" * 90)


# ============================================================
# 4. SEARCH STUDENTS
# ============================================================

def query_students(
    students: list[dict],
    search_term: str
) -> list[dict]:
    """
    Search students by:

        1. Student ID
        2. Student name
        3. Course name

    Returns:
        A list containing matching student dictionaries.
    """

    # This list will store matching records.
    results = []


    # --------------------------------------------------------
    # NORMALIZE SEARCH INPUT
    # --------------------------------------------------------

    # strip() removes spaces from beginning/end.
    # lower() makes searching case-insensitive.
    #
    # Example:
    # "  Python  " -> "python"
    search_term = search_term.strip().lower()


    # --------------------------------------------------------
    # CHECK EVERY STUDENT
    # --------------------------------------------------------

    for student in students:

        # ----------------------------------------------------
        # SEARCH BY ID
        # ----------------------------------------------------

        # isdigit() tells us whether the search text
        # contains only digits.
        #
        # "5".isdigit()     -> True
        # "python".isdigit() -> False
        if search_term.isdigit():

            # Convert search text from string to integer.
            if student["id"] == int(search_term):

                # Add matching student to results.
                results.append(student)


        # ----------------------------------------------------
        # SEARCH BY NAME OR COURSE
        # ----------------------------------------------------

        else:

            # Search is case-insensitive because both
            # sides have been converted to lowercase.
            #
            # "python" in "python core" -> True
            if (
                search_term in student["name"].lower()
                or search_term in student["course"].lower()
            ):
                results.append(student)


    # Return all matches.
    return results


# ============================================================
# 5. UPDATE / REVISE STUDENT
# ============================================================

def revise_evaluation(
    students: list[dict],
    student_id: int
) -> bool:
    """
    Find a student by ID and update:
        - name
        - course
        - marks
        - grade

    Returns:
        True  -> update successful
        False -> student ID not found
    """

    # Search through every student.
    for student in students:

        # Find the requested student.
        if student["id"] == student_id:


            # ------------------------------------------------
            # NEW NAME
            # ------------------------------------------------

            name = input(
                "Enter new name: "
            ).strip()

            # Name cannot be empty.
            while name == "":
                print("Name cannot be blank.")

                name = input(
                    "Enter new name: "
                ).strip()


            # ------------------------------------------------
            # NEW COURSE
            # ------------------------------------------------

            course = input(
                "Enter new course: "
            ).strip()

            # Course cannot be empty.
            while course == "":
                print("Course cannot be blank.")

                course = input(
                    "Enter new course: "
                ).strip()


            # ------------------------------------------------
            # NEW MARKS
            # ------------------------------------------------

            while True:

                try:

                    marks = float(
                        input("Enter new marks: ")
                    )

                    # Marks must remain within 0-100.
                    if 0 <= marks <= 100:
                        break

                    print(
                        "Marks must be between 0 and 100."
                    )

                except ValueError:

                    print(
                        "Marks must be a number."
                    )


            # ------------------------------------------------
            # AUTOMATICALLY RECALCULATE GRADE
            # ------------------------------------------------

            # IMPORTANT:
            # If marks change, grade must also change.
            grade = calculate_grade(marks)


            # ------------------------------------------------
            # MODIFY DICTIONARY
            # ------------------------------------------------

            student["name"] = name
            student["course"] = course
            student["marks"] = marks
            student["grade"] = grade


            # Update succeeded.
            return True


    # No matching ID was found.
    return False


# ============================================================
# 6. DELETE / PURGE STUDENT
# ============================================================

def purge_record(
    students: list[dict],
    student_id: int
) -> bool:
    """
    Delete a student after confirmation.

    Returns:
        True  -> student deleted
        False -> student not found or deletion cancelled
    """

    # Search for the student.
    for student in students:

        if student["id"] == student_id:


            # ------------------------------------------------
            # DISPLAY STUDENT BEFORE DELETION
            # ------------------------------------------------

            print("\nStudent Found:")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Course: {student['course']}")
            print(f"Marks: {student['marks']}")
            print(f"Grade: {student['grade']}")


            # ------------------------------------------------
            # ASK FOR CONFIRMATION
            # ------------------------------------------------

            confirmation = input(
                "Are you sure you want to delete (y/n): "
            ).strip().lower()


            # ------------------------------------------------
            # DELETE IF USER CONFIRMS
            # ------------------------------------------------

            if confirmation == "y":

                # remove() deletes this dictionary
                # from the students list.
                students.remove(student)

                return True


            # User entered something other than "y".
            return False


    # Student ID doesn't exist.
    return False


# ============================================================
# 7. SAVE STUDENTS TO JSON
# ============================================================

def save_to_json(
    filepath: str,
    students: list[dict]
) -> None:
    """
    Save the entire students list into a JSON file.
    """

    try:

        # Open file in write mode.
        #
        # "w" means:
        #   create file if it doesn't exist
        #   replace existing content if it does
        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as f:

            # Convert Python list/dictionaries
            # into JSON and write it to the file.
            #
            # indent=4 makes the JSON readable.
            json.dump(
                students,
                f,
                indent=4
            )


        print(
            "Student records saved successfully."
        )


    # Handles file-related errors.
    except OSError as e:

        print(
            f"Error saving file: {e}"
        )


# ============================================================
# 8. LOAD STUDENTS FROM JSON
# ============================================================

def load_from_json(
    filepath: str
) -> list[dict]:
    """
    Read student records from JSON file.

    Returns:
        list of student dictionaries
        OR empty list if loading fails
    """

    try:

        # Open file in read mode.
        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:

            # json.load() converts JSON data
            # into Python objects.
            students = json.load(f)


        print(
            "Student records loaded successfully."
        )


        # Return loaded records.
        return students


    # File doesn't exist.
    except FileNotFoundError:

        print(
            "students.json file does not exist."
        )


    # File exists but contains invalid JSON.
    except json.JSONDecodeError:

        print(
            "JSON file is invalid or corrupted."
        )


    # If either exception happened,
    # return an empty list.
    return []


# ============================================================
# 9. MENU
# ============================================================

def menu():
    """
    Display the menu and return the user's choice.
    """

    print("\n" + "=" * 55)
    print(
        "      STUDENT GRADE MANAGEMENT SYSTEM"
    )
    print("=" * 55)


    print("""
1. Enroll Student
2. Cohort Directory
3. Query Records
4. Revise Evaluation
5. Purge Record
6. Save to JSON
7. Load from JSON
8. Terminate
""")


    # --------------------------------------------------------
    # GET MENU CHOICE
    # --------------------------------------------------------

    try:

        # input() gives a string,
        # int() converts it into an integer.
        choice = int(
            input("Enter your choice: ")
        )

        return choice


    # Handles input such as:
    # "abc"
    # "hello"
    except ValueError:

        print(
            "Choice must be an integer."
        )

        # -1 represents an invalid choice.
        return -1


# ============================================================
# 10. MAIN PROGRAM
# ============================================================

def main():

    # --------------------------------------------------------
    # INITIAL SAMPLE DATA
    # --------------------------------------------------------

    students = [

        {
            "id": 1,
            "name": "Aarav Sharma",
            "course": "Python Core",
            "marks": 88.5,
            "grade": "A"
        },

        {
            "id": 2,
            "name": "Diya Patel",
            "course": "Data Science",
            "marks": 74.0,
            "grade": "B"
        },

        {
            "id": 3,
            "name": "Rohan Nair",
            "course": "Web Architecture",
            "marks": 45.0,
            "grade": "F"
        },

        {
            "id": 4,
            "name": "Sneha Kulkarni",
            "course": "Python Core",
            "marks": 92.0,
            "grade": "A"
        },

        {
            "id": 5,
            "name": "Amit Verma",
            "course": "Data Science",
            "marks": 63.5,
            "grade": "C"
        }
    ]


    # Since the largest initial ID is 5,
    # the next new student gets ID 6.
    next_id = 6


    # --------------------------------------------------------
    # CONTINUOUS MENU LOOP
    # --------------------------------------------------------

    while True:

        # Show menu and get choice.
        choice = menu()


        # ----------------------------------------------------
        # MATCH/CASE CONTROLLER
        # ----------------------------------------------------

        match choice:


            # =================================================
            # CASE 1: ENROLL STUDENT
            # =================================================

            case 1:

                # enroll_student() returns the NEXT ID.
                #
                # Example:
                # next_id = 6
                # student gets ID 6
                # function returns 7
                # next_id becomes 7
                next_id = enroll_student(
                    students,
                    next_id
                )


            # =================================================
            # CASE 2: VIEW ALL STUDENTS
            # =================================================

            case 2:

                render_students(students)


            # =================================================
            # CASE 3: SEARCH
            # =================================================

            case 3:

                # Ask user what to search.
                search_term = input(
                    "Enter Student ID, Name or Course: "
                )


                # Search and store returned results.
                results = query_students(
                    students,
                    search_term
                )


                # An empty list evaluates to False.
                #
                # A non-empty list evaluates to True.
                if results:

                    # Display matching records.
                    render_students(results)

                else:

                    print(
                        "No records found."
                    )


            # =================================================
            # CASE 4: UPDATE
            # =================================================

            case 4:

                try:

                    # Convert entered ID to integer.
                    student_id = int(
                        input("Enter Student ID: ")
                    )


                    # Try to update the student.
                    success = revise_evaluation(
                        students,
                        student_id
                    )


                    # Check returned Boolean.
                    if success:

                        print(
                            "Student record updated successfully."
                        )

                    else:

                        print(
                            "Student ID not found."
                        )


                except ValueError:

                    # Handles non-numeric IDs.
                    print(
                        "Student ID must be an integer."
                    )


            # =================================================
            # CASE 5: DELETE
            # =================================================

            case 5:

                try:

                    student_id = int(
                        input("Enter Student ID: ")
                    )


                    success = purge_record(
                        students,
                        student_id
                    )


                    if success:

                        print(
                            "Student record deleted successfully."
                        )

                    else:

                        print(
                            "Student not found or "
                            "deletion cancelled."
                        )


                except ValueError:

                    print(
                        "Student ID must be an integer."
                    )


            # =================================================
            # CASE 6: SAVE
            # =================================================

            case 6:

                # Save current list into students.json.
                save_to_json(
                    "students.json",
                    students
                )


            # =================================================
            # CASE 7: LOAD
            # =================================================

            case 7:

                # Get records from the JSON file.
                loaded_students = load_from_json(
                    "students.json"
                )


                # Only replace current data if something
                # was successfully loaded.
                if loaded_students:

                    students = loaded_students


                    # Find the largest ID and add 1.
                    #
                    # Example:
                    # IDs = 1,2,3,4,5
                    # max = 5
                    # next_id = 6
                    next_id = (
                        max(
                            student["id"]
                            for student in students
                        ) + 1
                    )


            # =================================================
            # CASE 8: EXIT
            # =================================================

            case 8:

                print(
                    "Program terminated."
                )

                # Stop the while True loop.
                break


            # =================================================
            # INVALID MENU CHOICE
            # =================================================

            case _:

                print(
                    "Invalid choice. Enter 1 to 8."
                )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

# Calling main() starts the entire application.
main()