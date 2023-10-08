# Step 1: Create a function that takes a file name as an argument and reads in the contents of the file as a list of dictionaries, with each dictionary representing a
# book and containing keys for title, author, ISBN, and price.
# Step 2: Create a function that takes an author's name as an argument and returns a list of all books written by that author.
# Step 3: Create a function that takes an ISBN as an argument and returns the title and price of the book with that ISBN.
# Step 4: Create a function that takes a minimum and maximum price as arguments and returns a list of all books within that price range.
# Step 5: Use the functions from steps 2-4 in a user interface that allows the user to search for books by author, ISBN, or price range.
# Bonus: Add the ability for the user to add new books to the CSV file.



import csv

def read_csv_file(file_name):
    books = []
    file = open(file_name, 'r')
    reader = csv.DictReader(file)
    for row in reader:
            books.append({
                'title': row['Title'],
                'author': row['Author'],
                'ISBN': row['ISBN'],
                'price': float(row['Price'])
            })
    return books


def search_by_author(books, author):
    return [book for book in books if author.lower() in book['author'].lower()]


def search_by_isbn(books, isbn):
    for book in books:
        if book['ISBN'] == isbn:
            return {'title': book['title'], 'price': book['price']}
    return None

def search_by_price_range(books, min_price, max_price):
    return [book for book in books if min_price <= book['price'] <= max_price]


