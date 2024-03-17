import requests
from bs4 import BeautifulSoup

def get_books_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    book_info = []
    for book in books:
        title = book.find('h3').a['title']
        price = book.find('p', class_='price_color').text.strip()
        book_info.append({'title': title, 'price': price})
    
    return book_info


def display_books(books):
    print("Какую книгу желаете приобрести?")
    for i, book in enumerate(books, 1):
        print(f"{i}) {book['title']}")
        
def get_book_details(book):
    print(f"Вот данные об этой книге:\n Название: {book['title']}\n Цена: {book['price']}")
    

def main():
    url = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"
    books = get_books_info(url)
    
    display_books(books)
    
    choice = int(input("Выберите книгу: "))
    selected_book = books[choice]
    
    get_book_details(selected_book)
    
main()
    
