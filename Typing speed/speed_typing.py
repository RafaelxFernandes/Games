import sys
import time
import random
import pygame
from pygame.locals import *
  
    
class Game:   
    def __init__(self):
        self.width = 750
        self.height = 500
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255,213,102)
        self.TEXT_C = (240,240,240)
        self.RESULT_C = (255,70,70)
        
        pygame.init()
        self.open_image = pygame.image.load('type-speed-open.png')
        self.open_image = pygame.transform.scale(self.open_image, (self.width,self.height))

        self.background = pygame.image.load('background.jpg')
        self.background = pygame.transform.scale(self.background, (500,750))

        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Type Speed Game by RafaelxFernandes')
       
        
    def draw_text(self, screen, message, y_cor ,font_size, color):
        font = pygame.font.Font(None, font_size)
        text = font.render(message, 1, color)
        text_rectangle = text.get_rect(center=(self.width/2, y_cor))
        screen.blit(text, text_rectangle)
        pygame.display.update()   

        
    def get_sentence(self):
        sentence_file = open('sentences.txt').read()
        sentences = sentence_file.split('\n')
        sentence = random.choice(sentences)
        return sentence


    # A typical word consists of around 5 characters, so we calculate the words per minute by ...
    # ... dividing the total number of words with five and then the result is again divided that with ... 
    # ... the total time it took in minutes. 
    # Since the total time was in seconds, I had to convert it into minutes by dividing total time with 60.
    # At last, I have drawn the typing icon image at the bottom of the screen which ... 
    # ... we will be used as a reset button. When the user clicks it, the game would reset. 
    def show_results(self, screen):
        # Calculate time
        if(not self.end):
            self.total_time = time.time() - self.time_start
               
            # Calculate accuracy
            count = 0

            for index, character in enumerate(self.word):
                try:
                    if self.input_text[index] == character:
                        count += 1
                except:
                    pass

            self.accuracy = count/ len(self.word) * 100
           
            # Calculate words per minute
            self.wpm = len(self.input_text) * 60/ (5 * self.total_time)
            self.end = True
            print(self.total_time)
                
            self.results = 'Time: ' + str(round(self.total_time)) + " secs | Accuracy: " + str(round(self.accuracy)) + "%" + ' | Wpm: ' + str(round(self.wpm))

            # Draw icon image
            self.time_image = pygame.image.load('icon.png')
            self.time_image = pygame.transform.scale(self.time_image, (150,150))
            screen.blit(self.time_image, (self.width/2-75, self.height-140))
            self.draw_text(screen,"Reset", self.height - 70, 26, (100,100,100))
            
            print(self.results)
            pygame.display.update()


    # This is the main method of our class that will handle all the events. 
    # We call the reset_game() method at the starting of this method which resets all the variables. 
    # Next, we run an infinite loop which will capture all the mouse and keyboard events. 
    # Then, we draw the heading and the input box on the screen.
    # We then use another loop that will look for the mouse and keyboard events. 
    # When the mouse button is pressed, we check the position of the mouse if it is on the input box...
    # ... then we start the time and set the active to True. 
    # If it is on the reset button, then we reset the game.
    # When the active is True and typing has not ended then we look for keyboard events. 
    # If the user presses any key then we need to update the message on our input box. 
    # The enter key will end typing and we will calculate the scores to display it.
    # Another event of a backspace is used to trim the input text by removing the last character
    def run(self):
        self.reset_game()
    
        self.running = True

        while(self.running):
            clock = pygame.time.Clock()

            self.screen.fill((0,0,0), (50,250,650,50))
            pygame.draw.rect(self.screen, self.HEAD_C, (50,250,650,50), 2)

            # Update the text of user input
            self.draw_text(self.screen, self.input_text, 274, 26,(250,250,250))
            pygame.display.update()

            for event in pygame.event.get():
                if(event.type == QUIT):
                    self.running = False
                    sys.exit()

                elif(event.type == pygame.MOUSEBUTTONUP):
                    x,y = pygame.mouse.get_pos()
                    
                    # Position of input box
                    if(x >= 50 and x <= 650 and y >= 250 and y <= 300):
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time() 
                    
                    # Position of reset box
                    if(x >= 310 and x <= 510 and y >= 390 and self.end):
                        self.reset_game()
                        x,y = pygame.mouse.get_pos()
                  
                elif(event.type == pygame.KEYDOWN):
                    if(self.active and not self.end):
                        if(event.key == pygame.K_RETURN):
                            print(self.input_text)

                            self.show_results(self.screen)
                            print(self.results)
                            
                            self.draw_text(self.screen, self.results,350, 28, self.RESULT_C)  
                            self.end = True
                            
                        elif(event.key == pygame.K_BACKSPACE):
                            self.input_text = self.input_text[:-1]

                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass
            
            pygame.display.update()
                
        clock.tick(60)


    def reset_game(self):
        self.screen.blit(self.open_image, (0,0))

        pygame.display.update()
        time.sleep(1)
        
        self.reset = False
        self.end = False

        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        # Get random sentence 
        self.word = self.get_sentence()
        if (not self.word): self.reset_game()

        # Drawing heading
        self.screen.fill((0,0,0))
        self.screen.blit(self.background,(0,0))
        message = "Typing Speed Game"
        self.draw_text(self.screen, message, 80, 80, self.HEAD_C)  
        
        # Draw the rectangle for input box
        pygame.draw.rect(self.screen,(255,192,25), (50,250,650,50), 2)

        # Draw the sentence string
        self.draw_text(self.screen, self.word,200, 28,self.TEXT_C)
        
        pygame.display.update()

# Game main loop
Game().run()