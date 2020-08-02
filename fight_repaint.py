import pygame
from fight import *

pygame.init()
win = pygame.display.set_mode((1000, 600))
win.fill((255, 255, 255))

fon = pygame.font.Font(None, 40)
text_win = fon.render('team1 WIN', 0, (255, 0, 0))
text_win1 = fon.render('team2 WIN', 0, (0, 255, 0))

run = 1


def repaint(hp, hp1):
	global run

	win.fill((10, 10, 10))
	for s in soldiers:
		if s.die(soldiers):
			pygame.draw.rect(win, s.color, (s.x, s.y, 5, 5))

	if hps <= 0:
		win.blit(text_win, (500, 300))
		run = 0
	elif hps1 <= 0:
		win.blit(text_win1, (500, 300))
		run = 0

	pygame.display.update()


clock = pygame.time.Clock()
hps = 10
hps1 = 10

while run:
	clock.tick(60)
	repaint(hps, hps1)
	hps = 0
	hps1 = 0
	our_color = (0, 255, 0)
	for s in soldiers:
		
		if s.color == our_color:
			hps += 1
		else:
			hps1 += 1

		try:
			tx = s.the_enemy(soldiers)[0]
			ty = s.the_enemy(soldiers)[1]
			s.go_to_this(tx, ty)
		except TypeError:
			pass

i = 10
while i > 0:
	clock.tick(5)
	i -= 1
