asdf=open('원자들.txt',encoding='utf8',mode='w')

with open('원자.txt',encoding='utf8') as f:
	d = f.readlines()
	for i, line in enumerate(d):
		if i % 6 == 1:
			name = d[i+1].rstrip()
			if '(' in name:
				name = name[:name.find('(')]
			print(d[i].rstrip(), name, file=asdf)

asdf.close()

"""
i = 0
		outputDict = {}
		while True:
			code, count = '?', 0
			if isUpper(formula[i]): #대
				if i + 1 == len(formula):
					code = formula[i]
					count = 1
					i=999
					# 끝
				else:
					if isUpper(formula[i+1]): #대대
						code = formula[i]
						count = 1
						i+=1
						# 다음
					elif isNum(formula[i+1]): #대수
						code = formula[i]
						if i + 2 == len(formula):
							count = int(formula[i+1])
							i=999
							# 끝
						else:
							if isNum(formula[i+2]): #대수수
								count = int(f"{formula[i+1]}{formula[i+2]}")
								i+=3
							else: #대수
								count = int(formula[i+1])
								i+=2

					elif isLower(formula[i+1]): #대소
						code = formula[i]
						if i + 2 == len(formula):
							count = 1
							i=999
							# 끝
						else:
							if isUpper(formula[i+2]): #대소
								count = 1
								i+=2
							else:
								if i + 3 == len(formula): #대소[]
									count = 1
									i=999
									# 끝
								else:
									if isNum(formula[i+3]):

			outputDict[code] = count

			if i >= len(formula):
				break
"""