import random, sys, math, time
import pygame
from pygame.locals import *


        
















#game variables
debugging_mode = True
game_on = False
game_height = 800
game_width = 1400
fps = 60
name = 'Sadistic Stars'
screen_colour = (250, 250, 250)
events = []
mouse_x = 0
mouse_y = 0
drift_speed = 2
running = True
edges = [750,0,1365,0]
bad_bullets = []
good_bullets = []
good_guys = []
bad_guys = []
effects = []
balls = []
explosions = []
#          ID : [IMAGE, AIM ANGLE FLUCTUATION, TICKS BETWEEN SHOT, DAMAGE]
bullets = {1 : ['bullet1.png', 3, 10, 16, 3],
           2 : ['bullet2.png', 20, 7, 3, .8],
           3 : ['bullet3.png', 0, 30, 60, 20],
           4 : ['bullet4.png', 40, 7, 120, 2]}
map_count = 0
map_image = pygame.image.load('stars.png')
#        ID : [TICKS BETWEEN SPAWN, SECONDS TO WAIT, LILL_TIMS, LILL_TIMS2, TIMS, BOMBS, BOBS]
waves = {1 : [40, 0, 30, 0, 0, 0, 0],
         2 : [30, 10, 60, 0, 0, 0, 0],
         3 : [12, 10, 100, 0, 0, 0, 0],
         4 : [16, 10, 60, 10, 0, 0, 0],
         5 : [12, 10, 100, 40, 0, 0, 0],
         6 : [8, 10, 200, 80, 0, 0, 0],
         7 : [16, 10, 100, 30, 2, 0, 0],
         8 : [12, 10, 200, 80, 15, 0, 0],
         9 : [16, 10, 100, 30, 2, 0, 4],
         10 : [16, 10, 100, 50, 10, 0, 10]}


wave_done = True
wave_to_do_list = []
players_to_make = []
skin_l = [1,2,3,4]
gun_l = [1,2,3,4]
controls_l = ['ijkl','wasd','tfgh', 'arrow']
players_l = [1,2,3,4]
options = True
wave_count = 0
scrolling_background = True

tim_stats = {'image1' : pygame.image.load('tim.png'),
             'image2' : pygame.image.load('tim2.png'),
             'health' : 10,
             'speed' : 1,
             'pitch' : 3,
             'roll' : .025,
             'shoot_rate' : 60,
             'costume_rate' : 10}

lill_tim_stats = {'image1' : pygame.image.load('lill_tim.png'),
                  'image2' : pygame.image.load('lill_tim2.png'),
                  'health' : 3,
                  'speed' : 1,
                  'pitch' : None,
                  'roll' : None,
                  'costume_rate' : 10}

lill_tim2_stats = {'image1' : pygame.image.load('lill_tim-2.png'),
                   'image2' : pygame.image.load('lill_tim2-2.png'),
                   'health' : 5,
                   'speed' : 1,
                   'pitch' : 3,
                   'roll' : .025,
                   'costume_rate' : 10}

bob_stats = {'image1' : pygame.image.load('worm_head1.png'),
             'image2' : pygame.image.load('worm_head2.png'),
             'health' : 5,
             'speed' : 3,
             'pitch' : 3,
             'roll' : .010,
             'costume_rate' : 10,
             'distance' : 5,
             'length' : 200}

bob_body_stats = {'image1' : pygame.image.load('worm_body.png')}
                  
player_stats = {'speed' : 5,
                'costume_rate' : 10,
                'controls' : {'wasd' : ['w','s','a','d'],
                              'tfgh' : ['t','g','f','h'],
                              'ijkl' : ['i','k','j','l'],
                              'arrow' : ['up','down','left','right']},
                'shotgun_count' : 12,
                'skins' : {1 : [pygame.image.load('player1-1.png'),pygame.image.load('player1-2.png')],
                           2 : [pygame.image.load('player2-1.png'),pygame.image.load('player2-2.png')],
                           3 : [pygame.image.load('player3-1.png'),pygame.image.load('player3-2.png')],
                           4 : [pygame.image.load('player4-1.png'),pygame.image.load('player4-2.png')]}}

explosion_stats = {'image1' : pygame.image.load('explosion.png'),
                   'length' : 15}







#classes




class count():

    def __init__(self):
        self.timer = 0

    def count_loop(self, timer):
        if self.timer == timer:
            self.timer = 0
            return True
        else:
            self.timer = self.timer + 1

    def count(self, timer):
        if self.timer == timer:
            return True
        else:
            self.timer = self.timer + 1

    def reset_timer(self):
        self.timer = 0


class player(pygame.sprite.Sprite):

    #sprite variables
    

    def __init__(self, num, skin, cntr, x, y, gun):
        self.skins = player_stats['skins']
        self.controls = player_stats['controls']
        self.image1 = ((self.skins[skin])[0])
        self.image2 = ((self.skins[skin])[1])
        self.player_num = num
        self.x = x
        self.y = y
        self.player_speed = player_stats['speed']
        pygame.sprite.Sprite.__init__(self)
        self.chosen_image = self.image1
        self.player_controls = cntr
        self.d = count()
        self.g = count()
        self.gun_type = gun
        self.gun_rate = (bullets[self.gun_type])[3]
        self.mask = maskFromSurface(self.chosen_image)
    def hit(self):
        if self in good_guys:
            explosions.append(explosion(self.x, self.y))
            good_guys.remove(self)

    def loop(self):
        if not(((self.controls[self.player_controls])[1]) in events and self.y >= edges[0]):
            if self.y >= 0:
                if game_on:
                    self.y = self.y - drift_speed
        if ((self.controls[self.player_controls])[0]) in events and self.y >= edges[1]:
            self.y = self.y - self.player_speed
        if ((self.controls[self.player_controls])[1]) in events and self.y <= edges[0]:
            self.y = self.y + self.player_speed + drift_speed
        if ((self.controls[self.player_controls])[2]) in events and self.x >= edges[3]:
            self.x = self.x - self.player_speed
        if ((self.controls[self.player_controls])[3]) in events and self.x <= edges[2]:
            self.x = self.x + self.player_speed
        if self.d.count_loop(player_stats['costume_rate']):
            if self.chosen_image == self.image1:
                self.chosen_image = self.image2
            elif self.chosen_image == self.image2:
                self.chosen_image = self.image1
        if game_on:
            if self.g.count_loop(self.gun_rate):
                good_bullets.append(player_bullet(self.gun_type,self.x,self.y))
                if self.gun_type == 4:
                    for x in range(player_stats['shotgun_count'] - 1):
                        good_bullets.append(player_bullet(self.gun_type,self.x,self.y))

        self.mask = maskFromSurface(self.chosen_image)
        screen.blit(self.chosen_image, (self.x, self.y))





class tim(pygame.sprite.Sprite):

    def __init__(self, skin, x, y):
        self.health = tim_stats['health']
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image1 = tim_stats['image1']
        self.image2 = tim_stats['image2']
        self.chosen_image = self.image1
        self.d = count()
        self.g = count()
        self.speed = tim_stats['speed']
        self.pitch = tim_stats['pitch']
        self.roll = tim_stats['roll']
        self.shoot_rate = tim_stats['shoot_rate']
        self.costume_rate = tim_stats['costume_rate']
        self.mask = maskFromSurface(self.chosen_image)


    def hit(self, dam):
        self.health = self.health - dam
        explosions.append(explosion(self.x, self.y))
        if self.health <= 0:
            if self in bad_guys:
                bad_guys.remove(self)


    
    def loop(self):
        if self.y >= 1000:
            wave_to_do_list.append('tim')
            bad_guys.remove(self)
            
        self.y = self.y + self.speed
        self.x = self.x + ((math.cos(self.y * self.roll)) * self.pitch)
        if self.d.count_loop(self.costume_rate):
            if self.chosen_image == self.image1:
                self.chosen_image = self.image2
            else:
                self.chosen_image = self.image1
        if self.g.count_loop(self.shoot_rate):
            bad_bullets.append(bad_bullet(1,self.x + 45,self.y + 80,180))
        self.mask = maskFromSurface(self.chosen_image)
        screen.blit(self.chosen_image, (self.x, self.y))

class bob(pygame.sprite.Sprite):

    def __init__(self, skin, y, direction):
        self.health = bob_stats['health']
        self.y = y
        self.speed = bob_stats['speed']
        pygame.sprite.Sprite.__init__(self)
        self.image1 = bob_stats['image1']
        self.image2 = bob_stats['image2']
        self.chosen_image = self.image1
        self.d = count()
        self.g = count()
        self.pitch = bob_stats['pitch']
        self.roll = bob_stats['roll']
        #self.pitch2 = 2
        #self.roll2 = .01
        self.costume_speed = bob_stats['costume_rate']
        self.body_length = bob_stats['length']
        self.body_distance = bob_stats['distance']
        self.direction = direction
        if self.direction == 'left':
            self.x = 1500
        if self.direction == 'right':
            self.x = -100
            self.image1 = pygame.transform.rotate(self.image1, 180)
            self.image2 = pygame.transform.rotate(self.image2, 180)
        self.mask = maskFromSurface(self.chosen_image)



    def hit(self, dam):
        self.health = self.health - dam
        explosions.append(explosion(self.x, self.y))
        if self.health <= 0:
            if self in bad_guys:
                bad_guys.remove(self)
                



            
    def loop(self):
        #angle = 0
        if self.x >= 1700 or self.x <= -300:
            wave_to_do_list.append('bob')
            bad_guys.remove(self)
        if self.direction == 'left':
            self.x = self.x - self.speed
        if self.direction == 'right':
            self.x = self.x + self.speed
        self.y = self.y + ((math.cos(self.x * self.roll)) * self.pitch)
        if self.d.count_loop(self.costume_speed):
            if self.chosen_image == self.image1:
                self.chosen_image = self.image2
            else:
                self.chosen_image = self.image1
        if self.g.count_loop(self.body_distance):
            if self.direction == 'left':
                balls.append(bob_body(self.x, self.y - 23, self.body_length))
            if self.direction == 'right':
                balls.append(bob_body(self.x - 30, self.y - 23, self.body_length))
        #angle = angle + ((math.cos(self.x * self.roll2)) * self.pitch2)
        #self.chosen_image = pygame.transform.rotate(self.chosen_image, angle)
        self.mask = maskFromSurface(self.chosen_image)
        screen.blit(self.chosen_image, (self.x, self.y))

class bob_body(pygame.sprite.Sprite):

    def __init__(self, x, y, length):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = bob_body_stats['image1']
        self.x = x
        self.y = y
        self.length = length
        self.turn_speed = 1
        self.d = count()
        self.mask = maskFromSurface(self.image1)
        

    def loop(self):
        screen.blit(self.image1, (self.x, self.y))
        if self.d.count(self.length):
            balls.remove(self)
        
class explosion(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = explosion_stats['image1']
        self.x = x
        self.y = y
        self.length = explosion_stats['length']
        self.turn_speed = 1
        self.d = count()

        

    def loop(self):
        screen.blit(self.image1, (self.x, self.y))
        if self.d.count(self.length):
            if self in explosions:
                explosions.remove(self)
    
    

class lill_tim(pygame.sprite.Sprite):

    def __init__(self, skin, x, y):
        if skin == 1:
            self.stats = lill_tim_stats
        else:
            self.stats = lill_tim2_stats
        self.health = self.stats['health']
        self.x = x
        self.y = y
        self.speed = self.stats['speed']
        pygame.sprite.Sprite.__init__(self)
        self.image1 = self.stats['image1']
        self.image2 = self.stats['image2']
        self.chosen_image = self.image1
        self.d = count()
        self.pitch = self.stats['pitch']
        self.roll = self.stats['roll']
        self.skin = skin
        self.mask = maskFromSurface(self.chosen_image)


    def hit(self, dam):
        self.health = self.health - dam
        explosions.append(explosion(self.x, self.y))
        if self.health <= 0:
            if self in bad_guys:
                bad_guys.remove(self)
                


    def loop(self):
        if self.y >= 1000:
            if self.skin == 1:
                wave_to_do_list.append('lill_tim')
            else:
                wave_to_do_list.append('lill_tim2')
            bad_guys.remove(self)
        self.y = self.y + self.speed
        if self.skin == 2:
            self.x = self.x + ((math.cos(self.y * .025)) * self.pitch)
        if self.d.count_loop(self.stats['costume_rate']):
            if self.chosen_image == self.image1:
                self.chosen_image = self.image2
            else:
                self.chosen_image = self.image1
        self.mask = maskFromSurface(self.chosen_image)
        screen.blit(self.chosen_image, (self.x, self.y))



class bad_bullet(pygame.sprite.Sprite):

    def __init__(self, skin, x, y, angle):
        self.skins = {1 : ['bad_bullet.png',5,10], 2 : ['player2-1.png',0,15] }
        self.image1 = ((self.skins[skin])[0])
        self.x = x
        self.y = y
        self.speed = ((self.skins[skin])[1])
        self.accuracy = ((self.skins[skin])[2])
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load(self.image1)
        self.chosen_image = self.image1
        self.d = count()
        self.g = count()
        self.angle_possibilities = (list(range((self.accuracy * -1), (self.accuracy + 1))))
        self.angle = random.choice(self.angle_possibilities)
        self.angle = self.angle + angle
        self.chosen_image = pygame.transform.rotate(self.chosen_image, self.angle)
        self.mask = maskFromSurface(self.chosen_image)

    
    def hit(self):
        if self in bad_bullets:
            bad_bullets.remove(self)

    def loop(self):
        if self.y > 900:
            bad_bullets.remove(self)
        self.y = self.y + self.speed
        self.y_add = (self.speed*math.sin(math.radians(self.angle + 90)))
        self.x_add = (self.speed*math.cos(math.radians(self.angle + 90)))
        self.x = self.x + self.x_add
        self.y = self.y - self.y_add
        self.mask = maskFromSurface(self.chosen_image)
        screen.blit(self.chosen_image, (self.x, self.y))
        



        
class player_bullet(pygame.sprite.Sprite):

    #sprite variables
    

    def __init__(self, num, x, y):
        self.bullet = num
        self.bullet_image = (bullets[num])[0]
        self.x = x
        self.y = y
        self.bullet_speed = (bullets[num])[2]
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(self.bullet_image)
        self.d = count()
        self.accuracy = (bullets[num])[1]
        self.angle_possibilities = (list(range((self.accuracy * -1), (self.accuracy + 1))))
        self.angle = random.choice(self.angle_possibilities)
        pygame.transform.rotate(self.image, self.angle)
        self.mask = maskFromSurface(self.image)

    def hit(self):
        if self.bullet != 3:
            if self in good_bullets:
                good_bullets.remove(self)


    def loop(self):
        if self.y < -10:
            good_bullets.remove(self)
        #self.bullet_y = self.bullet_y - self.bullet_speed
        self.yl = (self.bullet_speed*math.sin(math.radians(self.angle + 90)))
        self.xl = (self.bullet_speed*math.cos(math.radians(self.angle + 90)))
        self.x = self.x + self.xl
        self.y = self.y - self.yl
        self.mask = maskFromSurface(self.image)
        screen.blit(self.image, (self.x + 14, self.y))
        
        
class stars(pygame.sprite.Sprite):

    #sprite variables
    

    def __init__(self):
        self.map_x = 0
        self.map_y = -8001
        pygame.sprite.Sprite.__init__(self)
        
        self.scale_factor = 2.3
        
        global map_count 
        if map_count == 0:
            self.map_y = -7200
            
            map_count = 1


    def loop(self):
        global map_count
        self.map_y = self.map_y + .5
        screen.blit(map_image, (self.map_x, self.map_y))
        if self.map_y == 0:
            
            map_count = map_count + 1
       
            effects.append(stars())
        if self.map_y >= 800:
            effects.remove(self)





















#functions

def maskFromSurface(surface, threshold=127):
    return pygame.mask.from_surface(surface, threshold)
            
            
def ask_player():
    global wave_count
    global scrolling_background
    global options
    global player_stats
    while True:
        players = int(input('How many players(1-4): '))
        if players in players_l:
            break
        else:
            print('Not an option')

    for x in range(players):
        x = x + 1
        while True:
            skin = int(input('player%s skin(1-4): ' % str(x)))
            if skin in skin_l:
                skin_l.remove(skin)
                break
            else:
                print('Not an option')
        while True:
            gun = int(input('player%s gun(1-4): ' % str(x)))
            if gun in gun_l:
                break
            else:
                print('Not an option')
        while True:
            controls = input('player%s controls(ijkl,wasd,tfgh,arrow): ' % str(x))
            if controls in controls_l:
                controls_l.remove(controls)
                break
            else:
                print('Not an option')
            
            
        if x == 1:
            startx = 700
            starty = 400
        if x == 2:
            startx = 800
            starty = 400
        custom_player = [x,skin,controls,startx,starty,gun]
        players_to_make.append(custom_player)
    print('OPTIONAL SETTINGS, press enter for defaults')

    while True:
        wave = input('Starting wave(1 - %s): ' % len(waves))
        try:
            wave = int(wave)
            if wave in range(1, (len(waves)) + 1):
                
                wave_count = wave - 1
                break
            else:
                print('Not an option')
        except:
            
            if wave == '':
                options = False
                break
            else:
                print('Not an option')
    if options:
        while True:
                scrolling = input('Scrolling background(y,n): ')
                if scrolling in ['y','n']:
                    if scrolling == 'n':
                        print('done')
                        scrolling_background = False
        
                    break
                elif scrolling == '':
                    options = False
                    break
                else:
                    print('Not an option')


def touching(sprite_obj1, sprite_obj2):
    offset = [int(sprite_obj1.x - sprite_obj2.x), int(sprite_obj1.y - sprite_obj2.y)]
    overlap = sprite_obj2.mask.overlap_area(sprite_obj1.mask, (offset))
    if overlap > 0:
        return True
                    
def run_wave():
    
    global wave_done
    global wave_count
    if len(wave_to_do_list) == 0:
        wave_timer1.reset_timer()
        wave_timer2.reset_timer()
    if len(wave_to_do_list) == 0 and len(bad_guys) == 0:
        wave_done = True
        wave_count = wave_count + 1
        f = (waves[wave_count])[2]
        g = (waves[wave_count])[3]
        h = (waves[wave_count])[4]
        j = (waves[wave_count])[6]
   
        for x in range(f):
            wave_to_do_list.append('lill_tim')
        for x in range(g):
            wave_to_do_list.append('lill_tim2')
        for x in range(h):
            wave_to_do_list.append('tim')
        for x in range(j):
            wave_to_do_list.append('bob')
        
    if wave_timer1.count(((60 * (waves[wave_count])[1]))):
        wave_done = False
    if not wave_done:
        if wave_timer2.count_loop((waves[wave_count])[0]):
            p = random.choice(wave_to_do_list)
            if p == 'tim':
                x = random.choice(list(range(0, 1400)))
                bad_guys.append(tim(1,x,-100)) 
            if p == 'lill_tim':
                x = random.choice(list(range(0, 1400)))
                bad_guys.append(lill_tim(1,x,-100))
            if p == 'lill_tim2':
                x = random.choice(list(range(0, 1400)))
                bad_guys.append(lill_tim(2,x,-100))
            if p == 'bob':
                y = random.choice(list(range(0, 800)))
                direction = random.choice(('left','right'))
                bad_guys.append(bob(1,y,direction))
            wave_to_do_list.remove(p)
    



def start_button():
    global game_on
    if 'space' in events:
        game_on = True
    fg = 250, 240, 230
    bg = 5, 5, 5
    pygame.init()
    font1 = pygame.font.Font(None, 100)
    text1 = "Press space to start"
    size1 = font1.size(text1)
    ren1 = font1.render(text1, 0, fg, bg)
    screen.blit(ren1, (350, 390))

def game_over():
    fg = 250, 240, 230
    bg = 5, 5, 5
    pygame.init()
    font1 = pygame.font.Font(None, 100)
    text1 = "Game Over"
    size1 = font1.size(text1)
    ren1 = font1.render(text1, 0, fg, bg)
    screen.blit(ren1, (350, 390))

def search_events():
        keys_dict = {'space' : pygame.K_SPACE,
                     'up' : pygame.K_UP,
                     'down' : pygame.K_DOWN,
                     'left' : pygame.K_LEFT,
                     'right' : pygame.K_RIGHT,
                     'tab' : pygame.K_TAB,
                     'clear' : pygame.K_CLEAR,
                     'return' : pygame.K_RETURN,
                     '=' : pygame.K_EQUALS,
                     '`' : pygame.K_BACKQUOTE,
                     ']' : pygame.K_RIGHTBRACKET,
                     '.' : pygame.K_PERIOD,
                     'delete' : pygame.K_DELETE,
                     '/' : pygame.K_SLASH,
                     '-' : pygame.K_MINUS,
                     '[' : pygame.K_LEFTBRACKET,
                     ',' : pygame.K_COMMA,
                     ';' : pygame.K_SEMICOLON,
                     'backspace' : pygame.K_BACKSPACE,
                     '1' : pygame.K_1,
                     '2' : pygame.K_2,
                     '3' : pygame.K_3,
                     '4' : pygame.K_4,
                     '5' : pygame.K_5,
                     '6' : pygame.K_6,
                     '7' : pygame.K_7,
                     '8' : pygame.K_8,
                     '9' : pygame.K_9,
                     '0' : pygame.K_0,
                     'q' : pygame.K_q,
                     'w' : pygame.K_w,
                     'e' : pygame.K_e,
                     'r' : pygame.K_r,
                     't' : pygame.K_t,
                     'y' : pygame.K_y,
                     'u' : pygame.K_u,
                     'i' : pygame.K_i,
                     'o' : pygame.K_o,
                     'p' : pygame.K_p,
                     'a' : pygame.K_a,
                     's' : pygame.K_s,
                     'd' : pygame.K_d,
                     'f' : pygame.K_f,
                     'g' : pygame.K_g,
                     'h' : pygame.K_h,
                     'j' : pygame.K_j,
                     'k' : pygame.K_k,
                     'l' : pygame.K_l,
                     'z' : pygame.K_z,
                     'x' : pygame.K_x,
                     'c' : pygame.K_c,
                     'v' : pygame.K_v,
                     'b' : pygame.K_b,
                     'n' : pygame.K_n,
                     'm' : pygame.K_m}
        keys = list(keys_dict.keys())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global running
                running = False
            if event.type == pygame.KEYDOWN:
                for k in keys:
                    if event.key == keys_dict[k]:
                        events.append(k)
            if event.type == pygame.KEYUP:
                for k in keys:
                    if event.key == keys_dict[k]:
                        events.remove(k)
            if event.type == pygame.MOUSEBUTTONDOWN:
                events.append('click')
            if event.type == pygame.MOUSEBUTTONUP:
                events.remove('click')
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
def display_wave():
    fg = 250, 240, 230
    bg = 5, 5, 5
    pygame.init()
    font1 = pygame.font.Font(None, 40)
    text1 = "Wave: %s" % wave_count
    text2 = "Bad guys alive: %s" % (len(bad_guys))
    size1 = font1.size(text1)
    size2 = font1.size(text2)
    ren2 = font1.render(text2, 0, fg, bg)
    ren1 = font1.render(text1, 0, fg, bg)
    screen.blit(ren2, (0, 0))
    screen.blit(ren1, (1200, 0))
    
def create_players():
    for x in players_to_make:
        x = list(x)
        good_guys.append(player(x[0],x[1],x[2],x[3],x[4],x[5]))


def main():
    screen.fill(screen_colour)
    search_events()
    
    for x in effects:
        x.loop()
    for y in balls:
        y.loop()
    for x in good_guys:
        x.loop()
        for p in bad_guys:
            if touching(x, p):
                x.hit()
        for p in balls:
            if touching(x, p):
                x.hit()
        for p in bad_bullets:
            if touching(x, p):
                x.hit()
                p.hit()
    for x in bad_guys:
        x.loop()
    for x in good_bullets:
        x.loop()
        for p in bad_guys:
            if touching(x, p):
                x.hit()
                p.hit((bullets[x.bullet])[4])
    for x in bad_bullets:
        x.loop()
    for x in explosions:
        x.loop()
    if not game_on:
        start_button()
    if len(good_guys) == 0:
        game_over()
        if game_over_timer.count(240):
            print('game over')
            quit_game()
    if game_on:
        run_wave()
    display_wave()    
    pygame.display.update()
    clock.tick(fps)




def start_game():
    create_players()
    if scrolling_background:
        effects.append(stars())
    pygame.display.set_caption(name)


def quit_game():
    pygame.quit()
    sys.exit()

def game_logic():
    if not debugging_mode:
        try:
            start_game()
            while running:
                main()
            quit_game()
        except:
            try:
                print('There has been an error in the game')
                quit_game()
            except:
                print('The game could not auto log-out. Press the minus sign if the game window is still open and exit out of the python shell')
    else:
        start_game()
        while running:
            main()
        quit_game()     


#setup functions
ask_player()







#dumb game stuff
map_image = pygame.transform.scale(map_image, (int(map_image.get_width() * 2.3), int(map_image.get_height() * 2.3)))
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()






#timers
wave_timer1 = count()
wave_timer2 = count()
game_over_timer = count()












    




game_logic()
