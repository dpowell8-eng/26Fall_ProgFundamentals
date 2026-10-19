import sqlite3

# Connect to the database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Remove the existing table so the program can run again
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
    (3, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction", 2, 4),
    (4, "A Brief History of Time", "Stephen Hawking", 1988, "Science", 3, None),
    (5, "The Art of War", "Sun Tzu", -500, "History", 5, 5),
    (6, "Murder on the Orient Express", "Agatha Christie", 1934, "Mystery", 4, None),
    (7, "Sapiens", "Yuval Noah Harari", 2011, "History", 3, 5),
    (8, "The Old Man and the Sea", "Ernest Hemingway", 1952, "Fiction", 4, 4)
]

cursor.executemany("""
INSERT INTO books (id, title, author, year, genre, copies, rating)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", books)

conn.commit()


# 1. Books published after 1990
print("\nBooks published after 1990:")
cursor.execute("""
SELECT title, author
FROM books
WHERE year > ?
""", (1990,))
for row in cursor.fetchall():
    print(f"Title: {row[0]}, Author: {row[1]}")


# 2. Fiction books with more than 2 copies (AND)
print("\nFiction books with more than 2 copies:")
cursor.execute("""
SELECT title
FROM books
WHERE genre = ? AND copies > ?
""", ("Fiction", 2))
for row in cursor.fetchall():
    print(row[0])


# 3. Books published before 1900 OR rated 5
print("\nBooks published before 1900 OR rated 5:")
cursor.execute("""
SELECT title
FROM books
WHERE year < ? OR rating = ?
""", (1900, 5))
for row in cursor.fetchall():
    print(row[0])


# 4. Books NOT in the Mystery genre
print("\nBooks not in the Mystery genre:")
cursor.execute("""
SELECT title
FROM books
WHERE NOT genre = ?
""", ("Mystery",))
for row in cursor.fetchall():
    print(row[0])


# 5. Books in either Science or History (IN)
print("\nBooks in the Science or History genre:")
cursor.execute("""
SELECT title
FROM books
WHERE genre IN (?, ?)
""", ("Science", "History"))
for row in cursor.fetchall():
    print(row[0])


# 6. Authors whose names start with a user-provided letter (LIKE)
letter = input("\nEnter a letter to search for authors: ").strip()

while len(letter) != 1 or not letter.isalpha():
    print("Please enter exactly one letter.")
    letter = input("Enter a letter to search for authors: ").strip()

print(f"\nAuthors whose names start with '{letter}':")
cursor.execute("""
SELECT author
FROM books
WHERE author LIKE ?
""", (letter + "%",))
for row in cursor.fetchall():
    print(row[0])


# 7. Books with no rating (IS NULL)
print("\nBooks with no rating:")
cursor.execute("""
SELECT title
FROM books
WHERE rating IS NULL
""")
for row in cursor.fetchall():
    print(row[0])


# Close the database connection
conn.close()


