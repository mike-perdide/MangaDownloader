import getopt
from sys import argv, exit

from MD.downloader import download_japanshin


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
    exit(exitcode)


try:
    opts, args = getopt.getopt(argv[1:], 's:m:d:fh')
except getopt.GetoptError, err:
    print str(err)
    _usage('1')

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

if site == "japanshin":
    download_japanshin(manga, basedir)
else:
    print "reading site %s unknown" % site
    _usage('1')
