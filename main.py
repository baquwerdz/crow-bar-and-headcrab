import random
import pgzrun

WIDTH = 800
HEIGHT = 800

score  = 0
crowbar = Actor("crowbar")
crowbar.pos = (150,100)

headcrab = Actor("headcrab")
headcrab.pos = (100,100)

def draw():
    screen.clear()
    screen.blit("city17",(0,0))
    crowbar.draw()
    headcrab.draw()

def place_headcrab():
    headcrab.x = random.randint(70,(WIDTH - 70))
    headcrab.y = random.randint(70,(HEIGHT - 70))

def update():
    global score
    if keyboard.left:
        crowbar.x -= 2
    if keyboard.right:
        crowbar.x += 2
    if keyboard.up:
        crowbar.y -= 2
    if keyboard.down:
        crowbar.y += 2
    headcrab_killed = crowbar.colliderect(headcrab)
    if headcrab_killed:
        score = score +10
        place_headcrab()



    


pgzrun.go()