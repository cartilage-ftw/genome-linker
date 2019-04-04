import pandas as pd
import numpy as np

# Import self-written files

from pathlib import Path

# Downloaded from the PheGenI database
phe_gen_i_path = 'PheGenI_Association_full.tab'

# Downloaded from DisGeNET
gene_dis_assn_path = 'curated_gene_disease_associations.tsv'
variant_dis_assn_path = 'curated_variant_disease_associations.tsv'

# Reads the data downloaded from the PheGenI database of NCBI
# TODO: get rid of the NaN values from StudyId and Study names without removing
# the rows themselves (just empty the cells)
# Similarly, clean all cells with Analysis ID == 0
'''
def read_phe_gen_i():
    file_path = Path(__file__).resolve().parents[1] / 'data' / file_name
    df = pd.read_csv(file_path, sep='\t', engine='python')
    #print(df.head())
    return df
'''

def load_tab_sep(file_name):
    '''
    Reads a tab-separated file into a pandas dataframe
    '''
    file_path = Path(__file__).resolve().parents[1] / 'data' / file_name
    df = pd.read_csv(file_path, sep='\t', engine='python')
    print(df.shape)
    df.fillna('', inplace=True)
    #df_clean = df.applymap(lambda x: np.nan if isinstance(x, str) and x.isspace()
    #                        else x)
    #df_clean.dropna()
    #print(df_clean.shape)
    #df.dropna()
    print("Successfully read:", file_name)
    return df


# Pandas dataframes for each of the data files

phe_gen_i_data = load_tab_sep(phe_gen_i_path)
gene_dis_assn_data = load_tab_sep(gene_dis_assn_path)
variant_dis_assn_data = load_tab_sep(variant_dis_assn_path)
