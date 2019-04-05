import pandas as pd
import numpy as np

from pathlib import Path

# Downloaded from the PheGenI database
phe_gen_i_path = 'PheGenI_Association_full.tab'

# Downloaded from DisGeNET
gene_dis_assn_path = 'curated_gene_disease_associations.tsv'
variant_dis_assn_path = 'curated_variant_disease_associations.tsv'

def load_tab_sep(file_name):
    '''
    Reads a tab-separated file into a pandas dataframe
    :return: a pandas dataframe object matrix which contains the values from the dataset
    '''
    file_path = Path(__file__).resolve().parents[1] / 'data' / file_name
    df = pd.read_csv(file_path, sep='\t', engine='python')
    df.fillna('', inplace=True)
    print("Successfully read:", file_name)
    return df


# Pandas dataframes for each of the data files

phe_gen_i_data = load_tab_sep(phe_gen_i_path)
gene_dis_assn_data = load_tab_sep(gene_dis_assn_path)
variant_dis_assn_data = load_tab_sep(variant_dis_assn_path)