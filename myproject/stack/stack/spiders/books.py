# importing required lib
from pathlib import Path
import scrapy 
import datetime
from pymongo import MongoClient # importing a function which will help send data to database


client = MongoClient("mongodb://localhost:27017/") # connecting with database

def database(title,image,price,rating,available):

    db = client.test_collection # inatalizing database a file will be created in the database named test.database

    collection = db.test_collection# sending the collected data

    # Data format

    data = {
           "Title": title, 
           "Image-link": image,
           "Rating": rating,
           "Price": price,
           "Available": available,
           "Date":datetime.datetime.now()
    }
    sendData = collection.insert_one(data) # inserting data

    return sendData.sendData_id # returning the data transfer id

class books(scrapy.Spider): # calls an inbuild function which helps crawl website { Note: the syntax of this is important }
    name = 'books'
    start_urls = [
        "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
        "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
        "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
    ]

    def parse(self, response):

        # Searching of the data 

        cards = response.css(".product_pod")
        for card in cards:

            title = card.css("h3>a::text").get()
            print(title)

            image = card.css(".image_container img::attr(src)").get()
        #  print(image)
            rating = card.css(".star-rating").attrib["class"].split(" ")[1]
        #  print(rating)

            price = card.css(".price_color::text").get()
        #  print(price)

            instock = card.css(".availability")
            if len(instock.css(".icon-ok")) > 0:
                available = True
            else:
                available =  False

            database(title,image,price,rating,available) # calling the database function
        