from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=YCXEX11SS2465QB2MHK1&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1').text
soup = BeautifulSoup(html_text, 'lxml')

movies = soup.find_all('div', class_='lister-item-content')

for movie in movies:
    movie_name = movie.find('a').text
    about = movie.find_all('p', class_='text-muted')[1].text
    more_info = movie.h3.a['href']
    print(f'Movie name : {movie_name.strip()}')
    print(f'About : {about.strip()}')
    print(f'More info : https://www.imdb.com/{more_info}')
    print(' ')