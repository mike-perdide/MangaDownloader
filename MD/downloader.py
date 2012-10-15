import os
import japanshin
import tools


def download_japanshin(manga, directory):
    baseurl = 'http://www.japan-shin.com/lectureenligne/reader/series/'
    mangaurl = baseurl + manga
    mangadir = os.path.join(directory, manga)

    for chapitre in japanshin.parse_for_chap(mangaurl):
        workingdir = os.path.join(mangadir, chapitre[0])
        tools.test_mkdir(workingdir)
        for page in japanshin.parse_for_page(chapitre[1]):
            print "downloading page %s from %s" % (page[0],
                                    len(japanshin.parse_for_page(chapitre[1])))
            image = japanshin.parse_for_image(page[1])
            imagename = os.path.join(workingdir, page[0] + "." + image[0])
            realimg = open(imagename, 'wb')
            realimg.write(image[1])
            realimg.close()
