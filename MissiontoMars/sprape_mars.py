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
    executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
    return Browser("chrome", **executable_path, headless=False)

browser = init_browser()
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

#LATEST NEWS
mars_news = BeautifulSoup(browser.html, 'html.parser')
browser.visit(url)

elem = mars_news.select_one('ul.item_list li.slide')
elem.find("div", class_='content_title').get_text()

paragraph = elem.find("div", class_='article_teaser_body').get_text()
print(paragraph)


#Visit the url for JPL Featured Space Image here.
#Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
#Make sure to find the image url to the full size .jpg image.
#Make sure to save a complete url string for this image.

#PHOTO URL
photo_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(photo_url)

html = browser.html

mars_photo = BeautifulSoup(html, 'html.parser')

img = mars_photo.select_one('article.carousel_item').get('style')
#Here is the URL for the image, without the extra characters
img_url = img[23:75]


#IMAGE DICTIONARY FOR THE HEMISPHERES
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/4e59980c1c57f89c680c0e1ccabbeff1_valles_marineris_enhanced.tif_thumb.png"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/55a0a1e2796313fdeafb17c35925e8ac_syrtis_major_enhanced.tif_thumb.png"},
]






"""
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

"""

