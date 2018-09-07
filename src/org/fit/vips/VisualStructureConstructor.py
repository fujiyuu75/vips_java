#!/usr/bin/env python
""" generated source for module VisualStructureConstructor """
# 
#  * Tomas Popela, 2012
#  * VIPS - Visual Internet Page Segmentation
#  * Module - VisualStructureConstructor.java
#  
# package: org.fit.vips
import java.util.ArrayList

import java.util.Collections

import java.util.HashSet

import java.util.List

# 
#  * Class that constructs final visual structure of page.
#  * @author Tomas Popela
#  *
#  
class VisualStructureConstructor(object):
    """ generated source for class VisualStructureConstructor """
    _vipsBlocks = None
    _visualBlocks = None
    _visualStructure = None
    _horizontalSeparators = None
    _verticalSeparators = None
    _pageWidth = 0
    _pageHeight = 0
    _srcOrder = 1
    _iteration = 0
    _pDoC = 5
    _maxDoC = 11
    _minDoC = 11
    _graphicsOutput = True

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        self._horizontalSeparators = ArrayList()
        self._verticalSeparators = ArrayList()

    @__init__.register(object, int)
    def __init___0(self, pDoC):
        """ generated source for method __init___0 """
        self._horizontalSeparators = ArrayList()
        self._verticalSeparators = ArrayList()
        setPDoC(pDoC)

    @__init__.register(object, VipsBlock)
    def __init___1(self, vipsBlocks):
        """ generated source for method __init___1 """
        self._horizontalSeparators = ArrayList()
        self._verticalSeparators = ArrayList()
        self._vipsBlocks = vipsBlocks

    @__init__.register(object, VipsBlock, int)
    def __init___2(self, vipsBlocks, pDoC):
        """ generated source for method __init___2 """
        self._horizontalSeparators = ArrayList()
        self._verticalSeparators = ArrayList()
        self._vipsBlocks = vipsBlocks
        setPDoC(pDoC)

    # 
    # 	 * Sets Permitted Degree of Coherence
    # 	 * @param pDoC Permitted Degree of Coherence
    # 	 
    def setPDoC(self, pDoC):
        """ generated source for method setPDoC """
        if pDoC <= 0 or pDoC > 11:
            System.err.println("pDoC value must be between 1 and 11! Not " + pDoC + "!")
            return
        else:
            self._pDoC = pDoC

    # 
    # 	 * Enables of disables graphics output
    # 	 * @param enabled Enabled
    # 	 
    def setGraphicsOutput(self, enabled):
        """ generated source for method setGraphicsOutput """
        self._graphicsOutput = enabled

    # 
    # 	 * Tries to construct visual structure
    # 	 
    def constructVisualStructure(self):
        """ generated source for method constructVisualStructure """
        self._iteration += 1
        #  in first iterations we try to find vertical separators before horizontal
        if self._iteration < 4:
            constructVerticalVisualStructure()
            constructHorizontalVisualStructure()
            constructVerticalVisualStructure()
            constructHorizontalVisualStructure()
        else:
            #  and now we are trying to find horizontal before verical sepators
            constructHorizontalVisualStructure()
            constructVerticalVisualStructure()
        if self._iteration != 1:
            updateSeparators()
        # sets order to visual structure
        self._srcOrder = 1
        setOrder(self._visualStructure)
        #  if graphics output is enabled
        if self._graphicsOutput:
            exportSeparators()

    # 
    # 	 * Constructs visual structure with blocks and horizontal separators
    # 	 
    def constructHorizontalVisualStructure(self):
        """ generated source for method constructHorizontalVisualStructure """
        #  first run
        if self._visualStructure == None:
            if self._graphicsOutput:
                detector = VipsSeparatorGraphicsDetector(self._pageWidth, self._pageHeight)
            else:
                detector = VipsSeparatorNonGraphicsDetector(self._pageWidth, self._pageHeight)
            detector.setCleanUpSeparators(3)
            detector.setVipsBlock(self._vipsBlocks)
            detector.setVisualBlocks(self._visualBlocks)
            detector.detectHorizontalSeparators()
            self._horizontalSeparators = detector.getHorizontalSeparators()
            Collections.sort(self._horizontalSeparators)
            self._visualStructure = VisualStructure()
            self._visualStructure.setId("1")
            self._visualStructure.setNestedBlocks(self._visualBlocks)
            self._visualStructure.setWidth(self._pageWidth)
            self._visualStructure.setHeight(self._pageHeight)
            for separator in _horizontalSeparators:
                separator.setLeftUp(self._visualStructure.getX(), separator.startPoint)
                separator.setRightDown(self._visualStructure.getX() + self._visualStructure.getWidth(), separator.endPoint)
            constructWithHorizontalSeparators(self._visualStructure)
        else:
            findListVisualStructures(self._visualStructure, listStructures)
            for childVisualStructure in listStructures:
                if self._graphicsOutput:
                    detector = VipsSeparatorGraphicsDetector(self._pageWidth, self._pageHeight)
                else:
                    detector = VipsSeparatorNonGraphicsDetector(self._pageWidth, self._pageHeight)
                detector.setCleanUpSeparators(4)
                detector.setVipsBlock(self._vipsBlocks)
                detector.setVisualBlocks(childVisualStructure.getNestedBlocks())
                detector.detectHorizontalSeparators()
                self._horizontalSeparators = detector.getHorizontalSeparators()
                for separator in _horizontalSeparators:
                    separator.setLeftUp(childVisualStructure.getX(), separator.startPoint)
                    separator.setRightDown(childVisualStructure.getX() + childVisualStructure.getWidth(), separator.endPoint)
                constructWithHorizontalSeparators(childVisualStructure)

    # 
    # 	 * Constructs visual structure with blocks and vertical separators
    # 	 
    def constructVerticalVisualStructure(self):
        """ generated source for method constructVerticalVisualStructure """
        #  first run
        if self._visualStructure == None:
            if self._graphicsOutput:
                detector = VipsSeparatorGraphicsDetector(self._pageWidth, self._pageHeight)
            else:
                detector = VipsSeparatorNonGraphicsDetector(self._pageWidth, self._pageHeight)
            detector.setCleanUpSeparators(3)
            detector.setVipsBlock(self._vipsBlocks)
            detector.setVisualBlocks(self._visualBlocks)
            detector.detectVerticalSeparators()
            self._verticalSeparators = detector.getVerticalSeparators()
            Collections.sort(self._verticalSeparators)
            self._visualStructure = VisualStructure()
            self._visualStructure.setId("1")
            self._visualStructure.setNestedBlocks(self._visualBlocks)
            self._visualStructure.setWidth(self._pageWidth)
            self._visualStructure.setHeight(self._pageHeight)
            for separator in _verticalSeparators:
                separator.setLeftUp(separator.startPoint, self._visualStructure.getY())
                separator.setRightDown(separator.endPoint, self._visualStructure.getY() + self._visualStructure.getHeight())
            constructWithVerticalSeparators(self._visualStructure)
        else:
            findListVisualStructures(self._visualStructure, listStructures)
            for childVisualStructure in listStructures:
                if self._graphicsOutput:
                    detector = VipsSeparatorGraphicsDetector(self._pageWidth, self._pageHeight)
                else:
                    detector = VipsSeparatorNonGraphicsDetector(self._pageWidth, self._pageHeight)
                detector.setCleanUpSeparators(4)
                detector.setVipsBlock(self._vipsBlocks)
                detector.setVisualBlocks(childVisualStructure.getNestedBlocks())
                detector.detectVerticalSeparators()
                self._verticalSeparators = detector.getVerticalSeparators()
                for separator in _verticalSeparators:
                    separator.setLeftUp(separator.startPoint, childVisualStructure.getY())
                    separator.setRightDown(separator.endPoint, childVisualStructure.getY() + childVisualStructure.getHeight())
                constructWithVerticalSeparators(childVisualStructure)

    # 
    # 	 * Performs actual constructing of visual structure with horizontal separators
    # 	 * @param actualStructure Actual visual structure
    # 	 
    def constructWithHorizontalSeparators(self, actualStructure):
        """ generated source for method constructWithHorizontalSeparators """
        #  if we have no visual blocks or separators
        if actualStructure.getNestedBlocks().size() == 0 or len(self._horizontalSeparators) == 0:
            return
        topVisualStructure = None
        bottomVisualStructure = None
        nestedBlocks = None
        # construct children visual structures
        for separator in _horizontalSeparators:
            if actualStructure.getChildrenVisualStructures().size() == 0:
                topVisualStructure = VisualStructure()
                topVisualStructure.setX(actualStructure.getX())
                topVisualStructure.setY(actualStructure.getY())
                topVisualStructure.setHeight((separator.startPoint - 1) - actualStructure.getY())
                topVisualStructure.setWidth(actualStructure.getWidth())
                actualStructure.addChild(topVisualStructure)
                bottomVisualStructure = VisualStructure()
                bottomVisualStructure.setX(actualStructure.getX())
                bottomVisualStructure.setY(separator.endPoint + 1)
                bottomVisualStructure.setHeight((actualStructure.getHeight() + actualStructure.getY()) - separator.endPoint - 1)
                bottomVisualStructure.setWidth(actualStructure.getWidth())
                actualStructure.addChild(bottomVisualStructure)
                nestedBlocks = actualStructure.getNestedBlocks()
            else:
                for childVisualStructure in actualStructure.getChildrenVisualStructures():
                    if separator.startPoint >= childVisualStructure.getY() and separator.endPoint <= (childVisualStructure.getY() + childVisualStructure.getHeight()):
                        topVisualStructure = VisualStructure()
                        topVisualStructure.setX(childVisualStructure.getX())
                        topVisualStructure.setY(childVisualStructure.getY())
                        topVisualStructure.setHeight((separator.startPoint - 1) - childVisualStructure.getY())
                        topVisualStructure.setWidth(childVisualStructure.getWidth())
                        actualStructure.addChildAt(topVisualStructure, index)
                        bottomVisualStructure = VisualStructure()
                        bottomVisualStructure.setX(childVisualStructure.getX())
                        bottomVisualStructure.setY(separator.endPoint + 1)
                        bottomVisualStructure.setHeight(height)
                        bottomVisualStructure.setWidth(childVisualStructure.getWidth())
                        actualStructure.addChildAt(bottomVisualStructure, index + 1)
                        oldStructure = childVisualStructure
                        break
                if oldStructure != None:
                    nestedBlocks = oldStructure.getNestedBlocks()
                    actualStructure.getChildrenVisualStructures().remove(oldStructure)
            if topVisualStructure == None or bottomVisualStructure == None:
                return
            for vipsBlock in nestedBlocks:
                if vipsBlock.getBox().getAbsoluteContentY() <= separator.startPoint:
                    topVisualStructure.addNestedBlock(vipsBlock)
                else:
                    bottomVisualStructure.addNestedBlock(vipsBlock)
            topVisualStructure = None
            bottomVisualStructure = None
        #  set id for visual structures
        iterator = 1
        for visualStructure in actualStructure.getChildrenVisualStructures():
            visualStructure.setId(actualStructure.getId() + "-" + iterator)
            iterator += 1
        allSeparatorsInBlock = ArrayList()
        allSeparatorsInBlock.addAll(self._horizontalSeparators)
        # remove all children separators
        for vs in actualStructure.getChildrenVisualStructures():
            vs.getHorizontalSeparators().clear()
        # save all horizontal separators in my region
        actualStructure.addHorizontalSeparators(self._horizontalSeparators)

    # 
    # 	 * Performs actual constructing of visual structure with vertical separators
    # 	 * @param actualStructure Actual visual structure
    # 	 
    def constructWithVerticalSeparators(self, actualStructure):
        """ generated source for method constructWithVerticalSeparators """
        #  if we have no visual blocks or separators
        if actualStructure.getNestedBlocks().size() == 0 or len(self._verticalSeparators) == 0:
            return
        leftVisualStructure = None
        rightVisualStructure = None
        nestedBlocks = None
        # construct children visual structures
        for separator in _verticalSeparators:
            if actualStructure.getChildrenVisualStructures().size() == 0:
                leftVisualStructure = VisualStructure()
                leftVisualStructure.setX(actualStructure.getX())
                leftVisualStructure.setY(actualStructure.getY())
                leftVisualStructure.setHeight(actualStructure.getHeight())
                leftVisualStructure.setWidth((separator.startPoint - 1) - actualStructure.getX())
                actualStructure.addChild(leftVisualStructure)
                rightVisualStructure = VisualStructure()
                rightVisualStructure.setX(separator.endPoint + 1)
                rightVisualStructure.setY(actualStructure.getY())
                rightVisualStructure.setHeight(actualStructure.getHeight())
                rightVisualStructure.setWidth((actualStructure.getWidth() + actualStructure.getX()) - separator.endPoint - 1)
                actualStructure.addChild(rightVisualStructure)
                nestedBlocks = actualStructure.getNestedBlocks()
            else:
                for childVisualStructure in actualStructure.getChildrenVisualStructures():
                    if separator.startPoint >= childVisualStructure.getX() and separator.endPoint <= (childVisualStructure.getX() + childVisualStructure.getWidth()):
                        leftVisualStructure = VisualStructure()
                        leftVisualStructure.setX(childVisualStructure.getX())
                        leftVisualStructure.setY(childVisualStructure.getY())
                        leftVisualStructure.setHeight(childVisualStructure.getHeight())
                        leftVisualStructure.setWidth((separator.startPoint - 1) - childVisualStructure.getX())
                        actualStructure.addChildAt(leftVisualStructure, index)
                        rightVisualStructure = VisualStructure()
                        rightVisualStructure.setX(separator.endPoint + 1)
                        rightVisualStructure.setY(childVisualStructure.getY())
                        rightVisualStructure.setHeight(childVisualStructure.getHeight())
                        rightVisualStructure.setWidth(width)
                        actualStructure.addChildAt(rightVisualStructure, index + 1)
                        oldStructure = childVisualStructure
                        break
                if oldStructure != None:
                    nestedBlocks = oldStructure.getNestedBlocks()
                    actualStructure.getChildrenVisualStructures().remove(oldStructure)
            if leftVisualStructure == None or rightVisualStructure == None:
                return
            for vipsBlock in nestedBlocks:
                if vipsBlock.getBox().getAbsoluteContentX() <= separator.startPoint:
                    leftVisualStructure.addNestedBlock(vipsBlock)
                else:
                    rightVisualStructure.addNestedBlock(vipsBlock)
            leftVisualStructure = None
            rightVisualStructure = None
        #  set id for visual structures
        iterator = 1
        for visualStructure in actualStructure.getChildrenVisualStructures():
            visualStructure.setId(actualStructure.getId() + "-" + iterator)
            iterator += 1
        allSeparatorsInBlock = ArrayList()
        allSeparatorsInBlock.addAll(self._verticalSeparators)
        # remove all children separators
        for vs in actualStructure.getChildrenVisualStructures():
            vs.getVerticalSeparators().clear()
        # save all horizontal separators in my region
        actualStructure.addVerticalSeparators(self._verticalSeparators)

    # 
    # 	 * Exports all separators to output images
    # 	 
    def exportSeparators(self):
        """ generated source for method exportSeparators """
        detector = VipsSeparatorGraphicsDetector(self._pageWidth, self._pageHeight)
        allSeparators = ArrayList()
        getAllHorizontalSeparators(self._visualStructure, allSeparators)
        Collections.sort(allSeparators)
        detector.setHorizontalSeparators(allSeparators)
        detector.exportHorizontalSeparatorsToImage(self._iteration)
        allSeparators.clear()
        getAllVerticalSeparators(self._visualStructure, allSeparators)
        Collections.sort(allSeparators)
        detector.setVerticalSeparators(allSeparators)
        detector.exportVerticalSeparatorsToImage(self._iteration)
        detector.setVisualBlocks(self._visualBlocks)
        detector.exportAllToImage(self._iteration)

    # 
    # 	 * Sets page's size
    # 	 * @param width Page's width
    # 	 * @param height Page's height
    # 	 
    def setPageSize(self, width, height):
        """ generated source for method setPageSize """
        self._pageHeight = height
        self._pageWidth = width

    # 
    # 	 * @return Returns VipsBlocks structure with all blocks from page
    # 	 
    def getVipsBlocks(self):
        """ generated source for method getVipsBlocks """
        return self._vipsBlocks

    # 
    # 	 * @return Returns final visual structure
    # 	 
    def getVisualStructure(self):
        """ generated source for method getVisualStructure """
        return self._visualStructure

    # 
    # 	 * Finds all visual blocks in VipsBlock structure
    # 	 * @param vipsBlock Actual VipsBlock
    # 	 * @param results	Results
    # 	 
    def findVisualBlocks(self, vipsBlock, results):
        """ generated source for method findVisualBlocks """
        if vipsBlock.isVisualBlock():
            results.add(vipsBlock)
        for child in vipsBlock.getChildren():
            self.findVisualBlocks(child, results)

    # 
    # 	 * Sets VipsBlock structure and also finds and saves all visual blocks from its
    # 	 * @param vipsBlocks VipsBlock structure
    # 	 
    def setVipsBlocks(self, vipsBlocks):
        """ generated source for method setVipsBlocks """
        self._vipsBlocks = vipsBlocks
        self._visualBlocks = ArrayList()
        self.findVisualBlocks(vipsBlocks, self._visualBlocks)

    # 
    # 	 * Returns all visual blocks in page
    # 	 * @return Visual Blocks
    # 	 
    def getVisualBlocks(self):
        """ generated source for method getVisualBlocks """
        return self._visualBlocks

    # 
    # 	 * Returns all horizontal separators detected on page
    # 	 * @return List of horizontal separators
    # 	 
    def getHorizontalSeparators(self):
        """ generated source for method getHorizontalSeparators """
        return self._horizontalSeparators

    # 
    # 	 * Sets horizontal separators to page
    # 	 * @param  horizontalSeparators List of horizontal separators
    # 	 
    def setHorizontalSeparator(self, horizontalSeparators):
        """ generated source for method setHorizontalSeparator """
        self._horizontalSeparators = horizontalSeparators

    # 
    # 	 * Returns all vertical separators detected on page
    # 	 * @return List of vertical separators
    # 	 
    def getVerticalSeparators(self):
        """ generated source for method getVerticalSeparators """
        return self._verticalSeparators

    # 
    # 	 * Sets vertical separators to page
    # 	 * @param  verticalSeparators List of vertical separators
    # 	 
    def setVerticalSeparator(self, verticalSeparators):
        """ generated source for method setVerticalSeparator """
        self._verticalSeparators = verticalSeparators

    # 
    # 	 * Sets vertical and horizontal separators to page
    # 	 * @param horizontalSeparators List of horizontal separators
    # 	 * @param verticalSeparators List of vertical separators
    # 	 
    def setSeparators(self, horizontalSeparators, verticalSeparators):
        """ generated source for method setSeparators """
        self._verticalSeparators = verticalSeparators
        self._horizontalSeparators = horizontalSeparators

    # 
    # 	 * Finds list visual structures in visual structure tree
    # 	 * @param visualStructure Actual structure
    # 	 * @param results Results
    # 	 
    def findListVisualStructures(self, visualStructure, results):
        """ generated source for method findListVisualStructures """
        if visualStructure.getChildrenVisualStructures().size() == 0:
            results.add(visualStructure)
        for child in visualStructure.getChildrenVisualStructures():
            self.findListVisualStructures(child, results)

    # 
    # 	 * Replaces given old blocks with given new one
    # 	 * @param oldBlocks	List of old blocks
    # 	 * @param newBlocks List of new blocks
    # 	 * @param actualStructure Actual Structure
    # 	 * @param pathStructures Path from structure to root of the structure
    # 	 
    def replaceBlocksInPredecessors(self, oldBlocks, newBlocks, actualStructure, pathStructures):
        """ generated source for method replaceBlocksInPredecessors """
        for child in actualStructure.getChildrenVisualStructures():
            self.replaceBlocksInPredecessors(oldBlocks, newBlocks, child, pathStructures)
        for structureId in pathStructures:
            if actualStructure.getId() == structureId:
                tempBlocks.addAll(actualStructure.getNestedBlocks())
                # remove old blocks
                for block in tempBlocks:
                    for oldBlock in oldBlocks:
                        if block == oldBlock:
                            actualStructure.getNestedBlocks().remove(block)
                # add new blocks
                actualStructure.addNestedBlocks(newBlocks)

    # 
    # 	 * Generates element's id's for elements that are on path
    # 	 * @param Path (Start visual strucure id)
    # 	 * @return List of id's
    # 	 
    def generatePathStructures(self, path):
        """ generated source for method generatePathStructures """
        pathStructures = ArrayList()
        aaa = path.split("-")
        tmp = ""
        i = 0
        while i < len(aaa):
            tmp += aaa[i]
            pathStructures.add(tmp)
            tmp += "-"
            i += 1
        return pathStructures

    # 
    # 	 * Updates VipsBlock structure with the new one and also updates visual blocks on page
    # 	 * @param vipsBlocks New VipsBlock structure
    # 	 
    def updateVipsBlocks(self, vipsBlocks):
        """ generated source for method updateVipsBlocks """
        self.setVipsBlocks(vipsBlocks)
        listsVisualStructures = ArrayList()
        oldNestedBlocks = ArrayList()
        self.findListVisualStructures(self._visualStructure, listsVisualStructures)
        for visualStructure in listsVisualStructures:
            oldNestedBlocks.addAll(visualStructure.getNestedBlocks())
            visualStructure.clearNestedBlocks()
            for visualBlock in _visualBlocks:
                if visualBlock.getBox().getAbsoluteContentX() >= visualStructure.getX() and visualBlock.getBox().getAbsoluteContentX() <= (visualStructure.getX() + visualStructure.getWidth()):
                    if visualBlock.getBox().getAbsoluteContentY() >= visualStructure.getY() and visualBlock.getBox().getAbsoluteContentY() <= (visualStructure.getY() + visualStructure.getHeight()):
                        if visualBlock.getBox().getContentHeight() != 0 and visualBlock.getBox().getContentWidth() != 0:
                            visualStructure.addNestedBlock(visualBlock)
            if visualStructure.getNestedBlocks().size() == 0:
                visualStructure.addNestedBlocks(oldNestedBlocks)
                self._visualBlocks.addAll(oldNestedBlocks)
            self.replaceBlocksInPredecessors(oldNestedBlocks, visualStructure.getNestedBlocks(), self._visualStructure, pathStructures)
            oldNestedBlocks.clear()

    # 
    # 	 * Sets order to visual structure
    # 	 * @param visualStructure
    # 	 
    def setOrder(self, visualStructure):
        """ generated source for method setOrder """
        visualStructure.setOrder(self._srcOrder)
        self._srcOrder += 1
        for child in visualStructure.getChildrenVisualStructures():
            self.setOrder(child)

    # 
    # 	 * Finds all horizontal and vertical separators in given structure
    # 	 * @param visualStructure Given structure
    # 	 * @param result Results
    # 	 
    def getAllSeparators(self, visualStructure, result):
        """ generated source for method getAllSeparators """
        findAllHorizontalSeparators(visualStructure, result)
        findAllVerticalSeparators(visualStructure, result)
        removeDuplicates(result)

    # 
    # 	 * Finds all horizontal separators in given structure
    # 	 * @param visualStructure Given structure
    # 	 * @param result Results
    # 	 
    def getAllHorizontalSeparators(self, visualStructure, result):
        """ generated source for method getAllHorizontalSeparators """
        findAllHorizontalSeparators(visualStructure, result)
        removeDuplicates(result)

    # 
    # 	 * Finds all vertical separators in given structure
    # 	 * @param visualStructure Given structure
    # 	 * @param result Results
    # 	 
    def getAllVerticalSeparators(self, visualStructure, result):
        """ generated source for method getAllVerticalSeparators """
        findAllVerticalSeparators(visualStructure, result)
        removeDuplicates(result)

    # 
    # 	 * Finds all horizontal separators in given structure
    # 	 * @param visualStructure Given structure
    # 	 * @param result Results
    # 	 
    def findAllHorizontalSeparators(self, visualStructure, result):
        """ generated source for method findAllHorizontalSeparators """
        result.addAll(visualStructure.getHorizontalSeparators())
        for child in visualStructure.getChildrenVisualStructures():
            self.findAllHorizontalSeparators(child, result)

    # 
    # 	 * Finds all vertical separators in given structure
    # 	 * @param visualStructure Given structure
    # 	 * @param result Results
    # 	 
    def findAllVerticalSeparators(self, visualStructure, result):
        """ generated source for method findAllVerticalSeparators """
        result.addAll(visualStructure.getVerticalSeparators())
        for child in visualStructure.getChildrenVisualStructures():
            self.findAllVerticalSeparators(child, result)

    # 
    # 	 * Updates separators when replacing blocks
    # 	 * @param visualStructure Actual visual structure
    # 	 
    def updateSeparatorsInStructure(self, visualStructure):
        """ generated source for method updateSeparatorsInStructure """
        adjacentBlocks = ArrayList()
        allSeparators = ArrayList()
        allSeparators.addAll(visualStructure.getHorizontalSeparators())
        #  separator between blocks
        for separator in allSeparators:
            adjacentBlocks.clear()
            for block in visualStructure.getNestedBlocks():
                if bottom <= separator.startPoint and bottom > aboveBottom:
                    aboveBottom = bottom
                    above = block
                if top >= separator.endPoint and top < belowTop:
                    belowTop = top
                    below = block
                    adjacentBlocks.add(block)
            if above == None or below == None:
                continue 
            adjacentBlocks.add(above)
            adjacentBlocks.add(below)
            if aboveBottom == separator.startPoint - 1 and belowTop == separator.endPoint + 1:
                continue 
            if len(adjacentBlocks) < 2:
                continue 
            if self._graphicsOutput:
                detector = VipsSeparatorGraphicsDetector(self._pageWidth, self._pageHeight)
            else:
                detector = VipsSeparatorNonGraphicsDetector(self._pageWidth, self._pageHeight)
            detector.setCleanUpSeparators(3)
            if self._iteration > 3:
                detector.setCleanUpSeparators(6)
            # detector.setVipsBlock(_vipsBlocks);
            detector.setVisualBlocks(adjacentBlocks)
            detector.detectHorizontalSeparators()
            tempSeparators.addAll(visualStructure.getHorizontalSeparators())
            if detector.getHorizontalSeparators().size() == 0:
                continue 
            newSeparator.setLeftUp(visualStructure.getX(), newSeparator.startPoint)
            newSeparator.setRightDown(visualStructure.getX() + visualStructure.getWidth(), newSeparator.endPoint)
            # remove all separators, that are included in block
            for other in tempSeparators:
                if other == separator:
                    visualStructure.getHorizontalSeparators().add(visualStructure.getHorizontalSeparators().indexOf(other) + 1, newSeparator)
                    visualStructure.getHorizontalSeparators().remove(other)
                    break
        #  new blocks in separator
        for separator in allSeparators:
            adjacentBlocks.clear()
            for block in visualStructure.getNestedBlocks():
                #  block is inside the separator
                if top > separator.startPoint and bottom < separator.endPoint:
                    adjacentBlocks.add(block)
                    if top < blockTop:
                        blockTop = top
                    if bottom > blockDown:
                        blockDown = bottom
            if len(adjacentBlocks) == 0:
                continue 
            if self._graphicsOutput:
                detector = VipsSeparatorGraphicsDetector(self._pageWidth, self._pageHeight)
            else:
                detector = VipsSeparatorNonGraphicsDetector(self._pageWidth, self._pageHeight)
            detector.setCleanUpSeparators(3)
            if self._iteration > 3:
                detector.setCleanUpSeparators(6)
            detector.setVisualBlocks(adjacentBlocks)
            detector.detectHorizontalSeparators()
            tempSeparators.addAll(visualStructure.getHorizontalSeparators())
            newSeparatorTop.setLeftUp(visualStructure.getX(), newSeparatorTop.startPoint)
            newSeparatorTop.setRightDown(visualStructure.getX() + visualStructure.getWidth(), newSeparatorTop.endPoint)
            newSeparators.add(newSeparatorTop)
            newSeparatorBottom.setLeftUp(visualStructure.getX(), newSeparatorBottom.startPoint)
            newSeparatorBottom.setRightDown(visualStructure.getX() + visualStructure.getWidth(), newSeparatorBottom.endPoint)
            if detector.getHorizontalSeparators().size() != 0:
                newSeparators.addAll(detector.getHorizontalSeparators())
            newSeparators.add(newSeparatorBottom)
            # remove all separators, that are included in block
            for other in tempSeparators:
                if other == separator:
                    visualStructure.getHorizontalSeparators().addAll(visualStructure.getHorizontalSeparators().indexOf(other) + 1, newSeparators)
                    visualStructure.getHorizontalSeparators().remove(other)
                    break
        for child in visualStructure.getChildrenVisualStructures():
            self.updateSeparatorsInStructure(child)

    # 
    # 	 * Updates separators on whole page
    # 	 
    def updateSeparators(self):
        """ generated source for method updateSeparators """
        self.updateSeparatorsInStructure(self._visualStructure)

    # 
    # 	 * Removes duplicates from list of separators
    # 	 * @param separators
    # 	 
    def removeDuplicates(self, separators):
        """ generated source for method removeDuplicates """
        hashSet = HashSet(separators)
        separators.clear()
        separators.addAll(hashSet)

    # 
    # 	 * Converts normalized weight of separator to DoC
    # 	 * @param Normalized weight of separator
    # 	 * @return DoC
    # 	 
    def getDoCValue(self, value):
        """ generated source for method getDoCValue """
        if value == 0:
            return self._maxDoC
        return ((self._maxDoC + 1) - value)

    # 
    # 	 * Normalizes separators weights with linear normalization
    # 	 
    def normalizeSeparatorsSoftMax(self):
        """ generated source for method normalizeSeparatorsSoftMax """
        separators = ArrayList()
        self.getAllSeparators(self._visualStructure, separators)
        Collections.sort(separators)
        stdev = getStdDeviation(separators)
        meanValue = 0
        lambda_ = 3.0
        alpha = 1.0
        for separator in separators:
            meanValue += separator.weight
        meanValue /= len(separators)
        for separator in separators:
            normalizedValue = 1 / (1 + Math.exp(-alpha * normalizedValue) + 1)
            normalizedValue = normalizedValue * (11 - 1) + 1
            separator.normalizedWeight = self.getDoCValue(int(Math.round(normalizedValue)))
            if separator.weight == 3:
                separator.normalizedWeight = 11
            # 			System.out.println(separator.startPoint + "\t" + separator.endPoint + "\t" +
            # 					(separator.endPoint - separator.startPoint + 1) +
            # 					"\t" + separator.weight + "\t" + separator.normalizedWeight +
            # 					"\t" + normalizedValue);
        updateDoC(self._visualStructure)
        self._visualStructure.setDoC(1)

    # 
    # 	 * Normalizes separators weights with linear normalization
    # 	 
    def normalizeSeparatorsMinMax(self):
        """ generated source for method normalizeSeparatorsMinMax """
        separators = ArrayList()
        self.getAllSeparators(self._visualStructure, separators)
        maxSep = Separator(0, self._pageHeight)
        separators.add(maxSep)
        maxSep.weight = 40
        Collections.sort(separators)
        minWeight = separators.get(0).weight
        maxWeight = separators.get(len(separators) - 1).weight
        for separator in separators:
            separator.normalizedWeight = self.getDoCValue(int(Math.ceil(normalizedValue)))
            # 		System.out.println(separator.startPoint + "\t" + separator.endPoint + "\t" +
            # 					(separator.endPoint - separator.startPoint + 1) +
            # 					"\t" + separator.weight + "\t" + separator.normalizedWeight +
            # 					"\t" + normalizedValue);
        updateDoC(self._visualStructure)
        self._visualStructure.setDoC(1)

    # 
    # 	 * Updates DoC of all visual structures nodes
    # 	 * @param visualStructure Visual Structure
    # 	 
    def updateDoC(self, visualStructure):
        """ generated source for method updateDoC """
        for child in visualStructure.getChildrenVisualStructures():
            self.updateDoC(child)
        visualStructure.updateToNormalizedDoC()

    # 
    # 	 * Finds minimal DoC in given structure
    # 	 * @param visualStructure
    # 	 
    def findMinimalDoC(self, visualStructure):
        """ generated source for method findMinimalDoC """
        if not visualStructure.getId() == "1":
            if visualStructure.getDoC() < self._minDoC:
                self._minDoC = visualStructure.getDoC()
        for child in visualStructure.getChildrenVisualStructures():
            self.findMinimalDoC(child)

    # 
    # 	 * Returns minimal DoC on page
    # 	 * @return Minimal DoC
    # 	 
    def getMinimalDoC(self):
        """ generated source for method getMinimalDoC """
        self._minDoC = 11
        self.findMinimalDoC(self._visualStructure)
        return self._minDoC

    # 
    # 	 * Checks if it's necessary to continue in segmentation
    # 	 * @return True if it's necessary to continue in segmentation, otherwise false
    # 	 
    def continueInSegmentation(self):
        """ generated source for method continueInSegmentation """
        self.getMinimalDoC()
        if self._pDoC < self._minDoC:
            return False
        return True

    # 
    # 	 * Counts standard deviation from list of separators
    # 	 * @param separators List of separators
    # 	 * @return Standard deviation
    # 	 
    def getStdDeviation(self, separators):
        """ generated source for method getStdDeviation """
        meanValue = 0.0
        stddev = 0.0
        deviations = ArrayList()
        squaredDeviations = ArrayList()
        sum = 0.0
        for separator in separators:
            meanValue += separator.weight
        meanValue /= len(separators)
        for separator in separators:
            deviations.add(separator.weight - meanValue)
        for deviation in deviations:
            squaredDeviations.add(deviation * deviation)
        for squaredDeviation in squaredDeviations:
            sum += squaredDeviation
        stddev = Math.sqrt(sum / len(squaredDeviations))
        return stddev

