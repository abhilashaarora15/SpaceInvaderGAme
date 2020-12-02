import pygame
import random
import math
from pygame.locals import*
from pygame import mixer
#initialise pygame and pygame module
pygame.init()
#display screen
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Space Shooting game")
surf=pygame.display.get_surface()
logo= pygame.image.load('ufo.png')
pygame.display.set_icon(logo)
pygame.display.flip()
#background
bgimg= pygame.image.load("myspacebackgnd.png")
#player
player=pygame.image.load('spaceship (1).png')
playerX=100
playerY=500
playerX_user=0
def players(x,y):
    surf.blit(player,(x,y))
#enemy
enemy=pygame.image.load('enemy.png')
enemyX=random.randint(0,735)
enemyY=random.randint(50,100)
enemyX_user=3
enemyY_user=40
enemy=[]
enemyX=[]
enemyY=[]
enemyX_user=[]
enemyY_user=[]
num_of_enemy=6
for i in range(num_of_enemy):
    enemy.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,100))
    enemyX_user.append(3)
    enemyY_user.append(40)

def enemys(x,y,i):
    surf.blit(enemy[i],(x,y))
#background sound
mixer.music.load('background.wav')
mixer.music.play(-1)
#bullets
bullets=pygame.image.load('bullet.png')
bulletsX=100
bulletsY=480
bulletsX_user=0
bulletsY_user=20
bullet_move="running"
def bullet(x,y):
    global bullet_move
    bullet_move="fire"
    surf.blit(bullets,(x+16,y+10))
#collision between bullets and enemy
def isCollision(enemyX,enemyY,bulletsX,bulletsY):
    distance=math.sqrt((math.pow((enemyX-bulletsX),2))+(math.pow((enemyY-bulletsY),2)))
    if distance<27:
        return True
    else:
        return False
#scoreboard
score=0
font=pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=10
def scoreboard(x,y):
    myscore=font.render("Score:"+ str(score),True,(255,255,255))
    surf.blit(myscore,(x,y))
#game over(text)
game_over_font=pygame.font.Font('freesansbold.ttf',64)
def game_over():
    myscore=game_over_font.render("GAME OVER",True,(255,255,255))
    surf.blit(myscore,(200,200))
#events
while True:
    surf.fill((0,0,0))
    surf.blit(bgimg,(0,0))
    #playerX+=0.1
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                playerX-=50
            elif event.key== K_RIGHT:
                playerX+=50
            elif event.key== K_SPACE:
                if bullet_move is "running":
                    bullet_sound=mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletsX=playerX


                    bullet(bulletsX,bulletsY)
    #changing the position of spaceship whenever it reaches the boundary
    playerX+=playerX_user
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    #enemy movement
    for i in range(num_of_enemy):
        #game over
        if enemyY[i]>440:
            for j in range(num_of_enemy):
                enemyY[j]=2000
            game_over()
            break
        enemyX[i]+=enemyX_user[i]
        if enemyX[i]<=0:
            enemyX_user[i]=3
            enemyY[i]+=enemyY_user[i]
        elif enemyX[i]>=736:
            enemyX_user[i]=-3
            enemyY[i]+=enemyY_user[i]
        #collision between bullet and the enemy
        collision=isCollision(enemyX[i],enemyY[i],bulletsX,bulletsY)
        if collision:
            exposion_sound=mixer.Sound("explosion.wav")
            exposion_sound.play()
            bulletsY=480
            score +=1
            #print(score)
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,100)
        enemys(enemyX[i],enemyY[i],i)
    #to create multiple bullets
    if bulletsY<=0:
        bulletsY=480
        bullet_move="running"
    #bullet movement
    if bullet_move=="fire":
        bullet(bulletsX,bulletsY)
        bulletsY-=bulletsY_user
    #to create multiple bullets
    if bulletsY<=0:
        bulletsY=480
        bullet_move="running"
    players(playerX, playerY)
    scoreboard(textX,textY)
    pygame.display.update()
