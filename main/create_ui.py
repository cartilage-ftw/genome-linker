import load_dbs

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ApplicationUI(QMainWindow):

	def __init__(self):
		self.app = QApplication([])
		super().__init__()
		self.setWindowTitle('Genome Linker')
		self.resize(600, 400)

		# TODO: add a radio button list which asks whether you're searching by symptom,
		# disease name or phenotype
		# TODO: add a search button and results field

		self.searchbox = QLineEdit(self)
		self.searchbox.move(12, 12)
		self.searchbox.resize(500, 24)

		self.auto_completer = QCompleter()
		self.searchbox.setCompleter(self.auto_completer)

		self.model = QStringListModel()
		self.model.setStringList(set(load_dbs.gene_dis_assn_data['diseaseName'].iloc[:]))
		self.auto_completer.setModel(self.model)

		self.show()
		self.app.exec_()