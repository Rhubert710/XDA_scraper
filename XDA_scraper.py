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

    headlines =[]
    excerpts = []
    authors = []
    dates = []
    pages = 5 # limits number of pages

    while True:

        print('wwwwww')
        
        
        for article in bs.find_all('div', class_ ="row latest-news-2"):


            for headline in article.find_all('h4'):

                headlines.append(headline.text)
                # print(headline.text)
                # print('hhhhhh')

            for excerpt in article.find_all('div', class_ = 'the-excerpt'):

                excerpts.append(excerpt.text)
                # print(excerpt.text)
                # print('eeeeeeee')

            for author in article.find_all('span', class_ = 'meta_author'):
    
                authors.append(author.text)
                print(author.text)
                print('aaaaaaaaa')

            for date in article.find_all('span', class_ = 'meta_date'):
        
                dates.append(date.text)
                # print(date.text)
                # print('ddddddddd')

            # for a in bs.find_all('a', class_ = 'next page-numbers'):
        
                # a.append(date.text)
                # print(a['href'])
                # print('nnnnnnnnn')

        next = bs.find('a', class_ = 'next page-numbers')
        print(next['href'])
        html = requests.get(next['href'])
        bs = BeautifulSoup(html.text, 'html.parser')
        # print(headlines)
        # print(excerpts)

        # print(len(headlines))
        # print(len(excerpts))

        # for i in range(len(headlines)):
        #     #writes all headlines into csv
        #     dictwriter.writerow({'Headline': headlines[i], 'Excerpt': excerpts[i], 'Author': authors[i], 'Date_Posted': dates[i]})


            # print('tru')
        
        pages -= 1
        print(pages)
        if pages == 0:
            print('999999999')
            for i in range(len(headlines)):
                #writes all headlines into csv
                dictwriter.writerow({'Headline': headlines[i], 'Excerpt': excerpts[i], 'Author': authors[i], 'Date_Posted': dates[i]})
            break
except:
    print('Unknown Error!!!')
finally:
    csv_file.close()
