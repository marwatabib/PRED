import cirpy
import pandas as pd
import json

df = pd.read_csv("Fichiers-Sources/OdorCAS.csv", delimiter="\t")
print(df.columns)
cas_to_smile = {}
Does_not_Work = {'is_none':[], 'error' : []}
Smile_is_None=[]
for cas in df['Unnamed: 0']:
#	try :
	smile = cirpy.resolve(cas,'smiles')
	if smile is None:
		Does_not_Work['is_none'].append(cas)
	else:
		if smile in cas_to_smile.keys():
			cas_to_smile[smile].append(cas)
		else:
			cas_to_smile[smile]= [cas]
		"""
	except:
		Does_not_Work["error"].append(cas)
"""

f= open("Cas_to_smiles.json",'w')
json.dump(cas_to_smile, f)
f.close()

f = open('Error_to_smiles.json','w')
json.dump(Does_not_Work, f)
f.close


