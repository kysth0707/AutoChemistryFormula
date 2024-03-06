from AChemicalData import ChemicalData


# ================ 필수 함수
def isUpper(txt : str) -> bool:
	return txt in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def isLower(txt : str) -> bool:
	return txt in list("abcdefghijklmnopqrstuvwxyz")

def isNum(txt : str) -> bool:
	return txt in list('0123456789')


# ================ 화학식 불러오기
atomDatas = []
with open('원자들.txt',encoding='utf8') as f:
	for line in f.readlines():
		code, name = line.rstrip().split()
		atomDatas.append((code, name))
# 원자 불러오기 완료

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
		count = 1
		for atom in formula.split('/'):
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
			ChemicalData(
				formulaBeautiful,
				name,
				outputDict
			)
		)
# print(ChemicalDatas[0].formula, ChemicalDatas[0].name, ChemicalDatas[0].components)
# 화학식 로드 완료
