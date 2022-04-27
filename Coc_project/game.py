#import climage
from pickle import NONE
import colorama
import time
from src.input import *
from colorama import Fore, Back, Style
import os
#from replay import *
class buildings:
    def __init__(self, name, hitpoints,x,y):
        self.name = name
        self.hitpoints = hitpoints
        self.x = x
        self.y = y


class cannons(buildings):
    def __init__(self, name, hitpoints,x,y,dps,range,attacking):
        self.dps = dps
        self.range = range
        self.attacking = attacking
        buildings.__init__(self, name, hitpoints,x,y)

class wizardtower(buildings):
    def __init__(self, name, hitpoints,x,y,dps,range,attacking):
        self.dps = dps
        self.range = range
        self.attacking = attacking
        buildings.__init__(self, name, hitpoints,x,y)

class TownHall:
    hitpoints = 100
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y 
class troops:
    def __init__(self, name, hitpoints):
        self.name = name
        self.hitpoints = hitpoints

class Queen(troops):
    def __init__(self, name, hitpoints, dps, x, y, prev,speed):
        self.dps = dps
        self.x = x
        self.y = y
        self.prev = prev
        self.speed = speed
        troops.__init__(self, name, hitpoints)
    def queenbar(self,hitpoints):
        x = self.hitpoints/4
        print("Queen health bar =======>|",end = " ")
        t = 1
        while(x >= t):
            print(Back.BLUE+" ",end = " ")
            print(Style.RESET_ALL,end = "")
            t+=1
        while(t <=25):
            print(" ",end = "")
            t += 1
        print("\n")    
        
class King(troops):
    def __init__(self, name, hitpoints, dps, x, y, prev,speed):
        self.dps = dps
        self.x = x
        self.y = y
        self.prev = prev
        self.speed = speed
        troops.__init__(self, name, hitpoints)
        
    def kingbar(self,hitpoints):
        x = self.hitpoints/4
        print("King health bar =======>|",end = " ")
        t = 1
        while(x >= t):
            print(Back.CYAN+" ",end = " ")
            print(Style.RESET_ALL,end = "")
            t+=1
        while(t <=25):
            print(" ",end = "")
            t += 1
        print("\n")


class barbarians(troops):
    def __init__(self, name, hitpoints, dps,x,y,target_x,target_y,prev,speed):
        self.dps = dps
        self.x = x
        self.y =y
        self.target_x = target_x
        self.target_y = target_y
        self.prev = prev
        self.speed = speed
        troops.__init__(self, name, hitpoints)
        
class archers(troops):
    def __init__(self, name, hitpoints, dps,x,y,target_x,target_y,prev,speed):
        self.dps = dps
        self.x = x
        self.y =y
        self.target_x = target_x
        self.target_y = target_y
        self.prev = prev
        self.speed = speed
        troops.__init__(self, name, hitpoints)
        
class balloon(troops):
    def __init__(self,name, hitpoints, dps,x,y,target_x,target_y,prev,speed):
        self.dps = dps
        self.x = x
        self.y =y
        self.target_x = target_x
        self.target_y = target_y
        self.prev = prev
        self.speed = speed
        troops.__init__(self, name, hitpoints)


class spell:
    def __init__(self, name, range, x, y):
        self.name = name
        self.range = range
        self.x = x
        self.y = y

build = []
king_spawned = 0
queen_spawned = 0
coordinates = []
bot = []
fembot = []
balloons = []

TownHall1 = TownHall("TownHall", 11,11)
TownHall2 = TownHall("TownHall1", 11,12)
TownHall3 = TownHall("TownHall2", 11,13)
TownHall4 = TownHall("TownHall3", 12,11)
TownHall5 = TownHall("TownHall4", 12,12)
TownHall6 = TownHall("TownHall5", 12,13)
TownHall7 = TownHall("TownHall6", 13,11)
TownHall8 = TownHall("TownHall7", 13,12)
TownHall9 = TownHall("TownHall8", 13,13)
TownHall10 = TownHall("TownHall9", 14,11)
TownHall11 = TownHall("TownHall10", 14,12)
TownHall12 = TownHall("TownHall11", 14,13)



build.append(TownHall1)
build.append(TownHall2)
build.append(TownHall3)
build.append(TownHall4)
build.append(TownHall5)
build.append(TownHall6)
build.append(TownHall7)
build.append(TownHall8)
build.append(TownHall9)
build.append(TownHall10)
build.append(TownHall11)
build.append(TownHall12)

walls = []
huts = []


Tower1 = wizardtower("Wizard",60,16,9,1,1.5,0)
Tower2 = wizardtower("Wizard",60,16,15,1,1.5,0)
build.append(Tower1)
build.append(Tower2)


hut1 = buildings("HUT", 50,2,2)
build.append(hut1)
hut2 = buildings("HUT", 50,0,1)
build.append(hut2)
hut3 = buildings("HUT", 50,1,0)
build.append(hut3)
hut4 = buildings("HUT", 50,1,1)
build.append(hut4)
hut5 = buildings("HUT", 50,3,3)
build.append(hut5)
cannon1 = cannons("Cannon", 75,20,12, 0.5, 5,0)
build.append(cannon1)
cannon2 = cannons("Cannon", 75,12,7, 0.5, 5,0)
build.append(cannon2)
#cannon3 = cannons("Cannon", 75,12,16, 0.5, 5,0)
#build.append(cannon3)
#cannon4 = cannons("Cannon", 75,8,12, 0.5, 5,0)
#build.append(cannon4)
#cannon5 = cannons("Cannon", 75,0,0, 0.5, 5,0)
#build.append(cannon5)
n = 26
m = 26

king_last = ''
queen_last = ''
prev = "|-|"
king = King("King", 100, 5, 20, 15, prev,1)
queen = Queen("Queen",100,5,20,15,prev,1)

def spawn_king():
    coordinates[20][15] = "|K|"
    king.prev = "|-|"
    king.hitpoints = 100
def spawn_queen():
    coordinates[20][15] = "|Q|"
    queen.prev = "|-|"
    queen.hitpoints = 100
    
def deal_with_wall(i,x,y):
    for j in range(len(fembot)):
        if j != i: 
            continue
        else:
            for k in range(len(build)):
                if build[k].x == fembot[j].x + x and fembot[j].y + y == build[k].y:
                    if build[k].hitpoints >= fembot[j].dps:
                        build[k].hitpoints -= fembot[j].dps
                    else:
                        build[k].hitpoints = 0     
    
        
def king_movement(p):
    if king.hitpoints <= 0:
        return
    coordinates[king.x][king.y] = king.prev
    if (p == 'W' or p == 'w'):
        king.x -= 1*king.speed
        king_last = 'w'
    if p == 'S' or p == 's':
        king.x += 1*king.speed
        king_last = 's'
    if p == 'A' or p == 'a':
        king.y -= 1*king.speed
        king_last = 'a'
    if p == 'D' or p == 'd':
        king.y += 1*king.speed
        king_last = 'd'
    if king.x < 0:
        king.x = 0
    if king.y > 25:
        king.y = 25
    if king.y < 0:
        king.y = 0
    if king.x > 25:
        king.x = 25
    if coordinates[king.x][king.y] == "|-|":
        king.prev = coordinates[king.x][king.y]
        coordinates[king.x][king.y] = "|K|"
    else:
        if p == 'W' or p == 'w':
            king.x += 1*king.speed
        if p == 'S' or p == 's':
            king.x -= 1*king.speed
        if p == 'A' or p == 'a':
            king.y += 1*king.speed
        if p == 'D' or p == 'd':
            king.y -= 1*king.speed
        coordinates[king.x][king.y] = "|K|"
def queen_movement(p):
    if king.hitpoints <= 0:
        return
    coordinates[queen.x][queen.y] = queen.prev
    if (p == 'W' or p == 'w'):
        queen.x -= 1*queen.speed
        queen_last = 'w'
    if p == 'S' or p == 's':
        queen.x += 1*queen.speed
        queen_last = 's'
    if p == 'A' or p == 'a':
        queen.y -= 1*queen.speed
        queen_last = 'a'
    if p == 'D' or p == 'd':
        queen.y += 1*queen.speed
        queen_last = 'd'
    if queen.x < 0:
        queen.x = 0
    if queen.y > 25:
        queen.y = 25
    if queen.y < 0:
        queen.y = 0
    if queen.x > 25:
        queen.x = 25
    if coordinates[queen.x][queen.y] == "|-|":
        queen.prev = coordinates[queen.x][queen.y]
        coordinates[queen.x][queen.y] = "|Q|"
    else:
        if p == 'W' or p == 'w':
            queen.x += 1*queen.speed
        if p == 'S' or p == 's':
            queen.x -= 1*queen.speed
        if p == 'A' or p == 'a':
            queen.y += 1*queen.speed
        if p == 'D' or p == 'd':
            queen.y -= 1*queen.speed
        coordinates[queen.x][queen.y] = "|Q|"
def queen_attack():
    if queen.hitpoints <= 0:
        return
    if queen_last == 'w':
        target_x = queen.x - 8 
        for i in range(len(build)):
            if build[i].name[0] != 'T' and build[i].hitpoints > 0:

                if abs(build[i].x- target_x) <=2 and  abs(build[i].y -queen.y) <= 2:
                    if build[i].hitpoints > queen.dps:
                        build[i].hitpoints -= queen.dps
                    else:
                        build[i].hitpoints = 0
                        coordinates[build[i].x][build[i].y] = "|-|"
            elif TownHall.hitpoints > 0:
                    if TownHall.hitpoints > queen.dps and abs(build[i].x - target_x) <= 2 and abs(build[i].y - queen.y) <= 2:
                        TownHall.hitpoints -= queen.dps
                    elif TownHall.hitpoints > queen.dps:
                        continue
                    else:
                        TownHall.hitpoints = 0
                        build[i].hitpoints = 0
                        coordinates[11][11] = "|-|"
                        coordinates[11][12] = "|-|"
                        coordinates[11][13] = "|-|"
                        coordinates[12][11] = "|-|"
                        coordinates[12][12] = "|-|"
                        coordinates[12][13] = "|-|"
                        coordinates[13][11] = "|-|"
                        coordinates[13][12] = "|-|"
                        coordinates[13][13] = "|-|"
                        coordinates[14][11] = "|-|"
                        coordinates[14][12] = "|-|"
                        coordinates[14][13] = "|-|"
    if queen_last == 's':
        target_x = queen.x + 8 
        for i in range(len(build)):
            if build[i].name[0] != 'T' and build[i].hitpoints > 0:

                if abs(build[i].x- target_x) <=2 and  abs(build[i].y -queen.y) <= 2:
                    if build[i].hitpoints > queen.dps:
                        build[i].hitpoints -= queen.dps
                    else:
                        build[i].hitpoints = 0
                        coordinates[build[i].x][build[i].y] = "|-|"
            elif TownHall.hitpoints > 0:
                    if TownHall.hitpoints > queen.dps and abs(build[i].x - target_x) <= 2 and abs(build[i].y - queen.y) <= 2:
                        TownHall.hitpoints -= queen.dps
                    elif TownHall.hitpoints > queen.dps:
                        continue
                    else:
                        TownHall.hitpoints = 0
                        build[i].hitpoints = 0
                        coordinates[11][11] = "|-|"
                        coordinates[11][12] = "|-|"
                        coordinates[11][13] = "|-|"
                        coordinates[12][11] = "|-|"
                        coordinates[12][12] = "|-|"
                        coordinates[12][13] = "|-|"
                        coordinates[13][11] = "|-|"
                        coordinates[13][12] = "|-|"
                        coordinates[13][13] = "|-|"
                        coordinates[14][11] = "|-|"
                        coordinates[14][12] = "|-|"
                        coordinates[14][13] = "|-|"

    if queen_last == 'a':
        target_y = queen.y - 8 
        for i in range(len(build)):
            if build[i].name[0] != 'T' and build[i].hitpoints > 0:

                if abs(build[i].x- queen.x) <=2 and  abs(build[i].y - target_y) <= 2:
                    if build[i].hitpoints > queen.dps:
                        build[i].hitpoints -= queen.dps
                    else:
                        build[i].hitpoints = 0
                        coordinates[build[i].x][build[i].y] = "|-|"
            elif TownHall.hitpoints > 0:
                    if TownHall.hitpoints > queen.dps and abs(build[i].x - queen.x) <= 2 and abs(build[i].y - target_y) <= 2:
                        TownHall.hitpoints -= queen.dps
                    elif TownHall.hitpoints > queen.dps:
                        continue
                    else:
                        TownHall.hitpoints = 0
                        build[i].hitpoints = 0
                        coordinates[11][11] = "|-|"
                        coordinates[11][12] = "|-|"
                        coordinates[11][13] = "|-|"
                        coordinates[12][11] = "|-|"
                        coordinates[12][12] = "|-|"
                        coordinates[12][13] = "|-|"
                        coordinates[13][11] = "|-|"
                        coordinates[13][12] = "|-|"
                        coordinates[13][13] = "|-|"
                        coordinates[14][11] = "|-|"
                        coordinates[14][12] = "|-|"
                        coordinates[14][13] = "|-|"
    if queen_last == 'd':
        target_y = queen.y + 8 
        for i in range(len(build)):
            if build[i].name[0] != 'T' and build[i].hitpoints > 0:

                if abs(build[i].x- queen.x) <=2 and  abs(build[i].y - target_y) <= 2:
                    if build[i].hitpoints > queen.dps:
                        build[i].hitpoints -= queen.dps
                    else:
                        build[i].hitpoints = 0
                        coordinates[build[i].x][build[i].y] = "|-|"
            elif TownHall.hitpoints > 0:
                    if TownHall.hitpoints > queen.dps and abs(build[i].x - queen.x) <= 2 and abs(build[i].y - target_y) <= 2:
                        TownHall.hitpoints -= queen.dps
                    elif TownHall.hitpoints > queen.dps:
                        continue
                    else:
                        TownHall.hitpoints = 0
                        build[i].hitpoints = 0
                        coordinates[11][11] = "|-|"
                        coordinates[11][12] = "|-|"
                        coordinates[11][13] = "|-|"
                        coordinates[12][11] = "|-|"
                        coordinates[12][12] = "|-|"
                        coordinates[12][13] = "|-|"
                        coordinates[13][11] = "|-|"
                        coordinates[13][12] = "|-|"
                        coordinates[13][13] = "|-|"
                        coordinates[14][11] = "|-|"
                        coordinates[14][12] = "|-|"
                        coordinates[14][13] = "|-|"



def king_attack():
    if king.hitpoints <= 0:
        return
    if king_last == 'w':
        for i in range(len(build)):
            if build[i].name[0] != 'T' and build[i].hitpoints > 0:
                if build[i].x == king.x-1 and build[i].y == king.y:
                    if build[i].hitpoints > king.dps:
                        build[i].hitpoints -= king.dps
                    else:
                        build[i].hitpoints = 0
                        coordinates[build[i].x][build[i].y] = "|-|"
            elif TownHall.hitpoints > 0:
                if (king.y == 11 or king.y == 12 or king.y == 13) and (king.x == 15):
                    if TownHall.hitpoints > king.dps and build[i].x == king.x-1 and build[i].y == king.y:
                        TownHall.hitpoints -= king.dps
                    elif TownHall.hitpoints > king.dps:
                        continue
                    else:
                        build[i].hitpoints = 0
                        coordinates[11][11] = "|-|"
                        coordinates[11][12] = "|-|"
                        coordinates[11][13] = "|-|"
                        coordinates[12][11] = "|-|"
                        coordinates[12][12] = "|-|"
                        coordinates[12][13] = "|-|"
                        coordinates[13][11] = "|-|"
                        coordinates[13][12] = "|-|"
                        coordinates[13][13] = "|-|"
                        coordinates[14][11] = "|-|"
                        coordinates[14][12] = "|-|"
                        coordinates[14][13] = "|-|"
    if king_last == 'a':
        for i in range(len(build)):
            if build[i].name[0] != "T" and build[i].hitpoints > 0:
                if build[i].y == king.y-1 and build[i].x == king.x:
                    if build[i].hitpoints > king.dps:
                        build[i].hitpoints -= king.dps
                    else:
                        build[i].hitpoints = 0
                        coordinates[build[i].x][build[i].y] = "|-|"
            else:
                if (king.x == 11 or king.x == 12 or king.x == 13 or king.x == 14) and (king.y == 14) :
                    if TownHall.hitpoints > king.dps and build[i].y == king.y-1 and build[i].x == king.x:
                        TownHall.hitpoints -= king.dps
                    elif TownHall.hitpoints > king.dps:
                        continue
                    else:
                        build[i].hitpoints = 0
                        coordinates[11][11] = "|-|"
                        coordinates[11][12] = "|-|"
                        coordinates[11][13] = "|-|"
                        coordinates[12][11] = "|-|"
                        coordinates[12][12] = "|-|"
                        coordinates[12][13] = "|-|"
                        coordinates[13][11] = "|-|"
                        coordinates[13][12] = "|-|"
                        coordinates[13][13] = "|-|"
                        coordinates[14][11] = "|-|"
                        coordinates[14][12] = "|-|"
                        coordinates[14][13] = "|-|"
    if king_last == 'd':
        for i in range(len(build)):
            if build[i].name[0] != "T" and build[i].hitpoints > 0:
                if build[i].y == king.y+1 and build[i].x == king.x:
                    if build[i].hitpoints > king.dps:
                        build[i].hitpoints -= king.dps
                    else:
                        build[i].hitpoints = 0
                        coordinates[build[i].x][build[i].y] = "|-|"
            else:
                if (king.x == 11 or king.x == 12 or king.x == 13 or king.x == 14) and (king.y == 10) and build[i].y == king.y+1 and build[i].x == king.x:
                    if TownHall.hitpoints > king.dps:
                        TownHall.hitpoints -= king.dps
                    elif TownHall.hitpoints > king.dps:
                        continue
                    else:
                        build[i].hitpoints = 0
                        coordinates[11][11] = "|-|"
                        coordinates[11][12] = "|-|"
                        coordinates[11][13] = "|-|"
                        coordinates[12][11] = "|-|"
                        coordinates[12][12] = "|-|"
                        coordinates[12][13] = "|-|"
                        coordinates[13][11] = "|-|"
                        coordinates[13][12] = "|-|"
                        coordinates[13][13] = "|-|"
                        coordinates[14][11] = "|-|"
                        coordinates[14][12] = "|-|"
                        coordinates[14][13] = "|-|"
    if king_last == 's':
        for i in range(len(build)):
            if build[i].name[0] != "T" and build[i].hitpoints > 0:
                if build[i].x == king.x+1 and build[i].y == king.y:
                    if build[i].hitpoints > king.dps:
                        build[i].hitpoints -= king.dps
                    else:
                        build[i].hitpoints = 0
                        coordinates[build[i].x][build[i].y] = "|-|"
            else:
                if (king.y == 11 or king.y == 12 or king.y == 13) and (king.x == 10) and build[i].x == king.x+1 and build[i].y == king.y:
                    if TownHall.hitpoints > king.dps:
                        TownHall.hitpoints -= king.dps
                    elif TownHall.hitpoints > king.dps:
                        continue
                    else:
                        build[i].hitpoints = 0
                        coordinates[11][11] = "|-|"
                        coordinates[11][12] = "|-|"
                        coordinates[11][13] = "|-|"
                        coordinates[12][11] = "|-|"
                        coordinates[12][12] = "|-|"
                        coordinates[12][13] = "|-|"
                        coordinates[13][11] = "|-|"
                        coordinates[13][12] = "|-|"
                        coordinates[13][13] = "|-|"
                        coordinates[14][11] = "|-|"
                        coordinates[14][12] = "|-|"
                        coordinates[14][13] = "|-|"
    
                        
        
for i in range(n):
    cols = []
    cnt = 0
    for j in range(m):
        if i >= 11 and i <= 14 and j >= 11 and j <= 13:
            cols.append('|T|')
        elif (i == 2 and j == 2) or (i == 0 and j == 1) or (i == 1 and j == 0) or (i == 1 and j == 1) or (i == 3 and j == 3):
            cols.append('|H|')
        elif (i == 20 and j == 5) or (i == 5 and j == 12) or (i == 20 and j == 18):
            cols.append('|S|')
        elif (i == 20 and j == 12) or (i == 12 and j == 7):
            cols.append('|C|')
        elif (i == 10 and j >= 10 and j <= 14) or (i == 15 and j > 10 and j <= 14) or (j == 10 and i > 10 and i <= 15) or (j == 14 and i > 10 and i <= 15) or (i == 0 and j == 2) or (i == 1 and j == 2) or (i == 2 and j == 1) or (i == 2 and j == 0):
            cnt += 1
            wall = "wall"
            wall += str(cnt)
            build.append(buildings(wall,25,i,j))
            cols.append('|W|')
        elif i == 16 and (j == 9 or j== 15):
            cols.append('|w|')
        else:
            cols.append('|-|')
    coordinates.append(cols)
    
    
    
def wizards_attack(): 
    for i in range(len(build)):
        target_x = -1
        target_y = -1
        min = 10000
        if build[i].name == 'Wizard' and build[i].hitpoints > 0 and king_spawned == 1:
            if abs(king.x - build[i].x) + abs(king.y -build[i].y) < min:
                target_x = king.x
                target_y = king.y
                min = abs(king.x - build[i].x) + abs(king.y -build[i].y)
        if build[i].name == 'Wizard' and build[i].hitpoints > 0 and queen_spawned == 1:
            if abs(queen.x - build[i].x) + abs(queen.y -build[i].y) < min:
                target_x = queen.x
                target_y = queen.y
                min = abs(queen.x - build[i].x) + abs(queen.y -build[i].y)
        if build[i].name == 'Wizard' and build[i].hitpoints > 0:
            for j in range(len(bot)):
                if abs(bot[j].x - build[i].x) + abs(bot[j].y - build[i].y) < min:
                    target_x = bot[j].x
                    target_y = bot[j].y
                    min = abs(bot[j].x - build[i].x) + abs(bot[j].y - build[i].y)
            for j in range(len(balloons)):
                if abs(balloons[j].x - build[i].x) + abs(balloons[j].y - build[i].y) < min:
                    target_x = balloons[j].x
                    target_y = balloons[j].y
                    min = abs(balloons[j].x - build[i].x) + abs(balloons[j].y - build[i].y)
            for j in range(len(fembot)):
                if abs(fembot[j].x - build[i].x) + abs(fembot[j].y - build[i].y) < min:
                    target_x = fembot[j].x
                    target_y = fembot[j].y
                    min = abs(fembot[j].x - build[i].x) + abs(fembot[j].y - build[i].y)
            if target_x == -1:
                continue
            elif min > build[i].range:
                continue
            else:
                if abs(king.x-target_x)+abs(king.y-target_y) <= 2 and king_spawned == 1:
                    if king.hitpoints > build[i].dps:
                        king.hitpoints -= build[i].dps
                    else:
                        king.hitpoints = 0
                if abs(queen.x-target_x)+abs(queen.y-target_y) <= 2 and queen_spawned == 1:
                    if queen.hitpoints > build[i].dps:
                        queen.hitpoints -= build[i].dps
                    else:
                        queen.hitpoints = 0
                for j in range(len(bot)):
                    if abs(bot[j].x - target_x )+ abs(bot[j].y -target_y) <=2:
                        if bot[j].hitpoints > build[i].dps:
                            bot[j].hitpoints -= build[i].dps
                        else:
                            bot[j].hitpoints = 0
                for j in range(len(fembot)):
                    if abs(fembot[j].x - target_x )+ abs(fembot[j].y -target_y) <=2:
                        if fembot[j].hitpoints > build[i].dps:
                            fembot[j].hitpoints -= build[i].dps
                        else:
                            fembot[j].hitpoints = 0
                for j in range(len(balloons)):
                    if abs(balloons[j].x - target_x )+ abs(balloons[j].y -target_y) <=2:
                        if balloons[j].hitpoints > build[i].dps:
                            balloons[j].hitpoints -= build[i].dps
                        else:
                            balloons[j].hitpoints = 0
                
                    
        
            
def cannons_attack():
    for i in range(len(build)):
        if build[i].name == "Cannon" and build[i].hitpoints > 0 and king_spawned == 1:
            if abs(king.x - build[i].x) + abs (king.y - build[i].y) <= build[i].range and build[i].attacking == 0 and king.hitpoints > build[i].dps:
                king.hitpoints -= build[i].dps  
                build[i].attacking = 1
            elif king.hitpoints <= build[i].dps and abs(king.x - build[i].x) + abs (king.y - build[i].y) <= build[i].range and build[i].attacking == 0:
                build[i].attacking = 0
                king.hitpoints = 0
                
        if build[i].name == "Cannon" and build[i].hitpoints > 0 and queen_spawned == 1:
            if abs(queen.x - build[i].x) + abs (queen.y - build[i].y) <= build[i].range and build[i].attacking == 0 and queen.hitpoints > build[i].dps:
                queen.hitpoints -= build[i].dps  
                build[i].attacking = 1
            elif queen.hitpoints <= build[i].dps and abs(queen.x - build[i].x) + abs (queen.y - build[i].y) <= build[i].range and build[i].attacking == 0:
                build[i].attacking = 0
                queen.hitpoints = 0
            
    for i in range(len(build)):
        if build[i].name == "Cannon" and build[i].attacking == 0 and build[i].hitpoints > 0:
            for j in range(len(bot)):         
                if abs(bot[j].x - build[i].x) + abs(bot[j].y - build[i].y) <= build[i].range and bot[j].hitpoints > build[i].dps:
                    bot[j].hitpoints -= build[i].dps
                    build[i].attacking = 1
                elif abs(bot[j].x - build[i].x) + abs(bot[j].y - build[i].y) <= build[i].range and bot[j].hitpoints <= build[i].dps:
                    bot[j].hitpoints = 0
                    coordinates[bot[j].x][bot[j].y] = '|-|'
                    build[i].attacking = 0
                    
            for j in range(len(fembot)):         
                if abs(fembot[j].x - build[i].x) + abs(fembot[j].y - build[i].y) <= build[i].range and fembot[j].hitpoints > build[i].dps:
                    fembot[j].hitpoints -= build[i].dps
                    build[i].attacking = 1
                elif abs(fembot[j].x - build[i].x) + abs(fembot[j].y - build[i].y) <= build[i].range and fembot[j].hitpoints <= build[i].dps:
                    fembot[j].hitpoints = 0
                    coordinates[fembot[j].x][fembot[j].y] = '|-|'
                    build[i].attacking = 0
    for i in range(len(build)):
        if build[i].name == "Cannon" and build[i].attacking == 1 and build[i].hitpoints > 0:
            build[i].attacking = 0
            
def spawn_archers(x):
    if len(fembot) == 10:
        return 
    if x == 1:
        t = len(fembot)+1
        name = "archer" + str(t)
        min = 1000000
        for i in range(len(build)):
            if abs(20 - build[i].x) + abs(build[i].y - 5) < min and build[i].hitpoints > 0:
                if build[i].name[0] == 'w':
                    continue
                min = abs(20-build[i].x) + abs(build[i].y -5)
                target_x = build[i].x
                target_y = build[i].y
        bot1 = archers(name,15,1.5,20,5,target_x,target_y,'|S|',2)
        fembot.append(bot1)
        coordinates[20][5] = "|A|"
    if x == 2:
        t =len(fembot)+1
        name = "archer" + str(t)
        min = 1000000
        for i in range(len(build)):
            if abs(5 - build[i].x) + abs(build[i].y - 12) < min and build[i].hitpoints > 0:
                if build[i].name[0] == 'w':
                    continue
                min = abs(5-build[i].x) + abs(build[i].y -12)
                target_x = build[i].x
                target_y = build[i].y
        bot1 = archers(name,15,1.5,5,12,target_x,target_y,'|S|',2)
        fembot.append(bot1)
        coordinates[5][12] = "|A|"
    if x == 3:
        t = len(fembot)+1
        name = "archer" + str(t)
        min = 1000000
        for i in range(len(build)):
            if abs(20 - build[i].x) + abs(build[i].y - 18) < min and build[i].hitpoints > 0:
                if build[i].name[0] == 'w':
                    continue
                min = abs(20-build[i].x) + abs(build[i].y -18)
                target_x = build[i].x
                target_y = build[i].y
        bot1 = archers(name,15,1.5,20,18,target_x,target_y,'|S|',2)
        fembot.append(bot1)
        coordinates[20][18] = "|A|"

def spawn_barbarian(x):
    if len(bot) == 10:
        return
    if x == 1:
        t = len(bot)+1
        name = "barbarian" + str(t)
        min = 1000000
        for i in range(len(build)):
            if abs(20 - build[i].x) + abs(build[i].y - 5) < min and build[i].hitpoints > 0:
                min = abs(20-build[i].x) + abs(build[i].y -5)
                target_x = build[i].x
                target_y = build[i].y
        bot1 = barbarians(name,30,3,20,5,target_x,target_y,'|S|',1)
        bot.append(bot1)
        coordinates[20][5] = "|B|"
    if x == 2:
        t =len(bot)+1
        name = "barbarian" + str(t)
        min = 1000000
        for i in range(len(build)):
            if abs(5 - build[i].x) + abs(build[i].y - 12) < min and build[i].hitpoints > 0:
                min = abs(5-build[i].x) + abs(build[i].y -12)
            target_x = build[i].x
            target_y = build[i].y
        bot1 = barbarians(name,30,3,5,12,target_x,target_y,'|S|',1)
        bot.append(bot1)
        coordinates[5][12] = "|B|"
    if x == 3:
        t = len(bot)+1
        name = "barbarian" + str(t)
        min = 1000000
        for i in range(len(build)):
            if abs(20 - build[i].x) + abs(build[i].y - 18) < min and build[i].hitpoints > 0:
                min = abs(20-build[i].x) + abs(build[i].y -18)
                target_x = build[i].x
                target_y = build[i].y
        bot1 = barbarians(name,30,3,20,18,target_x,target_y,'|S|',1)
        bot.append(bot1)
        coordinates[20][18] = "|B|"
def spawn_balloons(x):
    if len(balloons) == 10:
        return
    
    if x == 1:
        t = len(balloons)+1
        name = "balloon" + str(t)
        min = 1000000
        target_x = -1
        target_y = -1
        for i in range(len(build)):
            if build[i].name[0] == 'w':
                continue
            elif (build[i].name[0] == 'c' or build[i].name[0] == 'W') and build[i].hitpoints > 0:
                if abs(20-build[i].x) + abs(build[i].y - 5) < min:
                    min = abs(20-build[i].x) + abs(build[i].y -5)
                    target_x = build[i].x
                    target_y = build[i].y
        if min == 1000000:
            for i in range(len(build)):
                if build[i].name[0] == 'w':
                    continue
                elif abs(20 - build[i].x) + abs(build[i].y - 5) < min and build[i].hitpoints > 0:
                    min = abs(20-build[i].x) + abs(build[i].y -5)
                    target_x = build[i].x
                    target_y = build[i].y
        bot1 = balloon(name,30,6,20,5,target_x,target_y,'|S|',2)
        balloons.append(bot1)
        coordinates[20][5] = "|O|"
    if x == 2:
        t = len(balloons)+1
        name = "balloon" + str(t)
        min = 1000000
        target_x = -1
        target_y = -1
        for i in range(len(build)):
            if build[i].name[0] == 'w':
                continue
            elif (build[i].name[0] == 'c' or build[i].name[0] == 'W') and build[i].hitpoints > 0:
                if abs(5-build[i].x) + abs(build[i].y - 12) < min:
                    min = abs(5-build[i].x) + abs(build[i].y -12)
                    target_x = build[i].x
                    target_y = build[i].y
        if min == 1000000:
            for i in range(len(build)):
                if build[i].name[0] == 'w':
                    continue
                elif abs(5 - build[i].x) + abs(build[i].y - 12) < min and build[i].hitpoints > 0:
                    min = abs(5-build[i].x) + abs(build[i].y -12)
                    target_x = build[i].x
                    target_y = build[i].y
        bot1 = balloon(name,30,6,5,12,target_x,target_y,'|S|',2)
        balloons.append(bot1)
        coordinates[5][12] = "|O|"
    if x == 3:
        t = len(balloons)+1
        name = "balloon" + str(t)
        min = 1000000
        target_x = -1
        target_y = -1
        for i in range(len(build)):
            if build[i].name[0] == 'w':
                continue
            elif (build[i].name[0] == 'c' or build[i].name[0] == 'W') and build[i].hitpoints > 0:
                if abs(20-build[i].x) + abs(build[i].y - 18) < min:
                    min = abs(20-build[i].x) + abs(build[i].y -18)
                    target_x = build[i].x
                    target_y = build[i].y
        if min == 1000000:
            for i in range(len(build)):
                if build[i].name[0] == 'w':
                    continue
                elif abs(20 - build[i].x) + abs(build[i].y - 18) < min and build[i].hitpoints > 0:
                    min = abs(20-build[i].x) + abs(build[i].y -18)
                    target_x = build[i].x
                    target_y = build[i].y
        bot1 = balloon(name,30,6,20,18,target_x,target_y,'|S|',2)
        balloons.append(bot1)
        coordinates[20][18] = "|O|"
        
       
def move_balloons():
    for j in range(len(balloons)):
        min = 1000000
        balloons[j].target_x = -1
        balloons[j].target_y = -1
        for i in range(len(build)):
            if build[i].name[0] == 'w':
                continue
            elif (build[i].name[0] == 'C' or build[i].name[0] == 'W') and build[i].hitpoints > 0:
                if abs(balloons[j].x-build[i].x) + abs(balloons[j].y - build[i].y) < min:
                    min = abs(balloons[j].x-build[i].x) + abs(build[i].y -balloons[j].y)
                    balloons[j].target_x = build[i].x
                    balloons[j].target_y = build[i].y    
        if min == 1000000:
            for i in range(len(build)):
                if build[i].name[0] == 'w':
                    continue
                elif build[i].name[0] == 'T':
                    if TownHall.hitpoints > 0:
                        if abs(balloons[j].x - build[i].x) + abs(build[i].y - balloons[j].y) < min:
                            min = abs(balloons[j].x-build[i].x) + abs(build[i].y -balloons[j].y)
                            balloons[j].target_x = build[i].x
                            balloons[j].target_y = build[i].y
                elif abs(balloons[j].x - build[i].x) + abs(build[i].y - balloons[j].y) < min and build[i].hitpoints > 0:
                    min = abs(balloons[j].x-build[i].x) + abs(build[i].y-balloons[j].y)
                    balloons[j].target_x = build[i].x
                    balloons[j].target_y = build[i].y   
    g = 0
    h = 0
    for i in range(len(balloons)):
        if balloons[i].target_x == -1:
            continue
        if balloons[i].hitpoints <= 0:
            continue
        if abs(balloons[i].target_x - balloons[i].x) >= 2:
            if balloons[i].target_x - balloons[i].x > 0:
                balloons[i].x += 1*balloons[i].speed
                g = balloons[i].x-1*balloons[i].speed
            else:
                balloons[i].x-=1*balloons[i].speed
                g = balloons[i].x+1*balloons[i].speed
        elif abs(balloons[i].target_x - balloons[i].x) == 1:
            if balloons[i].target_x - balloons[i].x > 0:
                    balloons[i].x += 1
                    g = balloons[i].x-1    
            else:
                balloons[i].x-=1
                g = balloons[i].x+1
        elif abs(balloons[i].target_x - balloons[i].x) == 0:
            g = balloons[i].x
        if abs(balloons[i].target_y - balloons[i].y) >= 2:
            if balloons[i].target_y - balloons[i].y > 0:
                balloons[i].y += 1*balloons[i].speed
                h = balloons[i].y-1*balloons[i].speed 
            else:
                balloons[i].y-=1*balloons[i].speed
                h = balloons[i].y+1*balloons[i].speed
        elif abs(balloons[i].target_y - balloons[i].y) == 1:
            if balloons[i].target_y - balloons[i].y > 0:
                balloons[i].y += 1
                h = balloons[i].y -1 
            else:
                balloons[i].y-=1
                h = balloons[i].y+1
        elif abs(balloons[i].target_y - balloons[i].y) == 0:
            h = balloons[i].y
        if g == balloons[i].x and h == balloons[i].y:
            continue
        coordinates[g][h] = balloons[i].prev
        balloons[i].prev = coordinates[balloons[i].x][balloons[i].y]
                
                   
def move_archers():
    for i in range(len(fembot)):
        if fembot[i].hitpoints <= 0:
            continue
        min = 100000
        for j in range(len(build)):
            if build[j].name[0] == 'w':
                continue
            if build[j].name[0] == 'T':
                if TownHall.hitpoints > 0:
                    if abs(fembot[i].x - build[j].x) + abs(build[j].y - fembot[i].y) < min:
                        min = abs(fembot[i].x-build[j].x) + abs(build[j].y -fembot[i].y)
                        fembot[i].target_x = build[j].x
                        fembot[i].target_y = build[j].y
            elif abs(fembot[i].x - build[j].x) + abs(build[j].y - fembot[i].y) < min and build[j].hitpoints > 0:  
                min = abs(fembot[i].x-build[j].x) + abs(build[j].y -fembot[i].y)
                fembot[i].target_x = build[j].x
                fembot[i].target_y = build[j].y
        g = -1
        h = -1
        if abs(fembot[i].target_y - fembot[i].y) <= 6 and abs(fembot[i].target_x - fembot[i].x) <= 6:
            continue
        else:
            if abs(fembot[i].y - fembot[i].target_y) > abs(fembot[i].x - fembot[i].target_x):
                if fembot[i].y > fembot[i].target_y:
                    if coordinates[fembot[i].x][fembot[i].y-1] == '|W|':
                        deal_with_wall(i,0,-1)
                        continue
                    else:
                        fembot[i].y -=1
                        h = fembot[i].y + 1
                        g = fembot[i].x
                else:
                    if coordinates[fembot[i].x][fembot[i].y+1] == '|W|':
                        deal_with_wall(i,0,1)
                        continue
                    else:
                        fembot[i].y +=1
                        h = fembot[i].y - 1
                        g = fembot[i].x
            else:
                if fembot[i].x > fembot[i].target_x:
                    if coordinates[fembot[i].x-1][fembot[i].y] == '|W|':
                        deal_with_wall(i,-1,0)
                        continue
                    else:
                        fembot[i].x -=1
                        g = fembot[i].x +1
                        h = fembot[i].y
                else:
                    if coordinates[fembot[i].x+1][fembot[i].y] == '|W|':
                        deal_with_wall(i,1,0)
                        continue
                    else:
                        fembot[i].x +=1
                        g = fembot[i].x - 1
                        h = fembot[i].y
            
            coordinates[g][h] = fembot[i].prev
            fembot[i].prev = "|-|"

                         
                    
            
    
         
def move_barbarians():
    for i in range(len(bot)):
        if bot[i].hitpoints <= 0 :
            continue
        min = 10000
        for j in range(len(build)):
            if build[j].name[0] == 'T':
                if TownHall.hitpoints > 0:
                    if abs(bot[i].x - build[j].x) + abs(build[j].y - bot[i].y) < min:
                        min = abs(bot[i].x-build[j].x) + abs(build[j].y -bot[i].y)
                        bot[i].target_x = build[j].x
                        bot[i].target_y = build[j].y
            elif (abs(bot[i].x - build[j].x) + abs(build[j].y - bot[i].y) < min) and build[j].hitpoints > 0:  
                min = abs(bot[i].x-build[j].x) + abs(build[j].y -bot[i].y)
                bot[i].target_x = build[j].x
                bot[i].target_y = build[j].y
        
    g = 0
    h = 0
    for i in range(len(bot)):
        if bot[i].hitpoints <= 0:
            continue
        if abs(bot[i].target_x - bot[i].x) > 1 and abs(bot[i].target_y-bot[i].y) > 1:
            if bot[i].target_x - bot[i].x > 0:
                bot[i].x += 1*bot[i].speed
                g = bot[i].x-1*bot[i].speed
                
            else:
                bot[i].x-=1*bot[i].speed
                g = bot[i].x+1*bot[i].speed

            if bot[i].target_y - bot[i].y > 0:
                bot[i].y += 1*bot[i].speed
                h = bot[i].y-1*bot[i].speed 
    
            else:
                bot[i].y-=1*bot[i].speed
                h = bot[i].y+1*bot[i].speed

        elif abs(bot[i].target_x - bot[i].x) <= 1 and abs(bot[i].target_y - bot[i].y) > 1:
            if bot[i].target_y - bot[i].y > 0:
                bot[i].y += 1*bot[i].speed
                g = bot[i].x
                h = bot[i].y -1*bot[i].speed 
            else:
                bot[i].y-=1*bot[i].speed
                g = bot[i].x
                h = bot[i].y+1*bot[i].speed

        elif abs(bot[i].target_x - bot[i].x) > 1 and abs(bot[i].target_y - bot[i].y) <= 1:
            if bot[i].target_x - bot[i].x > 0:
                bot[i].x += 1*bot[i].speed
                g = bot[i].x-1*bot[i].speed
                h = bot[i].y
            else:
                bot[i].x -= 1*bot[i].speed
                g = bot[i].x+1*bot[i].speed
                h = bot[i].y 
        elif abs(bot[i].target_x - bot[i].x) <= 1 and abs(bot[i].target_y - bot[i].y) <= 1:
            continue  
        coordinates[g][h] = bot[i].prev
        bot[i].prev = "|-|"
           
     
def attack_barbarians():
    for i in range(len(bot)):
        if bot[i].hitpoints <= 0:
            continue
        if abs(bot[i].target_x - bot[i].x) <= 1 and abs(bot[i].target_y - bot[i].y) <= 1:
            for j in range(len(build)):
                if build[j].x == bot[i].target_x and build[j].y == bot[i].target_y:
                    if build[j].name[0] == 'T':
                        if TownHall.hitpoints > bot[i].dps:
                            TownHall.hitpoints -= bot[i].dps
                        else:
                            TownHall.hitpoints = 0  

                    elif build[j].hitpoints > bot[i].dps:
                        build[j].hitpoints -= bot[i].dps
                    else:
                        build[j].hitpoints = 0
                        coordinates[build[j].x][build[j].y] = "|-|"
                        
def attack_balloons():
    for i in range(len(balloons)):
        if balloons[i].hitpoints <= 0:
            continue
        if abs(balloons[i].target_x - balloons[i].x) == 0 and abs(balloons[i].target_y - balloons[i].y) == 0:
            for j in range(len(build)):
                if build[j].x == balloons[i].target_x and build[j].y == balloons[i].target_y:
                    if build[j].name[0] == 'T':
                        if TownHall.hitpoints > balloons[i].dps:
                            TownHall.hitpoints -= balloons[i].dps
                        else:
                            TownHall.hitpoints = 0  

                    elif build[j].hitpoints > balloons[i].dps:
                        build[j].hitpoints -= balloons[i].dps
                    else:
                        build[j].hitpoints = 0
                        coordinates[build[j].x][build[j].y] = "|-|"


def attack_archers():
    for i in range(len(fembot)):
        if fembot[i].hitpoints <= 0:
            continue
        if abs(fembot[i].x - fembot[i].target_x) <= 6 or abs(fembot[i].y - fembot[i].target_y) <= 6:
            for j in range(len(build)):
                if build[j].x == fembot[i].target_x and build[j].y == fembot[i].target_y:
                    if build[j].name[0] == 'T':
                        if TownHall.hitpoints > fembot[i].dps:
                            TownHall.hitpoints -= fembot[i].dps
                        else:
                            TownHall.hitpoints = 0
                    elif build[j].hitpoints > fembot[i].dps:
                        build[j].hitpoints -= fembot[i].dps
                    else:
                        build[j].hitpoints = 0
                        coordinates[build[j].x][build[j].y] = "|-|" 



def heal_spell():
    if king.hitpoints > 0 and king_spawned == 1:
        king.hitpoints *= 1.5
        if king.hitpoints > 100:
            king.hitpoints = 100
    if queen.hitpoints > 0 and queen_spawned == 1:
        queen.hitpoints *= 1.5
        if queen.hitpoints > 100:
            queen.hitpoints = 100
    for i in range(len(bot)):
        if bot[i].hitpoints > 0:
            bot[i].hitpoints *= 1.5
            if bot[i].hitpoints > 30:
                bot[i].hitpoints = 30   
    for i in range(len(fembot)):
            if fembot[i].hitpoints > 0:
                fembot[i].hitpoints *= 1.5
            if fembot[i].hitpoints > 30:
                fembot[i].hitpoints = 30
    for i in range(len(balloons)):
            if balloons[i].hitpoints > 0:
                ballons[i].hitpoints *= 1.5
            if balloons[i].hitpoints > 30:
                balloons[i].hitpoints = 30                       
                         
def rage_spell():
    if king.hitpoints > 0 and king_spawned == 1:
        king.speed *= 2
        king.dps *= 2
    if queen.hitpoints > 0 and queen_spawned == 1:
        queen.speed *= 2
        queen.dps *= 2
    for i in range(len(bot)):
        if bot[i].hitpoints > 0:
            bot[i].speed *=2
            bot[i].dps *=2
    for i in range(len(fembot)):
        if fembot[i].hitpoints > 0:
            fembot[i].speed *=2
            fembot[i].dps *=2
    for i in range(len(balloons)):
        if balloons[i].hitpoints > 0:
            balloons[i].speed *=2
            balloons[i].dps *=2

def Axe_of_king():
    if king_spawned == 0 or king.hitpoints <= 0:
        return
    x = king.x
    y = king.y
    cnt = 0
    for i in range(len(build)):
        if build[i].name[0] != 'T':
            if abs(x-build[i].x)+abs(y-build[i].y) <= 5:
                if build[i].hitpoints > 3:
                    build[i].hitpoints -=3
                else:
                    build[i].hitpoints = 0
                    coordinates[build[i].x][build[i].y] = "|-|"
        else:
            if abs(x- build[i].x) + abs(y-build[i].y) <= 5:
                cnt+=1
    if TownHall.hitpoints > cnt*3:
        TownHall.hitpoints -= cnt*3
    else:
        TownHall.hitpoints = 0
        coordinates[11][11] = "|-|"
        coordinates[11][12] = "|-|"
        coordinates[11][13] = "|-|"
        coordinates[12][11] = "|-|"
        coordinates[12][12] = "|-|"
        coordinates[12][13] = "|-|"
        coordinates[13][11] = "|-|"
        coordinates[13][12] = "|-|"
        coordinates[13][13] = "|-|"
        coordinates[14][11] = "|-|"
        coordinates[14][12] = "|-|"
        coordinates[14][13] = "|-|"

def display():
    grid1 = []
    grid2 = []
    for i in range(n):
        cols1 = []
        cols2 = []
        for j in range(m):
            flag = 0
            flag1 = 0
            flag2 = 0
            for k in range(len(fembot)):
                if fembot[k].hitpoints > 0 and i == fembot[k].x and j == fembot[k].y:
                    coordinates[i][j] = "|A|"
                    if fembot[k].hitpoints >= 7.5:
                        print(Back.GREEN + coordinates[i][j], end="")
                        print(Style.RESET_ALL, end=" ")
                        cols1.append(coordinates[i][j])
                        cols2.append("GREEN")
                        flag2 = 1
                    elif fembot[k].hitpoints >= 3:
                        print(Back.YELLOW + coordinates[i][j], end="")
                        print(Style.RESET_ALL, end=" ")
                        cols1.append(coordinates[i][j])
                        cols2.append("YELLOW")
                        flag2 = 1
                    elif fembot[k].hitpoints > 0:
                        print(Back.RED + coordinates[i][j], end="")
                        print(Style.RESET_ALL, end=" ")
                        cols1.append(coordinates[i][j])
                        cols2.append("RED")
                        flag2 = 1
            for k in range(len(balloons)):
                if balloons[k].hitpoints > 0 and i == balloons[k].x and j == balloons[k].y: 
                    coordinates[i][j] = "|O|"
                    if balloons[k].hitpoints >= 15:
                        print(Back.GREEN + coordinates[i][j], end="")
                        print(Style.RESET_ALL, end=" ")
                        cols1.append(coordinates[i][j])
                        cols2.append("GREEN")
                        flag1 = 1
                    elif balloons[k].hitpoints >= 6:
                        print(Back.YELLOW + coordinates[i][j], end="")
                        print(Style.RESET_ALL, end=" ")
                        cols1.append(coordinates[i][j])
                        cols2.append("YELLOW")
                        flag1 = 1
                    elif balloons[k].hitpoints > 0:
                        print(Back.RED + coordinates[i][j], end="")
                        print(Style.RESET_ALL, end=" ")
                        cols1.append(coordinates[i][j])
                        cols2.append("RED")
                        flag1 = 1
            for k in range(len(bot)):
                if bot[k].hitpoints > 0 and i == bot[k].x and j == bot[k].y: 
                    coordinates[i][j] = "|B|"
                    if bot[k].hitpoints >= 15:
                        print(Back.GREEN + coordinates[i][j], end="")
                        print(Style.RESET_ALL, end=" ")
                        cols1.append(coordinates[i][j])
                        cols2.append("GREEN")
                        flag = 1
                    elif bot[k].hitpoints >= 6:
                        print(Back.YELLOW + coordinates[i][j], end="")
                        print(Style.RESET_ALL, end=" ")
                        cols1.append(coordinates[i][j])
                        cols2.append("YELLOW")
                        flag = 1
                    elif bot[k].hitpoints >0:
                        print(Back.RED + coordinates[i][j], end="")
                        print(Style.RESET_ALL, end=" ")
                        cols1.append(coordinates[i][j])
                        cols2.append("RED")
                        flag = 1
            if coordinates[i][j] == "|T|":
                if TownHall.hitpoints >= 50:
                    print(Back.GREEN + coordinates[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    cols1.append(coordinates[i][j])
                    cols2.append("GREEN")
                elif TownHall.hitpoints >= 20:
                    print(Back.YELLOW + coordinates[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    cols1.append(coordinates[i][j])
                    cols2.append("YELLOW")
                elif TownHall.hitpoints > 0:
                    print(Back.RED + coordinates[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    cols1.append(coordinates[i][j])
                    cols2.append("RED") 
                else: 
                        coordinates[11][11] = "|-|"
                        coordinates[11][12] = "|-|"
                        coordinates[11][13] = "|-|"
                        coordinates[12][11] = "|-|"
                        coordinates[12][12] = "|-|"
                        coordinates[12][13] = "|-|"
                        coordinates[13][11] = "|-|"
                        coordinates[13][12] = "|-|"
                        coordinates[13][13] = "|-|"
                        coordinates[14][11] = "|-|"
                        coordinates[14][12] = "|-|"
                        coordinates[14][13] = "|-|"
                        cols1.append(coordinates[i][j])
                        cols2.append("WHITE")     
            elif coordinates[i][j] == "|H|":
                for k in range(len(build)):
                    if build[k].x == i and build[k].y == j:
                        if build[k].hitpoints >= 25:
                            print(Back.GREEN + coordinates[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("GREEN")
                        elif build[k].hitpoints >= 10:
                            print(Back.YELLOW + coordinates[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("YELLOW")
                        elif build[k].hitpoints > 0:
                            print(Back.RED + coordinates[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("RED")
                        else:
                            coordinates[i][j] = "|-|" 
                            print(coordinates[i][j], end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("WHITE")
  
            elif coordinates[i][j] == "|C|":
                for k in range(len(build)):
                    if build[k].x == i and build[k].y == j:
                        if build[k].hitpoints >= 37.5:
                            print(Back.GREEN + coordinates[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("GREEN")
                        elif build[k].hitpoints >= 15:
                            print(Back.YELLOW + coordinates[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("YELLOW")
                        elif build[k].hitpoints > 0:
                            print(Back.RED + coordinates[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("RED")
                        else: 
                            coordinates[i][j] = "|-|"
                            print(coordinates[i][j], end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("WHITE")
            elif coordinates[i][j] == "|w|":
                for k in range(len(build)):
                    if build[k].x == i and build[k].y == j:
                        if build[k].hitpoints >= 30:
                            print(Back.GREEN + coordinates[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("GREEN")
                        elif build[k].hitpoints >= 12:
                            print(Back.YELLOW + coordinates[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("YELLOW")
                        elif build[k].hitpoints > 0:
                            print(Back.RED + coordinates[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("RED")
                        else: 
                            coordinates[i][j] = "|-|"
                            print(coordinates[i][j], end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("WHITE")
            elif coordinates[i][j] == "|W|":
                for k in range(len(build)):
                    if build[k].x == i and build[k].y == j:
                        if build[k].hitpoints >= 12.5:
                            print(Back.GREEN + coordinates[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("GREEN")
                        elif build[k].hitpoints >= 5:
                            print(Back.YELLOW + coordinates[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("YELLOW")
                        elif build[k].hitpoints > 0:
                            print(Back.RED + coordinates[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("RED")
                        else:
                            coordinates[i][j] = "|-|"
                            print(coordinates[i][j], end=" ")
                            cols1.append(coordinates[i][j])
                            cols2.append("WHITE")
            elif coordinates[i][j] == "|K|":
                if king.hitpoints > 50:
                    print(Back.GREEN + coordinates[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    cols1.append(coordinates[i][j])
                    cols2.append("GREEN")
                elif king.hitpoints > 20:
                    print(Back.YELLOW + coordinates[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    cols1.append(coordinates[i][j])
                    cols2.append("YELLOW")
                elif king.hitpoints > 0:
                    print(Back.RED + coordinates[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    cols1.append(coordinates[i][j])
                    cols2.append("GREEN")
                else:
                    print(king.prev,end = " ")
                    cols1.append(king.prev)
                    cols2.append("WHITE")
            elif coordinates[i][j] == "|Q|":
                if queen.hitpoints > 50:
                    print(Back.GREEN + coordinates[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    cols1.append(coordinates[i][j])
                    cols2.append("GREEN")
                elif queen.hitpoints > 20:
                    print(Back.YELLOW + coordinates[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    cols1.append(coordinates[i][j])
                    cols2.append("YELLOW")
                elif queen.hitpoints > 0:
                    print(Back.RED + coordinates[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    cols1.append(coordinates[i][j])
                    cols2.append("GREEN")
                else:
                    print(queen.prev,end = " ")
                    cols1.append(queen.prev)
                    cols2.append("WHITE")
            else:   
                if flag == 1:
                    continue
                if flag1 == 1:
                    continue
                if flag2 == 1:
                    continue
                if flag == 0 and coordinates[i][j] == "|B|":
                    coordinates[i][j] = "|-|"
                if flag1 == 0 and coordinates[i][j] == "|O|":
                    coordinates[i][j] = "|-|" 
                if flag2 == 0 and coordinates[i][j] == "|A|":
                    coordinates[i][j] = "|-|"
                print(coordinates[i][j], end=" ")
                cols1.append(coordinates[i][j])
                cols2.append("WHITE")  
        print("\n")
        grid1.append(cols1)
        grid2.append(cols2)  
    replay.append(grid1)
    colors.append(grid2)
replay = []
colors = []
h_flag = 0
r_flag = 0
finished = 0

    
while(1):
    p = input_to()
    if p == 'A':
        v = input_to()
        while v == 'A' or v == None:
            v = input_to()
            continue
        if v == '1':
            spawn_archers(1)
        if v == '2':
            spawn_archers(2)
        if v == '3':
            spawn_archers(3) 
    if p == 'B':
        v = input_to()
        while v == 'B' or v == None:
            v = input_to()
            continue
        if v == '1':
            spawn_barbarian(1)
        elif v == '2':
            spawn_barbarian(2)
        elif v == '3':
            spawn_barbarian(3)
    if p == 'O':
        v= input_to()
        while v == 'O' or v == None:
            v= input_to()
            continue
        if v == '1':
            spawn_balloons(1)
        if v == '2':
            spawn_balloons(2)
        if v == '3':
            spawn_balloons(3)
    if (p == 'Q' or p == 'q') and king_spawned == 0 and queen_spawned == 0:
        spawn_queen()
        queen_spawned = 1 
    if (p == 'K' or p == 'k') and king_spawned == 0 and queen_spawned == 0:
        spawn_king()
        king_spawned = 1
    if king_spawned == 1 and (p == 'w' or p == 'W' or p == 'D' or p == 'd' or p == 'a' or p == 'A' or p == 's' or p == 'S'):
        king_movement(p)
        king_last = p.lower() 
    if king_spawned == 1 and p == " ":
        king_attack()
    if queen_spawned == 1 and (p == 'w' or p == 'W' or p == 'D' or p == 'd' or p == 'a' or p == 'A' or p == 's' or p == 'S'):
        queen_movement(p)
        queen_last = p.lower() 
    if queen_spawned == 1 and p == " ":
        queen_attack()
    elif (p == 'H' or p == 'h') and (h_flag == 0):
        heal_spell()
        h_flag = 1
    elif (p == 'R' or p == 'r') and r_flag == 0:
        rage_spell()
        r_flag = 1
    elif (p == 'X' or p == 'x' and king_spawned == 1):
        Axe_of_king()
    
    move_barbarians()
    move_balloons()
    attack_barbarians()
    attack_balloons()
    cannons_attack()
    wizards_attack()
    move_archers()
    move_archers()
    attack_archers()
    display()
    b_flag = 0
    k_flag = 0
    t_flag = 0
    o_flag = 0 
    q_flag = 0
    build_flag = 0
    if TownHall.hitpoints > 0:
        t_flag = 1
    if king.hitpoints > 0:
        k_flag = 1
    if king_spawned == 0:
        k_flag = 1
    if queen_spawned == 0:
        q_flag = 1
    if queen.hitpoints > 0:
        q_flag = 1
    if len(bot) < 10:
        b_flag = 1
    else:
        for i in range(len(bot)):
            if bot[i].hitpoints > 0:
                b_flag = 1
    if len(balloons) < 10:
        o_flag = 1
    else:
        for i in range(len(balloons)):
            if balloons[i].hitpoints > 0:
                o_flag = 1;
                 
    for i in range(len(build)):
        if build[i].name[0] != 'T' and build[i].hitpoints > 0 and (build[i].name[0] != 'w'):
            build_flag = 1
    if (b_flag == 0 and k_flag == 0 and o_flag == 0 and q_flag == 0) and (t_flag == 1 or build_flag == 1):
        finished = 0
        break
    if (t_flag == 0 and build_flag == 0):
        finished = 1
        break  
    if king_spawned == 1:
        king.kingbar(king.hitpoints)    
    if queen_spawned == 1:
        queen.queenbar(queen.hitpoints)
    time.sleep(0.03)
#dir = "./replays"
#cnt = 0
#for path in os.listdir(dir):
    #if os.path.isfile(os.path.join(dir,path)):
       #cnt+=1
#p = "./replays" + "/replay" + str(cnt)+".txt"
#f = open(p,"a+")
#csi = "\u001b["
#red = csi + "41m"
#yellow = csi +"43m"
#green = csi +"42m"
#end = csi + "0m"
# for i in range(len(replay)):
#     for j in range(len(replay[i])):
#         for k in range(len(replay[i][j])):
#             if colors[i][j][k] == "RED":
#                 f.write(red+replay[i][j][k])
#                 f.write(end+" ")
#             elif colors[i][j][k] == "YELLOW":
#                 f.write(yellow+replay[i][j][k])
#                 f.write(end+" ")
#             elif colors[i][j][k] == "GREEN":
#                 f.write(green+replay[i][j][k])
#                 f.write(end+" ")
#             else:
#                 f.write(end+replay[i][j][k])
#                 f.write(" ")
#         f.write("\n")
#     f.write("STOP\n")
# f.close()
if finished == 0:
    print("Defeat!!")
    exit()
else:
    print("Victory!!")
inting = input("Nice! Ready for next level?(Y/N)")
if inting != 'Y':
    exit()

build = []
king_spawned = 0
queen_spawned = 0
coordinates = []
bot = []
fembot = []
balloons = []
TownHall.hitpoints = 100
TownHall1 = TownHall("TownHall", 11,11)
TownHall2 = TownHall("TownHall1", 11,12)
TownHall3 = TownHall("TownHall2", 11,13)
TownHall4 = TownHall("TownHall3", 12,11)
TownHall5 = TownHall("TownHall4", 12,12)
TownHall6 = TownHall("TownHall5", 12,13)
TownHall7 = TownHall("TownHall6", 13,11)
TownHall8 = TownHall("TownHall7", 13,12)
TownHall9 = TownHall("TownHall8", 13,13)
TownHall10 = TownHall("TownHall9", 14,11)
TownHall11 = TownHall("TownHall10", 14,12)
TownHall12 = TownHall("TownHall11", 14,13)



build.append(TownHall1)
build.append(TownHall2)
build.append(TownHall3)
build.append(TownHall4)
build.append(TownHall5)
build.append(TownHall6)
build.append(TownHall7)
build.append(TownHall8)
build.append(TownHall9)
build.append(TownHall10)
build.append(TownHall11)
build.append(TownHall12)

walls = []
huts = []


Tower1 = wizardtower("Wizard",60,16,9,1,1.5,0)
Tower2 = wizardtower("Wizard",60,16,15,1,1.5,0)
Tower3 = wizardtower("Wizard",60,9,9,1,1.5,0)
#Tower4 = wizardtower("Wizard",60,9,15,1,1.5,0)
build.append(Tower1)
build.append(Tower2)
build.append(Tower3)

hut1 = buildings("HUT", 50,2,2)
build.append(hut1)
hut2 = buildings("HUT", 50,0,1)
build.append(hut2)
hut3 = buildings("HUT", 50,1,0)
build.append(hut3)
hut4 = buildings("HUT", 50,1,1)
build.append(hut4)
hut5 = buildings("HUT", 50,3,3)
build.append(hut5)
cannon1 = cannons("Cannon", 75,20,12, 0.5, 5,0)
build.append(cannon1)
cannon2 = cannons("Cannon", 75,12,7, 0.5, 5,0)
build.append(cannon2)
cannon3 = cannons("Cannon", 75,12,16, 0.5, 5,0)
build.append(cannon3)
#cannon4 = cannons("Cannon", 75,8,12, 0.5, 5,0)
#build.append(cannon4)
#cannon5 = cannons("Cannon", 75,0,0, 0.5, 5,0)
#build.append(cannon5)
n = 26
m = 26

king_last = ''
queen_last = ''
prev = "|-|"
king = King("King", 100, 5, 20, 15, prev,1)
queen = Queen("Queen",100,5,20,15,prev,1)                     
        
for i in range(n):
    cols = []
    cnt = 0
    for j in range(m):
        if i >= 11 and i <= 14 and j >= 11 and j <= 13:
            cols.append('|T|')
        elif (i == 2 and j == 2) or (i == 0 and j == 1) or (i == 1 and j == 0) or (i == 1 and j == 1) or (i == 3 and j == 3):
            cols.append('|H|')
        elif (i == 20 and j == 5) or (i == 5 and j == 12) or (i == 20 and j == 18):
            cols.append('|S|')
        elif (i == 20 and j == 12) or (i == 12 and j == 7) or (i == 12 and j == 16):
            cols.append('|C|')
        elif (i == 10 and j >= 10 and j <= 14) or (i == 15 and j > 10 and j <= 14) or (j == 10 and i > 10 and i <= 15) or (j == 14 and i > 10 and i <= 15) or (i == 0 and j == 2) or (i == 1 and j == 2) or (i == 2 and j == 1) or (i == 2 and j == 0):
            cnt += 1
            wall = "wall"
            wall += str(cnt)
            build.append(buildings(wall,25,i,j))
            cols.append('|W|')
        elif (i == 16 and (j == 9 or j== 15)) or (i == 9 and (j == 9)):
            cols.append('|w|')
        else:
            cols.append('|-|')
    coordinates.append(cols)
replay = []
colors = []
h_flag = 0
r_flag = 0
finished = 0

while(1):
    p = input_to()
    if p == 'A':
        v = input_to()
        while v == 'A' or v == None:
            v = input_to()
            continue
        if v == '1':
            spawn_archers(1)
        if v == '2':
            spawn_archers(2)
        if v == '3':
            spawn_archers(3) 
    if p == 'B':
        v = input_to()
        while v == 'B' or v == None:
            v = input_to()
            continue
        if v == '1':
            spawn_barbarian(1)
        elif v == '2':
            spawn_barbarian(2)
        elif v == '3':
            spawn_barbarian(3)
    if p == 'O':
        v= input_to()
        while v == 'O' or v == None:
            v= input_to()
            continue
        if v == '1':
            spawn_balloons(1)
        if v == '2':
            spawn_balloons(2)
        if v == '3':
            spawn_balloons(3)
    if (p == 'Q' or p == 'q') and king_spawned == 0 and queen_spawned == 0:
        spawn_queen()
        queen_spawned = 1 
    if (p == 'K' or p == 'k') and king_spawned == 0 and queen_spawned == 0:
        spawn_king()
        king_spawned = 1
    if king_spawned == 1 and (p == 'w' or p == 'W' or p == 'D' or p == 'd' or p == 'a' or p == 'A' or p == 's' or p == 'S'):
        king_movement(p)
        king_last = p.lower() 
    if king_spawned == 1 and p == " ":
        king_attack()
    if queen_spawned == 1 and (p == 'w' or p == 'W' or p == 'D' or p == 'd' or p == 'a' or p == 'A' or p == 's' or p == 'S'):
        queen_movement(p)
        queen_last = p.lower() 
    if queen_spawned == 1 and p == " ":
        queen_attack()
    elif (p == 'H' or p == 'h') and (h_flag == 0):
        heal_spell()
        h_flag = 1
    elif (p == 'R' or p == 'r') and r_flag == 0:
        rage_spell()
        r_flag = 1
    elif (p == 'X' or p == 'x' and king_spawned == 1):
        Axe_of_king()
    
    move_barbarians()
    move_balloons()
    attack_barbarians()
    attack_balloons()
    cannons_attack()
    wizards_attack()
    move_archers()
    move_archers()
    attack_archers()
    display()
    b_flag = 0
    k_flag = 0
    t_flag = 0
    o_flag = 0 
    q_flag = 0
    build_flag = 0
    if TownHall.hitpoints > 0:
        t_flag = 1
    if king.hitpoints > 0:
        k_flag = 1
    if king_spawned == 0:
        k_flag = 1
    if queen_spawned == 0:
        q_flag = 1
    if queen.hitpoints > 0:
        q_flag = 1
    if len(bot) < 10:
        b_flag = 1
    else:
        for i in range(len(bot)):
            if bot[i].hitpoints > 0:
                b_flag = 1
    if len(balloons) < 10:
        o_flag = 1
    else:
        for i in range(len(balloons)):
            if balloons[i].hitpoints > 0:
                o_flag = 1;
                 
    for i in range(len(build)):
        if build[i].name[0] != 'T' and build[i].hitpoints > 0 and (build[i].name[0] != 'w'):
            build_flag = 1
    if (b_flag == 0 and k_flag == 0 and o_flag == 0 and q_flag == 0) and (t_flag == 1 or build_flag == 1):
        finished = 0
        break
    if (t_flag == 0 and build_flag == 0):
        finished = 1
        break  
    if king_spawned == 1:
        king.kingbar(king.hitpoints)    
    if queen_spawned == 1:
        queen.queenbar(queen.hitpoints)
    time.sleep(0.03)

if finished == 0:
    print("Defeat!!")
    exit()
else:
    print("Victory!!")
inting = input("Nice! Ready for next level?(Y/N)")
if inting != 'Y':
    exit()

build = []
king_spawned = 0
queen_spawned = 0
coordinates = []
bot = []
fembot = []
balloons = []
TownHall.hitpoints = 100
TownHall1 = TownHall("TownHall", 11,11)
TownHall2 = TownHall("TownHall1", 11,12)
TownHall3 = TownHall("TownHall2", 11,13)
TownHall4 = TownHall("TownHall3", 12,11)
TownHall5 = TownHall("TownHall4", 12,12)
TownHall6 = TownHall("TownHall5", 12,13)
TownHall7 = TownHall("TownHall6", 13,11)
TownHall8 = TownHall("TownHall7", 13,12)
TownHall9 = TownHall("TownHall8", 13,13)
TownHall10 = TownHall("TownHall9", 14,11)
TownHall11 = TownHall("TownHall10", 14,12)
TownHall12 = TownHall("TownHall11", 14,13)



build.append(TownHall1)
build.append(TownHall2)
build.append(TownHall3)
build.append(TownHall4)
build.append(TownHall5)
build.append(TownHall6)
build.append(TownHall7)
build.append(TownHall8)
build.append(TownHall9)
build.append(TownHall10)
build.append(TownHall11)
build.append(TownHall12)

walls = []
huts = []


Tower1 = wizardtower("Wizard",60,16,9,1,1.5,0)
Tower2 = wizardtower("Wizard",60,16,15,1,1.5,0)
Tower3 = wizardtower("Wizard",60,9,9,1,1.5,0)
Tower4 = wizardtower("Wizard",60,9,15,1,1.5,0)
build.append(Tower1)
build.append(Tower2)
build.append(Tower3)
build.append(Tower4)

hut1 = buildings("HUT", 50,2,2)
build.append(hut1)
hut2 = buildings("HUT", 50,0,1)
build.append(hut2)
hut3 = buildings("HUT", 50,1,0)
build.append(hut3)
hut4 = buildings("HUT", 50,1,1)
build.append(hut4)
hut5 = buildings("HUT", 50,3,3)
build.append(hut5)
cannon1 = cannons("Cannon", 75,20,12, 0.5, 5,0)
build.append(cannon1)
cannon2 = cannons("Cannon", 75,12,7, 0.5, 5,0)
build.append(cannon2)
cannon3 = cannons("Cannon", 75,12,16, 0.5, 5,0)
build.append(cannon3)
#cannon4 = cannons("Cannon", 75,8,12, 0.5, 5,0)
#build.append(cannon4)
cannon5 = cannons("Cannon", 75,0,0, 0.5, 5,0)
build.append(cannon5)
n = 26
m = 26

king_last = ''
queen_last = ''
prev = "|-|"
king = King("King", 100, 5, 20, 15, prev,1)
queen = Queen("Queen",100,5,20,15,prev,1)                     
        
for i in range(n):
    cols = []
    cnt = 0
    for j in range(m):
        if i >= 11 and i <= 14 and j >= 11 and j <= 13:
            cols.append('|T|')
        elif (i == 2 and j == 2) or (i == 0 and j == 1) or (i == 1 and j == 0) or (i == 1 and j == 1) or (i == 3 and j == 3):
            cols.append('|H|')
        elif (i == 20 and j == 5) or (i == 5 and j == 12) or (i == 20 and j == 18):
            cols.append('|S|')
        elif (i == 20 and j == 12) or (i == 12 and j == 7) or (i == 12 and j == 16) or (i ==0 and j == 0):
            cols.append('|C|')
        elif (i == 10 and j >= 10 and j <= 14) or (i == 15 and j > 10 and j <= 14) or (j == 10 and i > 10 and i <= 15) or (j == 14 and i > 10 and i <= 15) or (i == 0 and j == 2) or (i == 1 and j == 2) or (i == 2 and j == 1) or (i == 2 and j == 0):
            cnt += 1
            wall = "wall"
            wall += str(cnt)
            build.append(buildings(wall,25,i,j))
            cols.append('|W|')
        elif (i == 16 and (j == 9 or j== 15)) or (i == 9 and (j == 9 or j == 15)):
            cols.append('|w|')
        else:
            cols.append('|-|')
    coordinates.append(cols)
replay = []
colors = []
h_flag = 0
r_flag = 0
finished = 0

while(1):
    p = input_to()
    if p == 'A':
        v = input_to()
        while v == 'A' or v == None:
            v = input_to()
            continue
        if v == '1':
            spawn_archers(1)
        if v == '2':
            spawn_archers(2)
        if v == '3':
            spawn_archers(3) 
    if p == 'B':
        v = input_to()
        while v == 'B' or v == None:
            v = input_to()
            continue
        if v == '1':
            spawn_barbarian(1)
        elif v == '2':
            spawn_barbarian(2)
        elif v == '3':
            spawn_barbarian(3)
    if p == 'O':
        v= input_to()
        while v == 'O' or v == None:
            v= input_to()
            continue
        if v == '1':
            spawn_balloons(1)
        if v == '2':
            spawn_balloons(2)
        if v == '3':
            spawn_balloons(3)
    if (p == 'Q' or p == 'q') and king_spawned == 0 and queen_spawned == 0:
        spawn_queen()
        queen_spawned = 1 
    if (p == 'K' or p == 'k') and king_spawned == 0 and queen_spawned == 0:
        spawn_king()
        king_spawned = 1
    if king_spawned == 1 and (p == 'w' or p == 'W' or p == 'D' or p == 'd' or p == 'a' or p == 'A' or p == 's' or p == 'S'):
        king_movement(p)
        king_last = p.lower() 
    if king_spawned == 1 and p == " ":
        king_attack()
    if queen_spawned == 1 and (p == 'w' or p == 'W' or p == 'D' or p == 'd' or p == 'a' or p == 'A' or p == 's' or p == 'S'):
        queen_movement(p)
        queen_last = p.lower() 
    if queen_spawned == 1 and p == " ":
        queen_attack()
    elif (p == 'H' or p == 'h') and (h_flag == 0):
        heal_spell()
        h_flag = 1
    elif (p == 'R' or p == 'r') and r_flag == 0:
        rage_spell()
        r_flag = 1
    elif (p == 'X' or p == 'x' and king_spawned == 1):
        Axe_of_king()
    
    move_barbarians()
    move_balloons()
    attack_barbarians()
    attack_balloons()
    cannons_attack()
    wizards_attack()
    move_archers()
    move_archers()
    attack_archers()
    display()
    b_flag = 0
    k_flag = 0
    t_flag = 0
    o_flag = 0 
    q_flag = 0
    build_flag = 0
    if TownHall.hitpoints > 0:
        t_flag = 1
    if king.hitpoints > 0:
        k_flag = 1
    if king_spawned == 0:
        k_flag = 1
    if queen_spawned == 0:
        q_flag = 1
    if queen.hitpoints > 0:
        q_flag = 1
    if len(bot) < 10:
        b_flag = 1
    else:
        for i in range(len(bot)):
            if bot[i].hitpoints > 0:
                b_flag = 1
    if len(balloons) < 10:
        o_flag = 1
    else:
        for i in range(len(balloons)):
            if balloons[i].hitpoints > 0:
                o_flag = 1;
                 
    for i in range(len(build)):
        if build[i].name[0] != 'T' and build[i].hitpoints > 0 and (build[i].name[0] != 'w'):
            build_flag = 1
    if (b_flag == 0 and k_flag == 0 and o_flag == 0 and q_flag == 0) and (t_flag == 1 or build_flag == 1):
        finished = 0
        break
    if (t_flag == 0 and build_flag == 0):
        finished = 1
        break  
    if king_spawned == 1:
        king.kingbar(king.hitpoints)    
    if queen_spawned == 1:
        queen.queenbar(queen.hitpoints)
    time.sleep(0.03)


if finished == 0:
    print("Defeat!!")
else:
    print("Well Done! You have defeated all the levels")
print("BYE!!!")
    
#f.close()
