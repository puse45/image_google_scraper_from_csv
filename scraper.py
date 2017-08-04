from bs4 import BeautifulSoup
import csv
from io import StringIO
import urllib2
import os
import json

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def download_image(query,name,DIR,keyword):
    jina = query
    image_type=name
    query = query +" "+ keyword
    query =query.replace(" ", "+")
    query =query.lower()
    # query='+'.join(query)

    url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"

    print  "Image: " + jina + " id: " + image_type

    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    }
    soup = get_soup(url,header)

    ActualImages = []  # contains the link for Large original images, type of  image
    try:
        a = soup.find("div",{"class":"rg_meta"})
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))
    except Exception as e:
        pass

    for i , (img , Type) in enumerate( ActualImages):
        try:
            req = urllib2.Request(img, headers={'User-Agent' : header})
            raw_img = urllib2.urlopen(req).read()

            cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
            # print cntr
            if len(Type)==0:
                # f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
                f = open(os.path.join(DIR , image_type +".jpg"), 'wb')
            else :
                # f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')
                f = open(os.path.join(DIR , image_type + "."+Type), 'wb')
            f.write(raw_img)
            f.close()
        except Exception as e:
            print "could not load : "+img
            print e

def get_csv(pathtodoc,dir,keyword):
    quotedData = StringIO()
    m = []

    # with open('doc/presidential_candidates.csv') as f:
    with open(pathtodoc) as f:
        reader = csv.reader(f)
        for row in reader:
            a = row
            row[1:3] = [' '.join(map(str, row[1:3]))]
            p = row[1]
            download_image(p,a[0],dir,keyword)
            m = m + (a)
# get_csv(path,image save dir,keyword)
get_csv('doc/.csv','dataset','keywords')
get_csv('doc/.csv','dataset','keywords')
get_csv('doc/.csv','dataset','keywords')

