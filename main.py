import pygame
import config
from field import Field
from rocket import Rocket
from userController import UserController
from kPController import KPController
from engine import Engine


pygame.init()
display = pygame.display.set_mode((config.game['width'], config.game['height']))
pygame.display.set_caption(config.game['caption'])
clock = pygame.time.Clock()


rocket = Rocket()
field = Field()
engine = Engine()


user = False

if user:
	userController = UserController();
	while True:
		display.fill(config.colors['black']);
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit();
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit();
			userController.updateEvent(event)

		engine.update(
			userController.getLeftPower(),
			userController.getRightPower())

		rocket.update(engine.rocket.x, engine.rocket.y, engine.rocket.angle, engine.rocket.leftMotor.power, engine.rocket.rightMotor.power)

		field.draw(display)
		rocket.draw(display);

		# pygame.display.update();
		pygame.display.flip();
		clock.tick(config.game['fps']);
else:
	controller = KPController();
	while True:
		display.fill(config.colors['black']);
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit();
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit();

		#The computer computes the best action
		action = controller.nextAction(engine.rocket.x, engine.rocket.y, engine.rocket.angle, engine.rocket.linSpd, engine.rocket.angSpd);
		engine.update(action[0], action[1])


		rocket.update(engine.rocket.x, engine.rocket.y, engine.rocket.angle, engine.rocket.leftMotor.power, engine.rocket.rightMotor.power)

		field.draw(display)
		rocket.draw(display);

		# pygame.display.update();
		pygame.display.flip();
		clock.tick(config.game['fps']);
	
