#Создай собственный Шутер!

from pygame import *
from random import *
import os
import time as tm
window=display.set_mode((700,500))
display.set_caption('Шутер')
galaxy=transform.scale(image.load('galaxy.jpg'),(700,500))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
z=0
fir=0
bulets=sprite.Group()

class GameSprite (sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,width,height):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(width,height))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def updates(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x-=self.speed
        if keys_pressed[K_RIGHT] and self.rect.x<635:
            self.rect.x+=self.speed

    def fire(self):
        bullet=Bulet('bullet.png',self.rect.centerx,self.rect.top,7,20,20)
        bulets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        global z
        if self.rect.y >= 600:
            self.rect.y=-10
            self.rect.x=randint(0,600)
            z+=1

class Bulet(GameSprite):
    def update(self):
        self.rect.y-=self.speed
        if self.rect.y<=0:
            self.kill()

class Asteroid(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        if self.rect.y >= 600:
            self.rect.y=-10
            self.rect.x=randint(0,600)


monsters = sprite.Group()
monsterss = sprite.Group()
for i in range (5):
    monster=Enemy('ufo.png',randint(0,600),10,randint(1,2),95,65)
    monsters.add(monster)

player=Player('rocket.png',300,400,5,65,85) 
bullet=Bulet('bullet.png',300,400,1,20,20)
steroid=Asteroid('asteroid.png',randint(0,600),8.5,randint(1,2),95,65)
monsterss.add(steroid)
clock=time.Clock()
FPS=60
font.init()
font1=font.SysFont(None,70)
win=font1.render('You win',True,(0, 255, 0))
lose=font1.render('You lose',True,(178, 34, 34))
reset=font1.render('Перезарядка',False,(178, 34, 34))
game=True
final=False
fire_fs=0
rel_fire=False
while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if fire_fs<5 and rel_fire==False:
                    player.fire()
                    fire_fs+=1
                elif fire_fs>=5 and rel_fire==False:
                    rel_fire=True
                    start=tm.time()



    if final != True:

        window.blit(galaxy,(0,0))

        if rel_fire==True:
            end=tm.time()
            if end-start<3:      
                window.blit(reset,(200,400))
            else:
                fire_fs=0
                rel_fire=False

        text=font.SysFont('serif',25).render(f'Пропущено: {z}',True,(255,255,255))
        fires=font.SysFont('serif',25).render(f'Счёт: {fir}',True,(255,255,255))



        sprite_list=sprite.groupcollide(monsters,bulets,True,True)
        for i in sprite_list:
            fir+=1
            monster=Enemy('ufo.png',randint(0,600),10,randint(1,2),95,65)
            monsters.add(monster)




        if sprite.spritecollide(player,monsters,False):
            window.blit(lose,(250,250))
            final=True

        if sprite.spritecollide(player,monsterss,False):
            window.blit(lose,(250,250))
            final=True




        player.reset()

        window.blit(text,(0,0))
        window.blit(fires,(0,30))
        monsters.update()
        monsterss.update()
        monsterss.draw(window)
        steroid.update()
        monsters.draw(window)
        bulets.update()
        bulets.draw(window)
        bullet.update()
        player.updates()

        if z>=5:
            final=True
            window.blit(lose,(250,250))
        
        if fir>=9:
            final=True
            window.blit(win,(250,250))

    display.update()
    clock.tick(FPS) 
