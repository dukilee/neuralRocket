import pygame

display = pygame.display.set_mode((800, 600));
pygame.display.set_caption('Anaconda');

clock = pygame.time.Clock();
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit();

		pygame.display.update();
		clock.tick(30);
