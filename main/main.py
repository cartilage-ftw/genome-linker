import requests
import pandas as pd

from bs4 import BeautifulSoup
from pathlib import Path
from PyQt5.QtWidgets import *

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

# Reads the data downloaded from the PheGenI database of NCBI
def read_phe_gen_i():
    file_name = 'PheGenI_Association_full.tab'
    file_path = Path(__file__).resolve().parents[1] / 'data' / file_name
    df = pd.read_csv(file_path, sep='\t', engine='python')
    print(df['Trait'].head())
    return df

'''
win = QWidget()
table = QTableWidget()
layout = QVBoxLayout()
layout.addWidget(table)
win.setLayout(layout)

def create_ui(dataframe):
    table.setColumnCount(len(dataframe.columns))
    table.setRowCount(len(dataframe.index))
    for i in range(len(dataframe.index)):
        for j in range(len(dataframe.columns)):
            table.setItem(i, j, QTableWidgetItem(str(dataframe.iloc[i,j])))
    win.show()
'''

dataframe = read_phe_gen_i()
#TODO: use something different from PyQt (doesn't work on my computer)
#create_ui(dataframe)

'''
parent_dir = Path(__file__).resolve().parents[1]
dump_path = parent_dir / 'data' / 'dump.txt'

try:
    f = open(dump_path, 'w')
    f.write(str(req.data))
except IOError:
    print("An error occured while reading the file at ", dump_path)
'''