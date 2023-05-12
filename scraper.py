import requests
from bs4 import BeautifulSoup as bs
import json
def return_isbn(books_url):
    books_isbn = []
    for i in books_url:
        url_book =  'https://www.goodreads.com/' + f'{i}/'
        url_page = requests.get(url_book)
        page_soup = bs(url_page.content,'html.parser')
        data = json.loads(page_soup.find('script', type='application/ld+json').text)
        try:
            books_isbn.append(data["isbn"])
        except KeyError or AttributeError:
            books_isbn.append('N/A')
    return books_isbn

def genre_list_generator():
    url = 'https://www.goodreads.com/shelf/show/'
    page = requests.get(url)
    soup = bs(page.content,'html.parser')
    genres = []
    for a in soup.select('a[href*="/genres/"]'):
        genres.append(a.text)

    for genre in genres[:10]:
        print(f'Genre: {genre}')
    print('\n\n\n')
    genre = input("Enter a book genre: ")
    if not genre or genre.isdigit() == True or genre.casefold() not in (item.casefold() for item in genres):
        print("Incorrect Input!")
        return
    else:
        books_display(genre,url)
    print('\n\n\n')
    return

def books_display(genre_choice,url_genre):
    url_book= url_genre+ f'{genre_choice}/'
    
    print(url_book)
    page = requests.get(url_book)
    soup = bs(page.content,'html.parser')
    
    books_url = []
    titles = soup.find_all('a',class_='bookTitle')
    authors = soup.find_all('a',class_='authorName')
    for a in titles:
        books_url.append(a['href'])

    genre_books_isbn = return_isbn(books_url)

    for title,authors in zip(titles,authors):
        isbn = 0
        title = title.get_text()
        authors = authors.get_text()
        print("BOOK: ",title, "AUTHOR NAME: ",authors,"ISBN: ",genre_books_isbn[isbn])
        isbn +=1
    
            
        

def menu():
    while True:
        choice = input("Press 1 to list some of the genres!\nPress 2 to quit!\n")
        if choice == '1':
            genre_list_generator()
        if choice == '2':
            print("Goodbye!\n")
            exit()
        if choice == '3':
            print("Incorrect Input! Try Again!")
            menu()
menu()