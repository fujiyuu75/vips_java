#!/usr/bin/env python
""" generated source for module Vips """
# 
#  * Tomas Popela, 2012
#  * VIPS - Visual Internet Page Segmentation
#  * Module - Vips.java
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class Vips(object):
    """ generated source for class Vips """

    def startSegmentation(self):
        """ generated source for method startSegmentation """
        self.setUrl()

        print(self._url.geturl())

        # self.segmentation()

    def __init__(
            self,
            _url=None,
            _domAnalyzer=None,
            _browserCanvas=None,
            _viewport=None,
            _graphicsOutput=False,
            _outputEscaping=True,
            _pDoC=11,
            _filename="",
            _outputToPath="",
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
        self._outputEscaping = _outputEscaping
        self._pDoC = _pDoC
        self._filename = _filename
        self._outputToFolder = _outputToPath
        self.sizeTresholdWidth = sizeTresholdWidth
        self.sizeTresholdHeight = sizeTresholdHeight
        self.originalOut = originalOut
        self.startTime = startTime
        self.endTime = endTime

        self.bs = None

    def setUrl(self):
        """ generated source for method setUrl """
        if self._url.scheme == "":
            self._url = urlparse("http://" + self._url.geturl())

    def segmentation(self):
        """ generated source for method startSegmentation """
        # self._url.openConnection()
        # self.redirectOut()
        self.bs = self.getDomTree(self._url)
        # self.getViewport()
        # self.restoreOut()
        self.performSegmentation()

    def getDomTree(self, url):
        """ generated source for method getDomTree """
        html = """
        <!DOCTYPE html>
        <html>
          <head>
          </head>
          <body>

            <h1 id="test-id" class="test-class">Test Text</h1>

            <a href="http://zombie-hunting-club.com">ゾンビ狩りクラブ</a>

            <ul>
                <li>item1</li>
                <li>item2</li>
                <li>item3</li>
            </ul>

            <div id="div1">
                <p class="p1">pタグ内のテキスト1</p>
            </div>

            <div id="div2">
                <p class="p2">pタグ内のテキスト2</p>
            </div>
          </body>
        </html>
        """

        return BeautifulSoup(html, "html.parser")

    def performSegmentation(self):
        """ generated source for method performSegmentation """
        numberOfIterations = 10
        # pageWidth = self._viewport.getWidth()
        # pageHeight = self._viewport.getHeight()
        # if self._graphicsOutput:
        #     self.exportPageToImage()
        # detector = VipsSeparatorGraphicsDetector()
        vipsParser = VipsParser(self.bs)
        constructor = VisualStructureConstructor(self._pDoC)
        # constructor.setGraphicsOutput(self._graphicsOutput)
        iterationNumber = 1
        while iterationNumber < numberOfIterations + 1:
            detector = VipsSeparatorGraphicsDetector(pageWidth, pageHeight)
            vipsParser.setSizeTresholdHeight(self.sizeTresholdHeight)
            vipsParser.setSizeTresholdWidth(self.sizeTresholdWidth)
            vipsParser.parse()
            if iterationNumber == 1:
                if self._graphicsOutput:
                    detector.setVipsBlock(vipsBlocks)
                    detector.fillPool()
                    detector.saveToImage("blocks" + iterationNumber)
                    detector.setCleanUpSeparators(0)
                    detector.detectHorizontalSeparators()
                    detector.detectVerticalSeparators()
                    detector.exportHorizontalSeparatorsToImage()
                    detector.exportVerticalSeparatorsToImage()
                    detector.exportAllToImage()
                constructor.setVipsBlocks(vipsBlocks)
                constructor.setPageSize(pageWidth, pageHeight)
            else:
                vipsBlocks = vipsParser.getVipsBlocks()
                constructor.updateVipsBlocks(vipsBlocks)
                if self._graphicsOutput:
                    detector.setVisualBlocks(constructor.getVisualBlocks())
                    detector.fillPool()
                    detector.saveToImage("blocks" + iterationNumber)
            constructor.constructVisualStructure()
            if iterationNumber <= 5:
                self.sizeTresholdHeight -= 50
                self.sizeTresholdWidth -= 50
            if iterationNumber == 6:
                self.sizeTresholdHeight = 100
                self.sizeTresholdWidth = 100
            if iterationNumber == 7:
                self.sizeTresholdHeight = 80
                self.sizeTresholdWidth = 80
            if iterationNumber == 8:
                self.sizeTresholdHeight = 40
                self.sizeTresholdWidth = 10
            if iterationNumber == 9:
                self.sizeTresholdHeight = 1
                self.sizeTresholdWidth = 1
            iterationNumber += 1
        constructor.normalizeSeparatorsMinMax()
        vipsOutput = VipsOutput(self._pDoC)
        vipsOutput.setEscapeOutput(self._outputEscaping)
        vipsOutput.setOutputFileName(self._filename)
        vipsOutput.writeXML(constructor.getVisualStructure(), self._viewport)
        self.endTime = System.nanoTime()
        diff = self.endTime - self.startTime
        print ("Execution time of VIPS: " + diff + " ns; " + (diff / 1000000.0) + " ms; " + (diff / 1000000000.0) + " sec")
