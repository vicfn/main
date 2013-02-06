#!/usr/bin/python -3

from __future__ import print_function

import xml.etree.cElementTree as et
tree=et.parse('sample2.xml')
root=tree.getroot()

print(root.tag)
for child in root:
	print("Child 1: ", child.tag, child.text)
	if(child.tag=='anime'):
		for child2 in child:
				print("    Child 2: ", child2.tag, child2.text)
