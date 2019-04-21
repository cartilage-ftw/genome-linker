import sys
import requests

# Import self-written files

import load_dbs
import create_ui

from bs4 import BeautifulSoup
from pathlib import Path
from PyQt5.QtWidgets import *

# Unused
def search_gene_ncbi(gene_name):
    open_url = requests.request('GET', 'https://www.ncbi.nlm.nih.gov/gene/?term=' + gene_name)
    soup = BeautifulSoup(open_url.text, 'html.parser')
    #results_table = soup.find('tbody')
    for name_result in soup.findAll('tr', {'class': 'rprt'}):
        gene_name_ids = name_result.find('td', {'class': 'gene-name-id'})
        input_data = gene_name_ids.input
        #print(input_data.attrs)
        print(input_data['sid'] + '. ' + input_data['value'])
        #print(input_data['value'])

# Let's print the IDs of the genes that appear upon searching for 'TP53'
#search_gene_ncbi('TP53')

app = QApplication(sys.argv)
#win = QWidget()
win = QMainWindow()
table = QTableWidget()
#layout = QVBoxLayout()
#layout.addWidget(table)
#win.setLayout(layout)

def preview_df(dataframe):
    win.setWindowTitle('Genome Linker')
    win.setCentralWidget(table)
    table.setColumnCount(len(dataframe.columns))
    # Avoid printing the entire dataframe due to their enormous size
    table.setRowCount(1000)#len(dataframe.index))
    table.setHorizontalHeaderLabels(dataframe.columns)
    for i in range(1000):#len(dataframe.index)):
        for j in range(len(dataframe.columns)):
            table.setItem(i, j, QTableWidgetItem(str(dataframe.iloc[i,j])))
    win.show()
    app.exec_()

#df = load_dbs.variant_dis_assn_data
#schizoph = df[df['diseaseName'] == 'Schizophrenia']
#preview_df(df)
create_ui.ApplicationUI()

'''
parent_dir = Path(__file__).resolve().parents[1]
dump_path = parent_dir / 'data' / 'dump.txt'

try:
    f = open(dump_path, 'w')
    f.write(str(req.data))
except IOError:
    print("An error occured while reading the file at ", dump_path)
'''