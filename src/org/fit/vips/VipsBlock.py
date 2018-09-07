#!/usr/bin/env python
""" generated source for module VipsBlock """
# 
#  * Tomas Popela, 2012
#  * VIPS - Visual Internet Page Segmentation
#  * Module - VipsBlock.java
#  
# package: org.fit.vips
import java.util.ArrayList

import java.util.List

import org.fit.cssbox.layout.Box

import org.fit.cssbox.layout.ElementBox

import org.fit.cssbox.layout.TextBox

import org.w3c.dom.Element

import org.w3c.dom.Node

# 
#  * Class that represents block on page.
#  * @author Tomas Popela
#  *
#  
class VipsBlock(object):
    """ generated source for class VipsBlock """
    # rendered Box, that corresponds to DOM element
    _box = None

    # children of this node
    _children = None

    # node id
    _id = 0

    # node's Degree Of Coherence
    _DoC = 0

    # number of images in node
    _containImg = 0

    # if node is image
    _isImg = False

    # if node is visual block
    _isVisualBlock = False

    # if node contains table
    _containTable = False

    # number of paragraphs in node
    _containP = 0

    # if node was already divided
    _alreadyDivided = False

    # if node can be divided
    _isDividable = True
    _bgColor = None
    _frameSourceIndex = 0
    _sourceIndex = 0
    _tmpSrcIndex = 0
    _order = 0

    # length of text in node
    _textLen = 0

    # length of text in links in node
    _linkTextLen = 0

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        self._children = ArrayList()

    @__init__.register(object, int, VipsBlock)
    def __init___0(self, id, node):
        """ generated source for method __init___0 """
        self._children = ArrayList()
        setId(id)
        addChild(node)

    # 
    # 	 * Sets block as visual block
    # 	 * @param isVisualBlock Value
    # 	 
    def setIsVisualBlock(self, isVisualBlock):
        """ generated source for method setIsVisualBlock """
        self._isVisualBlock = isVisualBlock
        checkProperties()

    # 
    # 	 * Checks if block is visual block
    # 	 * @return True if block if visual block, otherwise false
    # 	 
    def isVisualBlock(self):
        """ generated source for method isVisualBlock """
        return self._isVisualBlock

    # 
    # 	 * Checks the properties of visual block
    # 	 
    def checkProperties(self):
        """ generated source for method checkProperties """
        checkIsImg()
        checkContainImg(self)
        checkContainTable(self)
        checkContainP(self)
        self._linkTextLen = 0
        self._textLen = 0
        countTextLength(self)
        countLinkTextLength(self)
        setSourceIndex(self.getBox().getNode().getOwnerDocument())

    def checkIsImg(self):
        """ generated source for method checkIsImg """
        if self._box.getNode().getNodeName() == "img":
            self._isImg = True
        else:
            self._isImg = False

    def checkContainImg(self, vipsBlock):
        """ generated source for method checkContainImg """
        if vipsBlock.getBox().getNode().getNodeName() == "img":
            vipsBlock._isImg = True
            self._containImg += 1
        for childVipsBlock in vipsBlock.getChildren():
            self.checkContainImg(childVipsBlock)

    def checkContainTable(self, vipsBlock):
        """ generated source for method checkContainTable """
        if vipsBlock.getBox().getNode().getNodeName() == "table":
            self._containTable = True
        for childVipsBlock in vipsBlock.getChildren():
            self.checkContainTable(childVipsBlock)

    def checkContainP(self, vipsBlock):
        """ generated source for method checkContainP """
        if vipsBlock.getBox().getNode().getNodeName() == "p":
            self._containP += 1
        for childVipsBlock in vipsBlock.getChildren():
            self.checkContainP(childVipsBlock)

    def countLinkTextLength(self, vipsBlock):
        """ generated source for method countLinkTextLength """
        if vipsBlock.getBox().getNode().getNodeName() == "a":
            self._linkTextLen += len(length)
        for childVipsBlock in vipsBlock.getChildren():
            self.countLinkTextLength(childVipsBlock)

    def countTextLength(self, vipsBlock):
        """ generated source for method countTextLength """
        self._textLen = len(length)

    def addChild(self, child):
        """ generated source for method addChild """
        self._children.add(child)

    def getChildren(self):
        """ generated source for method getChildren """
        return self._children

    def setBox(self, box):
        """ generated source for method setBox """
        self._box = box

    def getBox(self):
        """ generated source for method getBox """
        return self._box

    def getElementBox(self):
        """ generated source for method getElementBox """
        if isinstance(self._box, (ElementBox, )):
            return self._box
        else:
            return None

    def setId(self, id):
        """ generated source for method setId """
        self._id = id

    def getId(self):
        """ generated source for method getId """
        return self._id

    def getDoC(self):
        """ generated source for method getDoC """
        return self._DoC

    def setDoC(self, doC):
        """ generated source for method setDoC """
        self._DoC = doC

    def isDividable(self):
        """ generated source for method isDividable """
        return self._isDividable

    def setIsDividable(self, isDividable):
        """ generated source for method setIsDividable """
        self._isDividable = isDividable

    def isAlreadyDivided(self):
        """ generated source for method isAlreadyDivided """
        return self._alreadyDivided

    def setAlreadyDivided(self, alreadyDivided):
        """ generated source for method setAlreadyDivided """
        self._alreadyDivided = alreadyDivided

    def isImg(self):
        """ generated source for method isImg """
        return self._isImg

    def containImg(self):
        """ generated source for method containImg """
        return self._containImg

    def containTable(self):
        """ generated source for method containTable """
        return self._containTable

    def getTextLength(self):
        """ generated source for method getTextLength """
        return self._textLen

    def getLinkTextLength(self):
        """ generated source for method getLinkTextLength """
        return self._linkTextLen

    def containP(self):
        """ generated source for method containP """
        return self._containP

    def findBgColor(self, element):
        """ generated source for method findBgColor """
        backgroundColor = element.getAttribute("background-color")
        if backgroundColor.isEmpty():
            if element.getParentNode() != None and not (isinstance(, (DeferredDocumentImpl, ))):
                self.findBgColor(element.getParentNode())
            else:
                self._bgColor = "#ffffff"
                return
        else:
            self._bgColor = backgroundColor
            return

    def getBgColor(self):
        """ generated source for method getBgColor """
        if self._bgColor != None:
            return self._bgColor
        if isinstance(, (TextBox, )):
            self._bgColor = "#ffffff"
        else:
            self._bgColor = self.getElementBox().getStylePropertyValue("background-color")
        if self._bgColor.isEmpty():
            self.findBgColor(self.getElementBox().getElement())
        return self._bgColor

    def getFontSize(self):
        """ generated source for method getFontSize """
        return self.getBox().getVisualContext().getFont().getSize()

    def getFontWeight(self):
        """ generated source for method getFontWeight """
        fontWeight = ""
        if isinstance(, (TextBox, )):
            return fontWeight
        if self.getElementBox().getStylePropertyValue("font-weight") == None:
            return fontWeight
        fontWeight = self.getElementBox().getStylePropertyValue("font-weight")
        if fontWeight.isEmpty():
            fontWeight = "normal"
        return fontWeight

    def getFrameSourceIndex(self):
        """ generated source for method getFrameSourceIndex """
        return self._frameSourceIndex

    def setSourceIndex(self, node):
        """ generated source for method setSourceIndex """
        if not self.getBox().getNode() == node:
            self._tmpSrcIndex += 1
        else:
            self._sourceIndex = self._tmpSrcIndex
        i = 0
        while i < node.getChildNodes().getLength():
            self.setSourceIndex(node.getChildNodes().item(i))
            i += 1

    def getSourceIndex(self):
        """ generated source for method getSourceIndex """
        return self._sourceIndex

    def getOrder(self):
        """ generated source for method getOrder """
        return self._order

