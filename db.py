import mysql.connector
from datetime import date

def webscrappy(htmltag, classname, sitename, url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find("span", class_='pdpprice-row2-main-text')
    rowcount = db.savetoDB(url, results.text,sitename)
    print(rowcount)


url_pricing = "https://www.kohls.com/product/prd-4554171/nespresso-vertuo-next-coffee-espresso-maker-by-delonghi.jsp?skuId=nespresso&search=4554171&submit-search=web-regular"
webscrappy("span", "pdpprice-row2-main-text", "kohls", url_pricing)



def savetoDB(URL, values, tag):
    mydb= mysql.connector.connect(
        host="localhost", 
        user="adSql",
        password="kikoolol",
        database="scrapTest"
    )

    today = date.today()
    mycursor = mydb.cursor()

    sql = "INSERT INTO pricing (url, value, tag, datecreated) values (%s,%s,%s,%s) "
    val = (URL, values, tag, today)
    mycursor.execute(sql, val)

    mydb.commit()
    return str(mycursor) + "nouvelle entrée"