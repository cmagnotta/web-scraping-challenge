from flask import Flask
import pymongo
from bs4 import BeautifulSoup
import requests
from requests import get
import pandas as pd
import time
from splinter import Browser
import os



#Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
app = Flask(__name__)
@app.route("/")
def root():
    print("Server received request for 'Home' page...")
    return "Aloha! Check out this data on Hawaiian climate!"

#Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
@app.route("/scrape")
def scrape():
    print("Server received request for 'routes' page...")
    

if __name__ == "__main__":
    app.run(debug=True)