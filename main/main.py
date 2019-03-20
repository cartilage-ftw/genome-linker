import requests
from bs4 import BeautifulSoup
from pathlib import Path

def search_gene_ncbi(gene_name):
    open_url = requests.request('GET', 'https://www.ncbi.nlm.nih.gov/gene/?term=' + gene_name)
    soup = BeautifulSoup(open_url.text, 'html.parser')
    #results_table = soup.find('tbody')
    for name_result in soup.findAll('tr', {'class': 'rprt'}):
        gene_name_ids = name_result.find('td', {'class': 'gene-name-id'})
        input_data = gene_name_ids.input
        print(input_data['value'])

# Let's print the IDs of the genes that appear upon searching for 'TP53'
search_gene_ncbi('TP53')


parent_dir = Path(__file__).resolve().parents[1]
dump_path = parent_dir / 'data' / 'dump.txt'

'''
try:
    f = open(dump_path, 'w')
    f.write(str(req.data))
except IOError:
    print("An error occured while reading the file at ", dump_path)
'''