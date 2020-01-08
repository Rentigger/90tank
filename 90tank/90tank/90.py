import pygame
import sys
import math
import Paodan
import enemy
import copy
import random
from pygame.locals import *

screen=pygame.display.set_mode([23*26+100,23*26])

playerpos=[23*8,23*24]
wallplace=[]
paolist=[]
boomlist=[]
enemylist=[]

bird = pygame.image.load('90/bird.jpg').convert_alpha()
ruinedbird = pygame.image.load('90/ruinedbird.jpg').convert_alpha()
f1=pygame.image.load('90/f1.jpg').convert_alpha()
f2=pygame.image.load('90/f2.jpg').convert_alpha()
life=pygame.image.load('90/life.png').convert_alpha()
enemybf00=pygame.image.load('90/enemybf00.png').convert_alpha()
enemybf01=pygame.image.load('90/enemybf01.png').convert_alpha()
enemybl00=pygame.image.load('90/enemybl00.png').convert_alpha()
enemybl01=pygame.image.load('90/enemybl01.png').convert_alpha()
enemybb00=pygame.image.load('90/enemybb00.png').convert_alpha()
enemybb01=pygame.image.load('90/enemybb01.png').convert_alpha()
enemybr00=pygame.image.load('90/enemybr00.png').convert_alpha()
enemybr01=pygame.image.load('90/enemybr01.png').convert_alpha()
enemyb0=[enemybf00,enemybf01,enemybl00,enemybl01,enemybb00,enemybb01,enemybr00,enemybr01]
enemycf00=pygame.image.load('90/enemycf00.png').convert_alpha()
enemycf01=pygame.image.load('90/enemycf01.png').convert_alpha()
enemycl00=pygame.image.load('90/enemycl00.png').convert_alpha()
enemycl01=pygame.image.load('90/enemycl01.png').convert_alpha()
enemycb00=pygame.image.load('90/enemycb00.png').convert_alpha()
enemycb01=pygame.image.load('90/enemycb01.png').convert_alpha()
enemycr00=pygame.image.load('90/enemycr00.png').convert_alpha()
enemycr01=pygame.image.load('90/enemycr01.png').convert_alpha()
enemyc0=[enemycf00,enemycf01,enemycl00,enemycl01,enemycb00,enemycb01,enemycr00,enemycr01]
enemydf00=pygame.image.load('90/enemydf00.png').convert_alpha()
enemydf01=pygame.image.load('90/enemydf01.png').convert_alpha()
enemydl00=pygame.image.load('90/enemydl00.png').convert_alpha()
enemydl01=pygame.image.load('90/enemydl01.png').convert_alpha()
enemydb00=pygame.image.load('90/enemydb00.png').convert_alpha()
enemydb01=pygame.image.load('90/enemydb01.png').convert_alpha()
enemydr00=pygame.image.load('90/enemydr00.png').convert_alpha()
enemydr01=pygame.image.load('90/enemydr01.png').convert_alpha()
enemyd0=[enemydf00,enemydf01,enemydl00,enemydl01,enemydb00,enemydb01,enemydr00,enemydr01]
enemydf10=pygame.image.load('90/enemydf10.png').convert_alpha()
enemydf11=pygame.image.load('90/enemydf11.png').convert_alpha()
enemydl10=pygame.image.load('90/enemydl10.png').convert_alpha()
enemydl11=pygame.image.load('90/enemydl11.png').convert_alpha()
enemydb10=pygame.image.load('90/enemydb10.png').convert_alpha()
enemydb11=pygame.image.load('90/enemydb11.png').convert_alpha()
enemydr10=pygame.image.load('90/enemydr10.png').convert_alpha()
enemydr11=pygame.image.load('90/enemydr11.png').convert_alpha()
enemyd1=[enemydf10,enemydf11,enemydl10,enemydl11,enemydb10,enemydb11,enemydr10,enemydr11]
enemydf30=pygame.image.load('90/enemydf30.png').convert_alpha()
enemydf31=pygame.image.load('90/enemydf31.png').convert_alpha()
enemydl30=pygame.image.load('90/enemydl30.png').convert_alpha()
enemydl31=pygame.image.load('90/enemydl31.png').convert_alpha()
enemydb30=pygame.image.load('90/enemydb30.png').convert_alpha()
enemydb31=pygame.image.load('90/enemydb31.png').convert_alpha()
enemydr30=pygame.image.load('90/enemydr30.png').convert_alpha()
enemydr31=pygame.image.load('90/enemydr31.png').convert_alpha()
enemyd3=[enemydf30,enemydf31,enemydl30,enemydl31,enemydb30,enemydb31,enemydr30,enemydr31]
enemykindlist=[[enemyb0],[enemyc0],[enemyd0,enemyd1,enemyd3]]
over=pygame.image.load('90/over.png').convert_alpha()
player0=pygame.image.load('90/a.png').convert_alpha()
player1=pygame.image.load('90/b.png').convert_alpha()
player2=pygame.image.load('90/al.png').convert_alpha()
player3=pygame.image.load('90/bl.png').convert_alpha()
player4=pygame.image.load('90/ab.png').convert_alpha()
player5=pygame.image.load('90/bb.png').convert_alpha()
player6=pygame.image.load('90/ar.png').convert_alpha()
player7=pygame.image.load('90/br.png').convert_alpha()
pao=pygame.image.load('90/pao.jpg').convert_alpha()
Boom=pygame.image.load('90/boom.png').convert_alpha()
wood=pygame.image.load('90/wood.jpg').convert_alpha()
ice=pygame.image.load('90/ice.jpg').convert_alpha()
eternalice=pygame.image.load('90/ice.jpg').convert_alpha()


pygame.mixer.init()
'''pygame.mixer.music.load("CLIFF EDGE - Endless Tears.mp3")
pygame.mixer.music.set_volume(0.5) 
pygame.mixer.music.play()'''

begin_voice = pygame.mixer.Sound("begin.wav")
begin_voice.set_volume(0.5) 
begin_voice.play()

boom_voice = pygame.mixer.Sound("boom.wav")
boom_voice.set_volume(0.5)

dead_voice = pygame.mixer.Sound("dead.wav")
dead_voice.set_volume(0.5) 

ending_voice = pygame.mixer.Sound("ending.wav")
ending_voice.set_volume(0.5)
ending_voice_flag=True

reduction_voice = pygame.mixer.Sound("reduction.wav")
reduction_voice.set_volume(0.5)



playerlist=[player0,player1,player2,player3,player4,player5,player6,player7]
walltype=[wood,ice,eternalice]


enemynum=3
blood=4
mf=0
press=False
Bird=True
lspawnpoint=600
mspawnpoint=600
rspawnpoint=600
Direction=0 #0meansfront 2meansbehind 4meansleft 6meansright
def refresh():
    global lspawnpoint
    global mspawnpoint
    global rspawnpoint
    global ending_voice_flag
    boom()
    screen.fill(0)
    for i in range(blood-1):
        screen.blit(life, [23*27,23*10+i*46])
    for i in wallplace:
        if i[1]<=3:
            screen.blit(walltype[i[1]],[i[0][0]*23,i[0][1]*23])
        
    if Bird:
        screen.blit(bird,[23*12,23*24])
    else:
        screen.blit(ruinedbird,[23*12,23*24])
    screen.blit(playerlist[Direction+mf%2],playerpos)
    if lspawnpoint>0:
        lspawnpoint-=1
    if mspawnpoint>0:
        mspawnpoint-=1
    if rspawnpoint>0:
        rspawnpoint-=1
    if lspawnpoint>350:
        if lspawnpoint//15%2:
            screen.blit(f1,[0,0])
        else:
            screen.blit(f2,[0,0])
    if mspawnpoint>350:
        if mspawnpoint//15%2:
            screen.blit(f1,[23*12,0])
        else:
            screen.blit(f2,[23*12,0])
    if rspawnpoint>350:
        if rspawnpoint//15%2:
            screen.blit(f1,[23*24,0])
        else:
            screen.blit(f2,[23*24,0])
    for i in paolist:
        screen.blit(pao,i.paopos)
        if   i.Direction==0:
            i.paopos[1]-=2    
            
        elif i.Direction==2:
            i.paopos[0]-=2
            
        elif i.Direction==4:
            i.paopos[1]+=2
            
        elif i.Direction==6:
            i.paopos[0]+=2
            
    for i in boomlist:
        screen.blit(Boom,i[0])
    
    

    for i in enemylist:
        screen.blit(enemykindlist[i.Type][i.blood-1][i.Direction+mf%2],i.enemypos)
    
    pygame.time.delay(1)

    if blood==0 or Bird == False:
        if ending_voice_flag:
            ending_voice.play()
            ending_voice_flag=False
        screen.blit(over,[23*7,23*9])
        

def playergif():
    global mf
    mf+=1


clock = 0
def enemymove():
    global clock
    for i in enemylist:
        point = False
        flag = False
        if   i.Direction==0 and notwallup(i.enemypos,0) and notwallup(i.enemypos,1) and notwallup(i.enemypos,2) and notwallup(i.enemypos,4):
            for j in enemylist:
                if i.enemypos!=j.enemypos and 0<i.enemypos[1]-j.enemypos[1]<=46 and abs(j.enemypos[0]-i.enemypos[0])<=46: 
                    point=True
            if point!=True:
                i.enemypos[1]-=i.speed
                flag = True
        
        elif i.Direction==2 and notwallleft(i.enemypos,0) and notwallleft(i.enemypos,1) and notwallleft(i.enemypos,2) and notwallleft(i.enemypos,4):
            for j in enemylist:
                if i.enemypos!=j.enemypos and 0<i.enemypos[0]-j.enemypos[0]<=46 and abs(j.enemypos[1]-i.enemypos[1])<=46:
                    i.enemypos[0]-j.enemypos[0]
                    point=True
            if point!=True:
                i.enemypos[0]-=i.speed
                flag = True
            
        elif i.Direction==4 and notwalldown(i.enemypos,0) and notwalldown(i.enemypos,1) and notwalldown(i.enemypos,2) and notwalldown(i.enemypos,4):
            for j in enemylist:
                if i.enemypos!=j.enemypos and 0<j.enemypos[1]-i.enemypos[1]<=46 and abs(j.enemypos[0]-i.enemypos[0])<=46:
                    point=True
            if point!=True:
                i.enemypos[1]+=i.speed
                flag = True
            
        elif i.Direction==6 and notwallright(i.enemypos,0) and notwallright(i.enemypos,1) and notwallright(i.enemypos,2) and notwallright(i.enemypos,4):
            for j in enemylist:
                if i.enemypos!=j.enemypos and 0<j.enemypos[0]-i.enemypos[0]<=46 and abs(j.enemypos[1]-i.enemypos[1])<=46:
                    point=True
            if point!=True:
                i.enemypos[0]+=i.speed
                flag = True

        if i.enemypos[0]%23==0 and i.enemypos[1]%23==0:
            if random.randint(0,10)%5==0:
                if clock<=0:
                    i.Direction = random.randint(0,3)*2
                    clock=50
            flag = True

        if flag==False:
            if i.Direction == 0:
                i.enemypos[1]+=i.speed
                Direction = 4
            if i.Direction == 2:
                i.enemypos[0]+=i.speed
                i.Direction = 6
            if i.Direction == 4:
                i.enemypos[1]-=i.speed
                i.Direction = 0
            if i.Direction == 6:
                i.enemypos[0]-=i.speed
                i.Direction = 2
            
    
    
def setenemy():
    global lspawnpoint
    global mspawnpoint
    global rspawnpoint
    if lspawnpoint==350:
        enemylist.append(enemy.Enemy([0,0],6,random.randint(0,2)%3,0,0.5,0))
        enemylist[-1].blood=len(enemykindlist[enemylist[-1].Type])
        lspawnpoint-=1
        if enemylist[-1].Type==1:
            enemylist[-1].speed=1
    if mspawnpoint==350:
        enemylist.append(enemy.Enemy([23*12,0],2,(random.randint(0,2)+1)%3,0,0.5,0))
        enemylist[-1].blood=len(enemykindlist[enemylist[-1].Type])
        mspawnpoint-=1
        if enemylist[-1].Type==1:
            enemylist[-1].speed=1
    if rspawnpoint==350:
        enemylist.append(enemy.Enemy([23*24,0],4,(random.randint(0,2)+2)%3,0,0.5,0))
        enemylist[-1].blood=len(enemykindlist[enemylist[-1].Type])
        rspawnpoint-=1
        if enemylist[-1].Type==1:
            enemylist[-1].speed=1

    
    

def setwall(x0 ,y0, x1,y1,types):
    for i in range(y0,y1+1):
        for j in range(x0,x1+1):
            wallplace.append([[j,i],types])
def setpao(Direction,pos):
    if Direction==0:
        return [pos[0]+18,pos[1]]
    elif Direction==2:
        return [pos[0]-5,pos[1]+18]
    elif Direction==4:
        return [pos[0]+18,pos[1]+46]
    elif Direction==6:
        return [pos[0]+41,pos[1]+18]

'''def deleteenemy(paopos):
    F=True
    global enemynum
    for i in enemylist:
        print(i.enemypos)
        print(paopos)
        print('-----')
        if -23<paopos[0]-i.enemypos[0]<=46 and -23<paopos[1]-i.enemypos[1]<=46:
            if(i.blood==1):
                print("ddd")
                enemylist.remove(i)
                enemynum-=1
            else:
                i.blood-=1
            F=False
            break
    if F:
        print(wallplace)
        input()'''

def enemyattack():
    for i in enemylist:
        if i.frequency!=0:
            i.frequency-=1
        if i.enemypos[0]%23==0 and i.enemypos[1]%23==0 and i.frequency==0:
            if random.randint(0,1)==0:
                 paolist.append(Paodan.Pao(setpao(i.Direction,i.enemypos),i.Direction,1))
                 i.frequency=150


def boom():
    global enemynum
    global playerpos
    global blood
    global Bird
    
    for i in boomlist:
        if i[1]==0:
            boomlist.remove(i)
        else:
            i[1]-=1

    
    for i in paolist:
        flag=False


        if i.source == 0:
            for j in enemylist:
                if -23<i.paopos[0]-j.enemypos[0]<=46 and -23<i.paopos[1]-j.enemypos[1]<=46:          
                    if(j.blood==1):
                        boom_voice.play() 
                        enemylist.remove(j)
                        enemynum-=1
                    else:
                        reduction_voice.play()
                        j.blood-=1
                    flag = True
                    break
        else:
            
            if -23<i.paopos[0]-playerpos[0]<=46 and -23<i.paopos[1]-playerpos[1]<=46:
                if ending_voice_flag:
                    
                    blood-=1
                boomlist.append([[i.paopos[0]-9,i.paopos[1]-14],5])
                if i in paolist:
                    paolist.remove(i)
                if blood!=0:
                    dead_voice.play()
                    playerpos=[23*8,23*24]


        for j in paolist:
            if abs(i.paopos[0]-j.paopos[0])<=23 and abs(i.paopos[1]-j.paopos[1])<=23 and i.source!=j.source:
                boomlist.append([[i.paopos[0]-9,i.paopos[1]-14],5])
                paolist.remove(i)
                paolist.remove(j)

        #print(i.paopos)   
        if 11.5*23<=i.paopos[0]<=14*23 and 23.5*23<=i.paopos[1]<=26*23:
            Bird=False
            boomlist.append([[i.paopos[0]-9,i.paopos[1]-14],5])
            if i in paolist:
                paolist.remove(i)
            break
            
            
        if   i.Direction==0:  
            if [[i.paopos[0]//23,math.ceil(i.paopos[1]/23)-1],0] in wallplace:
                flag=True
                wallplace.remove([[i.paopos[0]//23,math.ceil(i.paopos[1]/23)-1],0])
            if [[i.paopos[0]//23+1,math.ceil(i.paopos[1]/23)-1],0] in wallplace:
                flag=True
                wallplace.remove([[i.paopos[0]//23+1,math.ceil(i.paopos[1]/23)-1],0])
            if [[i.paopos[0]//23,math.ceil(i.paopos[1]/23)-1],1] in wallplace or [[i.paopos[0]//23,math.ceil(i.paopos[1]/23)-1],2] in wallplace:
                flag=True
            if [[i.paopos[0]//23+1,math.ceil(i.paopos[1]/23)-1],1] in wallplace or [[i.paopos[0]//23+1,math.ceil(i.paopos[1]/23)-1],2] in wallplace:
                flag=True
                
            if flag:
                boomlist.append([[i.paopos[0]-9,i.paopos[1]-14],5])
                if i in paolist:
                    paolist.remove(i)

        elif   i.Direction==2:
            if [[math.ceil(i.paopos[0]/23)-1,i.paopos[1]//23],0]in wallplace:
                flag=True
                wallplace.remove([[math.ceil(i.paopos[0]/23)-1,i.paopos[1]//23],0])
            if [[math.ceil(i.paopos[0]/23)-1,i.paopos[1]//23+1],0]in wallplace:
                flag=True
                wallplace.remove([[math.ceil(i.paopos[0]/23)-1,i.paopos[1]//23+1],0])
            if [[math.ceil(i.paopos[0]/23)-1,i.paopos[1]//23],1]in wallplace or [[math.ceil(i.paopos[0]/23)-1,i.paopos[1]//23],2]in wallplace:
                flag=True
            if [[math.ceil(i.paopos[0]/23)-1,i.paopos[1]//23+1],1]in wallplace or [[math.ceil(i.paopos[0]/23)-1,i.paopos[1]//23+1],2]in wallplace:
                flag=True
            if flag:
                boomlist.append([[i.paopos[0]-14,i.paopos[1]-9],5])
                if i in paolist:
                    paolist.remove(i)

        elif   i.Direction==4:
            if [[i.paopos[0]//23,(i.paopos[1]//23)],0] in wallplace:
                flag=True
                wallplace.remove([[i.paopos[0]//23,(i.paopos[1]//23)],0])
            if [[i.paopos[0]//23+1,(i.paopos[1]//23)],0] in wallplace:
                flag=True
                wallplace.remove([[i.paopos[0]//23+1,(i.paopos[1]//23)],0])
            if [[i.paopos[0]//23,(i.paopos[1]//23)],1] in wallplace or [[i.paopos[0]//23,(i.paopos[1]//23)],2] in wallplace:
                flag=True
            if [[i.paopos[0]//23+1,(i.paopos[1]//23)],1] in wallplace or [[i.paopos[0]//23+1,(i.paopos[1]//23)],2] in wallplace:
                flag=True
            if flag:
                boomlist.append([[i.paopos[0]-9,i.paopos[1]-14],5])
                if i in paolist:
                    paolist.remove(i)

        elif   i.Direction==6:
            if [[(i.paopos[0]//23),i.paopos[1]//23],0] in wallplace:
                flag=True
                wallplace.remove([[(i.paopos[0]//23),i.paopos[1]//23],0])
            if [[(i.paopos[0]//23),i.paopos[1]//23+1],0] in wallplace:
                flag=True
                wallplace.remove([[(i.paopos[0]//23),i.paopos[1]//23+1],0])
            if [[(i.paopos[0]//23),i.paopos[1]//23],1] in wallplace or [[(i.paopos[0]//23),i.paopos[1]//23],2] in wallplace:
                flag=True
            if [[(i.paopos[0]//23),i.paopos[1]//23+1],1] in wallplace or [[(i.paopos[0]//23),i.paopos[1]//23+1],2] in wallplace:
                flag=True
            if flag:
                boomlist.append([[i.paopos[0]-14,i.paopos[1]-9],5])
                if i in paolist:
                    paolist.remove(i)

def  notwallup(pos,Type):
    if [[pos[0]//23,math.ceil(pos[1]/23)-1],Type] not in wallplace and [[pos[0]//23+1,math.ceil(pos[1]/23)-1],Type] not in wallplace:
        return True
    else:
        return False
def  notwallleft(pos,Type):
    if [[math.ceil(pos[0]/23)-1,pos[1]//23],Type] not in wallplace and [[math.ceil(pos[0]/23)-1,pos[1]//23+1],Type] not in wallplace :
        return True
    else:
        return False
def  notwalldown(pos,Type):
    if [[pos[0]//23,(pos[1]//23)+2],Type] not in wallplace and [[pos[0]//23+1,(pos[1]//23)+2],Type] not in wallplace:
        return True
    else:
        return False
def  notwallright(pos,Type):
    if [[(pos[0]//23)+2,pos[1]//23],Type] not in wallplace and [[(pos[0]//23)+2,pos[1]//23+1],Type] not in wallplace:
        return True
    else:
        return False
     
def setplace(pos,Type,Direction):
    wallplace.append([[pos[0]//23,pos[1]//23],Type])
    wallplace.append([[pos[0]//23,pos[1]//23+1],Type])
    wallplace.append([[pos[0]//23+1,pos[1]//23],Type])
    wallplace.append([[pos[0]//23+1,pos[1]//23+1],Type])
    '''if Direction == 0 and pos[0]//23!=0:
        wallplace.append([[playerpos[0]//23,playerpos[1]//23+2],4])
        wallplace.append([[playerpos[0]+1//23,playerpos[1]//23+2],4])
    elif Direction == 2 and pos[1]//23!=0:
        wallplace.append([[playerpos[0]+2//23,playerpos[1]//23+2],4])
        wallplace.append([[playerpos[0]+2//23,playerpos[1]+1//23+2],4])
    elif Direction == 4 and pos[0]//23!=0:
        wallplace.append([[playerpos[0]//23,playerpos[1]//23-2],4])
        wallplace.append([[playerpos[0]+1//23,playerpos[1]//23-2],4])
    elif Direction == 6 and pos[1]//23!=0:
        wallplace.append([[playerpos[0]-2//23,playerpos[1]//23],4])
        wallplace.append([[playerpos[0]-2//23,playerpos[1]//23+1],4])'''

    

setwall(2,2,3,10,0)
setwall(6,2,7,10,0)
setwall(10,2,11,8,0)
setwall(14,2,15,8,0)
setwall(18,2,19,10,0)
setwall(22,2,23,10,0)
setwall(10,11,11,12,0)
setwall(14,11,15,12,0)
setwall(4,13,7,14,0)
setwall(0,13,1,13,0)
setwall(18,13,21,14,0)
setwall(24,13,25,13,0)
setwall(2,17,3,23,0)
setwall(6,17,7,23,0)
setwall(10,15,11,20,0)
setwall(12,16,13,17,0)
setwall(14,15,15,20,0)
setwall(18,17,19,23,0)
setwall(22,17,23,23,0)
setwall(11,23,14,23,0)
setwall(11,24,11,25,0)
setwall(14,24,14,25,0)
setwall(12,6,13,7,1)
setwall(0,14,1,14,1)
setwall(24,14,25,14,1)
setwall(-1,-1,26,-1,2)
setwall(-1,-2,-1,25,2)
setwall(-1,26,26,26,2)
setwall(26,-2,26,25,2)
setwall(12,24,13,25,2)
setwall(12,24,13,25,9)



while 1:
        
        
    clock -=1
    for i in reversed(wallplace):
        if i[1]>=4:
            wallplace.remove(i)
        else:
            break
    for i in enemylist:
        setplace(i.enemypos,5,i.Direction)

    setplace(playerpos,4,Direction)
    
    

    pygame.time.delay(5) 
    playergif()
    enemymove()
    refresh()
    setenemy()
    enemyattack()
    pygame.display.flip()

    
    
    if rspawnpoint==mspawnpoint==lspawnpoint==0 and enemynum!=4:
        enemynum+=1
        if random.randint(0,2)==0:
            rspawnpoint=600
        elif random.randint(0,1)==0:
            mspawnpoint=600
        else:
            lspawnpoint=600
            
    else:
        pass
        #print(rspawnpoint,mspawnpoint,lspawnpoint)

    if press or playerpos[0]%23!=0 or playerpos[1]%23!=0:
        if   Direction==0 and notwallup(playerpos,0) and notwallup(playerpos,1) and notwallup(playerpos,2) and notwallup(playerpos,5):
            playerpos[1]-=1    
            
        elif Direction==2 and notwallleft(playerpos,0) and notwallleft(playerpos,1) and notwallleft(playerpos,2) and notwallleft(playerpos,5):
            playerpos[0]-=1
            
        elif Direction==4 and notwalldown(playerpos,0) and notwalldown(playerpos,1) and notwalldown(playerpos,2) and notwalldown(playerpos,5):
            playerpos[1]+=1
            
        elif Direction==6 and notwallright(playerpos,0) and notwallright(playerpos,1) and notwallright(playerpos,2) and notwallright(playerpos,5):
            playerpos[0]+=1


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type==pygame.KEYDOWN:
            if blood!=0 and Bird == True:
                if event.key==K_w and playerpos[0]%23==0 and playerpos[1]%23==0:
                    Direction = 0
                    press=True
                    wallplace.append([[playerpos[0]//23,playerpos[1]//23-1],4])
                    wallplace.append([[playerpos[0]//23+1,playerpos[1]//23-1],4])

                elif event.key==K_a and playerpos[0]%23==0 and playerpos[1]%23==0:
                    Direction = 2
                    press=True
                    wallplace.append([[playerpos[0]//23-1,playerpos[1]//23],4])
                    wallplace.append([[playerpos[0]//23-1,playerpos[1]//23+1],4])

                elif event.key==K_s and playerpos[0]%23==0 and playerpos[1]%23==0:
                    Direction = 4
                    press=True
                    wallplace.append([[playerpos[0]//23,playerpos[1]//23+2],4])
                    wallplace.append([[playerpos[0]//23+1,playerpos[1]//23+2],4])

                elif event.key==K_d and playerpos[0]%23==0 and playerpos[1]%23==0:
                    Direction = 6
                    press=True
                    wallplace.append([[playerpos[0]//23+2,playerpos[1]//23],4])
                    wallplace.append([[playerpos[0]//23+2,playerpos[1]//23+1],4])

                if event.key==K_j :
                    paolist.append(Paodan.Pao(setpao(Direction,playerpos),Direction,0))



        if blood!=0 and Bird == True:
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_w:
                    press=False                 
                elif event.key==pygame.K_a:
                    press=False
                elif event.key==pygame.K_s:
                    press=False
                elif event.key==pygame.K_d:
                    press=False



        
