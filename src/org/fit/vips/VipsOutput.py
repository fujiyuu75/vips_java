#!/usr/bin/env python
""" generated source for module VipsOutput """
# 
#  * Tomas Popela, 2012
#  * VIPS - Visual Internet Page Segmentation
#  * Module - VipsOutput.java
#  
# package: org.fit.vips
import java.io.File

import java.io.FileWriter

import java.io.StringWriter

import javax.xml.parsers.DocumentBuilder

import javax.xml.parsers.DocumentBuilderFactory

import javax.xml.transform.OutputKeys

import javax.xml.transform.Transformer

import javax.xml.transform.TransformerException

import javax.xml.transform.TransformerFactory

import javax.xml.transform.dom.DOMSource

import javax.xml.transform.stream.StreamResult

import org.fit.cssbox.layout.Box

import org.fit.cssbox.layout.ElementBox

import org.fit.cssbox.layout.Viewport

import org.w3c.dom.Document

import org.w3c.dom.Element

# 
#  * Class, that handles output of VIPS algorithm.
#  * @author Tomas Popela
#  *
#  
class VipsOutput(object):
    """ generated source for class VipsOutput """
    doc = None
    _escapeOutput = True
    _pDoC = 0
    _order = 1
    _filename = "VIPSResult"

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """

    @__init__.register(object, int)
    def __init___0(self, pDoC):
        """ generated source for method __init___0 """
        self.setPDoC(pDoC)

    # 
    # 	 * Gets source code of visual structure nodes
    # 	 * @param node Given node
    # 	 * @return Source code
    # 	 
    def getSource(self, node):
        """ generated source for method getSource """
        content = ""
        try:
            transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes")
            transformer.transform(DOMSource(node), StreamResult(buffer_))
            content = buffer_.__str__().replaceAll("\n", "")
        except TransformerException as e:
            e.printStackTrace()
        return content

    # 
    # 	 * Append node from given visual structure to parent node
    # 	 * @param parentNode Given visual structure
    # 	 * @param visualStructure Parent node
    # 	 
    def writeVisualBlocks(self, parentNode, visualStructure):
        """ generated source for method writeVisualBlocks """
        layoutNode = self.doc.createElement("LayoutNode")
        layoutNode.setAttribute("FrameSourceIndex", String.valueOf(visualStructure.getFrameSourceIndex()))
        layoutNode.setAttribute("SourceIndex", visualStructure.getSourceIndex())
        layoutNode.setAttribute("DoC", String.valueOf(visualStructure.getDoC()))
        layoutNode.setAttribute("ContainImg", String.valueOf(visualStructure.containImg()))
        layoutNode.setAttribute("IsImg", String.valueOf(visualStructure.isImg()))
        layoutNode.setAttribute("ContainTable", String.valueOf(visualStructure.containTable()))
        layoutNode.setAttribute("ContainP", String.valueOf(visualStructure.containP()))
        layoutNode.setAttribute("TextLen", String.valueOf(visualStructure.getTextLength()))
        layoutNode.setAttribute("LinkTextLen", String.valueOf(visualStructure.getLinkTextLength()))
        parentBox = visualStructure.getNestedBlocks().get(0).getBox().getParent()
        layoutNode.setAttribute("DOMCldNum", String.valueOf(parentBox.getNode().getChildNodes().getLength()))
        layoutNode.setAttribute("FontSize", String.valueOf(visualStructure.getFontSize()))
        layoutNode.setAttribute("FontWeight", String.valueOf(visualStructure.getFontWeight()))
        layoutNode.setAttribute("BgColor", visualStructure.getBgColor())
        layoutNode.setAttribute("ObjectRectLeft", String.valueOf(visualStructure.getX()))
        layoutNode.setAttribute("ObjectRectTop", String.valueOf(visualStructure.getY()))
        layoutNode.setAttribute("ObjectRectWidth", String.valueOf(visualStructure.getWidth()))
        layoutNode.setAttribute("ObjectRectHeight", String.valueOf(visualStructure.getHeight()))
        layoutNode.setAttribute("ID", visualStructure.getId())
        layoutNode.setAttribute("order", String.valueOf(self._order))
        self._order += 1
        if self._pDoC >= visualStructure.getDoC():
            if visualStructure.getChildrenVisualStructures().size() == 0:
                if visualStructure.getNestedBlocks().size() > 0:
                    for block in visualStructure.getNestedBlocks():
                        if elementBox == None:
                            continue 
                        if not elementBox.getNode().getNodeName() == "Xdiv" and not elementBox.getNode().getNodeName() == "Xspan":
                            src += self.getSource(elementBox.getElement())
                        else:
                            src += elementBox.getText()
                        content += elementBox.getText() + " "
                    layoutNode.setAttribute("SRC", src)
                    layoutNode.setAttribute("Content", content)
            parentNode.appendChild(layoutNode)
            for child in visualStructure.getChildrenVisualStructures():
                self.writeVisualBlocks(layoutNode, child)
        else:
            if visualStructure.getNestedBlocks().size() > 0:
                for block in visualStructure.getNestedBlocks():
                    if elementBox == None:
                        continue 
                    if not elementBox.getNode().getNodeName() == "Xdiv" and not elementBox.getNode().getNodeName() == "Xspan":
                        src += self.getSource(elementBox.getElement())
                    else:
                        src += elementBox.getText()
                    content += elementBox.getText() + " "
                layoutNode.setAttribute("SRC", src)
                layoutNode.setAttribute("Content", content)
            parentNode.appendChild(layoutNode)

    def writeXML(self, visualStructure, pageViewport):
        """ generated source for method writeXML """
        try:
            self.doc = docBuilder.newDocument()
            vipsElement.setAttribute("Url", pageViewport.getRootBox().getBase().__str__())
            vipsElement.setAttribute("PageTitle", pageTitle)
            vipsElement.setAttribute("WindowWidth", String.valueOf(pageViewport.getContentWidth()))
            vipsElement.setAttribute("WindowHeight", String.valueOf(pageViewport.getContentHeight()))
            vipsElement.setAttribute("PageRectTop", String.valueOf(pageViewport.getAbsoluteContentY()))
            vipsElement.setAttribute("PageRectLeft", String.valueOf(pageViewport.getAbsoluteContentX()))
            vipsElement.setAttribute("PageRectWidth", String.valueOf(pageViewport.getContentWidth()))
            vipsElement.setAttribute("PageRectHeight", String.valueOf(pageViewport.getContentHeight()))
            vipsElement.setAttribute("neworder", "0")
            vipsElement.setAttribute("order", String.valueOf(pageViewport.getOrder()))
            self.doc.appendChild(vipsElement)
            self.writeVisualBlocks(vipsElement, visualStructure)
            transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes")
            transformer.setOutputProperty(OutputKeys.INDENT, "yes")
            if self._escapeOutput:
                transformer.transform(source, result)
            else:
                transformer.transform(source, StreamResult(writer))
                result = result.replaceAll("&gt;", ">")
                result = result.replaceAll("&lt;", "<")
                result = result.replaceAll("&quot;", "\"")
                fstream.write(result)
                fstream.close()
        except Exception as e:
            System.err.println("Error: " + e.getMessage())
            e.printStackTrace()

    def setEscapeOutput(self, value):
        """ generated source for method setEscapeOutput """
        self._escapeOutput = value

    def setPDoC(self, pDoC):
        """ generated source for method setPDoC """
        if pDoC <= 0 or pDoC > 11:
            System.err.println("pDoC value must be between 1 and 11! Not " + pDoC + "!")
            return
        else:
            self._pDoC = pDoC

    def setOutputFileName(self, filename):
        """ generated source for method setOutputFileName """
        if not filename == "":
            self._filename = filename

