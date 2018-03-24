import sys, os
import json

def lkupVonJson(key,fname):
	data = json.load(open(fname))
	if key not in data:
		return ''
	else:
		return(data[key])
		
if __name__=="__main__":
	if len(sys.argv)<2:
		print('Command Format: python wiktcrl.py [keyword]')
		sys.exit(0)
	kw = sys.argv[1]
	bdin = './word_dict/' + kw[0] + '/'
	for fn in os.listdir(bdin):
		fname = bdin + fn
		res = lkupVonJson(kw,fname)
		if res!='':
			break
	if res!='':
		print('Definition for ', kw, ' from Simplified Wiktionary')
		print(res)
	else:
		print('No Definition for ', kw, ' from Simplified Wiktionary')