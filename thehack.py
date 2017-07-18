import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

block_color = (53,115,255)
player_width = 148

class Map(pygame.sprite.Sprite):
#all__sprites__list =[map]

   def __init__(self, color, width, height):

       pygame.sprite.Sprite.__init__(self)

       self.rect = self.image.get_rect()
	
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('TheHack')
clock = pygame.time.Clock()

crashed = False
playeImg = pygame.image.load('hannah-a.png')

class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """
    # -- Methods

    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load('hannah-a.png')
        #self.image.fill(RED)

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        #score = 0
        # List of sprites we can bump against
        self.level = None

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
class Level ():
	def __init__(self, player):
		""" Constructor. Pass in a handle to player. Needed for when moving
		    platforms collide with the player. """
		self.platform_list = pygame.sprite.Group()  
	def draw(self, display):
		""" Draw everything on this level. """

		# Draw the background
		display.fill(BLUE)

		# Draw all the sprite lists that we have
		self.platform_list.draw(display)	
	def draw(self, display):
	def update(self):
        """ Update everything in this level."""
        self.platform_list.update()	
		""" Draw everything on this level. """

	 def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        screen.fill(BLUE)
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)	# Draw the background
		screen.fill(BLUE)

		# Draw all the sprite lists that we have
		self.platform_list.draw(display)
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.level_limit = -1000
 
        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False
        for block in block_hit_list:
	 if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= display_height - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = display_height - self.rect.height
 
    def jump(self):	
	self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
	if len(platform_hit_list) > 0 or self.rect.bottom >= display_height :
            self.change_y = -10	
def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
 class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
 
def things_dodged(count):
						     
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def player(x,y):
    gameDisplay.blit(playerImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def crash():
    message_display('You Crashed')
    
def game_loop():
	x =  (display_width * 0.45)
	y = (display_height * 0.8)
	
	x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    
    thingCount = 1
    dodged = 0
	player_speed = 0
	gameExit = False 
	
	while not gameExit:

	    for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    pygame.quit()
		    quit()
		   
		if event.type == pygame.KEYDOWN:
		    if event.key == pygame.K_LEFT:
			player.go_left()
		    elif event.key == pygame.K_RIGHT:
			player.go_right
		if event.type == pygame.K_UP:
	           player.jump()
		if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()    
		    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
		        player.stop()
                    if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
		
	     
	    x += x_change
	             
	    gameDisplay.fill(white)
	  
            things(thingx, thingy, thingw, thingh, color)
           things(thing_startx, thing_starty, thing_width, thing_height, black)
               
	   thing_starty += thing_speed
	   player(x,y)
	   things_dodged(dodged)
            
	    if x > display_width - player_width or x < 0:
            	crash()
            
	    if thing_starty > display_height:
	        thing_starty = 0 - thing_height
		thing_startx = random.randrange(0,display_width)
		dodged += 1
                thing_speed += 1
                thing_width += (dodged * 1.2)
        ###  
        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+player_width > thing_startx and x + player_width < thing_startx+thing_width:
                print('x crossover')
                crash()
       ###
	    pygame.display.update()
	    clock.tick(60)
pygame.quit()
quit()
