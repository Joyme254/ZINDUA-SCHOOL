



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


