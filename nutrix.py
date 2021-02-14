#! /usr/bin/env python

from bs4 import BeautifulSoup
import requests
import mysql.connector


url='https://wikileaks.org'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

def insertInBdd(values):
    mybdd= mysql.connector.connect(
        host='localhost',
        user='root',
        password='Legalcy97.1',
        database='scraptest'
    )
    mycursor = mybdd.cursor()
    val = values
    sql = "INSERT INTO articles (title,image,content,date) values (%s,%s,%s,%s)"

    mycursor.executemany(sql,val)
    mybdd.commit()
    return str(mycursor) + "nouvelle entree"
# def recupTitre():
#     listeTitle = []
#     listeDate = []
#     listeContent = []
#     listeImage = []

#     li_cards = soup.find_all('li', class_="tile")

#     for li in li_cards:
#         # li_title= li.h2.text
#         # li_img = li.img
#         listeTitle.append(li_title)
#         # lidate = li.find('div',class_='timestamp').text
#         listeDate.append(lidate)
#         print(lidate)
#         listeImage.append(li_img)
#         print(li_img)

#     for liste in listeTitle:
#         print(liste)
#         saveValues= insertInBdd([liste])
#         print(saveValues)

#     for liste2 in listeDate:
#         print(liste2)
#         saveValues2 = insertInBdd([liste2])
#         print(saveValues2)
    
#     for liste3 in listeImage:
#         print(liste3)
#         saveValues3 = insertInBdd([liste3])
#         print(liste3)
# recupTitre()

#print('search the latest articles')

def getArticle():
    url='https://wikileaks.org'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    article_main = soup.find_all('li', class_="tile")

    article_titles = []
    article_dates = []
    article_contents = []
    article_images = []
    

    for article in article_main:
        article_title = article.h2.text
        article_img = article.img.attrs['src']
        # article_img ="http://wikileaks.com" + article.img.attrs['src']
        article_date = article.find('div',class_='timestamp').text
        article_content = article.p.text

        article_titles.append(article_title)
        # for liste in article_titles:
        #     insertInBdd([liste])
        article_dates.append(article_date)
        # insertInBdd([article_dates])
        article_contents.append(article_content)
        # insertInBdd([article_contents])
        article_images.append(article_img)
        # insertInBdd([article_images])
        insertInBdd([article_titles],[article_dates],[article_contents],[article_images])

        print(article_titles)
        print(article_images)
        print(article_contents)
        print(article_dates)

getArticle()


# CREATE TABLE articles (
#   id TINYINT(6) UNSIGNED NOT NULL AUTO_INCREMENT,
#   title VARCHAR(250) NOT NULL,
#   image VARCHAR(250) NOT NULL,
#   content VARCHAR(250) NOT NULL,
#   date VARCHAR(255) NOT NULL,
#   PRIMARY KEY (id)
# );