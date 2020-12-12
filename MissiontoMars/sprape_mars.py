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
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    listings = []

    photo_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(photo_url)
    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    try:
        browser.links.find_by_partial_text('next').click()
          
    except:
        print("Scraping Complete")



