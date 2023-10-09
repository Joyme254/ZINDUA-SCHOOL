import requests
from bs4 import BeautifulSoup

# URL of a webpage containing book information
url = 'https://bookskenya.com/'

# Function to fetch book information from the webpage
def fetch_book_information(url):
    response = requests.get(url)
    print (response)
    
    soup = BeautifulSoup(response.content, 'html.parser')

    # To extract book titles, authors, and publication years
    titles = soup.find_all('h1')
    for title in titles:
        print (title.text)

    authors = soup.find_all('span', class_='author')
    for author in authors:
        print (author.text)

    years =soup.find_all('span', class_='publication-year')
    for year in years:
        print ( year.text)

    return list(zip(titles, authors, years))


# Function to save book information to a local text file
def save_to_text_file(book_data, filename):
    with open(filename, 'w') as file:
        for book in book_data:
            file.write(','.join(book) + '\n')

# Function to read and display data from the local text file
def read_and_display_from_text_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())



try:
    # Fetch book information from the URL
    book_data = fetch_book_information(url)

    # Save book information to a local text file
    save_to_text_file(book_data, 'book_data.txt')

    # Display data from the local text file
    read_and_display_from_text_file('book_data.txt')

except Exception as e:
    print("An error occurred:", str(e))