from requests import get  # to make GET request

from bs4 import BeautifulSoup
import urllib.request
import urllib

# use this image scraper from the location that
#you want to save scraped images to

def make_soup(url):
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html)

def get_images(url):
    soup = make_soup(url)
    path = "img/"
    #this makes a list of bs4 element tags
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + " images found.")
    print ('Downloading images.')
    #compile our unicode list of image links
    image_links = [each.get('src') for each in images]
    for each in image_links:
        filename=each.split('/')[-1]
        urllib.request.urlretrieve(each, path+filename)
    return image_links





get_images("http://www.cbsnews.com/pictures/")