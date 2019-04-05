import load_dbs

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ApplicationUI(QMainWindow):

	# Enter command-line arguments as a list

	def __init__(self):
		self.app = QApplication([])
		#self.win = QMainWindow()
		super().__init__()
		self.setWindowTitle('Genome Linker')
		#win.setCentralWidget(QWidget())
		self.resize(600, 400)

		self.searchbox = QLineEdit(self)
		self.searchbox.move(12, 12)
		self.searchbox.resize(500, 24)

		self.auto_completer = QCompleter()
		self.searchbox.setCompleter(self.auto_completer)

		self.model = QStringListModel()
		self.model.setStringList(set(load_dbs.gene_dis_assn_data['diseaseName'].iloc[:]))
		self.auto_completer.setModel(self.model)

		#searchbox.show()
		self.show()
		self.app.exec_()