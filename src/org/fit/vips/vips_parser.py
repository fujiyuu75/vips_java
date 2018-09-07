#!/usr/bin/env python
""" generated source for module VipsParser2 """


#
#  * Tomas Popela, 2012
#  * VIPS - Visual Internet Page Segmentation
#  * Module - VipsParser.java
#
# package: org.fit.vips
class VipsParser(object):
    """ generated source for class VipsParser """
    def __init__(
            self,
            _vipsBlocks=VipsBlock(),
            _sizeTresholdHeight=80,
            _sizeTresholdWidth=80,
    ):
        """ generated source for method __init__ """
        # self._viewport = viewport
        self._vipsBlocks = VipsBlock()
        self._sizeTresholdHeight = 80
        self._sizeTresholdWidth = 80
        # self._pageWidth = viewport.getWidth()
        # self._pageHeight = viewport.getHeight()

    #
    #      * Starts visual page segmentation on given page
    #
    def parse(self):
        """ generated source for method parse """
        if self._viewport != None:
            self._vipsBlocks = VipsBlock()
            self._visualBlocksCount = 0
            constructVipsBlockTree(self._viewport.getElementBoxByName("body", False), self._vipsBlocks)
            divideVipsBlockTree(self._vipsBlocks)
            getVisualBlocksCount(self._vipsBlocks)
            # System.err.println(String.valueOf("We have " + _visualBlocksCount + " visual blocks."));
        else:
            System.err.print_("Page's viewPort is not defined")



