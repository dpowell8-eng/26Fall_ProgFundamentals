
import sqlite3

# Connect to the database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Remove the existing books table
cursor.execute("DROP TABLE IF EXISTS books")

# Create the books table
cursor.execute("""
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    genre TEXT,
    copies INTEGER,
    rating INTEGER
)
""")

# Insert one book using a single INSERT statement
cursor.execute("""
INSERT INTO books (id, title, author, year, genre, copies, rating)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (1, "The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 4, 5))

# Insert the remaining books using executemany
books = [
    (2, "To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", 3, 5),
    (3, "The Da Vinci Code", "Dan Brown", 2003, "Mystery", 4, 4),
    (4, "A Brief History of Time", "Stephen Hawking", 1988, "Science", 2, None),
    (5, "Sapiens", "Yuval Noah Harari", 2011, "History", 3, 5),
    (6, "Pride and Prejudice", "Jane Austen", 1813, "Fiction", 5, None),
    (7, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction", 2, 4),
    (8, "The Hound of the Baskervilles", "Arthur Conan Doyle", 1902, "Mystery", 3, 3)
]

cursor.executemany("""
INSERT INTO books (id, title, author, year, genre, copies, rating)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", books)

# Save all inserted books
conn.commit()

# Display a menu until the user chooses to exit
while True:
    print("\n========== LIBRARY MENU ==========")
    print("1. Books published after 1990")
    print("2. Fiction books with more than 2 copies")
    print("3. Books published before 1900 OR rated 5")
    print("4. Books NOT in the Mystery genre")
    print("5. Books in Science or History")
    print("6. Search authors by first letter")
    print("7. Books with no rating")
    print("8. Exit")
    print("==================================")

    choice = input("Enter your choice (1-8): ")

    # 1. Books published after 1990
    if choice == "1":
        print("\n--- Books Published After 1990 ---")
        cursor.execute(
            "SELECT title, author FROM books WHERE year > ?",
            (1990,)
        )
        for row in cursor.fetchall():
            print(row[0], "-", row[1])

    # 2. Fiction books with more than 2 copies (AND)
    elif choice == "2":
        print("\n--- Fiction Books with More Than 2 Copies ---")
        cursor.execute("""
            SELECT title FROM books
            WHERE genre = ? AND copies > ?
        """, ("Fiction", 2))
        for row in cursor.fetchall():
            print(row[0])

    # 3. Books published before 1900 OR rated 5
    elif choice == "3":
        print("\n--- Books Published Before 1900 OR Rated 5 ---")
        cursor.execute("""
            SELECT title FROM books
            WHERE year < ? OR rating = ?
        """, (1900, 5))
        for row in cursor.fetchall():
            print(row[0])

    # 4. Books NOT in the Mystery genre
    elif choice == "4":
        print("\n--- Books NOT in the Mystery Genre ---")
        cursor.execute("""
            SELECT title FROM books
            WHERE NOT genre = ?
        """, ("Mystery",))
        for row in cursor.fetchall():
            print(row[0])

    # 5. Books in Science or History (IN)
    elif choice == "5":
        print("\n--- Science or History Books ---")
        cursor.execute("""
            SELECT title FROM books
            WHERE genre IN (?, ?)
        """, ("Science", "History"))
        for row in cursor.fetchall():
            print(row[0])

    # 6. Search authors by first letter (LIKE)
    elif choice == "6":
        letter = input("Enter a letter to search for authors: ")

        print(f"\n--- Authors Starting with '{letter}' ---")
        cursor.execute("""
            SELECT author FROM books
            WHERE author LIKE ?
        """, (letter + "%",))

        for row in cursor.fetchall():
            print(row[0])

    # 7. Books with no rating (IS NULL)
    elif choice == "7":
        print("\n--- Books with No Rating ---")
        cursor.execute("""
            SELECT title FROM books
            WHERE rating IS NULL
        """)
        for row in cursor.fetchall():
            print(row[0])

    # 8. Exit the program
    elif choice == "8":
        print("\nExiting the library program. Goodbye!")
        break

    # Handle invalid menu choices
    else:
        print("\nInvalid choice. Please enter a number from 1 to 8.")

# Close the database connection after exiting the menu
conn.close()
print("Database connection closed.")