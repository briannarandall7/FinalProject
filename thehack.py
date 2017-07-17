import pygame
import random
import time

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
player_width =148


class Map(pygame.sprite.Sprite):
#all__sprites__list =[map]

   def __init__(self, color, width, height):

       pygame.sprite.Sprite.__init__(self)

       self.rect = self.image.get_rect()



# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#SCREEN = pygame.display.set_mode([screen_width,screen_height]

#map_list = pygame.sprite.Group()
#all_sprites_list = pygame.sprite.Group()

#def   score(score):
'''def button (msg,x,y,w,h,ic,ac,action =None) :
   mouse = pygame.key.get_pos()
   mouse = pygame.key.get_pressed()
   If 250 > mouse [0] > 150 and 500 > mouse [1] > 40:
   If click[0] == 1 and action != None:
   If action == “play”:

   pygame.draw.rect(gameDisplay,bright_green, (150,450,100,50))
else:
    pygame.draw.rect(gameDisplay, green,(150,450,100,50))
    smallText = pygame.font.Font(“freesansbold.ttf”.20)
    textSurf, textRect = text_objects (“Play”,smallText)
    textRect.center = ((150+(100/2)), (450 + (50/2)) )
    gameDisplay.blit(textSurf, textRect)


def game_intro():
      Intro =True
      while intro:
             for event in pygame.event.
                  If event.type == pygame.QUIT
                     pygame.quit ()
                     quit ()
  gameDisplay.fill(BLUE)
def text_objects (text, font):
      textSurface = font.render (text, True, black)
      return textSurface, textSurface.get_rect()
def message_display(text):
      largeText = pygame.font.Font(‘freesansbold.ttf’, 25 )
      TextSurf, TextRect = text_objects(“  TheHack
Hello my name is Z and I’m a programer at the Pentagon. I’ve made a chat box for  morse code(a secret military language used to tell the government where they need their supplies dropped off ) But the chat box has been wiped out by a evil villain named man x!!!! .Who hid it in a secret location on a flash drive and to hide evidence  ripped up the map pieces all over the city .Use arrows to avoid green viruses and collect map pieces to find the location and get back your flash drive.
				   		You Go Girl !!!

”, largeText)
   TextRect.center = ((display_width/2), (dispaly_height/2))
   gameDisplay.blit(TextSurf, TextRect)
 K_LEFT = pygame.key.get_pressed()

If 150+100 > K_LEFT [0] > 150 and 450+50 > K_LEFT [1] > 450:
   pygame.draw.rect(gameDisplay,bright_green, (150,450,100,50, “play”))
else:
pygame.draw.rect(gameDisplay, green,(150,450,100,50))
smallText = pygame.font.Font(“freesansbold.ttf”.20)
textSurf, textRect = text_objects (“Play”,smallText)
textRect.center = ((150+(100/2)), (450 + (50/2)) )
gameDisplay.blit(textSurf, textRect)


pygame.draw.rect (gameDisplay, green, (150, 450, 100,  50))
for block in Map_hit_list:
score += 1
print( score )
If len (block_list) == 0
   Level += 1

pygame.display.update()
clock.tick(45)


def   score(count):
 font = pygame.font.SysFont(None, 15)
 Text = font.render(“score  “+str(count)True, black)
gameDisplay.blit(text,(0,0))


font = pygame.font.SyaFont(None, 15)
Text = font.render(“score  “+str(count)True, black)
gameDisplay.blit(text,(0,0))'''
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

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        map_hit_list = pygame.sprite.spritecollide(self, self.level.Map_list, True)
        drive_hit_list = pygame.sprite.spritecollide(self, self.level.drive_list, True)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        map_hit_list = pygame.sprite.spritecollide(self, self.level.Map_list, True)
        drive_hit_list = pygame.sprite.spritecollide(self, self.level.drive_list, True)
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
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        Map_hit_list = pygame.sprite.spritecollide(self, self.level.Map_list, True)
        drive_hit_list = pygame.sprite.spritecollide(self, self.level.drive_list, True)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
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

    def __init__(self, width, height, color):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        #Level.__init__(self.player)
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.Map_list = pygame.sprite.Group()
        self.drive_list = pygame.sprite.Group()
        self.player = player

        # How far this world has been scrolled left/right
        self.world_shift = 0

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.Map_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(BLUE)
        background=pygame.image.load("cartoon image of city.jpg")
        screen.blit(background,background.get_rect())


        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.Map_list.draw(screen)

        '''if score == 15:
            horrificImage=pygame.image.load("cartoon of office.jpg").convert()
            clock.tick(0)
            pygame.time.delay(30000)
            thescreen.bilt(horrificImage,(0,0))'''

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for Map in self.Map_list:
            Map.rect.x += shift_x

        #for drive  in self.drive_list
              #drive.rect.x +=shift_x



# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

                # Array with width, height, x, and y of platform
        levels = [[210, 70, 650, 500],
                [210, 70, 800, 400],
                [210, 70, 1000, 500],
                [210, 70, 1120, 280],
                [210, 70, 1100, 200],
                [210, 70, 1111, 630],
                [210, 70, 980, 390],
                ]

        coins_list = [[100, 50, 500, 100],
                [100, 50, 800, 200],
                [100, 50, 1000, 900],
                [100, 50, 1120, 480],
                [100, 50, 1100, 300],
                [100, 50, 900, 500],
                [100, 50, 300, 100],
                [100, 50, 800, 700],
                [100, 50, 1160, 500],
                [100, 50, 500, 300],
                ]

        for Map in coins_list:
            block = Platform(Map[0], Map[1], RED)
            block.rect.x = Map[2]
            block.rect.y = Map[3]
            block.player = self.player
            self.Map_list.add(block)


        for platform in levels:
            block = Platform(platform[0], platform[1], BLACK)
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)


        # Create platforms for the level
class Level_02(Level):
    #Definition for level 2.
    def __init__(self, player):
        """ Create level 1. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

                # Array with type of platform, and x, y location of the platform.
        levels = [[210, 30, 450, 570],
                [210, 30, 850, 420],
                [210, 30, 1000, 520],
                [210, 30, 1120, 280],
                [210, 30, 500, 300],
                [210, 30, 1000, 290],
                [210, 30, 600, 320],
                [210, 30, 460, 310],
                [210, 30, 589, 390],
                [210, 30, 1111, 546],
                ]

        flashdrive_list = [[ 100, 50, 1135, 559],
        	               ]
                # Go through the array above and add platforms
        for platform in levels:
            block = Platform(platform[0], platform[1], GREEN)
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for key in flashdrive_list:
            block = Platform(key[0], key[1], GREEN)
            block.rect.x = key[2]
            block.rect.y = key[3]
            block.player = self.player
            block.image= pygame.image.load("flashdrive.png")
            block.player = self.player
            self.platform_list.add(block)


def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    #score(score)
    pygame.display.set_caption("Side-scrolling Platformer")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    '''def game loop():
    def player (x,y)
         gameDisplay.blit(playerImg,(x,y))
    def text_object (text, font, color):
        text.Surface = font.render (text, True, black)
        return  textSurface, textSurface.get_rect ()
def obstacles ( obstaclesx,  obstaclesy,  obstaclesw,  obstaclesh,)
      Pygame.draw.rect (gameDisplay, [ obstaclesx,  obstaclesy,  obstaclesw,  obstaclesh])

def message_display (text) :
          largeText = pygame.font.Font (“freesansbold.tff”,115)
          TextSurf, TextRect = text_objects (text, largeText)
         TextRect.center = ((display_width/2), (display_height/2))
         gameDisplay.blit(TextSurf, TextRect)
         pygame.display.update'''


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
#     '''      obstacles( obstacles_listx,  obstacles_listy,  obstacles_width,  obstacles_hight)
#    obstacles_listy +=  obstacles_speed
# If x > display_width - car_width or x < 0:
#  crash ()
#  If  obstacles_listy > display_height:
#        obstacles_listy = 0 -  obstacles_height
#        obstacles_listx = random.randrange(0,display_width)
#   If y <  obstacles_listy +  obstacles_height
#       print (“y crossover”)
# If x >  obstacles_listx and x <  obstacles_listx +  obstacles_width or x+player width>  obstacles_listx and x + car_width <  obstacles_listx+ obstacles_width
#          print(“x crossover”)
#          crash()
#      Pygame.display.update ()
#      clock.tick(60)
#        def game_loop()'''


        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    #game_intro()
    pygame.quit()

if __name__ == "__main__":
    main()
