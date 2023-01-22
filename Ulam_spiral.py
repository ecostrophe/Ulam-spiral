import pygame

pygame.init()
window = pygame.display.set_mode((1000, 1000),pygame.RESIZABLE)

#Varibles
num = 1
step = 650
numprime = 1
sense = 0
run = True
clock=pygame.time.Clock()
red =(255,0,0)
green =(0,255,0)
star_position = [550,900]
weight = 1080
height = 2110

#Functions
def draw_dot(screen, color, x_pos, y_pos, dim):
	""" function to draw dots
	"""
	global numprime
	if isprime(numprime):
		pygame.draw.circle(screen, color, [x_pos,y_pos],dim, 0)
	pygame.display.update()
	numprime += 1


def direction(x):
	global sense
	if sense > 3:
		sense = 0
	if sense == 0:
		#=> make the spiral rotation to the Right"
		for t in range(x):
			star_position[0] += 5
			draw_dot(window, green, star_position[0], star_position[1], 2)
		sense += 1
	elif sense == 1:
		#=> make the spiral rotation to the Up
		for t in range(x):
			star_position[1] -= 5
			draw_dot(window, red, star_position[0], star_position[1], 2)
		sense += 1
	elif sense == 2:
		#=> make the spiral rotation to the Left
		for t in range(x):
			star_position[0] -= 5
			draw_dot(window, green, star_position[0], star_position[1], 2)
		sense += 1
	elif sense == 3:
		#=> make the spiral rotation to the Down
		for t in range(x):
			star_position[1] += 5
			draw_dot(window, red, star_position[0], star_position[1], 2)
		sense += 1


def move(step,num):
	""" Function to move step by step in spiral rotation
	"""
	while step > 0:
		for x in range(2):
			direction(num)
		num +=1
		step -=1


def isprime(number):
	"""function to find the prime number
	"""
	prime = 0
	if number > 1:
		for i in range(1,number+1):
			if number % i == 0:
				if i == 1:
					prime += 1
				elif i == number:
					prime += 1
				else:
					prime += 1
	else:
		return False

	if prime == 2:
		return True
	else:
		return False


#Start tests
while run:
	# Fill the screen with a black color
	window.fill((0,0, 0))
	#draw  on the screen with green color the prime numbers only
	win = pygame.draw.rect(window, (255,0,0), [0,0,weight,height], 2)
	move(step,num)
	clock.tick(50)
	#The differents events of pygame
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()


