import urllib2
import tools
from re import match, compile, findall
from bs4 import BeautifulSoup


def get_url(url):
    '''get_url accepts a URL string and return the server response code,
       response headers, and contents of the file'''
    req_headers = {
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'http://www.google.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/plain'}

    # create a request object for the URL
    request = urllib2.Request(url, headers=req_headers)
    # create an opener object
    opener = urllib2.build_opener()

    try:
        # open a connection and receive http the response headers + contents
        response = opener.open(request)
    except urllib2.HTTPError, e:
        #Petite gestion des codes 4xx
        if match('4..', e.code()):
            print e.code()

    code = response.code
    # headers object
    headers = response.headers
    # contents of the URL (HTML, javascript, css, img, etc.)
    contents = response.read()
    return code, headers, contents


def parse_for_chap(url):
    chap = []
    #page = get_url(url)
    soup = BeautifulSoup(get_url(url)[2])
    for item in soup.find_all(href=compile("/read/.*/fr/")):
        chap.append([tools.unifyChapter(findall('fr/[0-9]+/(.*)/', item['href'])), item['href']])
    return chap


def parse_for_page(url):
    page = []
    soup = BeautifulSoup(get_url(url)[2])
    for item in soup.find_all(onclick=compile("changePage")):
        page.append([tools.unifyNumber(findall('\d+', item.text)[0]), item['href']])
    return page


def parse_for_image(url):
    soup = BeautifulSoup(get_url(url)[2])
    link = soup.find_all(src=compile('/comics/'))
    imgurl =  link[0]['src']
    imgext = imgurl[len(imgurl)-3:len(imgurl)]
    return imgext, get_url(imgurl)[2]
