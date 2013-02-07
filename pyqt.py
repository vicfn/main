#!/usr/local/bin/python3
import subprocess
import sys
import PyQt4.QtGui as qtgui
import xml.etree.cElementTree as et

class MainWindow(qtgui.QWidget):
	layout_main_vert = None
	label_lineedit= []
	submit = None

#Initialize object variables. Has to be done in __init__ otherwise static vars
	def __init__(self):
		super(MainWindow, self).__init__()
		self.label_lineedit= []

		self.setGeometry(300,300,250,150)
		self.setWindowTitle("Dis Window Title")

		self.layout_main_vert = qtgui.QVBoxLayout()
		self.submit = qtgui.QPushButton("Submit!")

		self.initSignalSlots()
		self.initLayout()	

#Setup QT signals and slots
	def initSignalSlots(self):
		self.submit.clicked.connect(self.debug)
		
#Setup window layout. Main layout is vertical, with nested horizontals
	def initLayout(self):
		self.addLine("First", "one")
		self.addLine("Second", "two")
		self.addLine("Third", "three")
		self.layout_main_vert.addWidget(self.submit)
		self.setLayout(self.layout_main_vert)
		self.show()

#Add a line, which consists of a QLabel and a QLineEdit
	def addLine(self, label_text, lineedit_text):
		temp_layout_hz = qtgui.QHBoxLayout()
		temp_label = qtgui.QLabel(label_text)
		temp_lineedit = qtgui.QLineEdit(lineedit_text)
		temp_layout_hz.addWidget(temp_label)
		temp_layout_hz.addWidget(temp_lineedit)
	
		self.layout_main_vert.addLayout(temp_layout_hz)

	def debug(self):
		self.addLine("Hello", "World!")
		print("FLAGGED!")

class MALParser():
	anime_list = {}
	tree = None
	root = None
	
	def __init__(self):
		anime_list = {}
		
	def parse(self, xml_path):
		self.tree=et.parse(xml_path)
		self.root=self.tree.getroot()
		parse_root(self.root)

	def parse_root(self, xml_tree_root):
		for child in xml_tree_root:
			if(child.tag=='anime'):
				anime_series=parse_anime_entry(child)
				self.anime_list[anime_series['series_animedb_id']]=anime_series
		print(self.anime_list)
		return self.anime_list

	def parse_anime_entry(self, anime_entry):
		result = {}
		for tag in anime_entry:
			result[tag.tag] = tag.text
		return result

mal_parser=MALParser()
mal_parser.parse('sample2.xml')

#a = qtgui.QApplication(sys.argv)
#window = MainWindow()
#sys.exit(a.exec_())
