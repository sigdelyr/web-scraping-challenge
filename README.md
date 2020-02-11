# Web Scraping - Mission to Mars

# Tools / Technologies used:

Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter, MongoDB, Flask Application & GitHub

# Summary

In this project i Used BeautifulSoup, Pandas, and Requests/Splinter to web scrape the NASA Mars News Site. It was scraped for the latest news title and news paragraph. Then JPL Mars Space Images was scaraped for featured image. Next the Mars Weather Twitter account was scraped to obtain the latest Mars weather tweet. Lastly, Mars Facts was scraped to obtain the table containing facts about the planet including Diameter, Mass, etc and visited the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.

The python file scrape_mars has a function called scrape that executes all of the above scraped code and return one Python dictionary containing all of the scraped data. The route /scrape imports the scrape_mars.py file and calls the scrape function. The value returned is then stored in Mongo as a Python dictionary. The route / then queries the Mongo database and pass the mars data into an HTML template to display the data.
