#!/usr/bin/env python
""" generated source for module VipsSeparatorDetector """
# 
#  * Tomas Popela, 2012
#  * VIPS - Visual Internet Page Segmentation
#  * Module - VipsSeparatorDetector.java
#  
# package: org.fit.vips
import java.util.List

# 
#  * Common interface for separators detectors.
#  * @author Tomas Popela
#  *
#  
class VipsSeparatorDetector(object):
    """ generated source for interface VipsSeparatorDetector """
    __metaclass__ = ABCMeta
    @abstractmethod
    def fillPool(self):
        """ generated source for method fillPool """

    @abstractmethod
    def setVipsBlock(self, vipsBlock):
        """ generated source for method setVipsBlock """

    @abstractmethod
    def getVipsBlock(self):
        """ generated source for method getVipsBlock """

    @abstractmethod
    def setVisualBlocks(self, visualBlocks):
        """ generated source for method setVisualBlocks """

    @abstractmethod
    def getVisualBlocks(self):
        """ generated source for method getVisualBlocks """

    @abstractmethod
    def detectHorizontalSeparators(self):
        """ generated source for method detectHorizontalSeparators """

    @abstractmethod
    def detectVerticalSeparators(self):
        """ generated source for method detectVerticalSeparators """

    @abstractmethod
    def getHorizontalSeparators(self):
        """ generated source for method getHorizontalSeparators """

    @abstractmethod
    def setHorizontalSeparators(self, separators):
        """ generated source for method setHorizontalSeparators """

    @abstractmethod
    def setVerticalSeparators(self, separators):
        """ generated source for method setVerticalSeparators """

    @abstractmethod
    def getVerticalSeparators(self):
        """ generated source for method getVerticalSeparators """

    @abstractmethod
    def setCleanUpSeparators(self, treshold):
        """ generated source for method setCleanUpSeparators """

    @abstractmethod
    def isCleanUpEnabled(self):
        """ generated source for method isCleanUpEnabled """

