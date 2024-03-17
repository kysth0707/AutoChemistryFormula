"""
1. 숫자 뒤에 바   KACe1/2/3/Fa
2. 소문자 뒤에 바  KACe/1/2/3/Fa/
3. 바 숫자 삭제 KACe123/Fa/
4. 대 바 대 K/A/Ce123/Fa/

"""

def isUpper(txt : str) -> bool:
	return txt in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def isLower(txt : str) -> bool:
	return txt in list("abcdefghijklmnopqrstuvwxyz")

def isNum(txt : str) -> bool:
	return txt in list('0123456789')

def getChemicalDatas() -> list:
	ChemicalDatas=[]
	with open('화학식.txt',encoding='utf8') as f:
		for line in f.readlines():
			if line[0] == '-':
				formulaBeautiful, formula, name = line.replace('-','').rstrip().split(':')
			else:
				formula, name = line.rstrip().split(':')
				formulaBeautiful = formula.replace('/','')
			
			data = list(formula)


			# 숫자 뒤에 바 && 소문자 뒤에 바
			i = 0
			while True:
				if isNum(data[i]) or isLower(data[i]):
					data.insert(i+1, '/')
					i += 1

				i += 1
				if i >= len(data):
					break
			
			# 바 숫자 삭제
			i = 0
			while True:
				if data[i] == "/" and isNum(data[i + 1]):
					del data[i]

				i += 1
				if i >= len(data) - 1:
					break

			# 대 바 대
			i = 0
			while True:
				if isUpper(data[i]) and isUpper(data[i + 1]):
					data.insert(i+1, '/')
					i += 1

				i += 1
				if i >= len(data) - 1:
					break

			# 맨 뒤 바 삭제
			if data[-1] == "/":
				data = data[:-1]

			# 바로 쪼개기
			temp = "".join(data).split('/')

			# ㄷㄱㅈ
			outputDict = {}

			code = "?"
			for atom in temp:
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