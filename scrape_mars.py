# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
import time
from selenium import webdriver

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape_input():
    browser = init_browser()
    
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html,"html.parser")
    ## NASA Mars News
    article = soup.find("div", class_="list_text")
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_="article_teaser_body").text
     
    #Mars Featured Image
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, 'html.parser')
    image = soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image
    
    ## Mars Weather
    # URL page to be scraped
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    # Find all elements that contain tweets
    recent_tweets = soup.find_all('div', class_='js-tweet-text-container')
    # Retrieve all elements that contain news title 
    # Look for entries that display weather related words to exclude non weather related tweets 
    for tweet in recent_tweets: 
        mars_weather = tweet.find('p').text
        if 'sol' in mars_weather:
            print(mars_weather)
            break
        else: 
            pass
    #### Mars Facts
    # Scrape the table of Mars facts
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    time.sleep(1)
    mars_data = pd.read_html(facts_url)
    mars_df = pd.DataFrame(mars_data[0])
    mars_facts = mars_df.to_html(header = False, index = False)

    #### Mars Hemispheres
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    # Create empty list for hemisphere urls 
    mars_hemisphere = []

    products = soup.find("div", class_ = "result-list" )
    hemispheres = products.find_all("div", class_="item")
    # Loop through the hemisphere links to obtain the images
    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        html = browser.html
        soup=bs(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        mars_hemisphere.append({"title": title, "img_url": image_url})

    # Store data in a dictionary
    mars_library = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        #"mars_facts": mars_facts,
        "mars_hemisphere": mars_hemisphere
    }

    # Close the browser after scraping
    browser.quit()
    #return mars_library
    #print('THIS IS THE MARS_LIBRARY OBJECT: ', mars_library)
    return mars_library
         
    
