
import chemicalHelper
import pygame

# ================ 화학식 불러오기
atomDatas = chemicalHelper.getAtomDatas()
chemicalDatas = chemicalHelper.getChemicalDatas()

# ================ 화면 리셋
pygame.init()

ScreenWidth = 1600
ScreenHeight = 900
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('자동 화학 계수 - kysth0707 김태형')


# ================ 변수 설정
formulaTextFont = pygame.font.SysFont("malgungothic", 50, True)
formulaNumFont = pygame.font.SysFont("malgungothic", 35, True)

PLUS = 0
EQUAL = 1
CURSOR = 2

cursorPos = 0

# ================ 그리기 함수

def drawText(pos : tuple, data : list):
	x, y = pos
	for txt in data:
		if type(txt) == tuple:
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


# ================ 반복문
formulaData = [("H2",2),PLUS,("O2",1),EQUAL,('H2O',2)]


clock = pygame.time.Clock()
run = True
while run:
	clock.tick(60)


	

	# ================ 화면 그리기
	screen.fill((230, 230, 230))

	temp = formulaData.copy()
	temp.insert(cursorPos, CURSOR)
	drawText((100, int(ScreenHeight/2)-50), temp)

	pygame.display.update()

	# ================ 키 처리
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				if cursorPos > 0:
					cursorPos -= 1
			elif event.key == pygame.K_RIGHT:
				if cursorPos < len(formulaData):
					cursorPos += 1
			elif event.key in [pygame.K_EQUALS, pygame.K_KP_PLUS]:
				formulaData.insert(cursorPos, PLUS)
				cursorPos += 1
			elif event.key == pygame.K_SPACE:
				formulaData.insert(cursorPos, EQUAL)
				cursorPos += 1
			elif event.key == pygame.K_BACKSPACE:
				if cursorPos > 0:
					if type(formulaData[cursorPos-1]) == tuple:
						outputTxt, count = formulaData[cursorPos-1]
						if len(outputTxt) > 0:
							formulaData[cursorPos-1] = (outputTxt[:-1], count)
						else:
							del formulaData[cursorPos-1]
							cursorPos -= 1
					else:
						del formulaData[cursorPos-1]
						cursorPos -= 1
			else:
				pressedKey = pygame.key.name(event.key).capitalize()
				if len(pressedKey) == 3 and pressedKey[0] == '[' and pressedKey[2] == ']':
					pressedKey = pressedKey[1]
				elif len(pressedKey) > 1:
					continue
				if cursorPos > 0:
					if type(formulaData[cursorPos-1]) == tuple:
						outputTxt, count = formulaData[cursorPos-1]
						outputTxt += pressedKey
						formulaData[cursorPos-1] = (outputTxt, count)
						continue
				formulaData.insert(cursorPos, (pressedKey, 1))
				cursorPos += 1

