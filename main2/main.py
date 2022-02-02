from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.flipkart.com/books/fiction-books/fantasy-fiction-books/pr?sid=bks,wbi,z5d&q=books&p[]=facets.language%255B%255D%3DEnglish&otracker=categorytree').text
soup = BeautifulSoup(html_text, 'lxml')

books = soup.find_all('div', class_='_4ddWXP')

for book in books:
    book_name = book.find('a', class_='s1Q9rs').text
    price = book.find('div', class_='_30jeq3').text
    buy_now = book.a['href']
    print(f'Book name : {book_name}')
    print(f'Price : {price}')
    print(f'Buy now : https://www.flipkart.com{buy_now}')
    print(' ')