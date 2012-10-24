import os
import japanshin
import mangaaccess
import tools


def download_japanshin(manga, directory, force="n"):
    baseurl = 'http://www.japan-shin.com/lectureenligne/reader/series/'
    mangaurl = baseurl + manga
    mangadir = os.path.join(directory, manga)

    download(mangaurl, mangadir, japanshin)


def download_mangaaccess(manga, directory, force="n"):
    prefix = "http://www.manga-access.com"
    mangaurl = prefix + '/manga/' + manga[0:1] + "/" + manga +\
                                                 "?mature_confirm=1"
    mangadir = os.path.join(directory, manga)

    download(mangaurl, mangadir, mangaaccess)


def download(mangaurl, mangadir, manga_website):
    for chapitre in manga_website.parse_for_chap(mangaurl):
        workingdir = os.path.join(mangadir, chapitre[0])
        listPages = manga_website.parse_for_page(chapitre[1])
        tools.test_mkdir(workingdir)
        if not len(os.listdir(workingdir)) == len(listPages):
            dirlist = os.listdir(workingdir)

            if len(os.listdir(workingdir)) == '0':
                print "Downloading Chapter %s..." % chapitre[0]
            else:
                print "Completing Chapter %s..." % chapitre[0]

            for page in listPages:
                if not (page[0] + ".jpg" in dirlist or
                        page[0] + ".png" in dirlist):
                    print "downloading page %s from %s" % (page[0],
                                                           len(listPages))
                    image = manga_website.parse_for_image(page[1])
                    imagename = os.path.join(workingdir,
                                             page[0] + "." + image[0])
                    realimg = open(imagename, 'wb')
                    realimg.write(image[1])
                    realimg.close()
                else:
                    print "page %s from %s already retrive" %\
                          (page[0], len(listPages))
        else:
            print "skipping : chapter %s already retrive..." % chapitre[0]
