from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('шутр')
background = transform.scale(image.load('space2.jpg'),(700, 500))
win_height = 500
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
kick = mixer.Sound("fire.ogg")
kick.play
font.init()
font2 = font.SysFont('Arial', 40)
font1 = font.SysFont('Arial', 70)
lost = 0
score = 0
win = font1.render('YOU WIGRAL', True, (255, 255 , 255))
lose = font2.render('YOU LOOOOOOOSER', True, (180, 0 , 0))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, play_x, play_y, size_x, size_y, player_sped):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_sped
        self.rect = self.image.get_rect()
        self.rect.x = play_x
        self.rect.y = play_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update (self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_height - 80:
            self.rect.x += self.speed   
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 25, 20, -25)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update (self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_height - 700)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update (self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

class Asteroid(GameSprite):
    def update (self):           
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(90, win_height - 800)
            self.rect.y = 0



player = Player('pegas.png', 10, win_height-150 ,170,200,3)
antyplayers = sprite.Group()
bullets = sprite.Group()
asteroids = sprite.Group()
for i in range(1, 9):
    antyplayer = Enemy('weselk.png',randint(80, win_height - 80), -40, 80, 50, randint(1, 7)) 
    antyplayers.add(antyplayer)
for j in range(1, 150):
    asteroid = Asteroid('steroid.png',randint(80, win_height - 80), -40, 80, 50, randint(1, 10)) 
    asteroids.add(asteroid)
    
FPS = 60
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                kick.play()
                player.fire()
    if not finish:
        window.blit(background,(0, 0))
        player.update()
        antyplayers.update()
        asteroids.update()
        player.reset()
        asteroids.draw(window)
        antyplayers.draw(window)
        bullets.draw(window)
        bullets.update()
        colliedes = sprite.groupcollide(antyplayers, bullets, True, True)
        for c in colliedes:
            score = score + 1
            antyplayer = Enemy('weselk.png',randint(80, win_height - 80), -40, 80, 50, randint(1, 5)) 
            antyplayers.add(antyplayer)

        if sprite.spritecollide(player, antyplayers, False) or lost >= 20 :
            finish = True
            window.blit(lose, (200, 300))

        if sprite.spritecollide(player, asteroids, False) or lost >= 20 :
            finish = True
            window.blit(lose, (200, 300))
                           
        if score >= 35:
            finish = True
            window.blit(win , (200, 300))


         
        text = font2.render("счет" + str(score), 1, (255, 255, 255))
        display.update()


    time.delay(50)
# Привет! Немного подправила, но нет отображения счёта на эране, и надпи
    



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

# _  _
#/ \/ \
#\    /
# \  /
#  \/