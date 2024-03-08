import time
import chemicalHelper
import pygame

"""
무조건 자동완성!!
"""

# ================ 화학식 불러오기
atomDatas = chemicalHelper.getAtomDatas()
chemicalDatas = chemicalHelper.getChemicalDatas()

# helpDict = {}
# alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for c in alphabets:
# 	helpDict[c] = []
# 	for formula, name, components in chemicalDatas:
# 		if c in "".join(components.keys()):
# 			helpDict[c].append((formula, name, components))

# ================ 화면 리셋
pygame.init()

ScreenWidth = 1600
ScreenHeight = 900
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('자동 화학 계수 - kysth0707 김태형')


# ================ 변수 설정
formulaTextFont = pygame.font.SysFont("malgungothic", 45, True)
formulaNumFont = pygame.font.SysFont("malgungothic", 35, True)

PLUS = 0
EQUAL = 1
CURSOR = 2

DRAW_POS = (100, 100)

helpList = []
helpPos = 0
cursorPos = 0

# ================ 그리기 함수

def drawText(pos : tuple, data : list):
	x, y = pos
	for txt in data:
		if type(txt) == tuple:
			if len(txt) == 3:
				name, _, count = txt
			else:
				name, count = txt
			if int(count) != 1:
				screen.blit(formulaTextFont.render(f"{count}", True, (0, 0, 0)), (x, y))
				x += 30 * len(str(count))
			for t in name:
				if t in list('0123456789'): # 숫자라면
					screen.blit(formulaNumFont.render(t, True, (0, 0, 0)), (x, y + 20))
					x += 20
				else: # 문자라면
					screen.blit(formulaTextFont.render(t, True, (0, 0, 0)), (x, y))
					x += 40
		elif txt == PLUS:
			screen.blit(formulaTextFont.render('+', True, (0, 0, 0)), (x+20, y))
			x += 70
		elif txt == EQUAL:
			screen.blit(formulaTextFont.render('->', True, (0, 0, 0)), (x+20, y))
			x += 90
		elif txt == CURSOR:
			screen.blit(formulaTextFont.render('|', True, (100, 100, 100)), (x+20, y-5))
			x += 45


def getCursorPos(pos : tuple, data : list) -> tuple:
	x, y = pos
	for txt in data:
		if type(txt) == tuple:
			if len(txt) == 3:
				name, _, count = txt
			else:
				name, count = txt
			if int(count) != 1:
				x += 30 * len(str(count))
			for t in name:
				if t in list('0123456789'): # 숫자라면
					x += 20
				else: # 문자라면
					x += 40
		elif txt == PLUS:
			x += 70
		elif txt == EQUAL:
			x += 90
	return (x, y)

# ================ 반복문
formulaData = [("H2",{"H":2},2),PLUS,("O2",{"O":2},1),EQUAL,('H2O',{"H":2,"O":1},2)]

last = time.time()
clock = pygame.time.Clock()
run = True
while run:
	clock.tick(60)

	everyPointFiveSecond = False
	if last + 0.5 < time.time():
		last = time.time()
		everyPointFiveSecond = True

		helpList = []
		if cursorPos > 0:
			if type(formulaData[cursorPos-1]) == tuple: #도움말 불러오기
				nowText = str(formulaData[cursorPos-1][0])
				for n in '0123456789':
					nowText = nowText.replace(n, '')
				nowText = nowText.upper()
				# A
				# AGCL
				
				for formula, name, components in chemicalDatas:
					canAdd = True
					temp = "".join(components.keys()).upper()
					for checkTxt in nowText:
						canPass = False
						for c in temp:
							if checkTxt == c:
								canPass = True
						if not canPass:
							canAdd = False

					if canAdd:
						helpList.append((formula, name, components))
	

	# ================ 화면 그리기
	screen.fill((255, 255, 255))

	temp = formulaData.copy()
	temp.insert(cursorPos, CURSOR)
	drawText(DRAW_POS, temp)

	if cursorPos > 0:
		if type(formulaData[cursorPos-1]) == tuple and len(helpList) > 0: #도움말 그리기
			x, y = getCursorPos(DRAW_POS, formulaData[:cursorPos])
			y += 100
			drawText((x-80, y), [(">>",1)])
			for formula, name, components in helpList[helpPos:]:
				drawText((x, y), [(formula,1), (' '*5,1), (name,1)])
				y += 100

	pygame.display.update()

	# ================ 키 처리
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT: #왼쪽
				if cursorPos > 0:
					cursorPos -= 1
					helpPos = 0
			elif event.key == pygame.K_RIGHT: #오른쪽
				if cursorPos < len(formulaData):
					cursorPos += 1
					helpPos = 0
			elif event.key == pygame.K_UP: #위
				if helpPos > 0:
					helpPos -= 1
			elif event.key == pygame.K_DOWN: #아래
				if helpPos < len(helpList) - 1:
					helpPos += 1
			elif event.key in [pygame.K_EQUALS, pygame.K_KP_PLUS]: #+키
				formulaData.insert(cursorPos, PLUS)
				cursorPos += 1
				helpPos = 0
			elif event.key == pygame.K_SPACE: #-> 키
				formulaData.insert(cursorPos, EQUAL)
				cursorPos += 1
				helpPos = 0
			elif event.key == pygame.K_TAB: #자동완성
				if cursorPos > 0:
					if type(formulaData[cursorPos-1]) == tuple:
						if len(helpList) > 0:
							try:
								formula, name, components = helpList[helpPos]
								formulaData[cursorPos-1] = (formula, components, 1)
							except:
								pass
			elif event.key == pygame.KSCAN_KP_ENTER or event.key == 13:
				beforeComponents = []
				afterComponents = []
				isBefore = True
				# formulaData = [("H2",{"H":2},2),PLUS,("O2",{"O":2},1),EQUAL,('H2O',{"H":2,"O":1},2)]
				for data in formulaData:
					if data == EQUAL:
						isBefore = False
					elif data != PLUS:
						_, c, _ = formulaData
						if isBefore:
							beforeComponents.append(c)
						else:
							afterComponents.append(c)
							# 내일 여기 하기


			elif event.key == pygame.K_BACKSPACE: #지우기
				helpPos = 0
				if cursorPos > 0:
					if type(formulaData[cursorPos-1]) == tuple:
						outputTxt, components, count = formulaData[cursorPos-1]
						if len(outputTxt) > 0:
							formulaData[cursorPos-1] = (outputTxt[:-1], components, count)
						else:
							del formulaData[cursorPos-1]
							cursorPos -= 1
					else:
						del formulaData[cursorPos-1]
						cursorPos -= 1
			else:
				pressedKey = pygame.key.name(event.key).upper()
				if len(pressedKey) == 3 and pressedKey[0] == '[' and pressedKey[2] == ']':
					pressedKey = pressedKey[1]
				elif len(pressedKey) > 1:
					continue
				if cursorPos > 0:
					if type(formulaData[cursorPos-1]) == tuple:
						outputTxt, components, count = formulaData[cursorPos-1]
						outputTxt += pressedKey
						components[pressedKey] = 1
						formulaData[cursorPos-1] = (outputTxt, components, count)
						continue
				formulaData.insert(cursorPos, (pressedKey, {pressedKey:1}, 1))
				cursorPos += 1

