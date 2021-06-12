import random, sys, math, time
import pygame
from pygame.locals import *


        





last_preset = []
game_height = 800
game_width = 1400
fps = 60
name = 'Sadistic Stars'
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
pygame.display.set_caption(name)





#game variables
def set_variables():
    global debugging_mode, game_on, game_height, game_width, fps, name, screen_colour
    global events, mouse_x, mouse_y, drift_speed, running, edges, bad_bullets, good_bullets
    global good_guys, bad_guys, effects, balls, explosions, bullets, map_count, map_image
    global waves, wave_done, wave_to_do_list, players_to_make, skin_l, gun_l, controls_l, players_l
    global options, wave_count, scrolling_background, tim_stats, lill_tim_stats, lill_tim2_stats, bob_stats
    global bob_body_stats, player_stats, explosion_stats, game_ready, game_started, fg, bg, load_stage
    global preset, start_cycle, cross_out, which, last_clicked, check_mark, last_clicked2, last_clicked3
    global death_counts, cross_out2, progress, wave_timer1, wave_timer2, game_over_timer, sgt, death
    global damage, kills, hours, minutes, seconds, wave, counting, time_outs, time_out_time, boss_to_do_list
    global boss_tim_stats, bombs, bomb_stats
    boss_to_do_list = []
    time_out_time = 1
    time_outs = []
    counting = False
    progress = 1
    wave = -1
    damage = 0
    kills = 0
    hours = 0
    minutes = 0
    seconds = 0
    death_counts = False
    last_clicked = None
    last_clicked2 = None
    last_clicked3 = None
    preset = []
    which = 0
    load_stage = 1
    fg = 250, 240, 230
    bg = 5, 5, 5
    cross_out = pygame.image.load('cross_out.png')
    cross_out2 = pygame.image.load('cross_out2.png')
    check_mark = pygame.image.load('check_mark.png')
    game_started = False
    map_image = pygame.transform.scale(pygame.image.load('stars.png'), (int(pygame.image.load('stars.png').get_width() * 2.3), int(pygame.image.load('stars.png').get_height() * 2.3)))
    game_ready = False
    debugging_mode = True
    game_on = False
    screen_colour = (200, 200, 200)
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
    bombs = []
    balls = []
    default_wait_wave = 5
    explosions = []
    start_cycle = True
    #          ID : [IMAGE, AIM ANGLE FLUCTUATION, TICKS BETWEEN SHOT, DAMAGE]
    bullets = {1 : ['bullet1.png', 3, 10, 8, 3],
               2 : ['bullet2.png', 20, 7, 3, .7],
               3 : ['bullet3.png', 0, 30, 38, 10],
               4 : ['bullet4.png', 40, 7, 120, 2]}
    map_count = 0
    #        ID : [TICKS BETWEEN SPAWN, SECONDS TO WAIT, LILL_TIMS, LILL_TIMS2, TIMS, BOMBS, BOBS]
    waves = {1 : [30, 0, 40, 0, 0, 0, 0, None],
             2 : [20, default_wait_wave, 40, 0, 0, 0, 0, None],
             3 : [10, default_wait_wave, 100, 0, 0, 0, 0, None],
             4 : [20, default_wait_wave, 60, 15, 0, 0, 0, None],
             5 : [12, default_wait_wave, 50, 25, 0, 0, 0, None],
             6 : [8, default_wait_wave, 80, 60, 0, 1, 0, None],
             7 : [16, default_wait_wave, 20, 60, 0, 10, 0, None],
             8 : [12, default_wait_wave, 30, 10, 1, 1, 0, None],
             9 : [16, default_wait_wave, 60, 30, 2, 4, 4, None],
             10 : [16, default_wait_wave, 60, 30, 5, 4, 4, None],
             11 : [16, default_wait_wave, 50, 50, 10, 4, 4, None],
             12 : [20, default_wait_wave, 60, 60, 15, 4, 4, None]}


    wave_done = True
    wave_to_do_list = []
    players_to_make = []
    skin_l = [1,2,3,4]
    gun_l = [1,2,3,4]
    controls_l = ['wasd', 'arrow', 'ijkl', 'tfgh']
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
                 'shoot_rate' : 120,
                 'costume_rate' : 10}

    lill_tim_stats = {'image1' : pygame.image.load('lill_tim.png'),
                      'image2' : pygame.image.load('lill_tim2.png'),
                      'health' : 3,
                      'speed' : 1,
                      'pitch' : None,
                      'roll' : None,
                      'costume_rate' : 10}
    bomb_stats = {'image1' : pygame.image.load('mine.png'),
                      'image2' : pygame.image.load('mine2.png'),
                      'image3' : pygame.image.load('mine3.png'),
                      'image4' : pygame.image.load('explosion2.png'),
                      'health' : .1,
                      'speed' : 1,
                      'range' : 200}
                      

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
                    'shotgun_count' : 20,
                    'skins' : {1 : [pygame.image.load('player1-1.png'),pygame.image.load('player1-2.png')],
                               2 : [pygame.image.load('player2-1.png'),pygame.image.load('player2-2.png')],
                               3 : [pygame.image.load('player3-1.png'),pygame.image.load('player3-2.png')],
                               4 : [pygame.image.load('player4-1.png'),pygame.image.load('player4-2.png')]}}

    explosion_stats = {'image1' : pygame.image.load('explosion.png'),
                       'length' : 15}
    boss_tim_stats = {'image1' : pygame.image.load('boss_tim1.png'),
                      'image2' : pygame.image.load('boss_tim2.png'),
                      'health' : 2000,
                      'costume_rate' : 10,
                      'x' : 600,
                      'y' : -300,
                      'fall_speed' : 1,
                      'home' : [600, 100]}
                      

    #timers
    wave_timer1 = count()
    wave_timer2 = count()
    game_over_timer = count()
    sgt = count()
    death = count()







#classes







class bomb(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.health = bomb_stats['health']
        self.X = x
        self.Y = y
        self.x = x
        self.y = y
        self.speed = bomb_stats['speed']
        pygame.sprite.Sprite.__init__(self)
        self.image1 = bomb_stats['image1']
        self.image2 = bomb_stats['image2']
        self.image3 = bomb_stats['image3']
        self.image4 = bomb_stats['image4']
        self.chosen_image = self.image1
        self.d = count()
        self.mask = maskFromSurface(self.chosen_image)
        self.costume = 0
        self.scale = 0
        self.triggered = False

    def trigger(self):
        self.triggered = True
        
    def boom(self):
        if self.d.count_loop(10):
            self.costume += 1
            if self.costume == 1:
                self.chosen_image = self.image2
            elif self.costume == 2:
                self.chosen_image = self.image3
        if self.costume >= 3:
            self.chosen_image = self.image3
            self.scale += 1
            scale_factor = self.scale / 10
            new_width = int(self.image4.get_width() * scale_factor)
            new_height = int(self.image4.get_height() * scale_factor)
            self.chosen_image = pygame.transform.scale(self.image4, (new_width, new_height))
        if self.scale == 50:
            bombs.remove(self)
            kill()
        
        

    def hit(self, dam):
        if self.health <= 0:
            self.triggered = True
        print('damage %s' % dam)
        print(self.health)
        self.health = self.health - dam
        if self.health <= 0:
            self.trigger()

    

    def loop(self):
        if self.y >= 1000:
            wave_to_do_list.append('bomb')
            bombs.remove(self)
        if self.triggered:
            self.boom()
        self.Y = self.Y + self.speed
        offsetx = self.chosen_image.get_width() // 2
        offsety = self.chosen_image.get_height() // 2
        self.x = self.X - offsetx
        self.y = self.Y - offsety
        self.mask = maskFromSurface(self.chosen_image)
        screen.blit(self.chosen_image, (self.X - offsetx, self.Y - offsety))














class boss_tim(pygame.sprite.Sprite):

    def __init__(self):
        self.health = boss_tim_stats['health']
        self.x = boss_tim_stats['x']
        self.y = boss_tim_stats['y']
        pygame.sprite.Sprite.__init__(self)
        self.image1 = boss_tim_stats['image1']
        self.image2 = boss_tim_stats['image2']
        self.chosen_image = self.image1
        self.d = count()
        self.g = count()
        self.c = count()
        self.speed = boss_tim_stats['fall_speed']
        self.costume_rate = tim_stats['costume_rate']
        self.mask = maskFromSurface(self.chosen_image)
        self.task = 'come'
        self.tasks = ['sweep']#, 'fire_down', 'fire', 'circle']
        self.sweep_speed = 1
        self.roll = .05
        self.pitch = 20
        self.homex = (boss_tim_stats['home'])[0]
        self.homey = (boss_tim_stats['home'])[1]
        self.home_speed = 1
        self.rest_time = 240
        self.sweeps = True
    
    def rest(self):
        if self.g.count_loop(10):
            bad_bullets.append(bad_bullet(1,self.x + 45,self.y + 80,180))
        if self.c.count(self.rest_time):
            self.new_task()
        

    def sweep(self):
        if self.sweeps:
            self.y = self.y + self.sweep_speed
        else:
            self.y = self.y - self.sweep_speed
        self.x = self.x + ((math.sin((self.y + 51) * self.roll)) * self.pitch)
        if self.y == 600:
            self.sweeps = False

    def go_home(self):
        x = self.homex - self.x
        y = self.homey - self.y

        print(x_, y_)


    def hit(self, dam):
        self.health = self.health - dam
        if self.health <= 0:
            if self in bad_guys:
                bad_guys.remove(self)
                kill()

    def come(self):
        self.y += self.speed
        if self.y == (boss_tim_stats['home'])[1]:
            self.new_task()

    def new_task(self):
        if self.task != 'rest':
            self.task = 'rest'
            self.c.reset_timer()
        else:
            self.task = random.choice(self.tasks)

    
    def loop(self):
        if self.task == 'come':
            self.come()
        if self.task == 'sweep':
            self.sweep()
        if self.task == 'go_home':
            self.go_home()
        if self.task == 'rest':
            self.rest()
        if self.d.count_loop(self.costume_rate):
            if self.chosen_image == self.image1:
                self.chosen_image = self.image2
            else:
                self.chosen_image = self.image1
##        if self.g.count_loop(self.shoot_rate):
##            bad_bullets.append(bad_bullet(1,self.x + 45,self.y + 80,180))
        self.mask = maskFromSurface(self.chosen_image)
        screen.blit(self.chosen_image, (self.x, self.y))











class time_out():
    def __init__(self, player):
        self.old_wave_count = wave_count
        self.player = player
        self.waves_waited = 0

    def loop(self):
        if self.old_wave_count < wave_count:
            self.waves_waited += 1
        self.old_wave_count = wave_count
        if self.waves_waited == time_out_time:
            good_guys.append(self.player)
            time_outs.remove(self)
        if self.player.player_num == 1:
            create_text(35, 0, 100, 'P-1: %s' % (time_out_time - self.waves_waited))
        if self.player.player_num == 2:
            create_text(35, 0, 200, 'P-2: %s' % (time_out_time - self.waves_waited))
        if self.player.player_num == 3:
            create_text(35, 0, 300, 'P-3: %s' % (time_out_time - self.waves_waited))
        if self.player.player_num == 4:
            create_text(35, 0, 400, 'P-4: %s' % (time_out_time - self.waves_waited))


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
            self.x = 700
            self.y = 400
            time_outs.append(time_out(self))

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
        if self.health <= 0:
            if self in bad_guys:
                bad_guys.remove(self)
                kill()


    
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
        if self.health <= 0:
            if self in bad_guys:
                bad_guys.remove(self)
                kill()



            
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
        if self.health <= 0:
            if self in bad_guys:
                bad_guys.remove(self)
                kill()


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
        self.skins = {1 : ['bad_bullet.png',2,10], 2 : ['player2-1.png',0,15] }
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

def clicked(image, x, y):
    if mouse_x > x:
        if mouse_x < (image.get_width() + x):
            if mouse_y > y:
                if mouse_y < (image.get_height() + y):
                    if 'click' in events:
                        events.remove('click')
                        return(True)
        
def create_text(size, x, y, text):
    font = pygame.font.Font(None, size)
    size = font.size(text)
    ren = font.render(text, 0, fg, bg)
    screen.blit(ren, (x, y))
    return ren
            
            
def ask_player():
    global load_stage, preset, start_cycle, which, last_clicked, last_clicked2, last_clicked3
    global wave_count, progress, last_preset, game_ready
    pygame.init()
    create_text(100, 436, 0, name)
    if load_stage == 1:
        if clicked(create_text(150, 360, 350, 'Click To Play'), 360, 350):
            load_stage = load_stage + 1
    if load_stage == 2:
        if len(last_preset) != 0:
            if clicked(create_text(150, 360, 250, 'Last Settings'), 360, 250):
                load_stage = load_stage + 3
                preset = list(last_preset)
            if clicked(create_text(150, 360, 450, 'New Settings'), 360, 450):
                load_stage = load_stage + 1
        else:
            load_stage = load_stage + 1
    if load_stage == 3:
        if clicked(create_text(150, 475, 100, '1 Player'), 475, 100):
            load_stage = load_stage + 1
            preset.append(1)
        if clicked(create_text(150, 475, 250, '2 Player'), 475, 250):
            load_stage = load_stage + 1
            preset.append(2)
        if clicked(create_text(150, 475, 400, '3 Player'), 475, 400):
            load_stage = load_stage + 1
            preset.append(3)
        if clicked(create_text(150, 475, 550, '4 Player'), 475, 550):
            load_stage = load_stage + 1
            preset.append(4)
    if load_stage == 4:
        create_text(100, 520, 100, ('Player %s' % progress))
        y = 600
        x = 80
        space = 30
        scale_factor = 2
        if sgt.count_loop(10):
            
            if start_cycle == True:
                start_cycle = False
                which = 1
            else:
                start_cycle = True
                which = 0
        create_text(85, 80, 500, 'Choose Ship')
        create_text(85, 80, 100, 'Choose Gun')
        for t in (player_stats['skins']).keys():
            image = ((player_stats['skins'])[t])[which]
            new_width = int(image.get_width() * scale_factor)
            new_height = int(image.get_height() * scale_factor)
            image = pygame.transform.scale(image, (new_width, new_height))
            new_x = x + ((space + new_width) * (t - 1))
            screen.blit((image), (new_x, y))
            if t not in skin_l:
                screen.blit(pygame.transform.scale(cross_out, (new_width, new_height)), (new_x, y))
            else:
                if clicked(image, new_x, y):
                    last_clicked = t
            if last_clicked == t:
                screen.blit(pygame.transform.scale(check_mark, (new_width, new_height)), (new_x, y))
        create_text(85, 1000, 100, 'Choose Keys')
        if clicked(create_text(60, 100, 200, '50 Cal'), 100, 200):
            last_clicked2 = 1
        if clicked(create_text(60, 100, 250, 'Chain Gun'), 100, 250):
            last_clicked2 = 2
        if clicked(create_text(60, 100, 300, 'Rail Gun'), 100, 300):
            last_clicked2 = 3
        if clicked(create_text(60, 100, 350, 'Shot Gun'), 100, 350):
            last_clicked2 = 4
        gun_dict = {1 : 162,2 : 212,3 : 262,4 : 312}
        for x in (gun_dict.keys()):
            if x == last_clicked2:
                screen.blit(pygame.transform.scale(check_mark, (new_width, new_height)), (100, gun_dict[x]))
        
        wasd = create_text(60, 1000, 200, 'WASD')
        if 'wasd' in controls_l:
            if clicked(wasd, 1000, 200):
                last_clicked3 = 'wasd'
        else:
            screen.blit(pygame.transform.scale(cross_out2, (wasd.get_width(), wasd.get_height())), (1000, 200))
        tfgh = create_text(60, 1000, 250, 'TFGH')
        if 'tfgh' in controls_l:
            if clicked(tfgh, 1000, 250):
                last_clicked3 = 'tfgh'
        else:
            screen.blit(pygame.transform.scale(cross_out2, (tfgh.get_width(), tfgh.get_height())), (1000, 250))
        ijkl = create_text(60, 1000, 300, 'IJKL')
        if 'ijkl' in controls_l:
            if clicked(ijkl, 1000, 300):
                last_clicked3 = 'ijkl'
        else:
            screen.blit(pygame.transform.scale(cross_out2, (ijkl.get_width(), ijkl.get_height())), (1000, 300))
        arrow = create_text(60, 1000, 350, 'Arrows')
        if 'arrow' in controls_l:
            if clicked(arrow, 1000, 350):
                last_clicked3 = 'arrow'
        else:
            screen.blit(pygame.transform.scale(cross_out2, (arrow.get_width(), arrow.get_height())), (1000, 350))
        controls_dict = {'wasd' : 162, 'tfgh' : 212, 'ijkl' : 262, 'arrow' : 312}
        for x in (controls_dict.keys()):
            if x == last_clicked3:
                screen.blit(pygame.transform.scale(check_mark, (new_width, new_height)), (1000, controls_dict[x]))
        if clicked(create_text(200, 900, 500, 'Done'), 900, 500):
            if progress == preset[0]:
                load_stage = load_stage + 1
            else:
                progress = progress + 1
            if last_clicked == None:
                preset.append(skin_l[0])
                skin_l.remove(skin_l[0])
            else:
                preset.append(last_clicked)
                skin_l.remove(last_clicked)
            if last_clicked2 == None:
                preset.append(gun_l[0])
            else:
                preset.append(last_clicked2)
            if last_clicked3 == None:
                preset.append(controls_l[0])
                controls_l.remove(controls_l[0])
            else:
                preset.append(last_clicked3)
                controls_l.remove(last_clicked3)
            last_clicked = None
            last_clicked2 = None
            last_clicked3 = None
    if load_stage == 5:
        for k in waves.keys():
            if k <= 10:
                y_l = 100
            else: 
                y_1 = 200
            x_l = k * 100
            if clicked(create_text(100, x_l, y_l, str(k)), x_l, y_l):
                wave_count = k - 1
                #if len(last_preset) == 0:
                last_preset = list(preset)
                game_ready = True
            
                
def kill():
    global kills
    kills = kills + 1

def stop_watch():
    global hours, minutes, seconds
    seconds = seconds + 1
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    if minutes == 60:
        minutes = 0
        hours = hours + 1
    
def damage_(damages):
    global damage
    damage = damage + damages

def touching(sprite_obj1, sprite_obj2):
    offset = [(int(sprite_obj1.x - sprite_obj2.x) // 1), (int(sprite_obj1.y - sprite_obj2.y) // 1)]
    if sprite_obj2.mask.overlap_area(sprite_obj1.mask, (offset)) != 0:
        return True
                    
def run_wave():
    global wave_done
    global wave_count
    if len(wave_to_do_list) == 0:
        wave_timer1.reset_timer()
        wave_timer2.reset_timer()
    if len(wave_to_do_list) == 0 and len(boss_to_do_list) == 0 and len(bad_guys) == 0 and len(bombs) == 0:
        wave_done = True
        if wave_count != waves.keys():
            wave_count = wave_count + 1
            wave_()
            print(waves[wave_count])
            f = (waves[wave_count])[2]
            g = (waves[wave_count])[3]
            h = (waves[wave_count])[4]
            v = (waves[wave_count])[5]
            j = (waves[wave_count])[6]
            b = (waves[wave_count])[7]
       
            for x in range(f):
                wave_to_do_list.append('lill_tim')
            for x in range(g):
                wave_to_do_list.append('lill_tim2')
            for x in range(h):
                wave_to_do_list.append('tim')
            for x in range(j):
                wave_to_do_list.append('bob')
            for x in range(v):
                wave_to_do_list.append('bomb')
            if b != None:
                boss_to_do_list.append(b)
                
        
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
            if p == 'bomb':
                x = random.choice(list(range(0, 1400)))
                bombs.append(bomb(x,-100))
            wave_to_do_list.remove(p)
        if len(wave_to_do_list) == 0 and len(bad_guys) == 0 and len(bombs) == 0:
            if len(boss_to_do_list) == 1:
                if boss_to_do_list[0] == 'boss_tim':
                    bad_guys.append(boss_tim())
                    print('added boss')
                    boss_to_do_list.remove(boss_to_do_list[0])
    

def wave_():
    global wave
    wave = wave + 1
    

def start_button():
    global game_on
    if 'space' in events or clicked(create_text(100, 350, 390, 'Ready!'), 350, 390):
        game_on = True
    
def game_over():
    pygame.init()
    font1 = pygame.font.Font(None, 100)
    text1 = "Game Over"
    size1 = font1.size(text1)
    ren1 = font1.render(text1, 0, fg, bg)
    screen.blit(ren1, (350, 390))

def search_events():
        global mouse_x
        global mouse_y
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
                        try:
                            events.remove(k)
                        except:
                            pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                events.append('click')
            if event.type == pygame.MOUSEBUTTONUP:
                try:
                    events.remove('click')
                except:
                    pass
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
def display_wave():
    fg = 250, 240, 230
    bg = 5, 5, 5
    pygame.init()
    font1 = pygame.font.Font(None, 40)
    text1 = "Wave: %s" % wave_count
    text2 = "Bad guys alive: %s" % (len(bad_guys) + len(wave_to_do_list) + len(bombs))
    size1 = font1.size(text1)
    size2 = font1.size(text2)
    ren2 = font1.render(text2, 0, fg, bg)
    ren1 = font1.render(text1, 0, fg, bg)
    screen.blit(ren2, (0, 0))
    screen.blit(ren1, (1200, 0))
    
def create_players():
    global death_counts
    for x in range(preset[0]):
        x = x + 1
        x_values = {1 : 500, 2 : 550, 3 : 600, 4 : 650}
        good_guys.append(player(x,preset.pop(-3),preset.pop(),x_values[x],390,preset.pop()))
        
    death_counts = True
#(self, num, skin, cntr, x, y, gun)


def show_stats():
    create_text(100, 300, 200, 'Kills: %s' % kills)
    create_text(100, 300, 300, 'Damage: %s' % damage)
    create_text(100, 300, 400, 'Waves: %s' % wave)
    create_text(100, 300, 500, 'Time:  %s:%s:%s' % (hours, minutes, seconds))
    if clicked(create_text(200, 900, 500, 'Done'), 900, 500):
        set_variables()
    elif 'space' in events:
        set_variables()
                
                
    





def main():
    global game_started, death_counts, counting
    screen.fill(screen_colour)
    search_events()
    if counting:
        stop_watch()
    if game_ready:
        if not game_started:
            counting = True
            start_game()
            game_started = True
            print('game started')
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
        for x in bombs:
            x.loop()
            for p in good_guys:
                if touching(p, x):
                    print('oof')
                    p.hit()
                    x.trigger()
                if p.x > (x.x - bomb_stats['range']) and p.x < (x.x + bomb_stats['range']):
                    if p.y > (x.y - bomb_stats['range']) and p.y < (x.y + bomb_stats['range']):
                        print('in range')
                        x.trigger()
            for p in good_bullets:
                if touching(p, x):
                    p.hit()
                    x.hit((bullets[p.bullet])[4])
                    explosions.append(explosion(p.x - 20, p.y - 30))
        for x in good_bullets:
            x.loop()
            for p in bad_guys:
                if touching(x, p):
                    explosions.append(explosion(x.x - 20, x.y - 30))
                    x.hit()
                    p.hit((bullets[x.bullet])[4])
                    damage_((bullets[x.bullet])[4])
        for x in bad_bullets:
            x.loop()
        for x in explosions:
            x.loop()
        for x in time_outs:
            x.loop()
        if not game_on:
            start_button()
        if death_counts:
            if len(good_guys) == 0:
                game_over()
                if game_over_timer.count(240):
                    print('game over')
                    counting = False
                    screen.fill(screen_colour)
                    create_text(100, 300, 0, 'Game Over')
                    show_stats()
                    
                    
                    
        if game_on:
#            try:
            run_wave()
#            except:
                
#                if len(waves.keys()) < wave_count:
#                    if game_over_timer.count(240):
#                        screen.fill(screen_colour)
#                        counting = False
#                        create_text(100, 300, 0, 'You Win!')
#                        show_stats()
                        
#                else:    
#                    print('Error, run_wave Failed')
        if counting:
            display_wave()
        
    else:
        ask_player()
    pygame.display.update()
    clock.tick(fps)




def start_game():
    
    create_players()
    if scrolling_background:
        effects.append(stars())
    


def quit_game():
    pygame.quit()
    sys.exit()

def game_logic():
    if not debugging_mode:
        try:
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
        while running:
            main()
        quit_game()     


#setup functions

def glide_to(x,y,newx,newy):
    x1 = newx - x
    y1 = newy - y
    angle = math.tan(y1 / x1)
    print(1 / angle)

glide_to(0,0,1,1)



#dumb game stuff



















    



set_variables()
game_logic()
