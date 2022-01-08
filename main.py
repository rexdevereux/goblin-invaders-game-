import pygame
import random
import math

from pygame import mixer

# initialize game
pygame.init()

# create screen, set height and weight (())
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background1.png')
pygame.display.set_icon(background)

# Background sound
mixer.music.load('troubador.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Beasts of Cthulu")
icon = pygame.image.load('knight.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('wizard.png')
playerX = 370
playerY = 500
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5
max_enemies = 100

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('cthulhu.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(10, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)

# Fireball
# ready - you cannot see fireball on screen
# fire - fireball is currently moving
fireballImg = pygame.image.load('fireball.png')
fireballX = 0
fireballY = 370
fireballX_change = 0
fireballY_change = 8
fireball_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('Enchanted_Land.otf', 32)
textX = 10
textY = 10
threshold = 5

# Game over text
over_font = pygame.font.Font('Enchanted_Land.otf', 64)


#Add more enemies
enemySurf = pygame.image.load('cthulhu.png')

def addNewEnemy():
    enemyImg.append(enemySurf)0i znsmedr56    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(10, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (250, 200))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_fireball(x, y):
    global fireball_state
    fireball_state = "fire"
    screen.blit(fireballImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, fireballX, fireballY):
    distance = math.sqrt(math.pow(enemyX - fireballX, 2) + (math.pow(enemyY - fireballY, 2)))
    if distance < 27:
        return True
    else:
        return False

    # Game Loop


running = True
while running:

    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard actions
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if fireball_state == "ready":
                    fireball_Sound = mixer.Sound('fireball-1.wav')
                    fireball_Sound.play()
                    fireballX = playerX
                    fire_fireball(fireballX, fireballY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # checking for boundaries
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Fireball movement
    if fireballY <= 0:
        fireballY = 480
        fireball_state = "ready"

    if fireball_state == "fire":
        fire_fireball(fireballX, fireballY)
        fireballY -= fireballY_change


    # Enemy movement
    enemyX += enemyX_change

    for i in range(num_of_enemies):

        # Game Over
        if enemyY[1] > 370:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]



        # Collision
        collision = isCollision(enemyX[i], enemyY[i], fireballX, fireballY)
        if collision:
            explosion_Sound = mixer.Sound('fireball-explosion.wav')
            explosion_Sound.play()
            fireballY = 480
            fireball_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(10, 150)

        enemy(enemyX[i], enemyY[i], i)


        if score_value >= threshold:
            addNewEnemy()
            num_of_enemies += 1
            threshold += 5
            print(len(enemyX))









    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

# <a href="https://www.freepik.com/vectors/tree">Tree vector created by upklyak - www.freepik.com</a>
