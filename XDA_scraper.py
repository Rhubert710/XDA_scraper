import csv
from bs4 import BeautifulSoup
import requests

# URL to the website
URL = 'https://www.xda-developers.com/'

# Getting the html file and parsing with html.parser
html = requests.get(URL)
bs = BeautifulSoup(html.text, 'html.parser')

# Tries to open the file
try:
    csv_file = open('XDA_data.csv', 'w')
    fieldnames = ['Headline', 'Excerpt', 'Author', 'Date_Posted']
    dictwriter = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Writes the headers
    dictwriter.writeheader()

    headlines = []
    excerpts = []
    authors = []
    dates = []
    pages = 2  # limits number of pages

    while True:

        for article in bs.find_all('div', class_="row latest-news-2"):

            for headline in article.find_all('h4'):

                headlines.append(headline.text)

            for excerpt in article.find_all('div', class_='the-excerpt'):

                excerpt_str = str(excerpt.text)
                excerpts.append(excerpt_str.replace(',', ''))

            for author in article.find_all('span', class_='meta_author'):

                authors.append(author.text)

            for date in article.find_all('span', class_='meta_date'):

                dates.append(date.text)

        next_page_url = bs.find('a', class_='next page-numbers')
        print(next_page_url['href'])
        html = requests.get(next_page_url['href'])
        bs = BeautifulSoup(html.text, 'html.parser')

        pages -= 1
        if pages == 0:

            if len(headlines) == len(excerpts) == len(authors) == len(dates):

                for i in range(len(headlines)):
                    # writes data into csv
                    dictwriter.writerow(
                        {'Headline': headlines[i], 'Excerpt': excerpts[i], 'Author': authors[i], 'Date_Posted': dates[i]})
                break
except:
    print('Unknown Error!!!')
finally:
    csv_file.close()
