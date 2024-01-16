import random
import keyboard

Locations = [# 0 = Name of Group, 1 = Name of property, 2 = Player one counter location, 3 = Player two counter location, 4 = Cost, 5 = Owned?, 6 = House position, 7 = Hotel position
    ["Go", "Go", (840, 835), (840, 875)], #0
    ["Brown", "Space Dust", (742, 835), (742, 875), 100, False, (), ()], #1
    ["Gap", "PlaceHolder", (669, 835), (669, 875)], #2
    ["Brown", "Meteor", (596, 835), (596, 875), 150, False, (), ()], #3
    ["Gap", "PlaceHolder", (523, 835), (523, 875)], #4
    ["Telescope", "Hubble Space Telescope", (450, 835), (450, 875)], #5
    ["Cyan", "Uranus", (377, 835), (377, 875), 100, False, (), ()], #6
    ["Gap", "PlaceHolder", (304, 835), (304, 875)], #7
    ["Cyan", "Blue Supergiant", (231, 835), (231, 875), 100, False, (), ()], #8
    ["Cyan", "Neptune", (158, 835), (158, 875), 100, False, (), ()], #9
    ["NASA-HQ", "NASA-HQ", (30, 810), (90, 870)], #10
    ["Magenta", "Dark Matter", (25, 742), (65, 742)], #11
    ["Gap", "PlaceHolder", (25, 669), (65, 669)], #12
    ["Magenta", "Galaxy", (25, 596), (65, 596)], #13
    ["Magenta", "Dark Energy", (25, 523), (65, 523)], #14
    ["", "", (25, 450), (65, 450)], #15
    ["Orange", "Asteroid", (25, 377), (65, 377)], #16
    ["Gap", "PlaceHolder", (25, 304), (65, 304)], #17
    ["Orange", "Nebula", (25, 231), (65, 231)], #18
    ["Orange", "The Sun", (25, 158), (65, 158)], #19
    ["Inflation", "Inflation", (30, 30), (90, 90)], #20
    ["Red", "Red Dwarf", (158, 35), (158, 65)], #21
    ["Gap", "PlaceHolder", (231, 35), (231, 65)], #22
    ["Red", "Red Giant", (304, 35), (304, 65)], #23
    ["Red", "Mars", (377, 35), (377, 65)], #24
    ["ISS", "International Space Station", (450, 35), (450, 65)], #25
    ["Yellow", "Venus", (523, 35), (523, 65)], #26
    ["Yellow", "Saturn", (596, 35), (596, 65)], #27
    ["Gap", "PlaceHolder", (669, 35), (669, 65)], #28
    ["Yellow", "Jupiter", (742, 35), (742, 65)], #29
    ["Square", "Square", (810, 30), (870, 90)], #30
    ["Green", "Acid rain", (835, 158), (875, 158)], #31
    ["Green", "Earth", (835, 231), (875, 231)], #32
    ["Gap", "PlaceHolder", (835, 304), (875, 304)], #33
    ["Green", "Comet", (835, 377), (875, 377)], #34
    ["Telescope", "Spitzer Space Telescope", (835, 450), (875, 450)], #35
    ["Gap", "PlaceHolder", (835, 523), (875, 523)], #36
    ["Blue", "Neutron star", (835, 596), (875, 596)], #37
    ["Gap", "PlaceHolder", (835, 669), (875, 669)], #38
    ["Blue", "Black hole", (835, 742), (875, 742)], #39
]


def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    return [dice1, dice2]
class Player:
    def __init__(self,color,no):
        self.cash = 400000
        self.properties = []
        self.color = color
        self.no = no
        self.currentPosition = 0
        


class Property:
    def __init__(self, name, planet, cost):
        self.name = name
        self.planet = planet
        self.cost = cost
        self.telescopes = [0.1*self.cost,0.4*self.cost,0.5*self.cost,0.6*self.cost,self.cost]
        self.rocket = cost * 1.25
        self.owner = None
        self.no_of_houses = 0

Player1 = Player("Red", 1)
Player2 = Player("Blue", 2)


     
# while True:
#     dicelist = gameplay.roll_dice()
#     total = dicelist[0] + dicelist[1]
#     if Player1.currentPosition <= 39 - total:
#         Player1.currentPosition += total
#         print(Player1.currentPosition)
#         time.sleep(2)
#     else:
#         while Player1.currentPosition < 39:
#             Player1.currentPosition += 1
#             total -= 1
#         Player1.currentPosition = 0
#         Player1.currentPosition += total
#         print(Player1.currentPosition)
#         time.sleep(2)
    
#     dicelist = gameplay.roll_dice()
#     total = dicelist[0] + dicelist[1]
#     if Player2.currentPosition <= 39 - total:
#         Player2.currentPosition += total
#         print(Player2.currentPosition)
#         time.sleep(2)
#     else:
#         while Player2.currentPosition <= 39:
#             Player2.currentPosition += 1
#             total -= 1
#         Player2.currentPosition = 0
#         Player2.currentPosition += total
#         print(Player2.currentPosition)
#         time.sleep(2)

