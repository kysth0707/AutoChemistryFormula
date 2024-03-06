
import chemicalHelper
import pygame

# ================ 화학식 불러오기
atomDatas = chemicalHelper.getAtomDatas()
chemicalDatas = chemicalHelper.getChemicalDatas()

# ================ 화면 리셋
pygame.init()

ScreenWidth = 900
ScreenHeight = 600
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('자동 화학 계수 - kysth0707 김태형')


# ================ 변수 설정
formulaTextFont = pygame.font.SysFont("malgungothic", 50, True)
formulaNumFont = pygame.font.SysFont("malgungothic", 35, True)


# ================ 그리기 함수

def drawText(pos : tuple, text : str):
	x, y = pos
	for txt in text:
		if txt in list('0123456789'): # 숫자라면
			screen.blit(formulaNumFont.render(txt, True, (0, 0, 0)), (x, y + 20))
			x += 25
		else: # 문자라면
			screen.blit(formulaTextFont.render(txt, True, (0, 0, 0)), (x, y))
			x += 45


# ================ 반복문
clock = pygame.time.Clock()
run = True
while run:
	clock.tick(60)

	# ================ 화면 그리기
	screen.fill((230, 230, 230))

	drawText((0, 0), "H2 + O2 -> H2O")

	pygame.display.update()

	# ================ 이벤트 처리
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()