from flask import Flask
import pymongo
from bs4 import BeautifulSoup
import requests
from requests import get
import pandas as pd
import time
from splinter import Browser
import os



def init_browser():
    executable_path = {"/Users/myname/Documents/WebDriver"}
    return Browser("chrome", **executable_path, headless=False)

def news_scrape():
    browser = init_browser()
    news = []
    
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    news["headline"] = soup.find(class_="content-title").get_text()
    
    return news






"""
news_url = "https://mars.nasa.gov/news/"
news_response = requests.get(news_url)

mars_news = BeautifulSoup(news_response.text, 'html.parser')
#print(mars_news)

headlines = soup.find(class='content_title')



#Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
app = Flask(__name__)
@app.route("/")
def root():
    print("Server received request for 'Home' page...")
    return 


#Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
@app.route("/scrape")
def scrape():
    print("Server received request for 'routes' page...")
    

if __name__ == "__main__":
    app.run(debug=True)
"""