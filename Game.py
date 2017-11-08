import pygame

window = pygame.display.set_mode((800,500))
clock = pygame.time.Clock()
grass = pygame.Rect(0,400,800,100)

while True:
	#collectr events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	# processing 

	#display 
	window.fill(pygame.Color("deepskyblue"))
	grass.fill(pygame.Color("seagreen"))
	pygame.display.update()
	clock.tick(60)


