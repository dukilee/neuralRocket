import pygame
import config
import rocket

print(config.game);

display = pygame.display.set_mode((config.game['width'], config.game['height']));
pygame.display.set_caption(config.game['caption']);
clock = pygame.time.Clock();


rocket = rocket.Rocket();

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit();
	rocket.draw(display);

	pygame.display.update();
	clock.tick(config.game['fps']);
