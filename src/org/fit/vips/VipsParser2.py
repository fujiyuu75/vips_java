#!/usr/bin/env python
""" generated source for module VipsParser2 """
# 
#  * Tomas Popela, 2012
#  * VIPS - Visual Internet Page Segmentation
#  * Module - VipsParser.java
#  
# package: org.fit.vips
import java.util.ArrayList

import java.util.List

import org.fit.cssbox.layout.Box

import org.fit.cssbox.layout.ElementBox

import org.fit.cssbox.layout.TextBox

import org.fit.cssbox.layout.Viewport

import org.w3c.dom.Node

class VipsParser(object):
    """ generated source for class VipsParser """
    _vipsBlocks = None
    _currentVipsBlock = None
    _tempVipsBlock = None
    _sizeTresholdWidth = 0
    _sizeTresholdHeight = 0
    _viewport = None
    _visualBlocksCount = 0
    _pageWidth = 0
    _pageHeight = 0

    # 
    #      * Default constructor
    #      *
    #      * @param viewport Rendered's page viewport
    #      
    def __init__(self, viewport):
        """ generated source for method __init__ """
        self._viewport = viewport
        self._vipsBlocks = VipsBlock()
        self._sizeTresholdHeight = 80
        self._sizeTresholdWidth = 80
        self._pageWidth = viewport.getWidth()
        self._pageHeight = viewport.getHeight()

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

    # 
    #      * Counts number of visual blocks in visual structure
    #      * @param vipsBlock Visual structure
    #      
    def getVisualBlocksCount(self, vipsBlock):
        """ generated source for method getVisualBlocksCount """
        if vipsBlock.isVisualBlock():
            self._visualBlocksCount += 1
        for vipsBlockChild in vipsBlock.getChildren():
            if not (isinstance(, (TextBox, ))):
                self.getVisualBlocksCount(vipsBlockChild)

    def findVisualBlocks(self, vipsBlock, list_):
        """ generated source for method findVisualBlocks """
        if vipsBlock.isVisualBlock():
            list_.add(vipsBlock)
        for vipsStructureChild in vipsBlock.getChildren():
            self.findVisualBlocks(vipsStructureChild, list_)

    def getVisualBlocks(self):
        """ generated source for method getVisualBlocks """
        list_ = ArrayList()
        self.findVisualBlocks(self._vipsBlocks, list_)
        return list_

    # 
    #      * Construct VIPS block tree from viewport.
    #      * <p>
    #      * Starts from &lt;body&gt; element.
    #      * @param element Box that represents element
    #      * @param node Visual structure tree node
    #      
    def constructVipsBlockTree(self, element, node):
        """ generated source for method constructVipsBlockTree """
        node.setBox(element)
        if not (isinstance(element, (TextBox, ))):
            for box in (element).getSubBoxList():
                node.addChild(VipsBlock())
                self.constructVipsBlockTree(box, node.getChildren().get(node.getChildren().size() - 1))

    # 
    #      * Tries to divide DOM elements and finds visual blocks.
    #      * @param vipsBlock Visual structure
    #      
    def divideVipsBlockTree(self, vipsBlock):
        """ generated source for method divideVipsBlockTree """
        self._currentVipsBlock = vipsBlock
        elementBox = vipsBlock.getBox()
        # System.err.println(elementBox.getNode().getNodeName());
        # print elementBox.getText();
        if elementBox.getElement().getAttribute("id") == "logosLine":
            print 
        if applyVipsRules(elementBox) and vipsBlock.isDividable() and not vipsBlock.isVisualBlock():
            self._currentVipsBlock.setAlreadyDivided(True)
            for vipsBlockChild in vipsBlock.getChildren():
                if not (isinstance(, (TextBox, ))):
                    self.divideVipsBlockTree(vipsBlockChild)
        else:
            if vipsBlock.isDividable():
                vipsBlock.setIsVisualBlock(True)
                vipsBlock.setDoC(11)
            if not verifyValidity(elementBox):
                self._currentVipsBlock.setIsVisualBlock(False)

    def getAllTextLength(self, node):
        """ generated source for method getAllTextLength """
        childrenTextNodes = ArrayList()
        findTextChildrenNodes(node, childrenTextNodes)
        textLength = 0
        for child in childrenTextNodes:
            if not childText == "" and not childText == " " and not childText == "\n":
                textLength += len(childText)
        return textLength

    def getAllChildren(self, node, children):
        """ generated source for method getAllChildren """
        children.add(node)
        if isinstance(node, (TextBox, )):
            return
        for child in (node).getSubBoxList():
            self.getAllChildren(child, children)

    def verifyValidity(self, node):
        """ generated source for method verifyValidity """
        if node.getAbsoluteContentX() < 0 or node.getAbsoluteContentY() < 0:
            return False
        if node.getAbsoluteContentX() + node.getContentWidth() > self._pageWidth:
            return False
        if node.getAbsoluteContentY() + node.getContentHeight() > self._pageHeight:
            return False
        if node.getWidth() <= 0 or node.getHeight() <= 0:
            return False
        if not node.isDisplayed():
            return False
        if not node.isVisible():
            return False
        if self.getAllTextLength(node) == 0:
            self.getAllChildren(node, children)
            for child in children:
                if not child.isVisible():
                    continue 
                if childNodeName == "img":
                    return True
                if childNodeName == "input":
                    return True
            return False
        return True

    def isValidNode(self, node):
        """ generated source for method isValidNode """
        if node.getHeight() > 0 and node.getWidth() > 0:
            return True
        return False

    def isTextNode(self, box):
        """ generated source for method isTextNode """
        return True if (box.getNode().getNodeName() == "text") else False

    def isVirtualTextNode1(self, node):
        """ generated source for method isVirtualTextNode1 """
        if node.isBlock():
            return False
        for childNode in node.getSubBoxList():
            if not (isinstance(childNode, (TextBox, ))):
                if not self.isTextNode(childNode):
                    return False
        return True

    def isVirtualTextNode2(self, node):
        """ generated source for method isVirtualTextNode2 """
        if node.isBlock():
            return False
        for childNode in node.getSubBoxList():
            if not self.isTextNode(childNode) or not self.isVirtualTextNode1(childNode):
                return False
        return True

    def isVirtualTextNode(self, node):
        """ generated source for method isVirtualTextNode """
        if self.isVirtualTextNode1(node):
            return True
        if self.isVirtualTextNode2(node):
            return True
        return False

    _cnt = 0

    def checkValidChildrenNodes(self, node):
        """ generated source for method checkValidChildrenNodes """
        if isinstance(node, (TextBox, )):
            if not node.getText() == "":
                self._cnt += 1
            return
        else:
            if self.isValidNode(node):
                self._cnt += 1
        for childNode in (node).getSubBoxList():
            self.checkValidChildrenNodes(childNode)

    def hasValidChildrenNodes(self, node):
        """ generated source for method hasValidChildrenNodes """
        if node.getNode().getNodeName() == "img" or node.getNode().getNodeName() == "input":
            if node.getContentWidth() > 0 and node.getContentHeight() > 0:
                self._currentVipsBlock.setIsVisualBlock(True)
                self._currentVipsBlock.setDoC(8)
                return True
            else:
                return False
        if node.getSubBoxList().isEmpty():
            return False
        self._cnt = 0
        for child in node.getSubBoxList():
            self.checkValidChildrenNodes(child)
        return True if (self._cnt > 0) else False

    def numberOfValidChildNodes(self, node):
        """ generated source for method numberOfValidChildNodes """
        self._cnt = 0
        if node.getSubBoxList().isEmpty():
            return self._cnt
        for child in node.getSubBoxList():
            self.checkValidChildrenNodes(child)
        return self._cnt

    def applyVipsRules(self, node):
        """ generated source for method applyVipsRules """
        retVal = False
        if not node.isBlock():
            retVal = applyInlineTextNodeVipsRules(node)
        elif node.getNode().getNodeName() == "table":
            retVal = applyTableNodeVipsRules(node)
        elif node.getNode().getNodeName() == "tr":
            retVal = applyTrNodeVipsRules(node)
        elif node.getNode().getNodeName() == "td":
            retVal = applyTdNodeVipsRules(node)
        elif node.getNode().getNodeName() == "p":
            retVal = applyPNodeVipsRules(node)
        else:
            retVal = applyOtherNodeVipsRules(node)
        return retVal

    def applyOtherNodeVipsRules(self, node):
        """ generated source for method applyOtherNodeVipsRules """
        if ruleOne(node):
            return True
        if ruleTwo(node):
            return True
        if ruleThree(node):
            return True
        if ruleFour(node):
            return True
        if ruleSix(node):
            return True
        if ruleEight(node):
            return True
        if ruleNine(node):
            return True
        if ruleEleven(node):
            return True
        return False

    def applyPNodeVipsRules(self, node):
        """ generated source for method applyPNodeVipsRules """
        if ruleOne(node):
            return True
        if ruleTwo(node):
            return True
        if ruleThree(node):
            return True
        if ruleFour(node):
            return True
        if ruleFive(node):
            return True
        if ruleSix(node):
            return True
        if ruleSeven(node):
            return True
        if ruleEight(node):
            return True
        if ruleNine(node):
            return True
        if ruleTen(node):
            return True
        if ruleEleven(node):
            return True
        if ruleTwelve(node):
            return True
        return False

    def applyTdNodeVipsRules(self, node):
        """ generated source for method applyTdNodeVipsRules """
        if ruleOne(node):
            return True
        if ruleTwo(node):
            return True
        if ruleThree(node):
            return True
        if ruleFour(node):
            return True
        if ruleEight(node):
            return True
        if ruleNine(node):
            return True
        if ruleTen(node):
            return True
        if ruleTwelve(node):
            return True
        return False

    def applyTrNodeVipsRules(self, node):
        """ generated source for method applyTrNodeVipsRules """
        if ruleOne(node):
            return True
        if ruleTwo(node):
            return True
        if ruleThree(node):
            return True
        if ruleSeven(node):
            return True
        if ruleNine(node):
            return True
        if ruleTwelve(node):
            return True
        return False

    def applyTableNodeVipsRules(self, node):
        """ generated source for method applyTableNodeVipsRules """
        if ruleOne(node):
            return True
        if ruleTwo(node):
            return True
        if ruleThree(node):
            return True
        if ruleSeven(node):
            return True
        if ruleNine(node):
            return True
        if ruleTwelve(node):
            return True
        return False

    def applyInlineTextNodeVipsRules(self, node):
        """ generated source for method applyInlineTextNodeVipsRules """
        if ruleOne(node):
            return True
        if ruleTwo(node):
            return True
        if ruleThree(node):
            return True
        if ruleFour(node):
            return True
        if ruleFive(node):
            return True
        if ruleSix(node):
            return True
        if ruleEight(node):
            return True
        if ruleNine(node):
            return True
        if ruleTwelve(node):
            return True
        return False

    def ruleOne(self, node):
        """ generated source for method ruleOne """
        if not self.isTextNode(node):
            if not self.hasValidChildrenNodes(node):
                self._currentVipsBlock.setIsDividable(False)
                return True
        return False

    def ruleTwo(self, node):
        """ generated source for method ruleTwo """
        if self.numberOfValidChildNodes(node) == 1:
            if isinstance(, (TextBox, )):
                return False
            if not self.isTextNode(node.getSubBox(0)):
                return True
        return False

    def ruleThree(self, node):
        """ generated source for method ruleThree """
        if not node.isRootElement():
            return False
        result = True
        cnt = 0
        for vipsBlock in _vipsBlocks.getChildren():
            if vipsBlock.getBox().getNode().getNodeName() == node.getNode(.getNodeName()):
                result = True
                isOnlyOneDomSubTree(node.getNode(), vipsBlock.getBox().getNode(), result)
                if result:
                    cnt += 1
        return True if (cnt == 1) else False

    def isOnlyOneDomSubTree(self, pattern, node, result):
        """ generated source for method isOnlyOneDomSubTree """
        if not pattern.getNodeName() == node.getNodeName():
            result = False
        if pattern.getChildNodes().getLength() != node.getChildNodes().getLength():
            result = False
        if not result:
            return
        i = 0
        while i < pattern.getChildNodes().getLength():
            self.isOnlyOneDomSubTree(pattern.getChildNodes().item(i), node.getChildNodes().item(i), result)
            i += 1

    def ruleFour(self, node):
        """ generated source for method ruleFour """
        if node.getSubBoxList().isEmpty():
            return False
        for box in node.getSubBoxList():
            if isinstance(box, (TextBox, )):
                continue 
            if not self.isTextNode(box) or not self.isVirtualTextNode(box):
                return False
        self._currentVipsBlock.setIsVisualBlock(True)
        self._currentVipsBlock.setIsDividable(False)
        if node.getSubBoxList().size() == 1:
            if node.getSubBox(0).getNode().getNodeName() == "em":
                self._currentVipsBlock.setDoC(11)
            else:
                self._currentVipsBlock.setDoC(10)
            return True
        fontWeight = ""
        fontSize = 0
        for childNode in node.getSubBoxList():
            if isinstance(childNode, (TextBox, )):
                if fontSize > 0:
                    if fontSize != childFontSize:
                        self._currentVipsBlock.setDoC(9)
                        break
                    else:
                        self._currentVipsBlock.setDoC(10)
                else:
                    fontSize = childFontSize
                continue 
            if child.getStylePropertyValue("font-weight") == None:
                return False
            if fontSize > 0:
                if child.getStylePropertyValue("font-weight").__str__() == fontWeight and childFontSize == fontSize:
                    self._currentVipsBlock.setDoC(10)
                else:
                    self._currentVipsBlock.setDoC(9)
                    break
            else:
                fontWeight = child.getStylePropertyValue("font-weight").__str__()
                fontSize = childFontSize
        return True

    def ruleFive(self, node):
        """ generated source for method ruleFive """
        if node.getSubBoxList().isEmpty():
            return False
        for childNode in node.getSubBoxList():
            if childNode.isBlock():
                return True
        return False

    def ruleSix(self, node):
        """ generated source for method ruleSix """
        if node.getSubBoxList().isEmpty():
            return False
        children = ArrayList()
        self.getAllChildren(node, children)
        for child in children:
            if child.getNode().getNodeName() == "hr":
                return True
        return False

    def ruleSeven(self, node):
        """ generated source for method ruleSeven """
        if node.getSubBoxList().isEmpty():
            return False
        if self.isTextNode(node):
            return False
        nodeBgColor = self._currentVipsBlock.getBgColor()
        for vipsStructureChild in _currentVipsBlock.getChildren():
            if not (vipsStructureChild.getBgColor() == nodeBgColor):
                vipsStructureChild.setIsDividable(False)
                vipsStructureChild.setIsVisualBlock(True)
                vipsStructureChild.setDoC(7)
                return True
        return False

    def findTextChildrenNodes(self, node, results):
        """ generated source for method findTextChildrenNodes """
        if isinstance(node, (TextBox, )):
            results.add(node)
            return
        for childNode in (node).getSubBoxList():
            self.findTextChildrenNodes(childNode, results)

    def ruleEight(self, node):
        """ generated source for method ruleEight """
        if node.getSubBoxList().isEmpty():
            return False
        children = ArrayList()
        self.findTextChildrenNodes(node, children)
        cnt = len(children)
        if cnt == 0:
            return False
        if node.getWidth() == 0 or node.getHeight() == 0:
            children.clear()
            self.getAllChildren(node, children)
            for child in children:
                if child.getWidth() != 0 and child.getHeight() != 0:
                    return True
        if node.getWidth() * node.getHeight() > self._sizeTresholdHeight * self._sizeTresholdWidth:
            return False
        if node.getNode().getNodeName() == "ul":
            return True
        self._currentVipsBlock.setIsVisualBlock(True)
        self._currentVipsBlock.setIsDividable(False)
        if node.getNode().getNodeName() == "Xdiv":
            self._currentVipsBlock.setDoC(7)
        elif node.getNode().getNodeName() == "code":
            self._currentVipsBlock.setDoC(7)
        elif node.getNode().getNodeName() == "div":
            self._currentVipsBlock.setDoC(5)
        else:
            self._currentVipsBlock.setDoC(8)
        return True

    def ruleNine(self, node):
        """ generated source for method ruleNine """
        if node.getSubBoxList().isEmpty():
            return False
        maxSize = 0
        for childNode in node.getSubBoxList():
            if maxSize < childSize:
                maxSize = childSize
        if maxSize > self._sizeTresholdWidth * self._sizeTresholdHeight:
            return True
        self._currentVipsBlock.setIsVisualBlock(True)
        self._currentVipsBlock.setIsDividable(False)
        if node.getNode().getNodeName() == "Xdiv":
            self._currentVipsBlock.setDoC(7)
        if node.getNode().getNodeName() == "a":
            self._currentVipsBlock.setDoC(11)
        else:
            self._currentVipsBlock.setDoC(8)
        return True

    def ruleTen(self, node):
        """ generated source for method ruleTen """
        self._tempVipsBlock = None
        findPreviousSiblingNodeVipsBlock(node.getNode().getPreviousSibling(), self._vipsBlocks)
        if self._tempVipsBlock == None:
            return False
        if self._tempVipsBlock.isAlreadyDivided():
            return True
        return False

    def ruleEleven(self, node):
        """ generated source for method ruleEleven """
        return False if (self.isTextNode(node)) else True

    def ruleTwelve(self, node):
        """ generated source for method ruleTwelve """
        self._currentVipsBlock.setIsDividable(False)
        self._currentVipsBlock.setIsVisualBlock(True)
        if node.getNode().getNodeName() == "Xdiv":
            self._currentVipsBlock.setDoC(7)
        elif node.getNode().getNodeName() == "li":
            self._currentVipsBlock.setDoC(8)
        elif node.getNode().getNodeName() == "span":
            self._currentVipsBlock.setDoC(8)
        elif node.getNode().getNodeName() == "sup":
            self._currentVipsBlock.setDoC(8)
        elif node.getNode().getNodeName() == "img":
            self._currentVipsBlock.setDoC(8)
        else:
            self._currentVipsBlock.setDoC(333)
        return True

    def getSizeTresholdWidth(self):
        """ generated source for method getSizeTresholdWidth """
        return self._sizeTresholdWidth

    def setSizeTresholdWidth(self, sizeTresholdWidth):
        """ generated source for method setSizeTresholdWidth """
        self._sizeTresholdWidth = sizeTresholdWidth

    def getSizeTresholdHeight(self):
        """ generated source for method getSizeTresholdHeight """
        return self._sizeTresholdHeight

    def setSizeTresholdHeight(self, sizeTresholdHeight):
        """ generated source for method setSizeTresholdHeight """
        self._sizeTresholdHeight = sizeTresholdHeight

    def getVipsBlocks(self):
        """ generated source for method getVipsBlocks """
        return self._vipsBlocks

    def findPreviousSiblingNodeVipsBlock(self, node, vipsBlock):
        """ generated source for method findPreviousSiblingNodeVipsBlock """
        if vipsBlock.getBox().getNode() == node:
            self._tempVipsBlock = vipsBlock
            return
        else:
            for vipsBlockChild in vipsBlock.getChildren():
                self.findPreviousSiblingNodeVipsBlock(node, vipsBlockChild)

