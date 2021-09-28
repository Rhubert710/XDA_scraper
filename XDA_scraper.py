import csv
from bs4 import BeautifulSoup
import requests


def update_url(url):
    # Getting the html file and parsing with html.parser
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    return bs

bs = update_url('https://www.xda-developers.com/')

try:
    csv_file = open('XDA_data.csv', 'w')
    fieldnames = ['Headline', 'Excerpt', 'Author', 'Date_Posted']
    dictwriter = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Writes the headers
    dictwriter.writeheader()

    number_of_pages_to_scrape = 2  # limits number of pages
    PAGES = number_of_pages_to_scrape

    while True:

        headlines = []
        excerpts = []
        authors = []
        dates = []

        for article in bs.find_all('div', class_="row latest-news-2"):

            for headline in article.find_all('h4'):

                headlines.append(headline.text.replace(',', ''))

            for excerpt in article.find_all('div', class_='the-excerpt'):

                excerpts.append(excerpt.text.replace(',', ''))

            for author in article.find_all('span', class_='meta_author'):

                authors.append(author.text)

            for date in article.find_all('span', class_='meta_date'):

                dates.append(date.text)


        # writes data into csv
        if len(headlines) == len(excerpts) == len(authors) == len(dates):

            for i in range(len(headlines)):

                dictwriter.writerow(
                    {'Headline': headlines[i], 'Excerpt': excerpts[i], 'Author': authors[i], 'Date_Posted': dates[i]})


        #updates bs to next pages url
        bs = update_url(bs.find('a', class_='next page-numbers')['href'])


        #condiotion: number of pages to scrape before break
        number_of_pages_to_scrape -= 1
        if number_of_pages_to_scrape == 0:

            break

    print(f'Sucessfully Scraped {PAGES} pages!')

except:
    print('Unknown Error!!!')
finally:
    csv_file.close()
