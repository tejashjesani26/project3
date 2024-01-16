import pygame
from sys import exit
import gameplay
import keyboard
import time
import subprocess
import pyautogui

# logged_in = False
# html_file_path = 'C:/Users/Tejash/PycharmProjects/monopoly_game/web.html'
# chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'  # Adjust the path based on your Chrome installation
# subprocess.Popen([chrome_path, html_file_path])


# while not logged_in:
#     time.sleep(5)
#     logged_in = True
#     pyautogui.hotkey('ctrl', 'w')

fonts = pygame.font.get_fonts()


pygame.init()
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Monopoly: Space Edition")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/arial.ttf', 100)
boardimage = pygame.image.load('images/board.jpg')
boardimage = pygame.transform.scale(boardimage, (900, 900))
# bluecounterimage = pygame.image.load('images/bluecounter.png')
# redcounterimage = pygame.image.load('images/redcounter.png')


class PlayerTurn:
    def __init__(self, WhosTurn):
        self.WhosTurn = WhosTurn

running = True
waiting_for_input = True
Turn = PlayerTurn(1)


def rollDiceAndMove(turn):
    if turn == 1:
        

        dicevalues = gameplay.roll_dice()
        total = dicevalues[0] + dicevalues[1]
        diceimg1 = pygame.image.load(f'images/dice/{dicevalues[0]}.png')
        diceimg2 = pygame.image.load(f'images/dice/{dicevalues[1]}.png')
        diceimg1 = pygame.transform.scale(diceimg1, (40, 40))
        diceimg2 = pygame.transform.scale(diceimg2, (40, 40))
        screen.blit(diceimg1, diceimg1.get_rect(center = (300, 300)))
        screen.blit(diceimg2, diceimg2.get_rect(center = (400, 400)))
        pygame.display.update()
        print(total)
        if Player1.currentPosition <= 39 - total:
            Player1.currentPosition += total
            time.sleep(2)
            
            return [diceimg1, diceimg2]
        else:
            
            while Player1.currentPosition <= 39:
                Player1.currentPosition += 1
                total -= 1
               
            Player1.currentPosition = 0
            Player1.currentPosition += total
            time.sleep(2)
            return [diceimg1, diceimg2]

    if turn == 2:
        

        dicevalues = gameplay.roll_dice()
        total = dicevalues[0] + dicevalues[1]
        diceimg1 = pygame.image.load(f'images/dice/{dicevalues[0]}.png')
        diceimg2 = pygame.image.load(f'images/dice/{dicevalues[1]}.png')
        diceimg1 = pygame.transform.scale(diceimg1, (40, 40))
        diceimg2 = pygame.transform.scale(diceimg2, (40, 40))
        screen.blit(diceimg1, diceimg1.get_rect(center = (300, 300)))
        screen.blit(diceimg2, diceimg2.get_rect(center = (400, 400)))
        pygame.display.update()
        print(total)
        if Player2.currentPosition <= 39 - total:
            Player2.currentPosition += total
            time.sleep(2)
            return [diceimg1, diceimg2]
        else:
           
            while Player2.currentPosition <= 39:
                Player2.currentPosition += 1
                total -= 1
                
            Player2.currentPosition = 0
            Player2.currentPosition += total
            time.sleep(2)
            return [diceimg1, diceimg2]
propertiesBought = []

def PurchaseProperty(turn):
    if turn == 1:
        newProperty = gameplay.Property(gameplay.Locations[Player1.currentPosition][1], None, 150)
        newProperty.owner = Player1
        propertiesBought.append(newProperty)
        Player1.properties.append(newProperty)
        
        for x in Player1.properties:
            print(x.name)
    if turn == 2:
        newProperty = gameplay.Property(gameplay.Locations[Player2.currentPosition][1], None, 150)
        newProperty.owner = Player2
        propertiesBought.append(newProperty)
        Player2.properties.append(newProperty)
        
        for x in Player2.properties:
            print(x.name)




gameStatus = "Roll"   

Debounce = False
Player1obj = gameplay.Player1
Player2obj = gameplay.Player2
plr1counterimage = pygame.image.load(f'images/{Player1obj.color.lower()}counter2.png')
plr1counterimage = pygame.transform.scale(plr1counterimage, (30, 30))
plr2counterimage = pygame.image.load(f'images/{Player2obj.color.lower()}counter2.png')
plr2counterimage = pygame.transform.scale(plr2counterimage, (30, 30))



while running:
    Player1 = Player1obj
    Player2 = Player2obj
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            running = False

    background = screen.blit(boardimage, (0, 0))

    Counter1 = screen.blit(plr1counterimage, plr1counterimage.get_rect(center = gameplay.Locations[Player1.currentPosition][2]))
    Counter2 = screen.blit(plr2counterimage, plr2counterimage.get_rect(center = gameplay.Locations[Player2.currentPosition][3]))
    pygame.display.update()
    
    if keyboard.is_pressed("r"):  
        if gameStatus == "Roll":
            if Debounce == False:
                Debounce = True
                time.sleep(1)
                result = rollDiceAndMove(Turn.WhosTurn)
                gameStatus = "Buy"
                #print(Player1.currentPosition,Player2.currentPosition)
                time.sleep(2)
                Debounce = False

    # if keyboard.is_pressed("e"):
    #     if gameStatus == "Buy":
    #         if Debounce == False:
    #             Debounce = True
    #             PurchaseProperty(Turn.WhosTurn)
    #             gameStatus = "Roll"
    #             time.sleep(2)
    #             Debounce = False
    #             if Turn.WhosTurn == 1:
    #                 Turn.WhosTurn = 2
    #             else:
    #                 Turn.WhosTurn = 1
   
    #displayScore()
    
    clock.tick(60)



    