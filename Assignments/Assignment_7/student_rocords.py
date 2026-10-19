import sqlite3

# Connect to the database
conn = sqlite3.connect("StudentRecords.db")
cursor = conn.cursor()

# Remove the existing table and recreate it
cursor.execute("DROP TABLE IF EXISTS StudentRecords")

cursor.execute("""
CREATE TABLE StudentRecords (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Age INTEGER NOT NULL,
    Major TEXT NOT NULL
)
""")

# Add five students with fixed values
students = [
    (1, "Alice Johnson", 20, "Computer Science"),
    (2, "Brian Smith", 22, "Mathematics"),
    (3, "Carla Davis", 19, "Biology"),
    (4, "David Wilson", 21, "Information Technology"),
    (5, "Emma Brown", 23, "Business")
]

cursor.executemany("""
INSERT INTO StudentRecords (ID, Name, Age, Major)
VALUES (?, ?, ?, ?)
""", students)

conn.commit()

# Display students without printing their IDs
print("\nStudent Records:")
cursor.execute("""
SELECT Name, Age, Major
FROM StudentRecords
""")

for student in cursor.fetchall():
    print(f"Name: {student[0]}, Age: {student[1]}, Major: {student[2]}")


# Ask whether the user wants to add a student
while True:
    answer = input(
        "\nDo you want to add a new student? (yes/no): "
    ).strip().lower()

    if answer in ("yes", "no"):
        break

    print("Invalid answer. Please enter yes or no.")


if answer == "yes":

    # Get a valid, nonempty name
    while True:
        name = input("Enter the student's name: ").strip()

        if name:
            break

        print("Name cannot be empty. Please try again.")

    # Get a valid whole-number age
    while True:
        age_input = input("Enter the student's age: ").strip()

        try:
            age = int(age_input)
            break
        except ValueError:
            print("Age must be a whole number. Please try again.")

    # Get a valid, nonempty major
    while True:
        major = input("Enter the student's major: ").strip()

        if major:
            break

        print("Major cannot be empty. Please try again.")

    # Find an unused ID
    cursor.execute("""
    SELECT COALESCE(MAX(ID), 0) + 1
    FROM StudentRecords
    """)
    new_id = cursor.fetchone()[0]

    # Insert the new student using ? placeholders
    cursor.execute("""
    INSERT INTO StudentRecords (ID, Name, Age, Major)
    VALUES (?, ?, ?, ?)
    """, (new_id, name, age, major))

    conn.commit()

    print("\nNew student added successfully.")
    print(f"Name: {name}, Age: {age}, Major: {major}")

# Commit any remaining changes and close the connection
conn.commit()
conn.close()

print("\nDatabase connection closed.")