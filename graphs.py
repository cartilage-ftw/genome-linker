import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from pathlib import Path
from main import load_dbs

some_data = {"Neoplastic Syndromes, Hereditary" : 4864,
"Calcification of coronary artery" : 3393,
"Rheumatoid Arthritis" : 1618,
"Hereditary Breast and Ovarian Cancer Syndrome" : 1565,
"Hereditary Nonpolyposis Colorectal Cancer" : 1234,
"Hypercholesterolemia, Familial" : 1150,
"Schizophrenia" : 1114,
"Diabetes Mellitus, Non-Insulin-Dependent" : 803,
"Breast Carcinoma" : 803,
"Crohn Disease" : 774,
"Androgenetic Alopecia" : 742,
"Multiple Myeloma" : 734,
"Sarcoidosis" : 731,
"Breast Cancer, Familial" : 644,
"Diabetes Mellitus, Insulin-Dependent" : 605,
"Multiple Sclerosis" : 593,
"Alzheimer's Disease" : 585,
"Biliary cirrhosis" : 560,
"Psoriasis" : 559}

some_data2 = {"Hereditary Neoplastic Syndromes" : 4864,
"Calcification of coronary artery" : 3393,
"Rheumatoid Arthritis" : 1618,
"Hereditary Breast & Ovarian Cancer" : 1565,
"Hereditary Nonpolyposis Colorectal Cancer" : 1234,
"Familial Hypercholesterolemia" : 1150,
"Schizophrenia" : 1114,
"Non-Insulin-Dependent Diabetes Mellitus" : 803,
"Breast Carcinoma" : 803,
"Crohn Disease" : 774,
"Androgenetic Alopecia" : 742,
"Multiple Myeloma" : 734,
"Sarcoidosis" : 731,
"Breast Cancer, Familial" : 644,
"Diabetes Mellitus, Insulin-Dependent" : 605,
"Multiple Sclerosis" : 593,
"Alzheimer's Disease" : 585,
"Biliary cirrhosis" : 560,
"Psoriasis" : 559}

def getCount():
	x = load_dbs.variant_dis_assn_data
	y = x[x['diseaseType'] == 'group']
	x = x[x['diseaseType'] == 'disease']
	x.append(y)
	#unique_diseases = x['diseaseName'].unique()
	#unique_genes = x['geneSymbol'].unique()
	#print(unique_diseases)
	#print('There are %d unique diseases, influnced by %d known genes', 
	# 		len(unique_diseases), len(unique_genes))

	#print(list(some_data.values()))
	#plt.hist(list(some_data.values()), bins=19)
	x = list(range(19))
	plt.figure(figsize=(8, 8))
	plt.bar(x, list(some_data.values()), align='center')
	plt.xlabel("", rotation='vertical')
	plt.ylabel("No. of variants identified")
	plt.yticks(rotation='vertical')
	plt.xticks(x, list(some_data.keys()), rotation='vertical')
	plt.savefig('fig.png', bbox_inches='tight', pad_inches=0.25)
	plt.show()
	#plt.show()
	#print(x['diseaseName'].value_counts())
	'''file_path = Path(__file__).resolve().parents[0] / 'data/most_genes.csv'
	print(file_path)
	count = pd.read_csv(file_path, sep='\t', engine='python')
	count.describe()'''
	#print(count.describe())
		#print(element['diseaseName'], x[element].count())


if __name__ == "__main__":
	getCount()
