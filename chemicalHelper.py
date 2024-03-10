def isUpper(txt : str) -> bool:
	return txt in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def isLower(txt : str) -> bool:
	return txt in list("abcdefghijklmnopqrstuvwxyz")

def isNum(txt : str) -> bool:
	return txt in list('0123456789')

def getAtomDatas() -> list:
	atomDatas = []
	with open('원자들.txt',encoding='utf8') as f:
		for line in f.readlines():
			code, name = line.rstrip().split()
			atomDatas.append(
				(code, name, {code : 1})
			)
	return atomDatas

def getChemicalDatas() -> list:
	ChemicalDatas=[]
	with open('화학식.txt',encoding='utf8') as f:
		for line in f.readlines():
			if line[0] == '-':
				formulaBeautiful, formula, name = line.replace('-','').rstrip().split(':')
			else:
				formula, name = line.rstrip().split(':')
				formulaBeautiful = formula.replace('/','')

			outputDict = {}

			code = "?"
			for atom in formula.split('/'):
				count = 1
				code = atom
				if isNum(atom[-1]):
					if isNum(atom[-2]):
						# 2자리수
						count = int(f"{atom[-2]}{atom[-1]}")
						code = atom[:-2]
					else:
						# 1자리수
						count = int(atom[-1])
						code = atom[:-1]

				
				outputDict[code] = count
			ChemicalDatas.append(
				(
					formulaBeautiful,
					name,
					outputDict
				)
			)
	return ChemicalDatas