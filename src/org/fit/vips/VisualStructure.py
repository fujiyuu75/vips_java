#!/usr/bin/env python
""" generated source for module VisualStructure """
# 
#  * Tomas Popela, 2012
#  * VIPS - Visual Internet Page Segmentation
#  * Module - VisualStructurejava
#  
# package: org.fit.vips
import java.util.ArrayList

import java.util.List

import org.w3c.dom.Node

# 
#  * Class that represents visual structure.
#  * @author Tomas Popela
#  *
#  
class VisualStructure(object):
    """ generated source for class VisualStructure """
    _nestedBlocks = None
    _childrenVisualStructures = None
    _horizontalSeparators = None
    _verticalSeparators = None
    _width = 0
    _height = 0
    _x = 0
    _y = 0
    _doC = 12
    _containImg = -1
    _containP = -1
    _textLength = -1
    _linkTextLength = -1
    _order = int()
    _containTable = False
    _id = None
    _tmpSrcIndex = 0
    _srcIndex = 0
    _minimalDoC = 0

    def __init__(self):
        """ generated source for method __init__ """
        self._nestedBlocks = ArrayList()
        self._childrenVisualStructures = ArrayList()
        self._horizontalSeparators = ArrayList()
        self._verticalSeparators = ArrayList()

    # 
    # 	 * @return Nested blocks in structure
    # 	 
    def getNestedBlocks(self):
        """ generated source for method getNestedBlocks """
        return self._nestedBlocks

    # 
    # 	 * Adds block to nested blocks
    # 	 * @param nestedBlock New block
    # 	 
    def addNestedBlock(self, nestedBlock):
        """ generated source for method addNestedBlock """
        self._nestedBlocks.add(nestedBlock)

    # 
    # 	 * Adds blocks to nested blocks
    # 	 * @param nestedBlocks
    # 	 
    def addNestedBlocks(self, nestedBlocks):
        """ generated source for method addNestedBlocks """
        self._nestedBlocks.addAll(nestedBlocks)

    # 
    # 	 * Sets blocks as nested blocks
    # 	 * @param vipsBlocks
    # 	 
    def setNestedBlocks(self, vipsBlocks):
        """ generated source for method setNestedBlocks """
        self._nestedBlocks = vipsBlocks

    # 
    # 	 * Clears nested blocks list
    # 	 
    def clearNestedBlocks(self):
        """ generated source for method clearNestedBlocks """
        self._nestedBlocks.clear()

    # 
    # 	 * Removes nested block at given index
    # 	 * @param index Index of block
    # 	 
    def removeNestedBlockAt(self, index):
        """ generated source for method removeNestedBlockAt """
        self._nestedBlocks.remove(index)

    # 
    # 	 * Removes given child from structures children
    # 	 * @param visualStructure Child
    # 	 
    def removeChild(self, visualStructure):
        """ generated source for method removeChild """
        self._childrenVisualStructures.remove(visualStructure)

    # 
    # 	 * Adds new child to visual structure children
    # 	 * @param visualStructure New child
    # 	 
    def addChild(self, visualStructure):
        """ generated source for method addChild """
        self._childrenVisualStructures.add(visualStructure)

    # 
    # 	 * Adds new child to visual structure at given index
    # 	 * @param visualStructure New child
    # 	 * @param index Index
    # 	 
    def addChildAt(self, visualStructure, index):
        """ generated source for method addChildAt """
        self._childrenVisualStructures.add(index, visualStructure)

    # 
    # 	 * Returns all children structures
    # 	 * @return Children structures
    # 	 
    def getChildrenVisualStructures(self):
        """ generated source for method getChildrenVisualStructures """
        return self._childrenVisualStructures

    # 
    # 	 * Sets visual structures as children of visual structure
    # 	 * @param childrenVisualStructures List of visual structures
    # 	 
    def setChildrenVisualStructures(self, childrenVisualStructures):
        """ generated source for method setChildrenVisualStructures """
        self._childrenVisualStructures = childrenVisualStructures

    # 
    # 	 * Returns all horizontal separators form structure
    # 	 * @return List of horizontal separators
    # 	 
    def getHorizontalSeparators(self):
        """ generated source for method getHorizontalSeparators """
        return self._horizontalSeparators

    # 
    # 	 * Sets list of separators as horizontal separators of structure
    # 	 * @param horizontalSeparators List of separators
    # 	 
    def setHorizontalSeparators(self, horizontalSeparators):
        """ generated source for method setHorizontalSeparators """
        self._horizontalSeparators = horizontalSeparators

    # 
    # 	 * Adds separator to horizontal separators of structure
    # 	 * @param horizontalSeparator
    # 	 
    def addHorizontalSeparator(self, horizontalSeparator):
        """ generated source for method addHorizontalSeparator """
        self._horizontalSeparators.add(horizontalSeparator)

    # 
    # 	 * Adds separators to horizontal separators of structure
    # 	 * @param horizontalSeparators
    # 	 
    def addHorizontalSeparators(self, horizontalSeparators):
        """ generated source for method addHorizontalSeparators """
        self._horizontalSeparators.addAll(horizontalSeparators)

    # 
    # 	 * Returns X structure's coordinate
    # 	 * @return X coordinate
    # 	 
    def getX(self):
        """ generated source for method getX """
        return self._x

    # 
    # 	 * Returns structure's Y coordinate
    # 	 * @return Y coordinate
    # 	 
    def getY(self):
        """ generated source for method getY """
        return self._y

    # 
    # 	 * Sets X coordinate
    # 	 * @param x X coordinate
    # 	 
    def setX(self, x):
        """ generated source for method setX """
        self._x = x

    # 
    # 	 * Sets Y coordinate
    # 	 * @param y Y coordinate
    # 	 
    def setY(self, y):
        """ generated source for method setY """
        self._y = y

    # 
    # 	 * Sets width of visual structure
    # 	 * @param width Width
    # 	 
    def setWidth(self, width):
        """ generated source for method setWidth """
        self._width = width

    # 
    # 	 * Sets height of visual structure
    # 	 * @param height Height
    # 	 
    def setHeight(self, height):
        """ generated source for method setHeight """
        self._height = height

    # 
    # 	 * Returns width of visual structure
    # 	 * @return Visual structure's width
    # 	 
    def getWidth(self):
        """ generated source for method getWidth """
        return self._width

    # 
    # 	 * Returns height of visual structure
    # 	 * @return Visual structure's height
    # 	 
    def getHeight(self):
        """ generated source for method getHeight """
        return self._height

    # 
    # 	 * Returns list of all vertical separators in visual structure
    # 	 * @return List of vertical separators
    # 	 
    def getVerticalSeparators(self):
        """ generated source for method getVerticalSeparators """
        return self._verticalSeparators

    # 
    # 	 * Sets list of separators as vertical separators of structure
    # 	 * @param _verticalSeparators List of separators
    # 	 
    def setVerticalSeparators(self, _verticalSeparators):
        """ generated source for method setVerticalSeparators """
        self._verticalSeparators = _verticalSeparators

    # 
    # 	 * Adds separator to structure's vertical sepators
    # 	 * @param verticalSeparator
    # 	 
    def addVerticalSeparator(self, verticalSeparator):
        """ generated source for method addVerticalSeparator """
        self._verticalSeparators.add(verticalSeparator)

    # 
    # 	 * Sets if of visual structure
    # 	 * @param id Id
    # 	 
    def setId(self, id):
        """ generated source for method setId """
        self._id = id

    # 
    # 	 * Returns id of visual structure
    # 	 * @return Visual structure's id
    # 	 
    def getId(self):
        """ generated source for method getId """
        return self._id

    # 
    # 	 * Sets visual structure's degree of coherence DoC
    # 	 * @param doC Degree of coherence - DoC
    # 	 
    def setDoC(self, doC):
        """ generated source for method setDoC """
        self._doC = doC

    # 
    # 	 * Returns structure's degree of coherence DoC
    # 	 * @return Degree of coherence - DoC
    # 	 
    def getDoC(self):
        """ generated source for method getDoC """
        return self._doC

    # 
    # 	 * Finds minimal DoC in all children visual structures
    # 	 * @param visualStructure Given visual structure
    # 	 
    def findMinimalDoC(self, visualStructure):
        """ generated source for method findMinimalDoC """
        if not visualStructure.getId() == "1":
            if visualStructure.getDoC() < self._minimalDoC:
                self._minimalDoC = visualStructure.getDoC()
        for child in visualStructure.getChildrenVisualStructures():
            self.findMinimalDoC(child)

    # 
    # 	 * Updates DoC to normalized DoC
    # 	 
    def updateToNormalizedDoC(self):
        """ generated source for method updateToNormalizedDoC """
        self._doC = 12
        for separator in _horizontalSeparators:
            if separator.normalizedWeight < self._doC:
                self._doC = separator.normalizedWeight
        for separator in _verticalSeparators:
            if separator.normalizedWeight < self._doC:
                self._doC = separator.normalizedWeight
        if self._doC == 12:
            for nestedBlock in _nestedBlocks:
                if nestedBlock.getDoC() < self._doC:
                    self._doC = nestedBlock.getDoC()
        self._minimalDoC = 12
        self.findMinimalDoC(self)
        if self._minimalDoC < self._doC:
            self._doC = self._minimalDoC

    # 
    # 	 * Check if visual structure contain images
    # 	 * @return Number of images
    # 	 
    def containImg(self):
        """ generated source for method containImg """
        if self._containImg != -1:
            return self._containImg
        self._containImg = 0
        for vipsBlock in _nestedBlocks:
            self._containImg += vipsBlock.containImg()
        return self._containImg

    # 
    # 	 * Check if visual structure contain paragraphs
    # 	 * @return Nubmer of paragraphs
    # 	 
    def containP(self):
        """ generated source for method containP """
        if self._containP != -1:
            return self._containP
        self._containP = 0
        for vipsBlock in _nestedBlocks:
            self._containP += vipsBlock.containP()
        return self._containP

    # 
    # 	 * Checks visual structure contains table
    # 	 * @return True if contains, otherwise false
    # 	 
    def containTable(self):
        """ generated source for method containTable """
        if self._containTable:
            return self._containTable
        for vipsBlock in _nestedBlocks:
            if vipsBlock.containTable():
                self._containTable = True
                break
        return self._containTable

    # 
    # 	 * Checks if visual structure is image
    # 	 * @return True if is image, otherwise false
    # 	 
    def isImg(self):
        """ generated source for method isImg """
        if len(self._nestedBlocks) != 1:
            return False
        return self._nestedBlocks.get(0).isImg()

    # 
    # 	 * Returns length of text in visual structure
    # 	 * @return Text length
    # 	 
    def getTextLength(self):
        """ generated source for method getTextLength """
        if self._textLength != -1:
            return self._textLength
        self._textLength = 0
        for vipsBlock in _nestedBlocks:
            self._textLength += vipsBlock.getTextLength()
        return self._textLength

    # 
    # 	 * Returns length of text in links in visual structure
    # 	 * @return Link text length
    # 	 
    def getLinkTextLength(self):
        """ generated source for method getLinkTextLength """
        if self._linkTextLength != -1:
            return self._linkTextLength
        self._linkTextLength = 0
        for vipsBlock in _nestedBlocks:
            self._linkTextLength += vipsBlock.getLinkTextLength()
        return self._linkTextLength

    # 
    # 	 * Gets visual structure font size
    # 	 * @return Font size
    # 	 
    def getFontSize(self):
        """ generated source for method getFontSize """
        if len(self._nestedBlocks) > 0:
            return self._nestedBlocks.get(0).getFontSize()
        else:
            return -1

    # 
    # 	 * Gets visual structure font weight
    # 	 * @return Font weight
    # 	 
    def getFontWeight(self):
        """ generated source for method getFontWeight """
        if len(self._nestedBlocks) > 0:
            return self._nestedBlocks.get(0).getFontWeight()
        else:
            return "undef"

    # 
    # 	 * Gets visual structure background color
    # 	 * @return Background color
    # 	 
    def getBgColor(self):
        """ generated source for method getBgColor """
        if len(self._nestedBlocks) > 0:
            return self._nestedBlocks.get(0).getBgColor()
        else:
            return "undef"

    # 
    # 	 * Gets frame source index of visual structure
    # 	 * @return Frame source index
    # 	 
    def getFrameSourceIndex(self):
        """ generated source for method getFrameSourceIndex """
        if len(self._nestedBlocks) > 0:
            return self._nestedBlocks.get(0).getFrameSourceIndex()
        else:
            return -1

    # 
    # 	 * Sets source index of visual structure
    # 	 * @param node Node
    # 	 * @param nodeToFind Node to find
    # 	 
    def setSourceIndex(self, node, nodeToFind):
        """ generated source for method setSourceIndex """
        if not nodeToFind == node:
            self._tmpSrcIndex += 1
        else:
            self._srcIndex = self._tmpSrcIndex
        i = 0
        while i < node.getChildNodes().getLength():
            self.setSourceIndex(node.getChildNodes().item(i), nodeToFind)
            i += 1

    # 
    # 	 * Gets source index of visual strucure
    # 	 * @return Visual structure's source index
    # 	 
    def getSourceIndex(self):
        """ generated source for method getSourceIndex """
        sourceIndex = ""
        if len(self._childrenVisualStructures) > 0:
            self.setSourceIndex(self._nestedBlocks.get(0).getBox().getNode().getOwnerDocument(), self._nestedBlocks.get(0).getBox().getParent().getNode())
            sourceIndex = String.valueOf(self._srcIndex)
        else:
            for block in _nestedBlocks:
                if not sourceIndex == "":
                    sourceIndex += ";"
                sourceIndex += block.getSourceIndex()
        return sourceIndex

    def setOrder(self, order):
        """ generated source for method setOrder """
        self._order = order

    def getOrder(self):
        """ generated source for method getOrder """
        return self._order

    def addVerticalSeparators(self, verticalSeparators):
        """ generated source for method addVerticalSeparators """
        self._verticalSeparators.addAll(verticalSeparators)

