#!/usr/bin/env python
""" generated source for module VipsSeparatorNonGraphicsDetector """
# 
#  * Tomas Popela, 2012
#  * VIPS - Visual Internet Page Segmentation
#  * Module - VipsSeparatorNonGraphicsDetector.java
#  
# package: org.fit.vips
import java.util.ArrayList

import java.util.Collections

import java.util.List

import org.fit.cssbox.layout.TextBox

# 
#  * Seperators detector (faster than VipsSeparatorGraphicsDetector).
#  * @author Tomas Popela
#  *
#  
class VipsSeparatorNonGraphicsDetector(VipsSeparatorDetector):
    """ generated source for class VipsSeparatorNonGraphicsDetector """
    _vipsBlocks = None
    _visualBlocks = None
    _horizontalSeparators = None
    _verticalSeparators = None
    _width = 0
    _height = 0
    _cleanSeparatorsTreshold = 0

    # 
    # 	 * Defaults constructor.
    # 	 * @param width Pools width
    # 	 * @param height Pools height
    # 	 
    def __init__(self, width, height):
        """ generated source for method __init__ """
        super(VipsSeparatorNonGraphicsDetector, self).__init__()
        self._width = width
        self._height = height
        self._horizontalSeparators = ArrayList()
        self._verticalSeparators = ArrayList()
        self._visualBlocks = ArrayList()

    def fillPoolWithBlocks(self, vipsBlock):
        """ generated source for method fillPoolWithBlocks """
        if vipsBlock.isVisualBlock():
            self._visualBlocks.add(vipsBlock)
        for vipsBlockChild in vipsBlock.getChildren():
            self.fillPoolWithBlocks(vipsBlockChild)

    # 
    # 	 * Fills pool with all visual blocks from VIPS blocks.
    # 	 * 
    # 	 
    def fillPool(self):
        """ generated source for method fillPool """
        if self._vipsBlocks != None:
            self.fillPoolWithBlocks(self._vipsBlocks)

    # 
    # 	 * Sets VIPS block, that will be used for separators computing.
    # 	 * @param vipsBlock Visual structure
    # 	 
    def setVipsBlock(self, vipsBlock):
        """ generated source for method setVipsBlock """
        self._vipsBlocks = vipsBlock
        self._visualBlocks.clear()
        self.fillPoolWithBlocks(vipsBlock)

    # 
    # 	 * Gets VIPS block that is used for separators computing.
    # 	 
    def getVipsBlock(self):
        """ generated source for method getVipsBlock """
        return self._vipsBlocks

    # 
    # 	 * Sets VIPS block, that will be used for separators computing.
    # 	 * @param visualBlocks List of visual blocks
    # 	 
    def setVisualBlocks(self, visualBlocks):
        """ generated source for method setVisualBlocks """
        self._visualBlocks.clear()
        self._visualBlocks.addAll(visualBlocks)

    # 
    # 	 * Gets VIPS block that is used for separators computing.
    # 	 * @return Visual structure
    # 	 
    def getVisualBlocks(self):
        """ generated source for method getVisualBlocks """
        return self._visualBlocks

    # 
    # 	 * Computes vertical visual separators
    # 	 
    def findVerticalSeparators(self):
        """ generated source for method findVerticalSeparators """
        for vipsBlock in _visualBlocks:
            #  block vertical coordinates
            #  for each separator that we have in pool
            for separator in _verticalSeparators:
                #  find separator, that intersects with our visual block
                if blockStart < separator.endPoint:
                    #  next there are six relations that the separator and visual block can have
                    #  if separator is inside visual block
                    if blockStart < separator.startPoint and blockEnd >= separator.endPoint:
                        tempSeparators.addAll(self._verticalSeparators)
                        # remove all separators, that are included in block
                        for other in tempSeparators:
                            if blockStart < other.startPoint and blockEnd > other.endPoint:
                                self._verticalSeparators.remove(other)
                        # find separator, that is on end of this block (if exists)
                        for other in _verticalSeparators:
                            #  and if it's necessary change it's start point
                            if blockEnd > other.startPoint and blockEnd < other.endPoint:
                                other.startPoint = blockEnd + 1
                                break
                        break
                    #  if block is inside another block -> skip it
                    if blockEnd < separator.startPoint:
                        break
                    #  if separator starts in the middle of block
                    if blockStart < separator.startPoint and blockEnd >= separator.startPoint:
                        #  change separator start's point coordinate
                        separator.startPoint = blockEnd + 1
                        break
                    #  if block is inside the separator
                    if blockStart >= separator.startPoint and blockEnd <= separator.endPoint:
                        if blockStart == separator.startPoint:
                            separator.startPoint = blockEnd + 1
                            break
                        if blockEnd == separator.endPoint:
                            separator.endPoint = blockStart - 1
                            break
                        #  add new separator that starts behind the block
                        self._verticalSeparators.add(self._verticalSeparators.indexOf(separator) + 1, Separator(blockEnd + 1, separator.endPoint))
                        #  change end point coordinates of separator, that's before block
                        separator.endPoint = blockStart - 1
                        break
                    #  if in one block is one separator ending and another one starting
                    if blockStart > separator.startPoint and blockStart < separator.endPoint:
                        #  find the next one
                        #  if it's not the last separator
                        if nextSeparatorIndex + 1 < len(self._verticalSeparators):
                            #  next separator is really starting before the block ends
                            if blockEnd > nextSeparator.startPoint and blockEnd < nextSeparator.endPoint:
                                #  change separator start point coordinate
                                separator.endPoint = blockStart - 1
                                nextSeparator.startPoint = blockEnd + 1
                                break
                            else:
                                tempSeparators.addAll(self._verticalSeparators)
                                # remove all separators, that are included in block
                                for other in tempSeparators:
                                    if blockStart < other.startPoint and other.endPoint < blockEnd:
                                        self._verticalSeparators.remove(other)
                                        continue 
                                    if blockEnd > other.startPoint and blockEnd < other.endPoint:
                                        #  change separator start's point coordinate
                                        other.startPoint = blockEnd + 1
                                        break
                                    if blockStart > other.startPoint and blockStart < other.endPoint:
                                        other.endPoint = blockStart - 1
                                        continue 
                                break
                    #  if separator ends in the middle of block
                    #  change it's end point coordinate
                    separator.endPoint = blockStart - 1
                    break

    # 
    # 	 * Computes horizontal visual separators
    # 	 
    def findHorizontalSeparators(self):
        """ generated source for method findHorizontalSeparators """
        for vipsBlock in _visualBlocks:
            #  block vertical coordinates
            #  for each separator that we have in pool
            for separator in _horizontalSeparators:
                #  find separator, that intersects with our visual block
                if blockStart < separator.endPoint:
                    #  next there are six relations that the separator and visual block can have
                    #  if separator is inside visual block
                    if blockStart < separator.startPoint and blockEnd >= separator.endPoint:
                        tempSeparators.addAll(self._horizontalSeparators)
                        # remove all separators, that are included in block
                        for other in tempSeparators:
                            if blockStart < other.startPoint and blockEnd > other.endPoint:
                                self._horizontalSeparators.remove(other)
                        # find separator, that is on end of this block (if exists)
                        for other in _horizontalSeparators:
                            #  and if it's necessary change it's start point
                            if blockEnd > other.startPoint and blockEnd < other.endPoint:
                                other.startPoint = blockEnd + 1
                                break
                        break
                    #  if block is inside another block -> skip it
                    if blockEnd < separator.startPoint:
                        break
                    #  if separator starts in the middle of block
                    if blockStart <= separator.startPoint and blockEnd >= separator.startPoint:
                        #  change separator start's point coordinate
                        separator.startPoint = blockEnd + 1
                        break
                    #  if block is inside the separator
                    if blockStart >= separator.startPoint and blockEnd < separator.endPoint:
                        if blockStart == separator.startPoint:
                            separator.startPoint = blockEnd + 1
                            break
                        if blockEnd == separator.endPoint:
                            separator.endPoint = blockStart - 1
                            break
                        #  add new separator that starts behind the block
                        self._horizontalSeparators.add(self._horizontalSeparators.indexOf(separator) + 1, Separator(blockEnd + 1, separator.endPoint))
                        #  change end point coordinates of separator, that's before block
                        separator.endPoint = blockStart - 1
                        break
                    #  if in one block is one separator ending and another one starting
                    if blockStart > separator.startPoint and blockStart < separator.endPoint:
                        #  find the next one
                        #  if it's not the last separator
                        if nextSeparatorIndex + 1 < len(self._horizontalSeparators):
                            #  next separator is really starting before the block ends
                            if blockEnd > nextSeparator.startPoint and blockEnd < nextSeparator.endPoint:
                                #  change separator start point coordinate
                                separator.endPoint = blockStart - 1
                                nextSeparator.startPoint = blockEnd + 1
                                break
                            else:
                                tempSeparators.addAll(self._horizontalSeparators)
                                # remove all separators, that are included in block
                                for other in tempSeparators:
                                    if blockStart < other.startPoint and other.endPoint < blockEnd:
                                        self._horizontalSeparators.remove(other)
                                        continue 
                                    if blockEnd > other.startPoint and blockEnd < other.endPoint:
                                        #  change separator start's point coordinate
                                        other.startPoint = blockEnd + 1
                                        break
                                    if blockStart > other.startPoint and blockStart < other.endPoint:
                                        other.endPoint = blockStart - 1
                                        continue 
                                break
                    #  if separator ends in the middle of block
                    #  change it's end point coordinate
                    separator.endPoint = blockStart - 1
                    break

    # 
    # 	 * Detects horizontal visual separators from Vips blocks.
    # 	 
    def detectHorizontalSeparators(self):
        """ generated source for method detectHorizontalSeparators """
        if len(self._visualBlocks) == 0:
            System.err.println("I don't have any visual blocks!")
            return
        self._horizontalSeparators.clear()
        self._horizontalSeparators.add(Separator(0, self._height))
        self.findHorizontalSeparators()
        # remove pool borders
        tempSeparators = ArrayList()
        tempSeparators.addAll(self._horizontalSeparators)
        for separator in tempSeparators:
            if separator.startPoint == 0:
                self._horizontalSeparators.remove(separator)
            if separator.endPoint == self._height:
                self._horizontalSeparators.remove(separator)
        if self._cleanSeparatorsTreshold != 0:
            cleanUpSeparators(self._horizontalSeparators)
        computeHorizontalWeights()
        sortSeparatorsByWeight(self._horizontalSeparators)

    # 
    # 	 * Detects vertical visual separators from Vips blocks.
    # 	 
    def detectVerticalSeparators(self):
        """ generated source for method detectVerticalSeparators """
        if len(self._visualBlocks) == 0:
            System.err.println("I don't have any visual blocks!")
            return
        self._verticalSeparators.clear()
        self._verticalSeparators.add(Separator(0, self._width))
        self.findVerticalSeparators()
        # remove pool borders
        tempSeparators = ArrayList()
        tempSeparators.addAll(self._verticalSeparators)
        for separator in tempSeparators:
            if separator.startPoint == 0:
                self._verticalSeparators.remove(separator)
            if separator.endPoint == self._width:
                self._verticalSeparators.remove(separator)
        if self._cleanSeparatorsTreshold != 0:
            cleanUpSeparators(self._verticalSeparators)
        computeVerticalWeights()
        sortSeparatorsByWeight(self._verticalSeparators)

    def cleanUpSeparators(self, separators):
        """ generated source for method cleanUpSeparators """
        tempList = ArrayList()
        tempList.addAll(separators)
        for separator in tempList:
            if width < self._cleanSeparatorsTreshold:
                separators.remove(separator)

    # 
    # 	 * Sorts given separators by it's weight.
    # 	 * @param separators Separators
    # 	 
    def sortSeparatorsByWeight(self, separators):
        """ generated source for method sortSeparatorsByWeight """
        Collections.sort(separators)

    # 
    # 	 * Computes weights for vertical separators.
    # 	 
    def computeVerticalWeights(self):
        """ generated source for method computeVerticalWeights """
        for separator in _verticalSeparators:
            ruleOne(separator)
            ruleTwo(separator, False)
            ruleThree(separator, False)

    # 
    # 	 * Computes weights for horizontal separators.
    # 	 
    def computeHorizontalWeights(self):
        """ generated source for method computeHorizontalWeights """
        for separator in _horizontalSeparators:
            ruleOne(separator)
            ruleTwo(separator, True)
            ruleThree(separator, True)
            ruleFour(separator)
            ruleFive(separator)

    # 
    # 	 * The greater the distance between blocks on different
    # 	 * side of the separator, the higher the weight. <p>
    # 	 * For every 10 points of width we increase weight by 1 points.
    # 	 * @param separator Separator
    # 	 
    def ruleOne(self, separator):
        """ generated source for method ruleOne """
        width = separator.endPoint - separator.startPoint + 1
        # separator.weight += width;
        if width > 55:
            separator.weight += 12
        if width > 45 and width <= 55:
            separator.weight += 10
        if width > 35 and width <= 45:
            separator.weight += 8
        if width > 25 and width <= 35:
            separator.weight += 6
        elif width > 15 and width <= 25:
            separator.weight += 4
        elif width > 8 and width <= 15:
            separator.weight += 2
        else:
            separator.weight += 1

    # 
    # 	 * If a visual separator is overlapped with some certain HTML
    # 	 * tags (e.g., the &lt;HR&gt; HTML tag), its weight is set to be higher.
    # 	 * @param separator Separator
    # 	 
    def ruleTwo(self, separator, horizontal):
        """ generated source for method ruleTwo """
        overlappedElements = ArrayList()
        if horizontal:
            findHorizontalOverlappedElements(separator, overlappedElements)
        else:
            findVerticalOverlappedElements(separator, overlappedElements)
        if len(overlappedElements) == 0:
            return
        for vipsBlock in overlappedElements:
            if vipsBlock.getBox().getNode().getNodeName() == "hr":
                separator.weight += 2
                break

    def findHorizontalOverlappedElements(self, separator, result):
        """ generated source for method findHorizontalOverlappedElements """
        for vipsBlock in _visualBlocks:
            if topEdge > separator.startPoint and topEdge < separator.endPoint and bottomEdge > separator.endPoint:
                result.add(vipsBlock)
            if topEdge < separator.startPoint and bottomEdge > separator.startPoint and bottomEdge < separator.endPoint:
                result.add(vipsBlock)
            if topEdge >= separator.startPoint and bottomEdge <= separator.endPoint:
                result.add(vipsBlock)

    def findVerticalOverlappedElements(self, separator, result):
        """ generated source for method findVerticalOverlappedElements """
        for vipsBlock in _visualBlocks:
            if leftEdge > separator.startPoint and leftEdge < separator.endPoint and rightEdge > separator.endPoint:
                result.add(vipsBlock)
            if leftEdge < separator.startPoint and rightEdge > separator.startPoint and rightEdge < separator.endPoint:
                result.add(vipsBlock)
            if leftEdge >= separator.startPoint and rightEdge <= separator.endPoint:
                result.add(vipsBlock)

    def ruleThree(self, separator, horizontal):
        """ generated source for method ruleThree """
        topAdjacentElements = ArrayList()
        bottomAdjacentElements = ArrayList()
        if horizontal:
            findHorizontalAdjacentBlocks(separator, topAdjacentElements, bottomAdjacentElements)
        else:
            findVerticalAdjacentBlocks(separator, topAdjacentElements, bottomAdjacentElements)
        if len(topAdjacentElements) < 1 or len(bottomAdjacentElements) < 1:
            return
        weightIncreased = False
        for top in topAdjacentElements:
            for bottom in bottomAdjacentElements:
                if not top.getBgColor() == bottom.getBgColor():
                    separator.weight += 2
                    weightIncreased = True
                    break
            if weightIncreased:
                break

    def findHorizontalAdjacentBlocks(self, separator, resultTop, resultBottom):
        """ generated source for method findHorizontalAdjacentBlocks """
        for vipsBlock in _visualBlocks:
            if topEdge == separator.endPoint + 1 and bottomEdge > separator.endPoint + 1:
                resultBottom.add(vipsBlock)
            if bottomEdge == separator.startPoint - 1 and topEdge < separator.startPoint - 1:
                resultTop.add(0, vipsBlock)

    def findVerticalAdjacentBlocks(self, separator, resultLeft, resultRight):
        """ generated source for method findVerticalAdjacentBlocks """
        for vipsBlock in _visualBlocks:
            if leftEdge == separator.endPoint + 1 and rightEdge > separator.endPoint + 1:
                resultRight.add(vipsBlock)
            if rightEdge == separator.startPoint - 1 and leftEdge < separator.startPoint - 1:
                resultLeft.add(0, vipsBlock)

    def ruleFour(self, separator):
        """ generated source for method ruleFour """
        topAdjacentElements = ArrayList()
        bottomAdjacentElements = ArrayList()
        self.findHorizontalAdjacentBlocks(separator, topAdjacentElements, bottomAdjacentElements)
        if len(topAdjacentElements) < 1 or len(bottomAdjacentElements) < 1:
            return
        weightIncreased = False
        for top in topAdjacentElements:
            for bottom in bottomAdjacentElements:
                if diff != 0:
                    separator.weight += 2
                    weightIncreased = True
                    break
                else:
                    if not top.getFontWeight() == bottom.getFontWeight():
                        separator.weight += 2
            if weightIncreased:
                break
        weightIncreased = False
        for top in topAdjacentElements:
            for bottom in bottomAdjacentElements:
                if top.getFontSize() < bottom.getFontSize():
                    separator.weight += 2
                    weightIncreased = True
                    break
            if weightIncreased:
                break

    def ruleFive(self, separator):
        """ generated source for method ruleFive """
        topAdjacentElements = ArrayList()
        bottomAdjacentElements = ArrayList()
        self.findHorizontalAdjacentBlocks(separator, topAdjacentElements, bottomAdjacentElements)
        if len(topAdjacentElements) < 1 or len(bottomAdjacentElements) < 1:
            return
        weightDecreased = False
        for top in topAdjacentElements:
            for bottom in bottomAdjacentElements:
                if isinstance(, (TextBox, )) and isinstance(, (TextBox, )):
                    separator.weight -= 2
                    weightDecreased = True
                    break
            if weightDecreased:
                break

    def getHorizontalSeparators(self):
        """ generated source for method getHorizontalSeparators """
        return self._horizontalSeparators

    def setHorizontalSeparators(self, separators):
        """ generated source for method setHorizontalSeparators """
        self._horizontalSeparators.clear()
        self._horizontalSeparators.addAll(separators)

    def setVerticalSeparators(self, separators):
        """ generated source for method setVerticalSeparators """
        self._verticalSeparators.clear()
        self._verticalSeparators.addAll(separators)

    def getVerticalSeparators(self):
        """ generated source for method getVerticalSeparators """
        return self._verticalSeparators

    def setCleanUpSeparators(self, treshold):
        """ generated source for method setCleanUpSeparators """
        self._cleanSeparatorsTreshold = treshold

    def isCleanUpEnabled(self):
        """ generated source for method isCleanUpEnabled """
        if self._cleanSeparatorsTreshold == 0:
            return True
        return False

