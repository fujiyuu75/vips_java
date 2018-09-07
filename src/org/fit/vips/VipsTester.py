#!/usr/bin/env python

import Vips as vips


class VipsTester(object):
    """ generated source for class VipsTester """
    # 
    # 	 * Main function
    # 	 * @param args Internet address of web page.
    # 	 
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        #  we've just one argument - web address of page
        if len(args):
            print("We've just only one argument - web address of page!")
            return
        # url = args[0]
        url = "https://sports.yahoo.co.jp/"

        try:
            #  disable graphics output
            vips.enableGraphicsOutput(False)
            #  disable output to separate folder (no necessary, it's default value is false)
            vips.enableOutputToFolder(False)
            #  set permitted degree of coherence
            vips.setPredefinedDoC(8)
            #  start segmentation on page
            vips.startSegmentation(url)
        except Exception as e:
            e.printStackTrace()


if __name__ == '__main__':
    import sys
    VipsTester.main(sys.argv)

