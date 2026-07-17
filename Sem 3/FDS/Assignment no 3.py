# Sample list of books as tuples (title, cost)
books = [
    ("Book A", 400),
    ("Book B", 550),
    ("Book C", 300),
    ("Book D", 600),
    ("Book A", 400)  # Duplicate entry
]

# a) Function to delete duplicate entries
def remove_duplicates(books):
    return list(set(books))

# b) Function to display books in ascending order based on cost
def display_books_ascending(books):
    books_sorted = sorted(books, key=lambda book: book[1])
    print("Books in ascending order of cost:")
    for book in books_sorted:
        print(book)

# c) Function to count number of books with cost more than 500
def count_books_more_than_500(books):
    count = sum(1 for book in books if book[1] > 500)
    print(f"Number of books with cost more than 500: {count}")

# d) Function to copy books with cost less than 500 into a new list
def copy_books_less_than_500(books):
    books_less_than_500 = [book for book in books if book[1] < 500]
    print("Books with cost less than 500:")
    for book in books_less_than_500:
        print(book)

# Example usage
books = remove_duplicates(books)
display_books_ascending(books)
count_books_more_than_500(books)
copy_books_less_than_500(books)
