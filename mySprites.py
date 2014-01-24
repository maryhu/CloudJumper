'''
   Author: Mary Hu
   Date: June 5, 2012
   Description: This file contains sprite classes for the Cloud Jumper game 
   with the following classes:
                          - Sky
                          - Cloud
                          - Player
                          - Bullet
                          - Monster
                          - Star
                          - Shield
                          - ScoreKeeper
'''
import pygame, random   

class Sky(pygame.sprite.Sprite):
    '''This class defines the background which is capable of scrolling down.'''
    def __init__(self, screen):
        '''This initializer takes the screen surface as a parameter and 
        initializes the image and rect attributes along with the __scroll 
        value of the background.'''
        # Call the parent __init__() method  
        pygame.sprite.Sprite.__init__(self)   
        
        # Set the image and rect attributes of the sky
        self.image = pygame.image.load("./Images/sky.jpg")
        self.image.convert() 
        
        self.rect = self.image.get_rect()
        self.rect.bottom = screen.get_height()
        self.rect.left = 0
        
        # Initialize __scroll value of the sky
        self.__scroll = 0
        # Instance variable to keep track of the screen surface  
        self.__screen = screen
        
    def set_scroll(self, scroll):
        '''This method takes scroll as a parameter and assigns its value 
        to __scroll.'''
        self.__scroll = scroll
        
    def update(self):
        '''This method will be called automatically to reposition the         
        sky on the screen.''' 
        # Check if the y position is greater than 0
        # and sets it to the screen height if True
        if self.rect.top >= 0:
            self.rect.bottom = self.__screen.get_height()
        # If not, it will add __scroll to the y position of the sky background.
        else:
            self.rect.bottom += self.__scroll
        
class Cloud(pygame.sprite.Sprite):     
    '''This class defines the cloud sprite.'''    
    def __init__(self, screen, variable):   
        '''This initializer takes the screen surface and an integer variable as 
        parameters and initializes the image and rect attributes of the cloud.'''
        # Call the parent __init__() method  
        pygame.sprite.Sprite.__init__(self)           
        
        # Set the image (randomly) for the clouds 
        randnum = random.randrange(1, 6)
        self.image = pygame.image.load("./Images/cloud" + str(randnum) + ".png")
        self.image.convert()
        
        # Set the rect attributes
        self.rect = self.image.get_rect() 
        
        # Use a list to define the y value of clouds based on its variable
        self.yList = [0,40,80,120,160,200,250,310,360,400,450,500,590,530]
        self.rect.top = self.yList[variable]
        
        # Set x values for special clouds
        if variable == 12 or variable == 11:
            self.rect.left = screen.get_width()/2 -45
        elif variable == 13:
            self.rect.left = 260
        elif variable == 7:
            self.rect.left = 40
        # Assign a random x value for normal clouds
        else:
            self.rect.left = random.randrange(0, screen.get_width()-100) 
        
        # Instance variable to keep track of the screen surface  
        self.__screen = screen
        # Assign the cloud's variable to instance variable
        self.__variable = variable
        # Initialize __scroll value of the cloud
        self.__scroll = 0
    
    def set_scroll(self, scroll):
        '''This method takes scroll as a parameter and assigns its value 
        to __scroll.'''
        self.__scroll = scroll
        
    def reset(self):
        '''This method resets the cloud's y value and randomizes it's x value.'''
        self.rect.bottom = 0
        self.rect.left = random.randrange(0,7) * 50
        
    def update(self):
        '''This method will be called automatically to reposition the         
        cloud sprite on the screen.'''  
        # If the cloud goes off-screen, reset its x and y values
        if self.rect.top > self.__screen.get_height():
            self.rect.bottom = 0
            self.rect.left = random.randrange(0, self.__screen.get_width()-100) 
        # Add the __scroll value to cloud's y otherwise
        else:
            self.rect.bottom += self.__scroll
        
class Player(pygame.sprite.Sprite):
    '''This class defines the player sprite.'''    
    def __init__(self, screen, ground, centerx, bottom):
        '''This initializer takes screen, ground, centerx and bottom as 
        parameters. It loads the player's image and positions it at the 
        bottom of the game window.'''
        # Call the parent __init__() method  
        pygame.sprite.Sprite.__init__(self) 
        
        # Load the images of player with shield into a list
        self.__player_list_shield = [pygame.image.load("./Images/DoodleSL1.png")\
                                , pygame.image.load("./Images/DoodleSR1.png")]
        
        # Load the images of normal player into a list
        self.__player_list = [pygame.image.load("./Images/DoodleL1.png"), \
                              pygame.image.load("./Images/DoodleR1.png")]
        
        # Set player's image as one of the normal-list images
        self.image = self.__player_list[0]
        self.image.convert()

        # Set the rect attributes
        self.rect = self.image.get_rect() 

        self.rect.centerx = centerx
        self.rect.bottom = bottom
        
        # Instance variable to keep track of the screen surface  
        self.__screen = screen      
        # Set the initial dx for the player
        self.__dx = 0
        # Set the initial values of instance variables
        # that keep track of player's status
        self.__alive = True
        self.__immune = False
        self.__jump = True
        # Set the initial values of instance variables that control the player's
        # jumping movements
        self.__ground = ground
        self.__gravity = 2
        self.__velocity = -23
        # Initialize __scroll value of the player
        self.__scroll = 8
        # Initialze the player's counter with value 0
        self.__counter = 0
    
    def get_velocity(self):
        '''This method returns the player's __velocity.'''
        return self.__velocity
    
    def get_immunity(self):
        '''This method returns the player's immunity status.'''
        return self.__immune
    
    def get_scroll(self):
        '''This method returns the player's __scroll value. '''
        return self.__scroll
    
    def set_ground(self, new_ground):
        '''This method takes new_ground as a parameter and assigns its 
        value to __ground.'''
        self.__ground = new_ground
        
    def set_velocity(self, new_velocity):
        '''This method takes new_velocity as a parameter and assigns its 
        value to __velocity.'''
        self.__velocity = new_velocity
        
    def set_immunity(self, variable):
        '''This method takes a boolean variable as a parameter and assigns 
        its value to __immune.'''
        self.__immune = variable
        
        # Change player's image when immune to monster
        if self.__immune:
            self.image = self.__player_list_shield[1]
            self.image.convert()
        
    def change_direction(self, x):
        '''This method takes x as a parameter and assigns its value to __dx. 
        If x is positive, it will make the player's image look right.
        If x is negative, it will make the player's image look left.'''
        self.__dx = x
        
        # Use special immune images if player is immune
        if self.__immune:
            if x > 0:
                self.image = self.__player_list_shield[1]
                self.image.convert()
            elif x < 0 :
                self.image = self.__player_list_shield[0]
                self.image.convert()
        # Use normal images otherwise
        else:
            if x > 0:
                self.image = self.__player_list[1]
                self.image.convert()
            elif x < 0 :
                self.image = self.__player_list[0]
                self.image.convert()
    
    def kill(self):
        '''This method makes the boolean variable __alive False.'''
        self.__alive = False
    
    def lose(self):
        '''This method return True if the player is not alive, and 
        False otherwise.'''
        if self.__alive == False:
            return True
        else:
            return False
  
    def update(self):
        '''This method will be called automatically to reposition the         
        player sprite on the screen.''' 
        
        # Make player re-enter at the same x position if the player 
        # goes off-screen horizontally
        if(self.rect.centerx <0):
            self.rect.centerx = self.__screen.get_width()
        if (self.rect.centerx > self.__screen.get_width()):
            self.rect.centerx = 0
            
        # Check if player has fallen "off" the game area
        if self.rect.bottom >= self.__screen.get_height():
            self.__alive = False
        
        # Make the player jump as long as __jump is True
        if self.__jump:
            # Make sure adding the __velocity will still allow the player
            # To be above the __ground
            if (self.rect.bottom+self.__velocity <= self.__ground):
                # Add __velocity to player's y value
                self.rect.bottom = self.rect.bottom + self.__velocity
                # Add __gravity to velocity
                self.__velocity = self.__velocity + self.__gravity
                # Add dx to player's x value to move it left and right
                self.rect.centerx  += self.__dx
            # If the player would be below the __ground when __velocity is added
            # reset __velocity
            elif (self.rect.bottom+self.__velocity >= self.__ground):
                self.__velocity = -23
                
        # Start counter when the player is immune
        if self.__immune:
            self.__counter += 1
            
            # Turn off immunity after 10 seconds
            if self.__counter >= 300:
                self.__counter = 0
                self.__immune = False
                # Change player's image back to normal
                self.image = self.__player_list[1]
                self.image.convert()

class Bullet(pygame.sprite.Sprite):
    '''This class defines the sprite for the bullet.'''    
    def __init__(self, screen, x, y):
        '''This initializer takes a screen surface as well as x and y values
        as parameters.''' 
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image and rect attributes for the Ball         
        self.image = pygame.image.load("./Images/ball.png")
        self.image.convert()
        self.rect = self.image.get_rect() 

        self.rect.centerx = x
        self.rect.bottom = y
        
        # Instance variable to keep track of the screen surface 
        self.__screen = screen    
        # Initialize instance variable __dy
        self.__dy = 30
        
    def update(self):
        '''This method will be called automatically to reposition the         
        bullet sprite on the screen.'''
        # Subtract dy from bullet's y value to make it move up
        self.rect.centery -= self.__dy
        # Kill the bullet when it is off-screen
        if (self.rect.bottom < 0):
            self.kill()
            
class Monster(pygame.sprite.Sprite):
    '''This class defines the sprite for the monster.'''  
    def __init__(self, screen, welcome, x, y):
        '''This initializer takes screen, boolean variable welcome, and x and y
        values as parameters.''' 
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image and rect attributes for the Ball       
        self.__monster_images = []
        for number in range(4):
            self.__monster_images.append(pygame.image.load("./Images/alienR" \
                                                    + str(number) + ".png"))
            
        self.image = self.__monster_images[0]
        self.image.convert()

        self.rect = self.image.get_rect() 
        
        # Assign the x and y parameters if the monster is for the welcome screen
        if welcome:
            self.rect.centerx = x
            self.rect.bottom = y
        # Otherwise, assign it randomly (off screen)
        else:
            self.rect.centerx = random.randrange(0, screen.get_width()-80)
            self.rect.bottom = random.randrange(-1000, -5000, -1)
        
        # Instance variable to keep track of the screen surface 
        self.__screen = screen
        # Initialze the instance variable to keep track of which image to show
        self.__monster_number = 0
        # Initialze the __counter and __scroll values of monster
        self.__counter = 0
        self.__scroll = 0

    def set_scroll(self, scroll):
        '''This method takes scroll as a parameter and assigns its value 
        to __scroll.'''
        self.__scroll = scroll
        
    def reset(self):
        '''This method resets the monster's x and y values randomly.'''
        self.rect.bottom = random.randrange(-2000, -10000, -1)
        self.rect.left = random.randrange(0, self.__screen.get_width()-80)
        
    def update(self):
        '''This method will be called automatically to reposition the         
        monster on the screen.''' 
        # Change the monster's image number every 1/10 of a second
        if self.__counter == 3:
            if self.__monster_number < 3:
                self.__monster_number += 1
            else:
                self.__monster_number = 1
            self.__counter = 0
        
        # Add one to counter every time update is called
        self.__counter += 1
        
        # Change the monster's image according to image number
        self.image = self.__monster_images[self.__monster_number]
        self.image.convert()
        
        # Add 1 to monster's x as long as it is less than screen width
        if self.rect.left < self.__screen.get_width():
            self.rect.left += 1
        # Set monster's right to 0 otherwise
        else: 
            self.rect.right = 0
        
        # Add __scroll to monster's y value
        self.rect.top += self.__scroll
        
        # Reset the monster's x and y values if it goes off-screen
        if self.rect.top > self.__screen.get_height():
            self.rect.bottom = random.randrange(-2000, -10000, -1)
            self.rect.left = random.randrange(0, self.__screen.get_width()-80)
            
class Star(pygame.sprite.Sprite):
    '''This class defines the sprite for the enhancement star.'''  
    def __init__(self, screen, welcome):
        '''This initializer takes screen and boolean variable welcome
        as parameters.''' 
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image and rect attributes for the star   
        self.__star_images = []
        for number in range(12):
            self.__star_images.append(pygame.image.load("./Images/star" + \
                                                        str(number) + ".png"))
            
        self.image = self.__star_images[0]
        self.image.convert()
        
        self.rect = self.image.get_rect() 
        
        # Set the star's rect specifically if welcome is True
        if welcome:
            self.rect.centerx = 310
            self.rect.bottom = 300
        # Assign it randomly otherwise
        else:
            self.rect.centerx = random.randrange(0, screen.get_width()-50)
            self.rect.bottom = random.randrange(-500, -3000, -1)
        
        # Initialze the instance variable to keep track of which image to show
        self.__star_number = 0
        # Instance variable to keep track of the screen surface 
        self.__screen = screen
        # Initialze the __counter and __scroll values of star
        self.__scroll = 0
        self.__counter = 0
        
    def reset(self):
        '''This method resets the star's x and y values randomly.'''
        self.rect.bottom = random.randrange(-500, -3000, -1)
        self.rect.left = random.randrange(0, self.__screen.get_width()-50)
        
    def set_scroll(self, scroll):
        '''This method takes scroll as a parameter and assigns its value 
        to __scroll.'''
        self.__scroll = scroll
        
    def update(self):
        '''This method will be called automatically to reposition the         
        star on the screen.''' 
        # Change the star's image number every 1/10 of a second
        if self.__counter == 3:
            if self.__star_number < 3:
                self.__star_number += 1
            else:
                self.__star_number = 1
            self.__counter = 0
        
        # Add one to counter every time update is called
        self.__counter += 1
        
        # Change star's image according to image number
        self.image = self.__star_images[self.__star_number]
        self.image.convert()
        
        # Add __scroll to star's y value
        self.rect.top += self.__scroll
        
        # Reset the star's x and y values if it goes off-screen
        if self.rect.top > self.__screen.get_height():
            self.rect.bottom = random.randrange(-500, -3000, -1)
            self.rect.left = random.randrange(0, self.__screen.get_width()-50)
            
class Shield(Star):
    '''This class defines the sprite for the enhancement shield.'''  
    def __init__(self, screen):
        '''This initializer takes the screen surface as a parameter.''' 
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image and rect attributes for the shield   
        self.image = pygame.image.load("./Images/shield.png")
            
        self.image.convert()
        
        self.rect = self.image.get_rect() 

        self.rect.centerx = random.randrange(0, screen.get_width()-80)
        self.rect.bottom = random.randrange(-800, -3000, -1)
        
        # Instance variable to keep track of the screen surface 
        self.__screen = screen
        # Initialze  __scroll value of shield
        self.__scroll = 0
        
    def reset(self):
        '''This method resets shield's x and y values randomly.'''
        self.rect.bottom = random.randrange(-1000, -6000, -1)
        self.rect.left = random.randrange(0, self.__screen.get_width()-80)
        
    def set_scroll(self, scroll):
        '''This method takes scroll as a parameter and assigns its value 
        to __scroll.'''
        self.__scroll = scroll
        
    def update(self):
        '''This method will be called automatically to reposition the         
        shield on the screen.''' 
        # Add __scroll to shield's y value
        self.rect.top += self.__scroll
        
        # Reset the shield's x and y values if it goes off-screen
        if self.rect.top > self.__screen.get_height():
            self.rect.bottom = random.randrange(-1000, -6000, -1)
            self.rect.left = random.randrange(0, self.__screen.get_width()-80)
            
        
class ScoreKeeper(pygame.sprite.Sprite):     
    '''This class defines a label sprite to display the score.'''    
    def __init__(self):         
        '''This initializer loads the custom font for the game.'''  
        # Call the parent __init__() method         
        pygame.sprite.Sprite.__init__(self)           
        
        # Load custom font, and initialize the starting score.
        self.__font = pygame.font.Font("EHSMB.ttf", 30)         
        self.__score = 0 
        
    def set_score(self, point):         
        '''This method takes point as a parameter and adds it to the score of the player.'''
        self.__score += point
        
    def get_score(self):
        '''This method returns __score.'''
        return self.__score
    
    def update(self):         
        '''This method will be called automatically to display          
        the current game status at the top of the game window.'''  
        # Set the message
        message = "Score: %d" % (self.__score) 
        
        # Render and set rect
        self.image = self.__font.render(message, 1, (58,116,186))
        self.image.convert()
        self.rect = self.image.get_rect()         
        self.rect.left = 5
        self.rect.top = 15