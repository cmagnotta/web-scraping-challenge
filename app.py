from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import sprape_mars

app = Flask(__name__)


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/4e59980c1c57f89c680c0e1ccabbeff1_valles_marineris_enhanced.tif_thumb.png"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/55a0a1e2796313fdeafb17c35925e8ac_syrtis_major_enhanced.tif_thumb.png"},
]
app.config["MONGO_URI"] = "index.html"
mongo = PyMongo(app)

@app.route("/scrape")
def scraper():
    elem = mongo.db.mars_news
    latest_mars_news = sprape_mars.scrape()
    latest_mars_news.update({}, upsert=True)
    return redirect("/")

@app.route("/")
def index():
    return render_template("index.html", latest_mars_news=latest_mars_news)




# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, url="CHANGE THIS")


if __name__ == "__main__":
    app.run(debug=True)
