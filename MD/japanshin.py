import tools
from re import compile, findall, sub
from bs4 import BeautifulSoup


def parse_for_chap(url):
    chap = []
    soup = BeautifulSoup(tools.get_url(url)[2])
    for item in soup.find_all(href=compile("/read/.*/fr/")):
        chap.append([tools.unifyChapter(findall('fr/[0-9]+/(.*)/',
                                        item['href'])), item['href']])
    return chap


def parse_for_page(url):
    page = []
    soup = BeautifulSoup(tools.get_url(url)[2])
    for item in soup.find_all(onclick=compile("changePage")):
        page.append([tools.unifyNumber(findall('\d+', item.text)[0]),
                    item['href']])
    return page


def parse_for_image(url):
    soup = BeautifulSoup(tools.get_url(url)[2])
    link = soup.find_all(src=compile('/comics/'))
    imgurl = sub(' ', '%20', link[0]['src'])
    imgext = imgurl[len(imgurl) - 3:len(imgurl)]
    return imgext, tools.get_url(imgurl)[2]
