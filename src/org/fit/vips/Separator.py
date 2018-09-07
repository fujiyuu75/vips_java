#!/usr/bin/env python
""" generated source for module Separator """
# 
#  * Tomas Popela, 2012
#  * VIPS - Visual Internet Page Segmentation
#  * Module - Separator.java
#  
# package: org.fit.vips
import java.awt.Point

# 
#  * Class that represents visual separator.
#  * @author Tomas Popela
#  *
#  
class Separator(Comparable, Separator):
    """ generated source for class Separator """
    startPoint = 0
    endPoint = 0
    weight = 3
    normalizedWeight = 0

    #  for horizontal separators it means
    leftUp = Point()
    rightDown = Point()

    @overloaded
    def __init__(self, start, end):
        """ generated source for method __init__ """
        super(Separator, self).__init__()
        self.startPoint = start
        self.endPoint = end

    @__init__.register(object, int, int, int)
    def __init___0(self, start, end, weight):
        """ generated source for method __init___0 """
        super(Separator, self).__init__()
        self.startPoint = start
        self.endPoint = end
        self.weight = weight

    @__init__.register(object, int, int, int, int)
    def __init___1(self, leftUpX, leftUpY, rightDownX, rightDownY):
        """ generated source for method __init___1 """
        super(Separator, self).__init__()
        self.leftUp = Point(leftUpX, leftUpY)
        self.rightDown = Point(rightDownX, rightDownY)
        self.startPoint = leftUpX
        self.endPoint = rightDownY

    def setLeftUp(self, leftUpX, leftUpY):
        """ generated source for method setLeftUp """
        self.leftUp = Point(leftUpX, leftUpY)

    def setRightDown(self, rightDownX, rightDownY):
        """ generated source for method setRightDown """
        self.rightDown = Point(rightDownX, rightDownY)

    def compareTo(self, otherSeparator):
        """ generated source for method compareTo """
        return self.weight - otherSeparator.weight

