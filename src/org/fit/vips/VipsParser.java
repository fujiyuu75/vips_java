/*
 * Tomas Popela, xpopel11, 2012
 * VIPS - Visual Internet Page Segmentation
 * Module - VipsParser.java
 */

package org.fit.vips;

import org.fit.cssbox.layout.Box;
import org.fit.cssbox.layout.ElementBox;
import org.fit.cssbox.layout.TextBox;
import org.fit.cssbox.layout.Viewport;
import org.w3c.dom.Node;

public class VipsParser {

	private VisualStructure _visualStructure = null;
	private VisualStructure _currentVisualStructure = null;
	private VisualStructure _tempVisualStructure = null;
	
	private int _sizeTresholdWidth = 0;
	private int _sizeTresholdHeight = 0;
	private Viewport _viewport = null;
	private int visualBlockCount = 0;

	/**
	 * Default constructor
	 * 
	 * @param viewport Rendered's page viewport            
	 */
	public VipsParser(Viewport viewport) {
		this._viewport = viewport;
		this._visualStructure = new VisualStructure();
		this._sizeTresholdHeight = 50;
		this._sizeTresholdWidth = 50;
	}

	/**
	 * Starts visual page segmentation on given page
	 */
	public void parse()
	{
		if (_viewport != null)
		{
			constructVisualStructureTree(_viewport.getElementBoxByName("body", false), _visualStructure);
			checkViewportTree(_visualStructure);
			getVisualBlockCount(_visualStructure);
			System.out.println(String.valueOf(visualBlockCount));
		}
		else
			System.out.print("Page's ViewPort is not defined");
	}
	
	private void getVisualBlockCount(VisualStructure visualStructure)
	{
		if (visualStructure.isVisualBlock())
			visualBlockCount++;
			
		for (VisualStructure visualStructureChild : visualStructure.getChilds())
		{
			if (!(visualStructureChild.getBox() instanceof TextBox))
				getVisualBlockCount(visualStructureChild);
		}
	}
	
	private void constructVisualStructureTree(Box element, VisualStructure node)
	{
		node.setBox(element);
		
		if (! (element instanceof TextBox))
		{
			for (Box box: ((ElementBox) element).getSubBoxList()) 
			{
				node.addChild(new VisualStructure());
				constructVisualStructureTree(box, node.getChilds().get(node.getChilds().size()-1));
			}
		}
	}
	
	private void checkViewportTree(VisualStructure visualStructure)
	{
		_currentVisualStructure = visualStructure;
		ElementBox elementBox = (ElementBox) visualStructure.getBox();
		System.out.println(elementBox.getNode().getNodeName());
		
		if (applyVipsRules(elementBox) && visualStructure.isDividable() && !visualStructure.isVisualBlock())
		{
			_currentVisualStructure.setAlreadyDivided(true);
			for (VisualStructure visualStructureChild : visualStructure.getChilds())
			{
				if (!(visualStructureChild.getBox() instanceof TextBox))
					checkViewportTree(visualStructureChild);
			}
		}
		else
		{
			if (visualStructure.isDividable())
			{
				System.out.println("Element " + elementBox.getNode().getNodeName() + " is visual block");
				visualStructure.setIsVisualBlock(true);
			}
			else
				System.out.println("Element " + elementBox.getNode().getNodeName() + " is not dividable");
		}
	}
	
	/**
	 * Checks, if node is a valid node.
	 * <p>
	 * Node is valid, if it's visible in browser. This means, that the node's
	 * width and height are not zero.
	 * 
	 * @param node
	 *            Input node
	 * 
	 * @return True, if node is valid, otherwise false.
	 */
	private boolean isValidNode(ElementBox node)
	{
		if (node.getHeight() > 0 && node.getWidth() > 0)
			return true;
		
		return false;
	}
	
	/**
	 * Checks, if node is a text node.
	 * 
	 * @param node
	 *            Input node
	 * 
	 * @return True, if node is a text node, otherwise false.
	 */
	private boolean isTextNode(ElementBox box)
	{
		return (box.getNode().getNodeName().equals("text")) ? true : false;
	}

	/**
	 * Checks, if node is a virtual text node.
	 * <p>
	 * Inline node with only text node children is a virtual text node.
	 * 
	 * @param node
	 *            Input node
	 * 
	 * @return True, if node is virtual text node, otherwise false.
	 */
	private boolean isVirtualTextNode1(ElementBox node)
	{
		if (node.isBlock())
			return false;
		
		for (Box childNode : node.getSubBoxList()) 
		{
			if (!(childNode instanceof TextBox))
				if (!isTextNode((ElementBox) childNode))
					return false;
		}
	
		return true;
	}

	/**
	 * Checks, if node is virtual text node.
	 * <p>
	 * Inline node with only text node and virtual text node children is a
	 * virtual text node.
	 *
	 * @param node
	 *            Input node
	 * 
	 * @return True, if node is virtual text node, otherwise false.
	 */
	private boolean isVirtualTextNode2(ElementBox node)
	{		
		if (node.isBlock())
			return false;
		
		for (Box childNode : node.getSubBoxList())
			if (!isTextNode((ElementBox) childNode) ||
				!isVirtualTextNode1((ElementBox) childNode))
				return false;
		
		return true;
	}
	
	/**
	 * Checks, if node is virtual text node.
	 * 
	 * @param node
	 *            Input node
	 * 
	 * @return True, if node is virtual text node, otherwise false.
	 */
	private boolean isVirtualTextNode(ElementBox node)
	{
		if (isVirtualTextNode1(node))
			return true;
		if (isVirtualTextNode2(node))
			return true;
		
		return false;			
	}
	
	/*
	 * Checks if node has valid children nodes
	 */
	private boolean hasValidChildNodes(ElementBox node)
	{
		if (node.getSubBoxList().isEmpty())
			return false;
		
		for (Box childNode : node.getSubBoxList())
		{
			if (childNode instanceof TextBox)
				continue;
			if (!isValidNode((ElementBox) childNode))
				return false;
			
		}
		return true;
	}

	/*
	 * Returns the number of node's valid children
	 */
	private int numberOfValidChildNodes(ElementBox node)
	{
		int cnt = 0;

		if (node.getSubBoxList().isEmpty())
			return cnt;
		
		for (Box childNode : node.getSubBoxList())
		{
			//TODO nebo text neni validni uzel?
			if (childNode instanceof TextBox) 
			{
				cnt++;
				continue;
			}
			if (isValidNode((ElementBox) childNode))
				cnt++;
		}

		return cnt;
	}
	
	private boolean applyVipsRules(ElementBox node)
	{
		boolean retVal = false;
		
		System.out.println("Applying VIPS rules on " + node.getNode().getNodeName() + " node");
		
		if (!node.isBlock())
		//if (isInlineNode(node))
		{
			//????????
			retVal = applyInlineTextNodeVipsRules(node);
			//retVal = false;
		}
		else if (node.getElement().getNodeName().equals("table"))
		{
			retVal = applyTableNodeVipsRules(node);
		}
		else if (node.getElement().getNodeName().equals("#tr"))
		{
			retVal = applyTrNodeVipsRules(node);
		}		
		else if (node.getElement().getNodeName().equals("#td"))
		{
			retVal = applyTdNodeVipsRules(node);
		}
		else if (node.getElement().getNodeName().equals("#p"))
		{
			retVal = applyPNodeVipsRules(node);
		}
		else if (node.getElement().getNodeName().substring(0, 1).equals("X"))
		{
			retVal = false;
		}
		else
		{
			retVal = applyOtherNodeVipsRules(node);
		}
		
		return retVal;
	}
	
	private boolean applyOtherNodeVipsRules(ElementBox node)
	{
		// 1 2 3 4 6 8 9 11 
		
		if (ruleOne(node))
			return true;
			
		if (ruleTwo(node))
			return true;
		
		if (ruleThree(node))
			return true;
		
		if (ruleFour(node))
			return true;
		
		if (ruleSix(node))
			return true;
			
		if (ruleEight(node))
			return true;
		
		if (ruleNine(node))
			return true;
		
		if (ruleEleven(node))
			return true;
		
		return false;
	}

	private boolean applyPNodeVipsRules(ElementBox node)
	{
		// 1 2 3 4 5 6 8 9 11 
		
		if (ruleOne(node))
			return true;
			
		if (ruleTwo(node))
			return true;
		
		if (ruleThree(node))
			return true;
		
		if (ruleFour(node))
			return true;
		
		if (ruleFive(node))
			return true;
		
		if (ruleSix(node))
			return true;
			
		if (ruleSeven(node))
			return true;
		
		if (ruleEight(node))
			return true;
		
		if (ruleNine(node))
			return true;
		
		if (ruleTen(node))
			return true;
		
		if (ruleEleven(node))
			return true;
		
		if (ruleTwelve(node))
			return true;
		
		return false;
	}

	private boolean applyTdNodeVipsRules(ElementBox node)
	{
		// 1 2 3 4 8 9 10 12 
		
		if (ruleOne(node))
			return true;
			
		if (ruleTwo(node))
			return true;
		
		if (ruleThree(node))
			return true;
		
		if (ruleFour(node))
			return true;
		
		if (ruleEight(node))
			return true;
		
		if (ruleNine(node))
			return true;
		
		if (ruleTen(node))
			return true;
		
		if (ruleTwelve(node))
			return true;
		
		return false;
	}

	private boolean applyTrNodeVipsRules(ElementBox node)
	{
		// 1 2 3 7 9 12 
		
		if (ruleOne(node))
			return true;
			
		if (ruleTwo(node))
			return true;
		
		if (ruleThree(node))
			return true;
		
		if (ruleSeven(node))
			return true;
		
		if (ruleNine(node))
			return true;
		
		if (ruleTwelve(node))
			return true;
		
		return false;
	}

	private boolean applyTableNodeVipsRules(ElementBox node)
	{
		// 1 2 3 7 9 12 
		
		if (ruleOne(node))
			return true;
			
		if (ruleTwo(node))
			return true;
		
		if (ruleThree(node))
			return true;
		
		if (ruleSeven(node))
			return true;
		
		if (ruleNine(node))
			return true;
		
		if (ruleTwelve(node))
			return true;
		
		return false;
	}

	private boolean applyInlineTextNodeVipsRules(ElementBox node)
	{
		// 1 2 3 4 5 6 8 9 11 
		
		if (ruleOne(node))
			return true;
			
		if (ruleTwo(node))
			return true;
		
		if (ruleThree(node))
			return true;
		
		if (ruleFour(node))
			return true;
		
		if (ruleFive(node))
			return true;
		
		if (ruleSix(node))
			return true;
			
		if (ruleEight(node))
			return true;
		
		if (ruleNine(node))
			return true;
		
		if (ruleTwelve(node))
			return true;
		
		return false;
	}

	/**
	 * VIPS Rule One
	 * <p>
	 * If the DOM node is not a text node and it has no valid children, then
	 * this node cannot be divided and will be cut.
	 * 
	 * @param node
	 *            Input node
	 * 
	 * @return True, if rule is applied, otherwise false.
	 */
	private boolean ruleOne(ElementBox node)
	{
		System.out.println("Applying rule One on " + node.getNode().getNodeName() + " node");
		
		if (!isTextNode(node))
			if (!hasValidChildNodes(node))
			{
				_currentVisualStructure.setIsDividable(false);
				return true;
			}

		return false;
	}

	/**
	 * VIPS Rule Two
	 * <p>
	 * If the DOM node has only one valid child and the child is not a text
	 * node, then divide this node
	 * 
	 * @param node
	 *            Input node
	 * 
	 * @return True, if rule is applied, otherwise false.
	 */
	private boolean ruleTwo(ElementBox node)
	{
		System.out.println("Applying rule Two on " + node.getNode().getNodeName() + " node");
		
		if (numberOfValidChildNodes(node) == 1)
		{
			if (node.getSubBox(0) instanceof TextBox)
				return false;
			if (!isTextNode((ElementBox) node.getSubBox(0)))
				return true;
		}

		return false;
	}

	/**
	 * VIPS Rule Three
	 * <p>
	 * If the DOM node is the root node of the sub-DOM tree (corresponding to
	 * the block), and there is only one sub DOM tree corresponding to this
	 * block, divide this node.
	 * 
	 * @param node
	 *            Input node
	 * 
	 * @return True, if rule is applied, otherwise false.
	 */
	private boolean ruleThree(ElementBox node)
	{
		System.out.println("Applying rule Three on " + node.getNode().getNodeName() + " node");
		// ???????????????????????????????????????????????
		return false;
	}

	/**
	 * VIPS Rule Four
	 * <p>
	 * If all of the child nodes of the DOM node are text nodes or virtual text
	 * nodes, do not divide the node. <br> 
	 * If the font size and font weight of all these child nodes are same, set 
	 * the DoC of the extracted block to 10.
	 * Otherwise, set the DoC of this extracted block to 9.
	 * 
	 * @param node
	 *            Input node
	 * 
	 * @return True, if rule is applied, otherwise false.
	 */
	private boolean ruleFour(ElementBox node)
	{
		System.out.println("Applying rule Four on " + node.getNode().getNodeName() + " node");
		
		if (node.getSubBoxList().isEmpty())
			return false;
		
		for (Box box : node.getSubBoxList())
		{
			if (box instanceof TextBox)
				continue;
			if (!isTextNode((ElementBox) box) ||
				!isVirtualTextNode((ElementBox) box))
				return false;
		}
		
		_currentVisualStructure.setIsVisualBlock(true);
	
		if (node.getStylePropertyValue("font-weight") == null)
			return false;

		if (node.getStylePropertyValue("font-size") == null)
			return false;
		
		String fontWeight = node.getStylePropertyValue("font-weight").toString();
		String fontSize = node.getStylePropertyValue("font-size").toString();
		
		for (Box childNode : node.getSubBoxList())
		{
			if (childNode instanceof TextBox)
				continue;
		
			ElementBox child = (ElementBox) childNode;
			
			if (child.getStylePropertyValue("font-weight") == null)
				return false;
	
			if (child.getStylePropertyValue("font-size") == null)
				return false;
			
			if (child.getStylePropertyValue("font-weight").toString().equals(fontWeight) &&
			    child.getStylePropertyValue("font-size").toString().equals(fontSize))
				_currentVisualStructure.setDoC(10);
			else
				_currentVisualStructure.setDoC(9);
		}
		
		return true;
	}

	/**
	 * VIPS Rule Five
	 * <p>
	 * If one of the child nodes of the DOM node is line-break node, then 
	 * divide this DOM node.
	 * 
	 * @param node
	 *            Input node
	 * 
	 * @return True, if rule is applied, otherwise false.
	 */
	private boolean ruleFive(ElementBox node)
	{
		System.out.println("Applying rule Five on " + node.getNode().getNodeName() + " node");
		
		if (node.getSubBoxList().isEmpty())
			return false;
	
		for (Box childNode : node.getSubBoxList())
			if (childNode.isBlock())
				return true;
		
		return false;
	}
	
	/**
	 * VIPS Rule Six
	 * <p>
	 * If one of the child nodes of the DOM node has HTML tag &lt;hr&gt;, then 
	 * divide this DOM node
	 * 
	 * @param node
	 *            Input node
	 * 
	 * @return True, if rule is applied, otherwise false.
	 */
	private boolean ruleSix(ElementBox node)
	{
		System.out.println("Applying rule Six on " + node.getNode().getNodeName() + " node");
		if (node.getSubBoxList().isEmpty())
			return false;
		
		for (Box childNode : node.getSubBoxList())
			if (childNode.getNode().getNodeName().equals("hr"))
				return true;
		
		return false;
	}
	
	/**
	 * VIPS Rule Seven
	 * <p>
	 * If the background color of this node is different from one of its 
	 * children’s, divide this node and at the same time, the child node with 
	 * different background color will not be divided in this round.
	 * Set the DoC value (6-8) for the child node based on the &lt;html&gt; 
	 * tag of the child node and the size of the child node.
	 * 
	 * @param node
	 *            Input node
	 * 
	 * @return True, if rule is applied, otherwise false.
	 */
	private boolean ruleSeven(ElementBox node)
	{
		System.out.println("Applying rule Seven on " + node.getNode().getNodeName() + " node");
		if (node.getSubBoxList().isEmpty())
			return false;
		
		if (isTextNode(node))
			return false;

		String nodeBgColor = node.getBgcolor().toString();
		
		for (VisualStructure childVisualStructure : _currentVisualStructure.getChilds())
		{
			if (!((ElementBox) childVisualStructure.getBox()).getBgcolor().equals(nodeBgColor))
			{
				childVisualStructure.setIsDividable(false);
				return true;
			}
		}
		
		// TODO DoC values
		return false;
	}

	/**
	 * VIPS Rule Eight
	 * <p>
	 * If the node has at least one text node child or at least one virtual 
	 * text node child, and the node's relative size is smaller than 
	 * a threshold, then the node cannot be divided.
	 * Set the DoC value (from 5-8) based on the html tag of the node.
	 * @param node
	 *            Input node
	 * 
	 * @return True, if rule is applied, otherwise false.
	 */
	private boolean ruleEight(ElementBox node)
	{		
		System.out.println("Applying rule Eight on " + node.getNode().getNodeName() + " node");
		if (node.getSubBoxList().isEmpty())
			return false;
		
		int cnt = 0;

		for (Box childNode : node.getSubBoxList())
		{
			if (childNode instanceof TextBox)
			{
				cnt++;
				continue;
			}
			ElementBox child = (ElementBox) childNode;
			if (isTextNode(child)|| isVirtualTextNode(child))
				cnt++;				
		}
			
		if (cnt == 0)
			return false;

		// misto rozmeru pouzit spise plochu, kterou prvek zabira
		if (node.getWidth() > _sizeTresholdWidth && 
			node.getHeight() > _sizeTresholdHeight)
			return false;
		
		_currentVisualStructure.setIsVisualBlock(true);
		_currentVisualStructure.setIsDividable(false);
		
		//TODO DoC Part
		return true;
	}
	
	/**
	 * VIPS Rule Nine
	 * <p>
	 * If the child of the node with maximum size are is than 
	 * a threshold (relative size), do not divide this node. <br>
	 * Set the DoC based on the html tag and size of this node.
	 * @param node
	 *            Input node
	 * 
	 * @return True, if rule is applied, otherwise false.
	 */
	private boolean ruleNine(ElementBox node)
	{	
		System.out.println("Applying rule Nine on " + node.getNode().getNodeName() + " node");
		if (node.getSubBoxList().isEmpty())
			return false;
		
		int maxSize = 0;
	
		for (Box childNode : node.getSubBoxList())
		{
			int childSize = childNode.getWidth() * childNode.getHeight();
			
			if (maxSize < childSize)
				maxSize = childSize;
		}
		
		if (maxSize > _sizeTresholdWidth * _sizeTresholdHeight)
			return true;
	
		//TODO set DOC
		_currentVisualStructure.setIsVisualBlock(true);
		_currentVisualStructure.setIsDividable(false);
		
		return false;
	}
	
	/**
	 * VIPS Rule Ten
	 * <p>
	 * If previous sibling node has not been divided, do not divide this node
	 * @param node
	 *            Input node
	 * 
	 * @return True, if rule is applied, otherwise false.
	 */
	private boolean ruleTen(ElementBox node)
	{
		System.out.println("Applying rule Ten on " + node.getNode().getNodeName() + " node");
		
		_tempVisualStructure = null;
		findPreviousSiblingNodeVisualStructure(node.getNode().getPreviousSibling(), _visualStructure);
		
		if (_tempVisualStructure != null)
			if (_tempVisualStructure.isAlreadyDivided())
				return true;
		
		return false;
	}
	
	/**
	 * VIPS Rule Eleven
	 * <p>
	 * Divide this node.
	 * @param node
	 *            Input node
	 * 
	 * @return True, if rule is applied, otherwise false.
	 */
	private boolean ruleEleven(ElementBox node)
	{
		System.out.println("Applying rule Eleven on " + node.getNode().getNodeName() + " node");
		if (isTextNode(node))
			return false;
		
		return true;
	}
	
	/**
	 * VIPS Rule Twelve
	 * <p>
	 * Do not divide this node <br>
	 * Set the DoC value based on the html tag and size of this node.
	 * @param node
	 *            Input node
	 * 
	 * @return True, if rule is applied, otherwise false.
	 */
	private boolean ruleTwelve(ElementBox node)
	{
		System.out.println("Applying rule Twelve on " + node.getNode().getNodeName() + " node");
		
		_currentVisualStructure.setIsDividable(false);
		_currentVisualStructure.setIsVisualBlock(true);
		
		//TODO DoC Part
		return false;
	}
	
	/*
	 * Checks if element is inline element
	 */
	private boolean isInlineNode(ElementBox node)
	{
		/*
		 * NodeData nodeData = _domAnalyzer.getElementStyle((Element) node);
		 * 
		 * if (nodeData.getProperty("display") != null) {
		 * System.out.print(" - ");
		 * System.out.print(nodeData.getProperty("display").toString()); return
		 * (nodeData.getProperty("display").toString().equals("inline")) ? true
		 * : false; }
		 */

		if (node.getNode().getNodeName().equals("a"))
			return true;
		if (node.getNode().getNodeName().equals("abbr"))
			return true;
		if (node.getNode().getNodeName().equals("acronym"))
			return true;
		if (node.getNode().getNodeName().equals("b"))
			return true;
		if (node.getNode().getNodeName().equals("bdo"))
			return true;
		if (node.getNode().getNodeName().equals("big"))
			return true;
		if (node.getNode().getNodeName().equals("br"))
			return true;
		if (node.getNode().getNodeName().equals("cite"))
			return true;
		if (node.getNode().getNodeName().equals("code"))
			return true;
		if (node.getNode().getNodeName().equals("dfn"))
			return true;
		if (node.getNode().getNodeName().equals("em"))
			return true;
		if (node.getNode().getNodeName().equals("i"))
			return true;
		if (node.getNode().getNodeName().equals("img"))
			return true;
		if (node.getNode().getNodeName().equals("input"))
			return true;
		if (node.getNode().getNodeName().equals("kdb"))
			return true;
		if (node.getNode().getNodeName().equals("label"))
			return true;
		if (node.getNode().getNodeName().equals("q"))
			return true;
		if (node.getNode().getNodeName().equals("samp"))
			return true;
		if (node.getNode().getNodeName().equals("select"))
			return true;
		if (node.getNode().getNodeName().equals("small"))
			return true;
		if (node.getNode().getNodeName().equals("span"))
			return true;
		if (node.getNode().getNodeName().equals("strong"))
			return true;
		if (node.getNode().getNodeName().equals("sub"))
			return true;
		if (node.getNode().getNodeName().equals("sup"))
			return true;
		if (node.getNode().getNodeName().equals("textarea"))
			return true;
		if (node.getNode().getNodeName().equals("tt"))
			return true;
		if (node.getNode().getNodeName().equals("var"))
			return true;
		
		return false;
	}

	/**
	 * @return the _sizeTresholdWidth
	 */
	public int getSizeTresholdWidth()
	{
		return _sizeTresholdWidth;
	}

	/**
	 * @param sizeTresholdWidth the _sizeTresholdWidth to set
	 */
	public void setSizeTresholdWidth(int sizeTresholdWidth)
	{
		this._sizeTresholdWidth = sizeTresholdWidth;
	}
	
	/**
	 * @return the _sizeTresholdHeight
	 */
	public int getSizeTresholdHeight()
	{
		return _sizeTresholdHeight;
	}

	/**
	 * @param sizeTresholdHeight the _sizeTresholdHeight to set
	 */
	public void setSizeTresholdHeight(int sizeTresholdHeight)
	{
		this._sizeTresholdHeight = sizeTresholdHeight;
	}
	
	public VisualStructure getVisualStrucure()
	{
		return _visualStructure;
	}
	
	private void findPreviousSiblingNodeVisualStructure(Node node, VisualStructure visualStructure)
	{
		if (!visualStructure.getBox().getNode().equals(node))
			_tempVisualStructure = visualStructure;
		else
			for (VisualStructure childVisualStructure : visualStructure.getChilds())
				findPreviousSiblingNodeVisualStructure(node, childVisualStructure);
	}
}
