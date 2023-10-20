import pygame
from random import choice
pygame.init()
pygame.mixer.init()

WIDTH = HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors!")

pygame.mixer.music.load("spritesAndBGM/opal.mp3")
pygame.mixer.music.play(-1)

CHOICE_SIZE = 60

CPU_CHOICES = ["rock", "paper", "scissors"]
CPU_CHOICE = choice(CPU_CHOICES)

ROCK_IMG = pygame.transform.scale(pygame.image.load("spritesAndBGM/rock.png"), (60, 60))
PAPER_IMG = pygame.transform.scale(pygame.image.load("spritesAndBGM/paper.png"), (60, 60))
SCISSORS_IMG = pygame.transform.scale(pygame.image.load("spritesAndBGM/scissors.png"), (60, 60))
PLAYER_IMG = pygame.transform.scale(pygame.image.load("spritesAndBGM/arrow.png"), (60, 60))

FONT = pygame.font.SysFont("ariel", 40)
TITLE = FONT.render("Rock, Paper, Scissors!", 1, "black")
TIE_TEXT = FONT.render("It's a tie!", 1, "black")
LOST_TEXT = FONT.render("You lost!", 1, "black")
WIN_TEXT = FONT.render("You won!", 1, "black")

PLAYER_SPEED = 4

RES_POS = (WIDTH/3 - CHOICE_SIZE/3, HEIGHT/2 - CHOICE_SIZE/2)
RES_CPU_POS = ((WIDTH/3 - CHOICE_SIZE/3)*2, HEIGHT/2 - CHOICE_SIZE/2)

wins, losses, ties = 0, 0, 0

clock = pygame.time.Clock()


def stats():
	W_L_COUNT = FONT.render(f"W:L:T = {wins}:{losses}:{ties}", 1, "black")
	WIN.blit(W_L_COUNT, (WIDTH/6 - W_L_COUNT.get_width()/6, HEIGHT/10 - W_L_COUNT.get_height()/10))


def draw(rock, paper, scissors, player):
	WIN.fill("teal")

	rock.x = paper.x = scissors.x = WIDTH/4 - CHOICE_SIZE/4
	rock.y, paper.y, scissors.y = 200, 400, 600

	WIN.blit(TITLE, (WIDTH/2 - TITLE.get_width()/2, HEIGHT/6 - TITLE.get_height()/6))

	stats()

	pygame.draw.rect(WIN, "teal", rock)
	WIN.blit(ROCK_IMG, rock)
	pygame.draw.rect(WIN, "teal", paper)
	WIN.blit(PAPER_IMG, paper)
	pygame.draw.rect(WIN, "teal", scissors)
	WIN.blit(SCISSORS_IMG, scissors)
	pygame.draw.rect(WIN, "teal", player)
	WIN.blit(PLAYER_IMG, player)
	pygame.display.flip()


def calc_results(rock, paper, scissors):

	global wins
	global losses
	global ties
	global W_L_COUNT

	WIN.fill("teal")

	# <-- Player Choice Rock Situations -->
	if player.y == 220:
		rock.x, rock.y = RES_POS
		pygame.draw.rect(WIN, "teal", rock)
		WIN.blit(ROCK_IMG, rock)

		if CPU_CHOICE == "rock":
			ties += 1
			cpu_rock.x, cpu_rock.y = RES_CPU_POS
			pygame.draw.rect(WIN, "teal", cpu_rock)
			WIN.blit(ROCK_IMG, cpu_rock)
			WIN.blit(TIE_TEXT, (WIDTH/2 - TIE_TEXT.get_width()/2, HEIGHT/3 - TIE_TEXT.get_height()/3))

		elif CPU_CHOICE == "paper":
			losses += 1
			cpu_paper.x, cpu_paper.y = RES_CPU_POS
			pygame.draw.rect(WIN, "teal", cpu_paper)
			WIN.blit(PAPER_IMG, cpu_paper)
			WIN.blit(LOST_TEXT, (WIDTH/2 - LOST_TEXT.get_width()/2, HEIGHT/3 - LOST_TEXT.get_height()/3))

		else:
			wins += 1
			cpu_scissors.x, cpu_scissors.y = RES_CPU_POS
			pygame.draw.rect(WIN, "teal", cpu_scissors)
			WIN.blit(SCISSORS_IMG, cpu_scissors)
			WIN.blit(WIN_TEXT, (WIDTH/2 - WIN_TEXT.get_width()/2, HEIGHT/3 - WIN_TEXT.get_height()/3))
	# <-- End of Player Choice Rock Situations -->

	# <-- Player Choice Paper Situations -->
	elif player.y == 420:
		paper.x, paper.y = RES_POS
		pygame.draw.rect(WIN, "teal", paper)
		WIN.blit(PAPER_IMG, paper)

		if CPU_CHOICE == "rock":
			wins += 1
			cpu_rock.x, cpu_rock.y = RES_CPU_POS
			pygame.draw.rect(WIN, "teal", cpu_rock)
			WIN.blit(ROCK_IMG, cpu_rock)
			WIN.blit(WIN_TEXT, (WIDTH/2 - WIN_TEXT.get_width()/2, HEIGHT/3 - WIN_TEXT.get_height()/3))

		elif CPU_CHOICE == "paper":
			ties += 1
			cpu_paper.x, cpu_paper.y = RES_CPU_POS
			pygame.draw.rect(WIN, "teal", cpu_paper)
			WIN.blit(PAPER_IMG, cpu_paper)
			WIN.blit(TIE_TEXT, (WIDTH/2 - TIE_TEXT.get_width()/2, HEIGHT/3 - TIE_TEXT.get_height()/3))

		else:
			losses += 1
			cpu_scissors.x, cpu_scissors.y = RES_CPU_POS
			pygame.draw.rect(WIN, "teal", cpu_scissors)
			WIN.blit(SCISSORS_IMG, cpu_scissors)
			WIN.blit(LOST_TEXT, (WIDTH/2 - LOST_TEXT.get_width()/2, HEIGHT/3 - LOST_TEXT.get_height()/3))
	# <-- End of Player Choice Paper Situations -->

	# <-- Player Choice Scissors Situations -->
	elif player.y == 620:
		scissors.x, scissors.y = RES_POS
		pygame.draw.rect(WIN, "teal", scissors)
		WIN.blit(SCISSORS_IMG, scissors)

		if CPU_CHOICE == "rock":
			losses += 1
			cpu_rock.x, cpu_rock.y = RES_CPU_POS
			pygame.draw.rect(WIN, "teal", cpu_rock)
			WIN.blit(ROCK_IMG, cpu_rock)
			WIN.blit(LOST_TEXT, (WIDTH/2 - LOST_TEXT.get_width()/2, HEIGHT/3 - LOST_TEXT.get_height()/3))
			
		elif CPU_CHOICE == "paper":
			wins += 1
			cpu_paper.x, cpu_paper.y = RES_CPU_POS
			pygame.draw.rect(WIN, "teal", cpu_paper)
			WIN.blit(PAPER_IMG, cpu_paper)
			WIN.blit(WIN_TEXT, (WIDTH/2 - WIN_TEXT.get_width()/2, HEIGHT/3 - WIN_TEXT.get_height()/3))

		else:
			ties += 1
			cpu_scissors.x, cpu_scissors.y = RES_CPU_POS
			pygame.draw.rect(WIN, "teal", cpu_scissors)
			WIN.blit(SCISSORS_IMG, cpu_scissors)
			WIN.blit(TIE_TEXT, (WIDTH/2 - TIE_TEXT.get_width()/2, HEIGHT/3 - TIE_TEXT.get_height()/3))
	
	stats()
	pygame.display.flip()
	# <-- End of Player Choice Scissors Situations -->


run = True
can_move = True
can_click = True

rock = pygame.Rect(WIDTH/4 - CHOICE_SIZE/4, 200,
				CHOICE_SIZE, CHOICE_SIZE)
paper = pygame.Rect(WIDTH/4 - CHOICE_SIZE/4, 400,
				CHOICE_SIZE, CHOICE_SIZE)
scissors = pygame.Rect(WIDTH/4 - CHOICE_SIZE/4, 600,
				CHOICE_SIZE, CHOICE_SIZE)


cpu_rock = rock.copy()
cpu_paper = paper.copy()
cpu_scissors = scissors.copy()

player = pygame.Rect(rock.x - 75, rock.y + 20, 45, 20)


draw(rock, paper, scissors, player)
while run:

	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			break

		# <-- Controls -->
		if event.type == pygame.KEYDOWN:
			keys = pygame.key.get_pressed()
			if keys[pygame.K_RETURN] and can_click == True:
				can_click = False
				can_move = False
				calc_results(rock, paper, scissors)
			elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (can_move == True):
				if player.y != 620:
					x = player.y
					while player.y != x + 200:
						player.y += PLAYER_SPEED
						draw(rock, paper, scissors, player)
				else:
					x = player.y
					while player.y != x - 400:
						player.y -= PLAYER_SPEED * 2
						draw(rock, paper, scissors, player)
			elif (keys[pygame.K_UP] or keys[pygame.K_w]) and (can_move == True):
				if player.y != 220:
					x = player.y
					while player.y != x - 200:
						player.y -= PLAYER_SPEED
						draw(rock, paper, scissors, player)
				else:
					x = player.y
					while player.y != x + 400:
						player.y += PLAYER_SPEED * 2
						draw(rock, paper, scissors, player)
			if keys[pygame.K_r] and can_move == False:
				can_move = True
				can_click = True
				draw(rock, paper, scissors, player)
				CPU_CHOICE = choice(CPU_CHOICES)

pygame.quit()
