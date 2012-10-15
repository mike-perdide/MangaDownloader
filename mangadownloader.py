import os
import MD.htmlfunct
import getopt
import sys

from MD.tools import test_mkdir, homepage


def _usage(exitcode):
    print '''
    usage: $0 -s SITE -m MANGA -d DIR
        -s : Download site
        -m : manga to download
        -d : destination directory \
             (The chapter and manga directory will be created)
        -f : force retriving
        -h : affiche cet aide
    '''
    sys.exit(exitcode)


try:
    opts, args = getopt.getopt(sys.argv[1:], 's:m:d:fh')
except getopt.GetoptError, err:
    print str(err)
    sys.exit(2)

for o, a in opts:
    if o == '-s':
        site = a
    elif o == '-m':
        manga = a
    elif o == '-d':
        basedir = a
    elif o == '-f':
        force = "yes"
    elif o == '-y':
        _usage('0')

basepage = homepage(site, manga)
mangadir = os.path.join(basedir, manga)

for chapitre in MD.htmlfunct.parse_for_chap(basepage):
    workingdir = os.path.join(mangadir, chapitre[0])
    test_mkdir(workingdir)
    for page in MD.htmlfunct.parse_for_page(chapitre[1]):
        print "downloading page %s from %s" % (page[0],
                                len(MD.htmlfunct.parse_for_page(chapitre[1])))
        image = MD.htmlfunct.parse_for_image(page[1])
        imagename = os.path.join(workingdir, page[0] + "." + image[0])
        realimg = open(imagename, 'wb')
        realimg.write(image[1])
        realimg.close()
