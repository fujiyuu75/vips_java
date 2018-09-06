#!/usr/bin/env python
""" generated source for module Vips """
# 
#  * Tomas Popela, 2012
#  * VIPS - Visual Internet Page Segmentation
#  * Module - Vips.java
from urllib.parse import urlparse


class Vips(object):
    """ generated source for class Vips """

    def __init__(
            self,
            _url=None,
            _domAnalyzer=None,
            _browserCanvas=None,
            _viewport=None,
            _graphicsOutput=False,
            _outputToFolder=False,
            _outputEscaping=True,
            _pDoC=11,
            _filename="",
            sizeTresholdWidth=350,
            sizeTresholdHeight=400,
            originalOut=None,
            startTime=0,
            endTime=0
    ):
        self._url = urlparse(_url)
        self._domAnalyzer = _domAnalyzer
        self._browserCanvas = _browserCanvas
        self._viewport = _viewport
        self._graphicsOutput = _graphicsOutput
        self._outputToFolder = _outputToFolder
        self._outputEscaping = _outputEscaping
        self._pDoC = _pDoC
        self._filename = _filename
        self.sizeTresholdWidth = sizeTresholdWidth
        self.sizeTresholdHeight = sizeTresholdHeight
        self.originalOut = originalOut
        self.startTime = startTime
        self.endTime = endTime

    def startSegmentation(self):
        """ generated source for method startSegmentation """
        self.setUrl()

        print(self._url.geturl())

        # self.egmentation()

    #
    # 	 * Sets web page's URL
    # 	 * @param url Url
    # 	 * @throws MalformedURLException
    #
    def setUrl(self):
        """ generated source for method setUrl """
        if self._url.scheme == "":
            self._url = urlparse("http://" + self._url.geturl())


