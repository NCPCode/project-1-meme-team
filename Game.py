import pygame

window = pygame.display.set_mode((800,500))
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	window.fill(pygame.Color("deepskyblue"))