import os
import japanshin
import mangaaccess
import tools


def download_japanshin(manga, directory, force="n"):
    baseurl = 'http://www.japan-shin.com/lectureenligne/reader/series/'
    mangaurl = baseurl + manga
    mangadir = os.path.join(directory, manga)

    for chapitre in japanshin.parse_for_chap(mangaurl):
        workingdir = os.path.join(mangadir, chapitre[0])
        if tools.test_mkdir(workingdir, force) == "ok":
            listPages = japanshin.parse_for_page(chapitre[1])
            for page in listPages:
                print "downloading page %s from %s" % (page[0],
                                                len(listPages))
                image = japanshin.parse_for_image(page[1])
                imagename = os.path.join(workingdir, page[0] + "." + image[0])
                realimg = open(imagename, 'wb')
                realimg.write(image[1])
                realimg.close()
        else:
            print "skipping chapter %s." % chapitre[0]


def download_mangaaccess(manga, directory, force="n"):
    prefix = "http://www.manga-access.com"
    mangaurl = prefix + '/manga/' + manga[0:1] + "/" + manga +\
                                                 "?mature_confirm=1"
    mangadir = os.path.join(directory, manga)

    for chapitre in mangaaccess.parse_for_chap(mangaurl):
        workingdir = os.path.join(mangadir, chapitre[0])
        if tools.test_mkdir(workingdir, force) == "ok":
            listPages = mangaaccess.parse_for_page(prefix + chapitre[1])
            for page in listPages:
                print "downloading page %s from %s" % (page[0],
                                                len(listPages))
                image = mangaaccess.parse_for_image(prefix + page[1])
                imagename = os.path.join(workingdir, page[0] + "." + image[0])
                realimg = open(imagename, 'wb')
                realimg.write(image[1])
                realimg.close()
        else:
            print "skipping chapter %s." % chapitre[0]
