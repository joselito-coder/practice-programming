#!/usr/bin/env python3

import requests,sys,webbrowser
from bs4 import BeautifulSoup

mainBaseUrl = "https://imgur.com/search?q={}"

galleryBaseUrl = "https://imgur.com/gallery/{}"

# Taking the input as an argument
if(len(sys.argv) < 2):
    print("usage: ./downloadImages.py [Search term]");
    sys.exit(1)

searchTerm = " ".join(sys.argv[1:])

print(searchTerm)

res = requests.get(mainBaseUrl.format(searchTerm))
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
galleryIds = []
for i in soup.select('.cards > div'):
    # print(i.get('id'))
    galleryIds.append(str(i.get('id')))


# print(galleryIds)

for i in range(0,min(5,len(galleryIds))) :
    galRes = requests.get(galleryBaseUrl.format(galleryIds[i]))
    galRes.raise_for_status()

    for chunks in galRes.iter_content(100000):
        with open('gallery_html_{}.html'.format(i),'wb') as gallery:
            gallery.write(chunks)

    # galSoup = BeautifulSoup(galRes.text,'lxml')

    # for images in galSoup.select('.GalleryPage img'):
    #     print(images)


    # print(galleryBaseUrl.format(galleryIds[i]))
    # webbrowser.open(galleryBaseUrl.format(galleryIds[i]))
    pass
    

