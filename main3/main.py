from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://leetcode.com/problemset/algorithms/?difficulty=EASY').text
soup = BeautifulSoup(html_text, 'lxml')

problems = soup.find_all('div', class_='odd:bg-overlay-3 dark:odd:bg-dark-overlay-1 even:bg-overlay-1 dark:even:bg-dark-overlay-3')

for problem in problems:
    problem_name = problem.find('a').text
    solution = problem.find('a', class_='truncate')['href']
    print(f'Problem name : {problem_name}')
    print(f'Solve now : https://leetcode.com{solution}')
    print(' ')
