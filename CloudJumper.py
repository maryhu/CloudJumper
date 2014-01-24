'''
   Author: Mary Hu
   Date: June 5, 2012
   Description: Cloud Jumper is a game in which the player must jump as 
   high as possible without falling off the clouds or touching the monster.
'''

import pygame, mySprites, time
pygame.init() 
screen = pygame.display.set_mode((420, 640))

def main():
    '''This function defines the mainline logic for the game.'''
    # Read the existing high score from file with exception handling
    try:
        high_scores = open("highscores.txt", 'r')
        for line in high_scores:
            old_score = int(line)
        
        high_scores.close()
    
    # Assign 0 to old_score's value if IOError occurs
    except IOError:
        old_score = 0
    
    # Assign initial values to variables
    high_score = old_score
    quit_game = False
    
    # Keep looping as long as the player does not choose to exit
    while not quit_game:
        quit_game = welcome_screen(high_score)
        
        if not quit_game:
            # Get player's score from the main game loop
            player_score = game()
            # Assign the highest of player's score and high score to high_score
            high_score = max(high_score, player_score)
            # Call the transition screen to display both scores
            # (with updated high score)
            transition_screen(player_score, high_score)
            
    # Write player's high score into the file
    high_scores = open("highscores.txt", 'w')
    high_scores.write(str(high_score))
    high_scores.close()
    
    # Close the game window
    pygame.quit()

def transition_screen(player_score, high_score):
    '''This function defines the transition screen between games. 
    It takes player_score and high_score as parameters.
    It will be called after the main game loop ends to display the player's 
    score as well as the current highscore.'''
    
    # Display    
    pygame.display.set_caption("Cloud Jumper")        
    
    # Entities    
    # Background image
    background = pygame.image.load("./Images/tscreen.jpg")
    background.convert()
    screen.blit(background, (0,0))
    
    # Display instructions
    font = pygame.font.Font("EHSMB.ttf", 25)        
    instructions = ("Your score: %d" %(player_score), "Highscore: %d" % \
            (high_score), "  ", "",  "", "", "", "PRESS SPACEBAR TO CONTINUE" )

    # Make a jumping player
    player = mySprites.Player(screen, 550, 300, 550)
    cloud = mySprites.Cloud(screen, 13)

    allSprites = pygame.sprite.OrderedUpdates(cloud, player,)

    # ACTION          
    # Assign     
    clock = pygame.time.Clock()   
    
    keepGoing = True   
    quit_game = False
    
    # Hide the mouse
    pygame.mouse.set_visible(False)
    
    # Loop    
    while keepGoing:             
        # Time       
        clock.tick(30)             
        
        # Events       
        # End the loop when user clicks exit button or press spacebar
        for event in pygame.event.get():          
            if event.type == pygame.QUIT: 
                keepGoing = False  
            elif event.type == pygame.KEYDOWN:      
                if event.key == pygame.K_SPACE:
                    keepGoing = False
                    
        # Display the messages
        for i in range(len(instructions)):
            message = font.render(instructions[i], 1, (58,116,186))
            background.blit(message, (15, 310+40*i))
        screen.blit(background, (0, 0))
        
        # Refresh screen       
        allSprites.clear(screen, background)       
        allSprites.update()       
        allSprites.draw(screen)                 
        
        pygame.display.flip() 
        
def instruction_screen():
    '''This function defines the instruction screen.
    It will be called when the user presses the I key at the welcome screen.'''
    # Display    
    pygame.display.set_caption("Cloud Jumper Instructions")  
    
    # Entities    
    # Background image
    background = pygame.image.load("./Images/instructions.jpg")
    background.convert()
    screen.blit(background, (0,0))
    pygame.display.flip() 
    
    # ACTION          
    # Assign     
    clock = pygame.time.Clock()   
    
    keepGoing = True   
    
    # Hide the mouse
    pygame.mouse.set_visible(False)
    
    # Loop    
    while keepGoing:             
        # Time       
        clock.tick(30)             
        
        # Events       
        # End loop when user clicks exit button or press spacebar
        for event in pygame.event.get():          
            if event.type == pygame.QUIT:             
                keepGoing = False
            elif event.type == pygame.KEYDOWN:      
                if event.key == pygame.K_SPACE:
                    keepGoing = False

def welcome_screen(high_score):
    '''This function defines the main menu screen for the game.
    It takes high_score as a parameter and returns the value of the boolean
    variable quit_game.'''
    # Display    
    pygame.display.set_caption("Welcome to Cloud Jumper!")        
    
    # Entities    
    
    # Background image
    background = pygame.image.load("./Images/screen.jpg")
    background.convert()
    screen.blit(background, (0,0))
    
    # Background music
    pygame.mixer.music.load("./Sounds/intro.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    
    # Display instructions
    font = pygame.font.Font("EHSMB.ttf", 23)        
    instructions = [ "     HIGH SCORE: %d" % (high_score), " ", "", "",  \
    "PRESS SPACEBAR TO BEGIN", "", "PRESS I FOR INSTRUCTIONS", "",\
    "PRESS ESC TO QUIT"]

    # Make a jumping player and animated monster on welcome screen
    player = mySprites.Player(screen, 550, 300, 550)
    cloud = mySprites.Cloud(screen, 13)
    star = mySprites.Star(screen, True)
    monster = mySprites.Monster(screen, True, 80, 355)
    
    allSprites = pygame.sprite.OrderedUpdates(cloud, player, star, monster)

    # ACTION          
    # Assign     
    clock = pygame.time.Clock()   
    
    keepGoing = True   
    quit_game = False
    
    # Hide the mouse
    pygame.mouse.set_visible(False)
    
    # Loop    
    while keepGoing:             
        # Time       
        clock.tick(30)             
        
        # Events       
        for event in pygame.event.get():          
            if event.type == pygame.QUIT:  
                # End loop and return True for quit_game
                keepGoing = False
                quit_game = True 
            elif event.type == pygame.KEYDOWN:      
                if event.key == pygame.K_SPACE:
                    # End loop
                    keepGoing = False
                if event.key == pygame.K_i:
                    # Call the instruction screen
                    instruction_screen()
                if event.key == pygame.K_ESCAPE:
                    # End loop and return True for quit_game
                    keepGoing = False
                    quit_game = True
                    
        #R- Refresh screen
        for i in range(len(instructions)):
            message = font.render(instructions[i], 1, (58,116,186))
            background.blit(message, (20, 330+20*i))
            screen.blit(background, (0, 0))
        
        # Refresh screen       
        allSprites.clear(screen, background)       
        allSprites.update()       
        allSprites.draw(screen)                 
        
        pygame.display.flip()  
        
    # Return the value of quit_game when user exits
    return quit_game
    
def game():
    '''This is the main game loop for Cloud Jumper.
    It does not have any parameters but it returns the player's score.'''
    
    # Display    
    pygame.display.set_caption("Cloud Jumper")    
    
    # Entities    
    background = pygame.Surface(screen.get_size())    
    background.fill((255, 255, 255))    
    screen.blit(background, (0, 0))   
    
    # Background music
    pygame.mixer.music.load("./Sounds/Rainbow Road.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    
    # Sound effects
    # Game over
    end_game = pygame.mixer.Sound("./Sounds/end.wav")
    end_game.set_volume(0.3)
    # Get star
    points_up = pygame.mixer.Sound("./Sounds/star.wav")
    points_up.set_volume(0.8)
    # Kill monster
    killed = pygame.mixer.Sound("./Sounds/killed.wav")
    killed.set_volume(0.7)
    # Get shield
    shield_sound = pygame.mixer.Sound("./Sounds/shield.wav")
    shield_sound.set_volume(0.8)
    # Shoot bullet
    shoot = pygame.mixer.Sound("./Sounds/shoot.wav")
    shoot.set_volume(0.8)
    
    # Create game over image
    gameover = pygame.image.load("./Images/gameover.png")
    gameover.convert()
    
    # Create sprite objects for game
    sky = mySprites.Sky(screen)   
       
    cloudSprites = pygame.sprite.Group()
    for i in range(13):       
        cloudSprites.add(mySprites.Cloud(screen,i))  

    player = mySprites.Player(screen, screen.get_height() - 20, \
                              screen.get_width()/2, screen.get_height() - 50)
    
    monster = mySprites.Monster(screen, False, 0, 0)
    star = mySprites.Star(screen, False)
    shield = mySprites.Shield(screen)
    bullets = pygame.sprite.Group()
    score = mySprites.ScoreKeeper()
    
    scroll_sprites = pygame.sprite.Group(sky, star, shield, monster)
    
    allSprites = pygame.sprite.OrderedUpdates(sky, cloudSprites, monster, \
                                    bullets, player, shield, star, score) 

    # ACTION          
    # Assign     
    keepGoing = True   
    clock = pygame.time.Clock()       
    shield_on = False
    
    # Hide the mouse
    pygame.mouse.set_visible(False)
    
    # Loop    
    while keepGoing:             
        # Time       
        clock.tick(30)             
        
        # Events       
        for event in pygame.event.get():          
            if event.type == pygame.QUIT:   
                keepGoing = False
            elif event.type == pygame.KEYDOWN:      
                if event.key == pygame.K_RIGHT:    
                    # Change the player's direction with a position x value
                    player.change_direction(10)
                if event.key == pygame.K_LEFT: 
                    # Change the player's direction with a position x value
                    player.change_direction(-10)
                if event.key == pygame.K_SPACE:
                    # Play sound effect
                    shoot.play()
                    # Add a bullet object to the list bullets
                    bullet = mySprites.Bullet(screen, player.rect.centerx, \
                                              player.rect.bottom)
                    bullets.add(bullet)
                    allSprites = pygame.sprite.OrderedUpdates(sky, \
                                cloudSprites, monster, bullets, player, score) 
                # Exit current game if "Q" key is pressed
                if event.key == pygame.K_q:
                    keepGoing = False 
            elif event.type == pygame.KEYUP:
                # Change the player's dx to 0 when no key is pressed
                player.change_direction(0)
           
        # Use a boolean variable to control the player's jumping movements
        cloud_list = pygame.sprite.spritecollide(player, cloudSprites, False) 
        # Set initial cloud height
        cloud_height = 640
        
        # Get player's velocity
        player_velocity = player.get_velocity()
        
        # Make player jump on clouds only when the jumping motion is downwards
        if player_velocity > 0:
            if cloud_list:
                for cloud in cloud_list:
                    # Check if player's bottom is greater than cloud's top
                    if player.rect.bottom > cloud.rect.top:
                        # Set the cloud's centery to the variable new_ground
                        new_ground = cloud.rect.centery
                        # Check if the player's bottom is less (higher)
                        # Than new_ground (cloud's centery)
                        if player.rect.bottom <= new_ground:
                            # Get cloud's centery value as new ground
                            player.set_ground(new_ground)
                            
                        # Check if cloud's top is less than cloud_height
                        # If True, set cloud_height to it
                        if cloud.rect.top < cloud_height:
                            cloud_height = cloud.rect.top
                            
                        # If the cloud_height is less than 500
                        # Scroll everything on screen down
                        if cloud_height<500:
                            # Set the scroll value for all clouds
                            for cloud in cloudSprites:
                                cloud.set_scroll(player.get_scroll())
                            # Add to player's score the scroll value
                            score.set_score(player.get_scroll())
                            # Set the scroll value for monster, sky
                            # shield, star, and monster
                            for item in scroll_sprites:
                                item.set_scroll(player.get_scroll())
                        # If the cloud_height is greater than 500
                        # Set all scroll values to 0 so they don't move
                        else:
                            for cloud in cloudSprites:
                                cloud.set_scroll(0)
                            for item in scroll_sprites:
                                item.set_scroll(0)
                            
            # Set the ground to greater than screen height if player 
            # does not collide with any clouds while jumping downwards
            else:
                player.set_ground(screen.get_height() + 20)
                
        # If a bullet collides with monster, reset monster and kill bullet
        for bullet in bullets:
            if bullet.rect.colliderect(monster.rect):
                monster.reset()
                bullet.kill()
                # Play sound effect
                killed.play()
                
        # Add 500 points to player's score when it collides with star
        # Reset the star's position and play sound effect
        if player.rect.colliderect(star.rect):
            star.reset()
            score.set_score(500)
            points_up.play()
            
        # When player collides with shield, reset shield's position
        # and turn on player's 'immunity', set shield_on to True
        if player.rect.colliderect(shield.rect):
            shield.reset()
            player.set_immunity(True)
            shield_on = True
            # Play shield sound effect
            shield_sound.play()
            
        # Set shield_on to false is player is no longer immune
        if not player.get_immunity():
            shield_on = False
        
        # Check player is in the game area 
        # (player will not be killed if jumping off-screen)
        if player.rect.top > 0:
             # Check if the player has collided with the monster
            if player.rect.colliderect(monster.rect):
                # Kill the player if the player does not have immunity
                if not shield_on:
                    player.kill()

        # Check if the player has lost
        # End game loop if True
        if player.lose():
            # Play game over sound
            end_game.play()
            keepGoing = False
        
        # Refresh screen       
        screen.blit(background, (0, 0))
        allSprites.update()       
        allSprites.draw(screen)                 
        
        pygame.display.flip()   
        
    # Get player's score at the end of the game
    score = score.get_score()
        
    # Show gameover image
    screen.blit(gameover, (50, 200))
    pygame.display.flip()
    
    # Sleep for 2 seconds
    time.sleep(2.0)
    
    # Return player's score to main function
    return score
    
# Call the main function 
main()