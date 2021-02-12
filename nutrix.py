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
    sql = "INSERT INTO articleTitle (image) values (%s)"
    val = values

    mycursor.execute(sql,val)
    mybdd.commit()
    return str(mycursor) + "nouvelle entree"

def recupTitre():
    listeTitle = []
    listeDate = []
    listeContent = []
    listeImage = []

    li_cards = soup.find_all('li', class_="tile")

    for li in li_cards:
        li_title= li.h2.text
        li_img = li.img
        listeTitle.append(li_title)
        lidate = li.find('div',class_='timestamp').text
        listeDate.append(lidate)
        print(lidate)
        listeImage.append(li_img)
        print(li_img)

    for liste in listeTitle:
        print(liste)
        saveValues= insertInBdd([liste])
        print(saveValues)

    for liste2 in listeDate:
        print(liste2)
        saveValues2 = insertInBdd([liste2])
        print(saveValues2)
    
    for liste3 in listeImage:
        print(liste3)
        saveValues3 = insertInBdd([liste3])
        print(liste3)
recupTitre()