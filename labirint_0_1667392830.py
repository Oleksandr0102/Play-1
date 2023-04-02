# Розроби свою гру в цьому файлі!
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_x_spead,player_y_spead):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)
        self.x_spead = player_x_spead
        self.y_spead = player_y_spead
    def update(self):
        if pacman.rect.x <= win_width-80 and pacman.x_spead > 0 or pacman.rect.x >= 0 and pacman.x_spead < 0:
            self.rect.x += self.x_spead
        platforms_touched = sprite.spritecollide(self,barriers,False)
        if self.x_spead > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right,p.rect.left)
        elif self.x_spead < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left,p.rect.right)
        if pacman.rect.y <= win_height-80 and pacman.y_spead > 0 or pacman.rect.y >= 0 and pacman.y_spead < 0:
            self.rect.y += self.y_spead
        platforms_touched = sprite.spritecollide(self,barriers,False)
        if self.y_spead > 0:
            for p in platforms_touched:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_spead < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top,p.rect.bottom)
    def fire(self):
        bullets.add(Bullet('bullet.jpeg',self.rect.centerx,self.rect.top,15,7,20))
class Enemy(GameSprite):
    side = 'width'
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_spead):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)  
        self.speed = player_spead
    def update(self):
        if self.rect.x <= 940:
            self.side = 'height'
        if self.rect.x >= win_width - 100:
            self.side = 'width'
        if self.side == 'width':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Enemy2(GameSprite):
    side = 'width'
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_spead):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)  
        self.speed = player_spead
    def update(self):
        if self.rect.x <= 0:
            self.side = 'height'
        if self.rect.x >= win_width - 1000:
            self.side = 'width'
        if self.side == 'width':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed 
class Enemy3(GameSprite):
    side = 'width'
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_spead):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)  
        self.speed = player_spead
    def update(self):
        if self.rect.x <= 940:
            self.side = 'height'
        if self.rect.x >= win_width - 100:
            self.side = 'width'
        if self.side == 'width':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed                        
class Enemy1(GameSprite):
    side = 'width'
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_spead):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)  
        self.speed = player_spead
    def update(self):
        if self.rect.y <= 0:
            self.side = 'height'
        if self.rect.y >= win_width - 690:
            self.side = 'width'
        if self.side == 'width':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed                           
class Bullet(GameSprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y, player_spead):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)  
        self.speed = player_spead
        shott.play() 
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width + 10:
            self.kill()       
mixer.init()
mixer.pre_init(44100,-16,1,512)  
mixer.music.load('5502.mp3')
mixer.music.play(-1)  
shott = mixer.Sound('shot.ogg') 
victory = mixer.Sound('victory.ogg') 
defeat = mixer.Sound('defeat.ogg') 
hitting = mixer.Sound('hitting.ogg')                                                                           
win_width = 1200
win_height = 600
display.set_caption('Пакмен')
window = display.set_mode((win_width,win_height))
back = (80,85,50)
barriers = sprite.Group()
bullets = sprite.Group()
monsters = sprite.Group()
barriers.add(GameSprite('wall1.jpeg',win_width-915,win_height-160,12,250))
barriers.add(GameSprite('wall2.jpeg',win_width-1060,win_height-310,150,12))
barriers.add(GameSprite('wall3_copy.jpeg',win_width-915,win_height-690,12,250))
barriers.add(GameSprite('wall4_copy.jpeg',win_width-300,win_height-310,150,12))
barriers.add(GameSprite('wall5_copy.jpeg',win_width-300,win_height-160,12,250))
barriers.add(GameSprite('wall6_copy.jpeg',win_width-300,win_height-690,12,250))
barriers.add(GameSprite('wall7_copy.jpeg',win_width-770,win_height-217,330,12))
barriers.add(GameSprite('wall8_copy.jpeg',win_width-787,win_height-110,370,12))
barriers.add(GameSprite('wall9_copy.jpeg',win_width-787,win_height-500,370,12))
barriers.add(GameSprite('wall10_copy.jpeg',win_width-525,win_height-360,80,12))
barriers.add(GameSprite('wall11_copy.jpeg',win_width-768,win_height-360,80,12))
barriers.add(GameSprite('wall12_copy.jpeg',win_width-770,win_height-361,12,156))
barriers.add(GameSprite('wall13_copy.jpeg',win_width-445,win_height-361,12,156))
barriers.add(GameSprite('wall14_copy.jpeg',win_width-150,win_height-450,12,300))
barriers.add(GameSprite('wall15_copy.jpeg',win_width-1070,win_height-450,12,300))
#Місце для стін 
pacman = Player('pacman.png',5,win_height - 80,80,80,0,0)
final_sprite = GameSprite('cherry1.jpeg',win_width-640,win_height-320,80,80)
monsters.add(Enemy('ghost.jpeg',win_width - 100,400,80,80,10))
monsters.add(Enemy2('ghost.jpeg',win_width - 1200,120,80,80,10))
monsters.add(Enemy3('ghost.jpeg',win_width - 300,120,80,80,10))
monsters.add(Enemy1('ghost.jpeg',win_width - 880,0,80,80,20))
monsters.add(Enemy1('ghost.jpeg',win_width - 400,510,80,80,20))
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False                   
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                pacman.x_spead = -18
            elif e.key == K_RIGHT:
                pacman.x_spead = 18
            elif e.key == K_UP:
                pacman.y_spead = -18
            elif e.key == K_DOWN:
                pacman.y_spead = 18
            elif e.key == K_SPACE:
                pacman.fire()                
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                pacman.x_spead = 0
            elif e.key == K_RIGHT:
                pacman.x_spead = 0
            elif e.key == K_UP:
                pacman.y_spead = 0
            elif e.key == K_DOWN:
                pacman.y_spead = 0
    if not finish:
        window.fill(back)
        pacman.reset()
        pacman.update()
        bullets.update()
        bullets.draw(window)
        barriers.draw(window)
        final_sprite.reset()
        if sprite.groupcollide(monsters,bullets,True,True):
            hitting.play()
        monsters.update()
        monsters.draw(window)
        sprite.groupcollide(bullets,barriers,True,False)
        if sprite.spritecollide(pacman,monsters,False):
            finish = True
            img = image.load('game_over.png')
            d = img.get_width()//img.get_height()
            window.fill((255,255,255))
            window.blit(transform.scale(img,(win_height * d,win_height)),(90,0))
            mixer.music.pause()
            defeat.play()
        if sprite.collide_rect(pacman,final_sprite):
            finish = True
            img = image.load('finger.png')
            window.fill((255,255,255))
            window.blit(transform.scale(img,(win_width,win_height)),(0,0))  
            mixer.music.pause()  
            victory.play()        
        time.delay(50)
        display.update()                            