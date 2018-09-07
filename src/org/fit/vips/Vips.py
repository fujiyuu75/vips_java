#!/usr/bin/env python
""" generated source for module Vips """
# 
#  * Tomas Popela, 2012
#  * VIPS - Visual Internet Page Segmentation
#  * Module - Vips.java

from urlparse import urlparse


class Vips(object):
    """ generated source for class Vips """
    _url = None
    _domAnalyzer = None
    _browserCanvas = None
    _viewport = None
    _graphicsOutput = False
    _outputToFolder = False
    _outputEscaping = True
    _pDoC = 11
    _filename = ""
    sizeTresholdWidth = 350
    sizeTresholdHeight = 400
    originalOut = None
    startTime = 0
    endTime = 0

    # 
    # 	 * Default constructor
    # 	 
    def __init__(self):
        """ generated source for method __init__ """


     # * Enables or disables graphics output of VIPS algorithm.
     # * @param enable True for enable, otherwise false.

    def enableGraphicsOutput(self, enable):
        """ generated source for method enableGraphicsOutput """
        self._graphicsOutput = enable

    #
    # 	 * Enables or disables creation of new directory for every algorithm run.
    # 	 * @param enable True for enable, otherwise false.
    #
    def enableOutputToFolder(self, enable):
        """ generated source for method enableOutputToFolder """
        self._outputToFolder = enable

    #
    # 	 * Enables or disables output XML character escaping.
    # 	 * @param enable True for enable, otherwise false.
    #
    def enableOutputEscaping(self, enable):
        """ generated source for method enableOutputEscaping """
        self._outputEscaping = enable

    #
    # 	 * Sets permitted degree of coherence (pDoC) value.
    # 	 * @param value pDoC value.
    #
    def setPredefinedDoC(self, value):
        """ generated source for method setPredefinedDoC """
        if value <= 0 or value > 11:
            System.err.println("pDoC value must be between 1 and 11! Not " + value + "!")
            return
        else:
            self._pDoC = value

    #
    # 	 * Sets web page's URL
    # 	 * @param url Url
    # 	 * @throws MalformedURLException
    #
    def setUrl(self, url):
        """ generated source for method setUrl """
        try:
            if url.startsWith("http://") or url.startsWith("https://"):
                self._url = URL(url)
            else:
                self._url = URL("http://" + url)
        except Exception as e:
            System.err.println("Invalid address: " + url)

    #
    # 	 * Parses a builds DOM tree from page source.
    # 	 * @param urlStream Input stream with page source.
    #
    def getDomTree(self, urlStream):
        """ generated source for method getDomTree """
        docSource = None
        try:
            docSource = DefaultDocumentSource(urlStream)
            self._domAnalyzer = DOMAnalyzer(domTree, self._url)
            self._domAnalyzer.attributesToStyles()
            self._domAnalyzer.addStyleSheet(None, CSSNorm.stdStyleSheet(), DOMAnalyzer.Origin.AGENT)
            self._domAnalyzer.addStyleSheet(None, CSSNorm.userStyleSheet(), DOMAnalyzer.Origin.AGENT)
            self._domAnalyzer.getStyleSheets()
        except Exception as e:
            System.err.print_(e.getMessage())

    #
    # 	 * Gets page's viewport
    #
    def getViewport(self):
        """ generated source for method getViewport """
        self._browserCanvas = BrowserCanvas(self._domAnalyzer.getRoot(), self._domAnalyzer, java.awt.Dimension(1000, 600), self._url)
        self._viewport = self._browserCanvas.getViewport()

    #
    # 	 * Exports rendered page to image.
    #
    def exportPageToImage(self):
        """ generated source for method exportPageToImage """
        try:
            ImageIO.write(page, "png", File(filename))
        except Exception as e:
            System.err.println("Error: " + e.getMessage())
            e.printStackTrace()

    #
    # 	 * Generates folder filename
    # 	 * @return Folder filename
    #
    def generateFolderName(self):
        """ generated source for method generateFolderName """
        outputFolder = ""
        cal = Calendar.getInstance()
        sdf = SimpleDateFormat("dd_MM_yyyy_HH_mm_ss")
        outputFolder += sdf.format(cal.getTime())
        outputFolder += "_"
        outputFolder += self._url.getHost().replaceAll("\\.", "_").replaceAll("/", "_")
        return outputFolder

    def performSegmentation(self):
        """ generated source for method performSegmentation """
        self.startTime = System.nanoTime()
        numberOfIterations = 10
        pageWidth = self._viewport.getWidth()
        pageHeight = self._viewport.getHeight()
        if self._graphicsOutput:
            self.exportPageToImage()
        detector = VipsSeparatorGraphicsDetector()
        vipsParser = VipsParser(self._viewport)
        constructor = VisualStructureConstructor(self._pDoC)
        constructor.setGraphicsOutput(self._graphicsOutput)
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

    @overloaded
    def startSegmentation(self, url):
        """ generated source for method startSegmentation """
        self.setUrl(url)
        self.startSegmentation()

    def restoreOut(self):
        """ generated source for method restoreOut """
        if self.originalOut != None:
            System.setOut(self.originalOut)

    def redirectOut(self):
        """ generated source for method redirectOut """
        self.originalOut = System.out
        System.setOut(PrintStream(OutputStream()))

    @startSegmentation.register(object)
    def startSegmentation_0(self):
        """ generated source for method startSegmentation_0 """
        try:
            self._url.openConnection()
            self.redirectOut()
            self.getDomTree(self._url)
            self.startTime = System.nanoTime()
            self.getViewport()
            self.restoreOut()
            if self._outputToFolder:
                outputFolder = self.generateFolderName()
                if not File(outputFolder).mkdir():
                    System.err.println("Something goes wrong during directory creation!")
                else:
                    oldWorkingDirectory = System.getProperty("user.dir")
                    newWorkingDirectory += oldWorkingDirectory + "/" + outputFolder + "/"
                    System.setProperty("user.dir", newWorkingDirectory)
            self.performSegmentation()
            if self._outputToFolder:
                System.setProperty("user.dir", oldWorkingDirectory)
        except Exception as e:
            System.err.println("Something's wrong!")
            e.printStackTrace()

    def setOutputFileName(self, filename):
        """ generated source for method setOutputFileName """
        if not filename == "":
            self._filename = filename
        else:
            print ("Invalid filename!")
