import os
from re import match, split


def unifyNumber(num):
    return "%03d" % int(num)


def unifyChapter(chap):
    chapter = ""
    for item in chap:
        if not match('.*/.*', item):
            item = unifyNumber(item)
        else:
            item = unifyNumber(split('/', item)[0]) + "." + split('/', item)[1]
        chapter += item
    return chapter


def test_mkdir(path):
    if not os.path.isdir(path):
        print "create directory %s" % path
        os.makedirs(path)
    else:
        print "%s exist" % path


def homepage(site, manga):
    if site == "japanshin":
        return 'http://www.japan-shin.com/lectureenligne/reader/series/' +\
               manga
    else:
        return
