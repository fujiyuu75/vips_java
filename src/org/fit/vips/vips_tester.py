#!/usr/bin/env python

import sys
from vip_s import Vips


class VipsTester():
    """ generated source for class VipsTester """

    #
    # 	 * Main function
    # 	 * @param args Internet address of web page.
    # 	 

    @staticmethod
    def main():
        """ generated source for method main """

        url = "sports.yahoo.co.jp/"

        vips = Vips(_url=url, _pDoC=8)
        # #  disable graphics output
        # vips.enableGraphicsOutput(False)
        # #  disable output to separate folder (no necessary, it's default value is false)
        # vips.enableOutputToFolder(False)
        #  start segmentation on page
        vips.startSegmentation()


if __name__ == '__main__':
    VipsTester.main()
