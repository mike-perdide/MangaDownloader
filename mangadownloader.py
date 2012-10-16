import getopt
from sys import argv, exit

from MD.downloader import download_japanshin, download_mangaaccess


def _usage(exitcode):
    print '''
    usage: $0 -s SITE -m MANGA -d DIR
        -s : Download site (japanshin, mangaaccess)
        -m : manga to download
        -d : destination directory \
             (The chapter and manga directory will be created)
        -f : force retriving
        -h : affiche cet aide
    '''
    exit(exitcode)


try:
    opts, args = getopt.getopt(argv[1:], 's:m:d:fh')
except getopt.GetoptError, err:
    print str(err)
    _usage('1')

force = 'n'
for o, a in opts:
    if o == '-s':
        site = a
    elif o == '-m':
        manga = a
    elif o == '-d':
        basedir = a
    elif o == '-f':
        force = "y"
    elif o == '-y':
        _usage('0')

if site == "japanshin":
    download_japanshin(manga, basedir, force)
elif site == "mangaaccess":
    download_mangaaccess(manga, basedir, force)
else:
    print "reading site %s unknown" % site
    _usage('1')
