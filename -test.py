beforeComponents = [{"H":2},{"O":2}]
afterComponents = [{"H":2, "O":1}]

varDatas = [1 for _ in range(len(beforeComponents) + len(afterComponents))]

loopLimit = 6

for _ in range(loopLimit ** (len(beforeComponents) + len(afterComponents))):
	testBefore = {}
	testAfter = {}
	for i, components in enumerate(beforeComponents):
		for key, value in components.items():
			if testBefore.get(key) == None:
				testBefore[key] = value * varDatas[i]
			else:
				testBefore[key] += value * varDatas[i]
	
	for i, components in enumerate(afterComponents):
		for key, value in components.items():
			if testAfter.get(key) == None:
				testAfter[key] = value * varDatas[len(beforeComponents)+i]
			else:
				testAfter[key] += value * varDatas[len(beforeComponents)+i]
				

	isSame = True
	if sorted(testBefore.keys()) == sorted(testAfter.keys()):
		for key in testBefore.keys():
			if testBefore[key] != testAfter[key]:
				isSame = False
				break
	
	if isSame:
		print(testBefore, testAfter, varDatas)
		break

	varDatas[-1] += 1
	for i, x in enumerate(varDatas):
		if x > loopLimit:
			varDatas[i] = 1
			varDatas[i-1] += 1