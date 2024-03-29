import os
import urllib2

from time import sleep
from re import match, split


def get_url(url, retry=0):
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
        print "error (%s) on : %s\n...try again" % (e.code, url)
        sleep(5)
        if retry <= 5:
            get_url(url, retry + 1)
        else:
            return

    code = response.code
    # headers object
    headers = response.headers
    # contents of the URL (HTML, javascript, css, img, etc.)
    contents = response.read()
    return code, headers, contents


def unifyNumber(num):
    return "%03d" % int(num)


def unifyChapter(chap):
    chapter = ""
    for item in chap:
        #Si item = XX/XX
        if match('.*/.*', item):
            item = unifyNumber(split('/', item)[0]) + "." + split('/', item)[1]
        #Si item = XX.XX
        elif match('.*[.].*', item):
            item = unifyNumber(split('[.]', item)[0]) + "." + split('[.]',
                                                                    item)[1]
        else:
            item = unifyNumber(item)
        chapter += item
    return chapter


def test_mkdir(path):
    if not os.path.isdir(path):
        print "create directory %s" % path
        os.makedirs(path)
    else:
        print "%s already exist, skipping..." % path
