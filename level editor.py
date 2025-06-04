import pygame
import sys, random, math, fractions
import pickle
import json
import os
from spritesheet import SpriteSheet
from maketiledimage import make_tiled_image

pygame.init()
screen_Width = 720
screen_Height = 544
level_width = 4000

SIZE = WIDTH, HEIGHT = screen_Width, screen_Height
FPS = 60
BACKGROUND_COLOR = pygame.Color(92, 148, 252)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

block_sheet = SpriteSheet('grafik\sprite sheet 3.png')
item_sheet = SpriteSheet('grafik\sprite sheet 2.png')
character_sheet = SpriteSheet('grafik\sprite sheet characters.png')
mario_sheet = SpriteSheet('grafik\sprite sheet mario.png')
enemy_sheet = SpriteSheet('grafik\sprite sheet enemies.png')

pipe_image = block_sheet.image_at((0, 151, 32, 8))
pipe_top_image = block_sheet.image_at((0, 128, 32, 16), colorkey = (255, 255, 255))
pipe_bottom_image = pygame.transform.flip(pipe_top_image, False, True)

flag_pole_image = block_sheet.image_at((263, 144, 2, 16), colorkey = (255, 255, 255))
flag_pole_top_image = block_sheet.image_at((260, 136, 8, 8), colorkey = (255, 255, 255))
goal_base_image = block_sheet.image_at((0, 16, 16, 16), colorkey = (255, 255, 255))
goal_flag_image = item_sheet.image_at((128, 16, 16, 16), colorkey = (255, 255, 255))

item_block_image = block_sheet.image_at((368, 0, 16, 16), colorkey = (255, 255, 255))

empty_item_block_image = block_sheet.image_at((416, 0, 16,16), colorkey = (255, 255, 255))

fire_ball_image = enemy_sheet.image_at((26, 150, 8, 8), colorkey = (255, 255, 255))

fire_bar_image = empty_item_block_image.copy()
fire_bar_image.blit(fire_ball_image, (4, 4))

block_image = block_sheet.image_at((0, 0, 16, 16), colorkey = (255, 255, 255))

rock_image = block_sheet.image_at((16, 112, 16, 16), colorkey = (255, 255, 255))
coral_image = block_sheet.image_at((176, 288, 16, 16), colorkey = (66, 66, 255))

breakable_block_image = block_sheet.image_at((16, 0, 16, 16), colorkey = (255, 255, 255))

thin_platform_image = item_sheet.image_at((80, 64, 16, 8), colorkey = (255, 255, 255))

goomba_image_list = [character_sheet.image_at((296, 187, 16,16), colorkey = (107, 49, 156)), character_sheet.image_at((315, 187, 16,16), colorkey = (107, 49, 156))]

green_koopa_left_image_list = [character_sheet.image_at((201, 206, 16, 16), colorkey = (107, 49, 156)), character_sheet.image_at((182, 206, 16, 24), colorkey = (107, 49, 156))]
green_koopa_right_image_list = [character_sheet.image_at((296, 206, 16, 16), colorkey = (107, 49, 156)), character_sheet.image_at((315, 206, 16, 24), colorkey = (107, 49, 156))]

red_koopa_left_image_list = [character_sheet.image_at((87, 206, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((68, 206, 16, 24), colorkey = (107, 49, 156))]
red_koopa_right_image_list = [character_sheet.image_at((410, 206, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((429, 206, 16, 24), colorkey = (107, 49, 156))]

cheepcheep_image_left = [character_sheet.image_at((90, 268 ,15 ,16), colorkey = (107, 49, 156)), character_sheet.image_at((108, 268 ,16 ,16), colorkey = (107, 49, 156))]

blooper_image = [character_sheet.image_at((239, 260, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((258, 260, 16, 16), colorkey = (107, 49, 156))]

bowser_image_left = [character_sheet.image_at((187, 368, 32, 32), colorkey = (107, 49, 156))]

pirhana_plant_image = [[enemy_sheet.image_at((390, 30, 16, 24), colorkey = (255, 255, 255)), enemy_sheet.image_at((420, 29, 16, 24), colorkey = (163, 73, 164))], [enemy_sheet.image_at((390, 60, 16, 24), colorkey = (255, 255, 255)), enemy_sheet.image_at((420, 60, 16, 24), colorkey = (255, 255, 255))]]
pirhana_plant_image_down = [[],[]]
for x in range(len(pirhana_plant_image)):
    for image in pirhana_plant_image[x]:
        pirhana_plant_image_down[x].append(pygame.transform.flip(image, False, True))
pipe_bottom_image = pygame.transform.flip(pipe_top_image, False, True)

item_block_shimmer_list = [block_sheet.image_at((368, 0, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 0, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 0, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 0, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 0, 16,16), colorkey = (255, 255, 255))]

power_star_image = item_sheet.image_at((0, 32, 16,16), colorkey = (255, 255, 255))
fire_flower_image = item_sheet.image_at((0, 16, 16,16), colorkey = (255, 255, 255))


coin_shimmer_list = [item_sheet.image_at((0, 64, 16,16), colorkey = (255, 255, 255)), item_sheet.image_at((0, 64, 16,16), colorkey = (255, 255, 255)), item_sheet.image_at((0, 64, 16,16), colorkey = (255, 255, 255)), item_sheet.image_at((0, 64, 16,16), colorkey = (255, 255, 255)), item_sheet.image_at((0, 64, 16,16), colorkey = (255, 255, 255))]


small_mario_standing_right_image = character_sheet.image_at((277, 44, 12, 16), colorkey = (107, 49, 156))

peach_image_left = character_sheet.image_at((241, 161, 16, 23), colorkey = (107, 49, 156))
peach_image_right = character_sheet.image_at((258, 161, 16, 23), colorkey = (107, 49, 156))

toad_image = character_sheet.image_at((222, 160, 16, 23), colorkey = (107, 49, 156))

big_hill_image = block_sheet.image_at ((336, 331, 80, 35), colorkey = (255, 255, 255))
small_hill_image = block_sheet.image_at ((352, 331, 48, 19), colorkey = (255, 255, 255))

bush_image = block_sheet.image_at ((184, 144, 32, 16), colorkey = (255, 255, 255))

cloud_image = block_sheet.image_at ((8, 320, 32, 23), colorkey = (163, 73, 164))

castle_image = block_sheet.image_at ((176, 320, 80, 80), colorkey = (255, 255, 255))

checkpoint_image = item_sheet.image_at ((271, 66, 18, 30), colorkey = (255, 255, 255))

for x in range(3):#fetch item blocks from sprite sheet
    item_block_shimmer_list.append(block_sheet.image_at((368 + x*16, 0, 16,16), colorkey = (255, 255, 255)))
for x in range(3):#fetch coins from sprite sheet
    coin_shimmer_list.append(item_sheet.image_at((0 + x*16, 64, 16,16), colorkey = (255, 255, 255)))

castle_bridge_image = item_sheet.image_at((272, 48, 16, 16), colorkey = (163, 73, 164))
castle_axe_image = [item_sheet.image_at((288, 96, 16, 16), colorkey = (255, 255, 255)), item_sheet.image_at((304, 96, 16, 16), colorkey = (255, 255, 255)), item_sheet.image_at((320, 96, 16, 16), colorkey = (255, 255, 255)), item_sheet.image_at((336, 96, 16, 16), colorkey = (255, 255, 255))]
castle_chain_image = block_sheet.image_at((192, 256, 16, 16), colorkey = (163, 73, 164))


class General():
    def __init__(self):
        self.level = 3
        self.level_mode = 1
general = General()

class Level():
    def __init__(self):
        
        self.level_width = level_width

class Menu_backdrop(pygame.sprite.Sprite):
    def __init__(self):

        self.width = 720
        self.height = 64

        self.color = 'grey'
        
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(self.color))
        self.rect = self.image.get_rect(topleft=(0, 480))
class Menu_button(pygame.sprite.Sprite):
    def __init__(self, position, tool, icon):
        super(Menu_button, self).__init__()
        
        menu_button_group.add(self)
        menu_button_list.append(self)

        self.tool = tool

        self.width = 32
        self.height = 32

        self.color = 'white'

        self.position = pygame.math.Vector2(position)
        
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(self.color))
        self.rect = self.image.get_rect(topleft=position)

        self.icon = pygame.Surface((16, 16))
        self.icon.fill(icon)
    def update(self):
        if editor.tool == 'block':
            self.icon = block_image
        if editor.tool == 'rock':
            self.icon = rock_image
        if editor.tool == 'coral':
            self.icon = coral_image
        elif editor.tool == 'thin block':
            self.icon = thin_platform_image
        elif editor.tool == 'item block':
            self.icon = item_block_image
        elif editor.tool == 'breakable block':
            self.icon = breakable_block_image
        elif editor.tool == 'castle_bridge':
            self.icon = castle_bridge_image
        elif editor.tool == 'castle_axe':
            self.icon = castle_axe_image
        elif editor.tool == 'castle_chain':
            self.icon = castle_chain_image
        elif editor.tool == 'castle_chain':
            self.icon = castle_chain_image
        elif editor.tool == 'fire box':
            self.icon = fire_bar_image
        elif editor.tool == 'goomba':
            self.icon = goomba_image_list[0]
        elif editor.tool == 'green koopa':
            self.icon = green_koopa_left_image_list[0]
        elif editor.tool == 'red koopa':
            self.icon = red_koopa_left_image_list[0]
        elif editor.tool == 'pirhana plant':
            self.icon = pirhana_plant_image[0][0]
        elif editor.tool == 'cheepcheep':
            self.icon = cheepcheep_image_left[0]
        elif editor.tool == 'blooper':
            self.icon = blooper_image[0]
        elif editor.tool == 'bowser':
            self.icon = bowser_image_left[0]
        elif editor.tool == 'coin':
            self.icon = coin_shimmer_list[0]
        elif editor.tool == 'fire flower':
            self.icon = fire_flower_image
        elif editor.tool == 'power star':
            self.icon = power_star_image
        elif editor.tool == 'checkpoint':
            self.icon = checkpoint_image
        elif editor.tool == 'pipe up':
            self.icon = pygame.Surface((16, 16))
            self.icon.fill(pygame.Color('green'))
        elif editor.tool == 'pipe down':
            self.icon = pygame.Surface((16, 16))
            self.icon.fill(pygame.Color('dark green'))
        elif editor.tool == 'water':
            self.icon = pygame.Surface((16, 16))
            self.icon.fill(pygame.Color('blue'))
        
menu_backdrop = Menu_backdrop()
menu_items = ['select', 'block', 'coin', 'enemy', 'decorations', 'goal post', 'connect pipes', 'scale']
menu_icons = [pygame.Color('black'), pygame.Color('black'), pygame.Color('blue'), pygame.Color('yellow'), pygame.Color('yellow'), pygame.Color('red'), pygame.Color('black'), pygame.Color('black')]
        
try:
    block_file = open(f'sprites/level {general.level}/block file.pickle', 'rb')
except FileNotFoundError:
    filename = f'sprites/level {general.level}/block file.pickle'#creates new folder
    os.makedirs(os.path.dirname(filename), exist_ok=True)#creates new folder
    block_file = open(f'sprites/level {general.level}/block file.pickle', 'x')
    block_file = open(f'sprites/level {general.level}/block file.pickle', 'rb')
try:
    rock_file = open(f'sprites/level {general.level}/rock file.pickle', 'rb')
except FileNotFoundError:
    filename = f'sprites/level {general.level}/rock file.pickle'#creates new folder
    os.makedirs(os.path.dirname(filename), exist_ok=True)#creates new folder
    rock_file = open(f'sprites/level {general.level}/rock file.pickle', 'x')
    rock_file = open(f'sprites/level {general.level}/rock file.pickle', 'rb')
try:
    coral_file = open(f'sprites/level {general.level}/coral file.pickle', 'rb')
except FileNotFoundError:
    filename = f'sprites/level {general.level}/coral file.pickle'#creates new folder
    os.makedirs(os.path.dirname(filename), exist_ok=True)#creates new folder
    coral_file = open(f'sprites/level {general.level}/coral file.pickle', 'x')
    coral_file = open(f'sprites/level {general.level}/coral file.pickle', 'rb')
try:
    thin_block_file = open(f'sprites/level {general.level}/thin block file.pickle', 'rb')
except FileNotFoundError:
    thin_block_file = open(f'sprites/level {general.level}/thin block file.pickle', 'x')
    thin_block_file = open(f'sprites/level {general.level}/thin block file.pickle', 'rb')
try:
    item_block_file = open(f'sprites/level {general.level}/item block file.pickle', 'rb')
except FileNotFoundError:
    item_block_file = open(f'sprites/level {general.level}/item block file.pickle', 'x')
    item_block_file = open(f'sprites/level {general.level}/item block file.pickle', 'rb')
try:
    pipe_file = open(f'sprites/level {general.level}/pipe file.pickle', 'rb')
except FileNotFoundError:
    pipe_file = open(f'sprites/level {general.level}/pipe file.pickle', 'x')
    pipe_file = open(f'sprites/level {general.level}/pipe file.pickle', 'rb')
try:
    breakable_block_file = open(f'sprites/level {general.level}/breakable block file.pickle', 'rb')
except FileNotFoundError:
    breakable_block_file = open(f'sprites/level {general.level}/breakable block file.pickle', 'x')
    breakable_block_file = open(f'sprites/level {general.level}/breakable block file.pickle', 'rb')
try:
    castle_bridge_file = open(f'sprites/level {general.level}/castle bridge file.pickle', 'rb')
except FileNotFoundError:
    castle_bridge_file = open(f'sprites/level {general.level}/castle bridge file.pickle', 'x')
    castle_bridge_file = open(f'sprites/level {general.level}/castle bridge file.pickle', 'rb')
try:
    castle_axe_file = open(f'sprites/level {general.level}/castle axe file.pickle', 'rb')
except FileNotFoundError:
    castle_axe_file = open(f'sprites/level {general.level}/castle axe file.pickle', 'x')
    castle_axe_file = open(f'sprites/level {general.level}/castle axe file.pickle', 'rb')
try:
    castle_chain_file = open(f'sprites/level {general.level}/castle chain file.pickle', 'rb')
except FileNotFoundError:
    castle_chain_file = open(f'sprites/level {general.level}/castle chain file.pickle', 'x')
    castle_chain_file = open(f'sprites/level {general.level}/castle chain file.pickle', 'rb')
try:
    fire_box_file = open(f'sprites/level {general.level}/fire box file.pickle', 'rb')
except FileNotFoundError:
    fire_box_file = open(f'sprites/level {general.level}/fire box file.pickle', 'x')
    fire_box_file = open(f'sprites/level {general.level}/fire box file.pickle', 'rb')
try:
    enemy_file = open(f'sprites/level {general.level}//enemy file.pickle', 'rb')
except FileNotFoundError:
    enemy_file = open(f'sprites/level {general.level}/enemy file.pickle', 'x')
    enemy_file = open(f'sprites/level {general.level}/enemy file.pickle', 'rb')
try:
    cheepcheep_file = open(f'sprites/level {general.level}//cheepcheep file.pickle', 'rb')
except FileNotFoundError:
    cheepcheep_file = open(f'sprites/level {general.level}/cheepcheep file.pickle', 'x')
    cheepcheep_file = open(f'sprites/level {general.level}/cheepcheep file.pickle', 'rb')
try:
    blooper_file = open(f'sprites/level {general.level}//blooper file.pickle', 'rb')
except FileNotFoundError:
    blooper_file = open(f'sprites/level {general.level}/blooper file.pickle', 'x')
    blooper_file = open(f'sprites/level {general.level}/blooper file.pickle', 'rb')
try:
    bowser_file = open(f'sprites/level {general.level}//bowser file.pickle', 'rb')
except FileNotFoundError:
    bowser_file = open(f'sprites/level {general.level}/bowser file.pickle', 'x')
    bowser_file = open(f'sprites/level {general.level}/bowser file.pickle', 'rb')
try:
    pirhana_plant_file = open(f'sprites/level {general.level}//pirhana plant file.pickle', 'rb')
except FileNotFoundError:
    pirhana_plant_file = open(f'sprites/level {general.level}/pirhana plant file.pickle', 'x')
    pirhana_plant_file = open(f'sprites/level {general.level}/pirhana plant file.pickle', 'rb')
try:
    coin_file = open(f'sprites/level {general.level}//coin file.pickle', 'rb')
except FileNotFoundError:
    coin_file = open(f'sprites/level {general.level}/coin file.pickle', 'x')
    coin_file = open(f'sprites/level {general.level}/coin file.pickle', 'rb')
try:
    goal_post_file = open(f'sprites/level {general.level}//goal post file.pickle', 'rb')
except FileNotFoundError:
    goal_post_file = open(f'sprites/level {general.level}/goal post file.pickle', 'x')
    goal_post_file = open(f'sprites/level {general.level}/goal post file.pickle', 'rb')
try:
    checkpoint_file = open(f'sprites/level {general.level}//checkpoint file.pickle', 'rb')
except FileNotFoundError:
    checkpoint_file = open(f'sprites/level {general.level}/checkpoint file.pickle', 'x')
    checkpoint_file = open(f'sprites/level {general.level}/checkpoint file.pickle', 'rb')
try:
    water_file = open(f'sprites/level {general.level}//water file.pickle', 'rb')
except FileNotFoundError:
    water_file = open(f'sprites/level {general.level}/water file.pickle', 'x')
    water_file = open(f'sprites/level {general.level}/water file.pickle', 'rb')
try:
    decoration_file = open(f'sprites/level {general.level}//decoration file.pickle', 'rb')
except FileNotFoundError:
    decoration_file = open(f'sprites/level {general.level}/decoration file.pickle', 'x')
    decoration_file = open(f'sprites/level {general.level}/decoration file.pickle', 'rb')
try:
    player_position_file = open(f'sprites/level {general.level}//player position file.pickle', 'rb')
except FileNotFoundError:
    player_position_file = open(f'sprites/level {general.level}/player position file.pickle', 'x')
    player_position_file = open(f'sprites/level {general.level}/player position file.pickle', 'rb')

hold_left_click = None

class Editor(pygame.sprite.Sprite):

    def __init__(self, position):
        self.tool = 'block'
        self.category = 'blocks'

        self.block_category = 0
        self.enemy_category = 0
        self.item_category = 0
        self.decoration_category = 0
        
        self.image = pygame.Surface((1, 1))
        self.rect = self.image.get_rect(topleft=position)
        
        self.selected_sprite = None

        self.selected_pipe = None

        self.delete_is_pressed = False


        self.position = pygame.math.Vector2(0, 0)

    def update(self):
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0] + camera.position.x
        self.rect.y = mouse_pos[1] + camera.position.y

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            camera.position.x -= 16
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            camera.position.x += 16
        if not keys[pygame.K_LCTRL]:
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                general.level_mode -= 1
                if general.level_mode < 0:
                    general.level_mode = 0
        else:
            self.s_pressed = False
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.w_pressed == False:
                self.w_pressed = True
                general.level_mode += 1
                if general.level_mode > 2:
                    general.level_mode = 2
        else:
            self.w_pressed = False
        if camera.position.x < 0:
            camera.position.x = 0
        if keys[pygame.K_DELETE]:
            if self.delete_is_pressed == False:
                if self.selected_sprite != None:
                    if self.selected_sprite in fire_box_group:#delete fire bars
                        for fire in self.selected_sprite.fire_bar_list:
                            fire.kill()
                        self.selected_sprite.fire_bar_list.clear()
                    self.selected_sprite.kill()#delete sprite
                    self.selected_sprite = None
                    self.delete_is_pressed = True
    
        else:
            self.delete_is_pressed = False

        if keys[pygame.K_ESCAPE]:
            save()
            running = False
            pygame.quit()
        if keys[pygame.K_LCTRL] and keys[pygame.K_s]:
            save()

        if keys[pygame.K_1]:
            self.tool = 'select'
            for sprite in menu_button_group:#returns preveiously selected button to white
                sprite.image.fill(pygame.Color('white'))
            menu_button_list[0].image.fill(pygame.Color(100, 100, 100))#turns selected button grey
        if keys[pygame.K_2]:
            self.category = 'blocks'
            self.tool = block_list[self.block_category]
            for sprite in menu_button_group:
                sprite.image.fill(pygame.Color('white'))
            menu_button_list[1].image.fill(pygame.Color(100, 100, 100))
            courser_sprite.update()
            
        if keys[pygame.K_3]:
            self.category = 'enemies'
            self.tool = enemy_list[self.enemy_category]
            for sprite in menu_button_group:
                sprite.image.fill(pygame.Color('white'))
            menu_button_list[2].image.fill(pygame.Color(100, 100, 100))
            courser_sprite.update()
            
        if keys[pygame.K_0]:
            self.tool = 'scale'
            for sprite in menu_button_group:
                sprite.image.fill(pygame.Color('white'))
            menu_button_list[6].image.fill(pygame.Color(100, 100, 100))
            
        if keys[pygame.K_4]:
            self.category = 'items'
            self.tool = item_list[self.item_category]
            for sprite in menu_button_group:
                sprite.image.fill(pygame.Color('white'))
            menu_button_list[3].image.fill(pygame.Color(100, 100, 100))
            courser_sprite.update()
            menu_button_list[3].image.fill(pygame.Color(100, 100, 100))
        
        if keys[pygame.K_5]:
            self.category = 'decorations'
            self.tool = decoration_list[self.decoration_category]
            for sprite in menu_button_group:
                sprite.image.fill(pygame.Color('white'))
            menu_button_list[3].image.fill(pygame.Color(100, 100, 100))
            courser_sprite.update()
            menu_button_list[3].image.fill(pygame.Color(100, 100, 100))
            
        if keys[pygame.K_6]:
            self.tool = 'goal post'
            courser_sprite.image = pygame.Surface((4, 96))
            courser_sprite.image.fill(pygame.Color('blue'))
            for sprite in menu_button_group:
                sprite.image.fill(pygame.Color('white'))
            menu_button_list[4].image.fill(pygame.Color(100, 100, 100))
        if keys[pygame.K_7]:
            self.tool = 'connect pipes'
            courser_sprite.image = pygame.Surface((4, 4))
            courser_sprite.image.fill(pygame.Color('black'))
            for sprite in menu_button_group:
                sprite.image.fill(pygame.Color('white'))
            menu_button_list[5].image.fill(pygame.Color(100, 100, 100))


class Courser_sprite(pygame.sprite.Sprite):
    
    def __init__(self, position):
        
        self.image = pygame.Surface((16, 16))
        self.image.fill(pygame.Color('black'))
        self.rect = self.image.get_rect(topleft=position)
        self.position = position

    def update(self):
        if editor.tool == 'block':
            self.image = block_image
        if editor.tool == 'rock':
            self.image = rock_image
        if editor.tool == 'coral':
            self.image = coral_image
        elif editor.tool == 'thin block':
            self.image = thin_platform_image
        elif editor.tool == 'item block':
            self.image = item_block_image
        elif editor.tool == 'breakable block':
            self.image = breakable_block_image
        elif editor.tool == 'castle bridge':
            self.image = castle_bridge_image
        elif editor.tool == 'castle axe':
            self.image = castle_axe_image[0]
        elif editor.tool == 'castle chain':
            self.image = castle_chain_image
        elif editor.tool == 'fire box':
            self.image = fire_bar_image
        elif editor.tool == 'goomba':
            self.image = goomba_image_list[0]
        elif editor.tool == 'green koopa':
            self.image = green_koopa_left_image_list[0]
        elif editor.tool == 'red koopa':
            self.image = red_koopa_left_image_list[0]
        elif editor.tool == 'pirhana plant':
            self.image = pirhana_plant_image[0][0]
        elif editor.tool == 'cheepcheep':
            self.image = cheepcheep_image_left[0]
        elif editor.tool == 'blooper':
            self.image = blooper_image[0]
        elif editor.tool == 'bowser':
            self.image = bowser_image_left[0]
        elif editor.tool == 'coin':
            self.image = coin_shimmer_list[0]
        elif editor.tool == 'fire flower':
            self.image = fire_flower_image
        elif editor.tool == 'power star':
            self.image = power_star_image
        elif editor.tool == 'pipe up':
            self.image = pipe_top_image
        elif editor.tool == 'pipe down':
            self.image = pipe_bottom_image
        elif editor.tool == 'water':
            self.image = pygame.Surface((16, 16))
            self.image.fill(pygame.Color('blue'))
        elif editor.tool == 'peach':
            self.image = peach_image_left
        elif editor.tool == 'toad':
            self.image = toad_image
        elif editor.tool == 'bush':
            self.image = bush_image
        elif editor.tool == 'small hill':
            self.image = small_hill_image
        elif editor.tool == 'big hill':
            self.image = big_hill_image
        elif editor.tool == 'cloud':
            self.image = cloud_image
        elif editor.tool == 'castle':
            self.image = castle_image
        elif editor.tool == 'checkpoint':
            self.image = checkpoint_image
    

def save():
    with open(f'sprites/level {general.level}/block file.pickle', 'wb') as handle:
        for sprite in block_group:
            pickle.dump([sprite.position, sprite.width, sprite.height], handle)
        handle.close()
    with open(f'sprites/level {general.level}/rock file.pickle', 'wb') as handle:
        for sprite in rock_group:
            pickle.dump([sprite.position, sprite.width, sprite.height], handle)
        handle.close()
    with open(f'sprites/level {general.level}/coral file.pickle', 'wb') as handle:
        for sprite in coral_group:
            pickle.dump([sprite.position, sprite.width, sprite.height], handle)
        handle.close()
    with open(f'sprites/level {general.level}/thin block file.pickle', 'wb') as handle:
        for sprite in thin_block_group:
            pickle.dump([sprite.position, sprite.width], handle)
        handle.close()
    with open(f'sprites/level {general.level}/item block file.pickle', 'wb') as handle:
        for sprite in item_block_group:
            pickle.dump([sprite.position, sprite.item], handle)
        handle.close()
    with open(f'sprites/level {general.level}/breakable block file.pickle', 'wb') as handle:
        for sprite in breakable_block_group:
            pickle.dump([sprite.position, sprite.item], handle)
        handle.close()
    with open(f'sprites/level {general.level}/castle bridge file.pickle', 'wb') as handle:
        for sprite in castle_bridge_group:
            pickle.dump([sprite.position], handle)
        handle.close()
    with open(f'sprites/level {general.level}/castle axe file.pickle', 'wb') as handle:
        for sprite in castle_axe_group:
            pickle.dump([sprite.position], handle)
        handle.close()
    with open(f'sprites/level {general.level}/castle chain file.pickle', 'wb') as handle:
        for sprite in castle_chain_group:
            pickle.dump([sprite.position], handle)
        handle.close()
    with open(f'sprites/level {general.level}/fire box file.pickle', 'wb') as handle:
        for sprite in fire_box_group:
            pickle.dump([sprite.position, sprite.length, sprite.direction], handle)
        handle.close()
    with open(f'sprites/level {general.level}/pipe file.pickle', 'wb') as handle:
        for sprite in pipe_group:
            pickle.dump([sprite.position, sprite.height, sprite.warp_position, sprite.direction, sprite.warp_direction], handle)
        handle.close()
    with open(f'sprites/level {general.level}/enemy file.pickle', 'wb') as handle:
        for sprite in enemy_group:
            pickle.dump([sprite.position, sprite.enemy_type], handle)
        handle.close()
    with open(f'sprites/level {general.level}/cheepcheep file.pickle', 'wb') as handle:
        for sprite in cheepcheep_group:
            pickle.dump([sprite.position], handle)
        handle.close()
    with open(f'sprites/level {general.level}/blooper file.pickle', 'wb') as handle:
        for sprite in blooper_group:
            pickle.dump([sprite.position], handle)
        handle.close()
    with open(f'sprites/level {general.level}/bowser file.pickle', 'wb') as handle:
        for sprite in bowser_group:
            pickle.dump([sprite.position], handle)
        handle.close()
    with open(f'sprites/level {general.level}/pirhana plant file.pickle', 'wb') as handle:
        for sprite in pirhana_plant_group:
            pickle.dump([sprite.position], handle)
        handle.close()
    with open(f'sprites/level {general.level}/coin file.pickle', 'wb') as handle:
        for sprite in coin_group:
            pickle.dump([sprite.position], handle)
        handle.close()
    with open(f'sprites/level {general.level}/goal post file.pickle', 'wb') as handle:
        for sprite in goal_post_group:
            pickle.dump([sprite.position], handle)
    with open(f'sprites/level {general.level}/water file.pickle', 'wb') as handle:
        for sprite in water_group:
            pickle.dump([sprite.position, sprite.width, sprite.height], handle)
        handle.close()
    with open(f'sprites/level {general.level}/player position file.pickle', 'wb') as handle:
        pickle.dump([player.position], handle)
        handle.close()
    with open(f'sprites/level {general.level}/decoration file.pickle', 'wb') as handle:
        for sprite in decoration_group:
            pickle.dump([sprite.position, sprite.type], handle)
        handle.close()
    with open(f'sprites/level {general.level}/checkpoint file.pickle', 'wb') as handle:
        for sprite in checkpoint_group:
            pickle.dump([sprite.position], handle)
        handle.close()
    
                
class Player(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Player, self).__init__()
        all_sprite_group.add(self)
        player_list.append(self)
        self.width = 16
        self.height = 16

        self.color = 'green'
        
        self.image = small_mario_standing_right_image
        self.rect = self.image.get_rect(topleft=position)

        self.jump = False#checks if you have performed a jump
        self.crouch = False
        self.standing = False#checks if you are standing
        self.wall_slide = False#checks if you are sliding on wall
        self.wall_jump = False#checks if you have performed a wall jump
        self.hold_jump = False
        self.speed = 4
        self.tall = False
        self.fire_form = False
        self.direction = 'right'
        self.attack_button_pressed = False
        self.jump_button_pressed = False
        self.x = 0

        self.coins = 0
        self.coin_text = coin_text_font.render(f'{self.coins}', True, (0, 0, 0))
        
        self.invincibility_time = 1000
        self.invincibility = False
        self.invincibility_jitter = False
        
        self.dead = False

        self.position = pygame.math.Vector2(position)
        self.velocity = pygame.math.Vector2(0, 0)

        self.time = None
        self.time2 = None
        
class Camera(pygame.sprite.Sprite):
    
    def __init__(self, position):
        super(Camera, self).__init__()

        self.position = pygame.math.Vector2(position)

    def update(self):
        if general.level_mode == 2:
            self.position.y = -800
        elif general.level_mode == 1:
            self.position.y = 0
        elif general.level_mode == 0:
            self.position.y = 640

class Decoration(pygame.sprite.Sprite):

    def __init__(self, position, image):
        super(Decoration, self).__init__()
        all_sprite_group.add(self)
        decoration_group.add(self)

        self.position = pygame.math.Vector2(position)

        self.type = image
        
        if image == 'peach':
            self.image = peach_image_left
        if image =='toad':
            self.image = toad_image
        if image =='bush':
            self.image = bush_image
        if image =='small hill':
            self.image = small_hill_image
        if image =='big hill':
            self.image = big_hill_image
        if image =='cloud':
            self.image = cloud_image
        if image =='castle':
            self.image = castle_image
        
        self.rect = self.image.get_rect(topleft = self.position)

        
        
class Block(pygame.sprite.Sprite):

    def __init__(self, position, width, height):
        super(Block, self).__init__()
        
        block_group.add(self)
        all_sprite_group.add(self)

        self.breakable = False
        self.thin = False
        self.item_block = False

        self.width = width
        
        self.height = height


        self.image = make_tiled_image(block_image, self.width, self.height )
        
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)
class Rock(pygame.sprite.Sprite):

    def __init__(self, position, width, height):
        super(Rock, self).__init__()
        
        rock_group.add(self)
        all_sprite_group.add(self)

        self.breakable = False
        self.thin = False
        self.item_block = False

        self.width = width
        
        self.height = height


        self.image = make_tiled_image(rock_image, self.width, self.height)
        
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)
class Coral(pygame.sprite.Sprite):

    def __init__(self, position, width, height):
        super(Coral, self).__init__()
        
        coral_group.add(self)
        all_sprite_group.add(self)

        self.breakable = False
        self.thin = False
        self.item_block = False

        self.width = width
        
        self.height = height


        self.image = make_tiled_image(coral_image, self.width, self.height, colorkey = (0, 0, 0))
        
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)


class Item_block(pygame.sprite.Sprite):

    def __init__(self, position, item):
        super(Item_block, self).__init__()
        
        item_block_group.add(self)
        all_sprite_group.add(self)

        self.breakable = False
        self.thin = False
        self.item_block = True
        self.item = item
        if item == None:
            self.item = None
        if self.item == 'fire flower':
            self.item_image = fire_flower_image
        elif self.item == 'power star':
            self.item_image = power_star_image
        elif self.item == 'coin':
            self.item_image = coin_shimmer_list[0]

        self.quantity = None
        self.time = None
        self.expiration_time = 3000
        
        self.width = 16
        self.height = 16

        self.image = item_block_image

        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

class Breakable_block(pygame.sprite.Sprite):

    def __init__(self, position, item):
        super(Breakable_block, self).__init__()
        all_sprite_group.add(self)
        breakable_block_group.add(self)

        self.breakable = True
        self.thin = False
        self.item_block = True

        self.item = item
        if self.item == 'fire flower':
            self.item_image = fire_flower_image
        elif self.item == 'power star':
            self.item_image = power_star_image
        elif self.item == 'coin':
            self.item_image = coin_shimmer_list[0]
        else:
            self.item_image = None
        
        self.width = 16
        self.height = 16


        self.image = breakable_block_image

        
        
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)
        self.animation_frame = 0

        sprite_replace_check(self)

class Castle_bridge(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Castle_bridge, self).__init__()
        
        castle_bridge_group.add(self)
        all_sprite_group.add(self)

        self.breakable = False
        self.thin = False
        self.item_block = False

        self.fall = False

        self.width = 16
        
        self.height = 16

        self.image = castle_bridge_image
        
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

class Castle_axe(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Castle_axe, self).__init__()

        castle_axe_group.add(self)
        all_sprite_group.add(self)

        self.width = 16
        
        self.height = 16

        self.hit = False

        self.image = castle_axe_image[0]
        
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

class Castle_chain(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Castle_chain, self).__init__()

        castle_chain_group.add(self)
        all_sprite_group.add(self)

        self.width = 16
        
        self.height = 16

        self.image = castle_chain_image
        
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

class Pipe(pygame.sprite.Sprite):

    def __init__(self, position, height, warp_position, direction, warp_direction):
        super(Pipe, self).__init__()
        all_sprite_group.add(self)
        pipe_group.add(self)
        self.breakable = True
        self.thin = False
        self.item_block = False

        self.warp_position = warp_position#where the player is warped to if entering the pipe
        self.warp_direction = warp_direction#the direction of the pipe the player is warped to
        
        self.width = 32
        self.height = height

        self.direction = direction

        self.image = make_tiled_image(pipe_image, self.width, self.height, colorkey = (255, 255, 255) )
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        sprite_replace_check(self)

class Thin_block(pygame.sprite.Sprite):

    def __init__(self, position, width):
        super(Thin_block, self).__init__()
        
        thin_block_group.add(self)
        all_sprite_group.add(self)

        self.breakable = False
        self.thin = True
        self.item_block = False
        
        self.width = width
        self.height = 8

        self.color = 'black'

        self.image = make_tiled_image(thin_platform_image, self.width, self.height, colorkey = (255, 255, 255) )
        self.rect = pygame.Surface ((self.width, 16)).get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        sprite_replace_check(self)

class Fire_box(pygame.sprite.Sprite):

    def __init__(self, position, length, direction):
        super(Fire_box, self).__init__()

        all_sprite_group.add(self)
        fire_box_group.add(self)

        self.bounce_offset = 0

        self.width = 16
        
        self.height = 16

        self.image = empty_item_block_image
        
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        self.length = length
        self.direction = direction

        self.fire_bar_list = []

        for x in range(self.length):#instanciate fire bar
            fire_bar = Fire_bar(position = (self.position.x, self.position.y - x*8), box = self)
            self.fire_bar_list.append(fire_bar)
        if direction == None:#sets default direction (up) if this is a new sprite
            self.direction = self.fire_bar_list[-1].position - self.position
            self.direction = self.direction.normalize()
        for i in range(len(self.fire_bar_list)):#sets saved direction if loaded from a file
            self.fire_bar_list[i].rect.x = self.rect.x - self.direction[0]*(i*8) + 4
            self.fire_bar_list[i].rect.y = self.rect.y - self.direction[1]*(i*8) + 4

    def update(self):
        position = self.position.copy()
        position.x += 8
        position.y += 8
        distance = position.distance_to((mouse_pos_x + camera.position.x, mouse_pos_y + camera.position.y)) // 8 + 1
        distance = int(distance)
        remove_list = []
        if distance > self.length:
            distance -= self.length
            for x in range(distance):
                fire_bar = Fire_bar(position = (self.position.x, self.position.y - x*8), box = self)
                self.fire_bar_list.append(fire_bar)
            self.length += distance
        elif distance < self.length:
            distance = distance - self.length
            
            for x in range(-distance):
                if len(self.fire_bar_list) > 4:
                    remove_list.append(self.fire_bar_list[x])
            for x in remove_list:
                if len(self.fire_bar_list) > 4:
                    x.kill()
                    self.fire_bar_list.remove(x)
            remove_list.clear()
            self.length += distance
            if self.length < 4:#minimum length
                self.length = 4
        print(self.length)
        
        for i in range(len(self.fire_bar_list)):
            self.fire_bar_list[i].rect.x = self.rect.x - self.direction[0]*(i*8) + 4
            self.fire_bar_list[i].rect.y = self.rect.y - self.direction[1]*(i*8) + 4
        
class Fire_bar(pygame.sprite.Sprite):

    def __init__(self, position, box):
        super(Fire_bar, self).__init__()

        fire_bar_group.add(self)
        all_sprite_group.add(self)

        self.box = box

        self.width = 8
        
        self.height = 8

        self.image = fire_ball_image
        
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

class Water(pygame.sprite.Sprite):

    def __init__(self, position, width, height):
        super(Water, self).__init__()
        
        water_group.add(self)
        all_sprite_group.add(self)
        
        self.width = width
        self.height = height

        self.color = 'blue'

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(self.color))
        self.rect = pygame.Surface ((self.width, self.height)).get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)
        
class Super_mushroom(pygame.sprite.Sprite):

    def __init__(self, position, spawn_counter):
        super(Super_mushroom, self).__init__()

        super_mushroom_group.add(self)

        self.width = 16
        self.height = 16

        self.color = 'dark green'
        
        self.speed = 1
        self.direction = 'left'
        self.spawn_counter = spawn_counter
        
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(self.color))
        self.rect = self.image.get_rect(bottomleft=position)
        self.position = pygame.math.Vector2(position)

        self.velocity = pygame.math.Vector2(0, 0)



class Fire_flower(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Fire_flower, self).__init__()

        fire_flower_group.add(self)
        all_sprite_group.add(self)
        
        self.width = 16
        self.height = 16

        self.color = 'white'
        
        self.speed = 1
        self.direction = 'left'
        
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color(self.color))
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        self.velocity = pygame.math.Vector2(0, 0)

        for sprite in item_block_group:
            if self.rect.colliderect(sprite):
                sprite.item = 'fire flower'
                sprite.quantity = 1
                sprite.item_image = fire_flower_image
                self.kill()
        for sprite in breakable_block_group:
            if self.rect.colliderect(sprite):
                sprite.item = 'fire flower'
                sprite.quantity = 1
                sprite.item_image = fire_flower_image
                self.kill()

class Coin(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Coin, self).__init__()

        coin_group.add(self)
        all_sprite_group.add(self)

        self.size = 16

        self.color = 'yellow'
        
        self.image = coin_shimmer_list[0]
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        self.velocity = pygame.math.Vector2(0, 0)

        for sprite in item_block_group:
            if self.rect.colliderect(sprite):
                sprite.item = 'coin'
                sprite.quantity = 10
                coin_group.remove(self)
                sprite.item_image = coin_shimmer_list[0]
                self.kill()
        for sprite in breakable_block_group:
            if self.rect.colliderect(sprite):
                sprite.item = 'coin'
                sprite.quantity = 10
                coin_group.remove(self)
                sprite.item_image = coin_shimmer_list[0]
                self.kill()
        for sprite in coin_group:
            if sprite != self:
                if self.rect.colliderect(sprite):
                    self.kill()
            
class Power_star(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Power_star, self).__init__()

        power_star_group.add(self)
        all_sprite_group.add(self)

        self.width = 16
        self.height = 16

        self.direction = 'right'

        self.speed = 2 

        self.image = power_star_image

        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        for sprite in item_block_group:
            if self.rect.colliderect(sprite):
                sprite.item = 'power star'
                sprite.quantity = 1
                power_star_group.remove(self)
                sprite.item_image = power_star_image
                self.kill()
        for sprite in breakable_block_group:
            if self.rect.colliderect(sprite):
                sprite.item = 'power star'
                sprite.quantity = 1
                power_star_group.remove(self)
                sprite.item_image = power_star_image
                self.kill()
        
class Enemy(pygame.sprite.Sprite):

    def __init__(self, position, enemy_type):
        super(Enemy, self).__init__()

        enemy_group.add(self)
        all_sprite_group.add(self)

        self.width = 16
        self.height = 16

        self.enemy_type = enemy_type
        
        self.speed = 1
        self.direction = 'left'
        self.standing = False

        self.image = pygame.Surface((self.width, self.height))
        #self.image.fill(pygame.Color('blue'))
        if self.enemy_type == 'goomba':
            self.image = goomba_image_list[0]
        elif self.enemy_type == 'green koopa':
            self.image = green_koopa_left_image_list[0]
        elif self.enemy_type == 'red koopa':
            self.image = red_koopa_left_image_list[0]
        else:
            print(self.enemy_type)
            self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        self.velocity = pygame.math.Vector2(0, 0)

class Cheepcheep(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Cheepcheep, self).__init__()

        cheepcheep_group.add(self)
        all_sprite_group.add(self)

        self.enemy_type = 'cheepcheep'

        #hit boxes
        self.width = 16
        self.height = 16
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)
        self.position_rect = self.image.get_rect(topleft = position)

        self.image = cheepcheep_image_left[0]
        

        self.position = pygame.math.Vector2(position)

class Blooper(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Blooper, self).__init__()

        blooper_group.add(self)
        all_sprite_group.add(self)

        self.enemy_type = 'blooper'

        #hit boxes
        self.width = 10
        self.height = 6

        self.image = blooper_image[0]
        self.rect = self.image.get_rect(topleft = position)


        self.position = pygame.math.Vector2(position)

class Bowser(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Bowser, self).__init__()

        bowser_group.add(self)
        all_sprite_group.add(self)

        self.enemy_type = 'bowser'
        
        #hit boxes
        self.width = 28
        self.height = 28
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)
        self.sub_position_x = 0

        self.position_rect = self.image.get_rect(topleft = position)

        self.hit_box_image = pygame.Surface((self.width, self.height))
        

        self.image = bowser_image_left[0]
                
        self.position = pygame.math.Vector2(position)
        
        self.velocity = pygame.math.Vector2(0, 0)

class Pirhana_plant(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Pirhana_plant, self).__init__()

        pirhana_plant_group.add(self)
        all_sprite_group.add(self)

        self.animation_frame = 0

        self.width = 16
        self.height = 20
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)
        self.position_rect = self.image.get_rect(topleft = position)

        self.hitbox_image = pygame.Surface((self.width, self.height))
        

        self.position = pygame.math.Vector2(position)

        in_pipe = False
        for pipe in pipe_group:
            if self.rect.colliderect(pipe.rect):
                if pipe.direction == 'up':
                    self.rect.x = pipe.rect.x + 8
                    self.rect.y = pipe.rect.y
                    self.position[0] = self.rect.x
                    self.position[1] = self.rect.y
                    self.direction = 'up'
                    self.image = pirhana_plant_image[0][0]
                elif pipe.direction == 'down':
                    self.rect.x = pipe.rect.x + 8
                    self.rect.y = pipe.rect.bottom - 24
                    self.position[0] = self.rect.x
                    self.position[1] = self.rect.y
                    self.direction = 'down'
                    self.image = pirhana_plant_image_down[0][0]
                in_pipe = True
        if in_pipe == False:
            self.kill()

class Goal_post(pygame.sprite.Sprite):
    
    def __init__(self, position):
        super(Goal_post, self).__init__()
        
        all_sprite_group.add(self)
        goal_post_group.add(self)

        self.width = 4
        self.height = 160

        self.color = 'blue'

        self.image = make_tiled_image(flag_pole_image, self.width, self.height )
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)
        
        self.goal_flag = Goal_flag(position = (self.position[0] - 8, self.position[1] + 8))
        self.goal_base = Goal_base(position = self.position)

class Goal_flag(pygame.sprite.Sprite):
    
    def __init__(self, position):
        super(Goal_flag, self).__init__()

        goal_flag_group.add(self)

        self.width = 16
        self.height = 16

        self.image = goal_flag_image
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

class Goal_base(pygame.sprite.Sprite):
    
    def __init__(self, position):
        super(Goal_base, self).__init__()

        goal_base_group.add(self)

        self.item_block = False
        self.thin = False

        self.width = 16
        self.height = 16

        self.image = goal_base_image
        self.rect = self.image.get_rect(topleft=position)
        self.rect.y += 144
        self.position = pygame.math.Vector2(position)
        self.position.y += 144

def sprite_replace_check(Self):
    for sprite in all_sprite_group:
        if Self.rect.colliderect(sprite):
            if Self != sprite:
                if sprite not in water_group:
                    if sprite not in fire_bar_group:
                        sprite.kill()

class Checkpoint(pygame.sprite.Sprite):
    
    def __init__(self, position):
        super(Checkpoint, self).__init__()

        checkpoint_group.add(self)
        all_sprite_group.add(self)

        self.image = checkpoint_image

        self.rect = self.image.get_rect(topleft=position)

        self.position = pygame.math.Vector2(position)


#create groups 
all_sprite_group = pygame.sprite.Group()

item_block_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
rock_group = pygame.sprite.Group()
coral_group = pygame.sprite.Group()
thin_block_group = pygame.sprite.Group()
breakable_block_group = pygame.sprite.Group()
castle_bridge_group = pygame.sprite.Group()
castle_axe_group = pygame.sprite.Group()
castle_chain_group = pygame.sprite.Group()
fire_box_group = pygame.sprite.Group()
fire_bar_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
cheepcheep_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
flattened_enemy_group = pygame.sprite.Group()
flipped_enemy_group = pygame.sprite.Group()
blooper_group = pygame.sprite.Group()
bowser_group = pygame.sprite.Group()
pirhana_plant_group = pygame.sprite.Group()
super_mushroom_group = pygame.sprite.Group()
fire_flower_group = pygame.sprite.Group()
fire_ball_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
power_star_group = pygame.sprite.Group()
show_coin_group = pygame.sprite.Group()
goal_post_group = pygame.sprite.Group()
goal_flag_group = pygame.sprite.Group()
goal_base_group = pygame.sprite.Group()
menu_button_group = pygame.sprite.Group()
menu_icon_group = pygame.sprite.Group()
decoration_group = pygame.sprite.Group()
checkpoint_group = pygame.sprite.Group()

player_list = []
menu_button_list = []

block_list = ['block', 'thin block', 'item block', 'breakable block', 'pipe up', 'pipe down', 'water', 'rock', 'coral', 'fire box', 'castle bridge', 'castle axe', 'castle chain', 'checkpoint']
enemy_list = ['goomba', 'green koopa', 'red koopa', 'pirhana plant', 'cheepcheep', 'blooper', 'bowser']
item_list = ['coin', 'fire flower', 'power star']
decoration_list = ['peach', 'toad', 'bush', 'small hill', 'big hill', 'cloud', 'castle']

general = General()

coin_text_font = pygame.font.SysFont('freesansbold.ttf', 30)

try:
    while True:
        block_data = pickle.load(block_file)
        block = Block(position = block_data[0], width = block_data[1], height = block_data[2])
except EOFError:
    pass
try:
    while True:
        rock_data = pickle.load(rock_file)
        rock = Rock(position = rock_data[0], width = rock_data[1], height = rock_data[2])
except EOFError:
    pass
try:
    while True:
        coral_data = pickle.load(coral_file)
        coral = Coral(position = coral_data[0], width = coral_data[1], height = coral_data[2])
except EOFError:
    pass
try:
    while True:
        thin_block_data = pickle.load(thin_block_file)
        thin_block = Thin_block(position = thin_block_data[0], width = thin_block_data[1])
except EOFError:
    pass
try:
    while True:
        item_block_data = pickle.load(item_block_file)
        item_block = Item_block(position = item_block_data[0], item = item_block_data[1])
except EOFError:
    pass
try:
    while True:
        breakable_block_data = pickle.load(breakable_block_file)
        breakable_block = Breakable_block(position = breakable_block_data[0], item = breakable_block_data[1])
except EOFError:
    pass
try:
    while True:
        castle_bridge_data = pickle.load(castle_bridge_file)
        castle_bridge = Castle_bridge(position = castle_bridge_data[0])
except EOFError:
    pass
try:
    while True:
        castle_axe_data = pickle.load(castle_axe_file)
        castle_axe = Castle_axe(position = castle_axe_data[0])
except EOFError:
    pass
try:
    while True:
        castle_chain_data = pickle.load(castle_chain_file)
        castle_chain = Castle_chain(position = castle_chain_data[0])
except EOFError:
    pass
try:
    while True:
        fire_box_data = pickle.load(fire_box_file)
        fire_box = Fire_box(position = fire_box_data[0], length = fire_box_data[1], direction = fire_box_data[2])
except EOFError:
    pass
try:
    while True:
        pipe_data = pickle.load(pipe_file)
        pipe = Pipe(position = pipe_data[0], height = pipe_data[1], warp_position = pipe_data[2], direction = pipe_data[3], warp_direction = pipe_data[4])
        print(pipe.warp_direction)
except EOFError:
    pass
try:
    while True:
        enemy_data = pickle.load(enemy_file)
        enemy = Enemy(position = enemy_data[0], enemy_type = enemy_data[1])

except EOFError:
    pass
try:
    while True:
        cheepcheep_data = pickle.load(cheepcheep_file)
        cheepcheep = Cheepcheep(position = cheepcheep_data[0])
except EOFError:
    pass
try:
    while True:
        blooper_data = pickle.load(blooper_file)
        blooper = Blooper(position = blooper_data[0])
except EOFError:
    pass
try:
    while True:
        bowser_data = pickle.load(bowser_file)
        bowser = Bowser(position = bowser_data[0])
except EOFError:
    pass
try:
    while True:
        pirhana_plant_data = pickle.load(pirhana_plant_file)
        pirhana_plant = Pirhana_plant(position = pirhana_plant_data[0])
except EOFError:
    pass
try:
    while True:
        coin_data = pickle.load(coin_file)
        coin = Coin(position = coin_data[0])
except EOFError:
    pass
try:
    while True:
        goal_post_data = pickle.load(goal_post_file)
        goal_post = Goal_post(position = goal_post_data[0])
except EOFError:
    pass
try:
    while True:
        checkpoint_data = pickle.load(checkpoint_file)
        checkpoint = Checkpoint(position = checkpoint_data[0])
except EOFError:
    pass
try:
    while True:
        water_data = pickle.load(water_file)
        water = Water(position = water_data[0], width = water_data[1], height = water_data[2])
except EOFError:
    pass
try:
    while True:
        decoration_data = pickle.load(decoration_file)
        decoration = Decoration(position = decoration_data[0], image = decoration_data[1])
except EOFError:
    pass
try:
    while True:
        player_position_data = pickle.load(player_position_file)
        print(player_position_data)
        player = Player(position=(player_position_data[0]))
except EOFError:
    pass
if len(player_list) == 0:#creates player sprite if one doesn't exist
    player = Player(position =(0, 0))
    

editor = Editor(position =(0, 0))
courser_sprite = Courser_sprite(position = editor.position)
camera = Camera(position = (0, 0))
for x in range(len(menu_items)):
    menu_button = Menu_button(position = (16 + x*64 , 496), tool = menu_items[x], icon = menu_icons[x])


running = True
while running:
    clock.tick(FPS)
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    for e in pygame.event.get():#button inputs
        if e == pygame.QUIT:
            Running = False
        if e.type == pygame.KEYDOWN and e.type == pygame.K_ESCAPE:
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN:#Mouse click
            if editor.tool != 'select' and editor.tool != 'scale':
                if e.button == 4:#scrollwheel up
                    print('down')
                    if editor.category == 'blocks':#scroll up through differect blocks
                        editor.block_category -= 1
                        if editor.block_category < 0:#restricts to 0
                            editor.block_category = 0
                        editor.tool = block_list[editor.block_category]
                        print(editor.block_category)
                    if editor.category == 'enemies':#scroll up through differect enemies
                        editor.enemy_category -= 1
                        if editor.enemy_category < 0:#restricts to 0
                            editor.enemy_category = 0
                        editor.tool = enemy_list[editor.enemy_category]
                        print(editor.tool)
                    if editor.category == 'items':#scroll up through differect items
                        editor.item_category -= 1
                        if editor.item_category < 0:#restricts to 0
                            editor.item_category = 0
                        editor.tool = item_list[editor.item_category]
                        print(editor.item_category)
                    if editor.category == 'decorations':#scroll up through differect items
                        editor.decoration_category -= 1
                        if editor.decoration_category < 0:#restricts to 0
                            editor.decoration_category = 0
                        editor.tool = decoration_list[editor.decoration_category]
                        print(editor.decoration_category)
                    courser_sprite.update()
                    if editor.category == 'blocks':
                        menu_button_list[1].update()
                    if editor.category == 'enemies':
                        menu_button_list[2].update()
                    if editor.category == 'items':
                        menu_button_list[3].update()
                    if editor.category == 'decorations':
                        menu_button_list[4].update()
                    
                    print(editor.tool)
                if e.button == 5:#scrollwheel down
                    print('up')
                    if editor.category == 'blocks':#scroll down through differect blocks
                        editor.block_category += 1
                        if editor.block_category >= len(block_list):#restricts to amount of different blocks
                            editor.block_category = (len(block_list) -1)
                        editor.tool = block_list[editor.block_category]
                        print(editor.block_category)
                    if editor.category == 'enemies':#scroll down through differect enemies
                        editor.enemy_category += 1
                        if editor.enemy_category >= len(enemy_list):#restricts to amount of different enemies
                            editor.enemy_category = (len(enemy_list) -1)
                        editor.tool = enemy_list[editor.enemy_category]
                        print(editor.tool)
                    if editor.category == 'items':#scroll down through differect items
                        editor.item_category += 1
                        if editor.item_category >= len(item_list):#restricts to amount of different items
                            editor.item_category = (len(item_list) -1)
                        editor.tool = item_list[editor.item_category]
                        print(editor.item_category)
                    if editor.category == 'decorations':#scroll up through differect decorations
                        editor.decoration_category += 1
                        if editor.decoration_category >= len(decoration_list):#restricts to amount of different decorations
                            editor.decoration_category = (len(decoration_list) -1)
                        editor.tool = decoration_list[editor.decoration_category]
                        print(editor.decoration_category)
                    courser_sprite.update()
                    if editor.category == 'blocks':
                        menu_button_list[1].update()
                    if editor.category == 'enemies':
                        menu_button_list[2].update()
                    if editor.category == 'items':
                        menu_button_list[3].update()
                    if editor.category == 'decorations':
                        menu_button_list[4].update()
                    print(editor.tool)
                
            if e.button == 1:#left click
                for button in menu_button_group:
                    editor.rect.x -= camera.position.x
                    if editor.rect.colliderect(button):
                        editor.tool = button.tool
                        courser_sprite.image = button.icon
                        for sprite in menu_button_group:#returns preveiously selected button to white
                            sprite.image.fill(pygame.Color('white'))
                        button.image.fill(pygame.Color(100, 100, 100))#turns selected button grey
                    editor.rect.x += camera.position.x
                if mouse_pos_y <= 480:
                    if editor.tool == 'block':
                        block = Block(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), width = 16, height = 16)
                        hold_left_click = block
                    if editor.tool == 'rock':
                        rock = Rock(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), width = 16, height = 16)
                        hold_left_click = rock
                    if editor.tool == 'coral':
                        coral = Coral(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), width = 16, height = 16)
                        hold_left_click = coral
                    if editor.tool == 'thin block':
                        thin_block = Thin_block(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), width = 16)
                        hold_left_click = thin_block
                    if editor.tool == 'item block':
                        item_block = Item_block(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), item = None)
                    if editor.tool == 'breakable block':
                        breakable_block = Breakable_block(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), item = None)
                    if editor.tool == 'castle bridge':
                        castle_bridge = Castle_bridge(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'castle axe':
                        castle_axe = Castle_axe(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'castle chain':
                        castle_chain = Castle_chain(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'fire box':
                        fire_box = Fire_box(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), length = 6, direction = None)
                    if editor.tool == 'checkpoint':
                        checkpoint = Checkpoint(position = (mouse_pos_x // 16 * 16 + camera.position.x + 6, mouse_pos_y // 16 * 16 + camera.position.y + 3))
                    if editor.tool == 'fire flower':
                        fire_flower = Fire_flower(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'coin':
                        coin = Coin(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'power star':
                        power_star = Power_star(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'goomba':
                        enemy = Enemy(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), enemy_type = 'goomba')
                    if editor.tool == 'green koopa':
                        enemy = Enemy(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), enemy_type = 'green koopa')
                    if editor.tool == 'red koopa':
                        enemy = Enemy(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), enemy_type = 'red koopa')
                    if editor.tool == 'pirhana plant':
                        pirhana_plant = Pirhana_plant(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'cheepcheep':
                        cheepcheep = Cheepcheep(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'blooper':
                        blooper = Blooper(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'bowser':
                        bowser = Bowser(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'goal post':
                        goal_post = Goal_post(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'pipe up':
                        pipe = Pipe(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), height = 48, warp_position = None, direction = 'up', warp_direction = None)
                    if editor.tool == 'pipe down':
                        pipe = Pipe(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), height = 48, warp_position = None, direction = 'down', warp_direction = None)
                    if editor.tool == 'water':
                        water = Water(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), width = 16, height = 16)
                        hold_left_click = water
                    if editor.category == 'decorations':
                        if editor.tool in decoration_list:
                            decoration = Decoration(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y + 16), image = editor.tool)
                            decoration.rect.y -= decoration.image.get_height()
                            decoration.position.y -= decoration.image.get_height()
                    if editor.tool == 'select':
                        for sprite in all_sprite_group:#selects sprite you click on
                            if sprite not in water_group:
                                if editor.rect.colliderect(sprite):
                                    drag_offset_x = editor.rect.x - sprite.rect.x
                                    drag_offset_y = editor.rect.y - sprite.rect.y
                                    hold_left_click = sprite
                                    editor.selected_sprite = sprite
                                    print(f'selected item: {sprite}')
                                    break
                                else:
                                    for sprite in water_group:#deprioritizes water sprites
                                        if editor.rect.colliderect(sprite):
                                            drag_offset_x = editor.rect.x - sprite.rect.x
                                            drag_offset_y = editor.rect.y - sprite.rect.y
                                            hold_left_click = sprite
                                            editor.selected_sprite = sprite
                                            print(f'selected item: {sprite}')
                                            break
                                        else:
                                            editor.selected_sprite = None#deselect sprite
                    if editor.tool == 'scale':
                        for sprite in all_sprite_group:#select sprite for size scaling
                            if sprite not in water_group:
                                if editor.rect.colliderect(sprite):
                                    print('test')
                                    hold_left_click = sprite
                                    scale_offset_x = sprite.rect.right - editor.rect.x - 1
                                    scale_offset_y = sprite.rect.bottom - editor.rect.y - 1
                                    break
                                else:
                                    for sprite in water_group:#deprioritizes water sprites
                                        if editor.rect.colliderect(sprite):
                                            print('test')
                                            hold_left_click = sprite
                                            scale_offset_x = sprite.rect.right - editor.rect.x - 1
                                            scale_offset_y = sprite.rect.bottom - editor.rect.y - 1
                                            break
                                
                    if editor.tool == 'connect pipes':
                        for pipe in pipe_group:
                            if editor.rect.colliderect(pipe):
                                if editor.selected_pipe == None:
                                    editor.selected_pipe = pipe
                                else:
                                    pipe.warp_direction = editor.selected_pipe.direction
                                    editor.selected_pipe.warp_direction = pipe.direction
                                    if editor.selected_pipe.direction == 'up':
                                        pipe.warp_position = editor.selected_pipe.rect.topleft
                                    else:
                                        pipe.warp_position = editor.selected_pipe.rect.bottomleft
                                    if pipe.direction == 'up':
                                        editor.selected_pipe.warp_position = pipe.rect.topleft
                                    else:
                                        editor.selected_pipe.warp_position = pipe.rect.bottomleft
                                    pipe.image.fill(pygame.Color('gray'))
                                    editor.selected_pipe.image.fill(pygame.Color('gray'))
                                    editor.selected_pipe = None
                    else:
                        editor.sellected_pipe = None
        elif e.type == pygame.MOUSEBUTTONUP:#Mouse release
            if e.button == 1:#left click
                hold_left_click = None
                for block in item_block_group:#add item to item block
                    for fireflower in fire_flower_group:
                        if fireflower.rect.colliderect(block):
                            block.item = 'fire flower'
                            block.quantity = 1
                            fire_flower_group.remove(fireflower)
                            fireflower.kill()
                            #block.image.fill(pygame.Color('orange'))
                    for coin in coin_group:
                        if coin.rect.colliderect(block):
                            block.item = 'coin'
                            block.quantity = 10
                            coin.kill()
                            #block.image.fill(pygame.Color('orange'))
                    for power_star in power_star_group:
                        if power_star.rect.colliderect(block):
                            block.item = 'power star'
                            block.quantity = 1
                            power_star_group.remove(power_star)
                            power_star.kill()
                            #block.image.fill(pygame.Color('orange'))
                for block in breakable_block_group:#add item to item block
                    for fireflower in fire_flower_group:
                        if fireflower.rect.colliderect(block):
                            block.item = 'fire flower'
                            block.quantity = 1
                            fire_flower_group.remove(fireflower)
                            fireflower.kill()
                            #block.image.fill(pygame.Color(100, 100, 100))
                    for coin in coin_group:
                        if coin.rect.colliderect(block):
                            block.item = 'coin'
                            block.quantity = 1
                            coin.kill()
                            #block.image.fill(pygame.Color(100, 100, 100))
                    for power_star in power_star_group:
                        if power_star.rect.colliderect(block):
                            block.item = 'power star'
                            block.quantity = 1
                            power_star_group.remove(power_star)
                            power_star.kill()
                            #block.image.fill(pygame.Color('orange'))
            
    if editor.tool == 'select':
        if hold_left_click in fire_bar_group:
                hold_left_click = hold_left_click.box.fire_bar_list[-1]
                hold_left_click.box.direction[0] = hold_left_click.box.rect.x + 8 - editor.rect.x
                hold_left_click.box.direction[1] = hold_left_click.box.rect.y + 8 - editor.rect.y
                if hold_left_click.box.direction[0] == 0:
                    hold_left_click.box.direction[0] = 0.01
                if hold_left_click.box.direction[1] == 0:
                    hold_left_click.box.direction[1] = 0.01

                hold_left_click.box.direction = hold_left_click.box.direction.normalize()
                hold_left_click.box.update()
        elif hold_left_click != None:#drag mouse to move sprites
            hold_left_click.rect.x = editor.rect.x // 16 * 16 - (drag_offset_x // 16 * 16)
            hold_left_click.position.x = editor.rect.x // 16 * 16 - (drag_offset_x // 16 * 16)
            hold_left_click.rect.y = editor.rect.y // 16 * 16 - (drag_offset_y // 16 * 16)
            hold_left_click.position.y = editor.rect.y // 16 * 16 - (drag_offset_y // 16 * 16)
            if hold_left_click in fire_box_group:
                for i in range(len(hold_left_click.fire_bar_list)):
                    hold_left_click.fire_bar_list[i].rect.x = hold_left_click.rect.x - hold_left_click.direction[0]*(i*8) + 4
                    hold_left_click.fire_bar_list[i].rect.y = hold_left_click.rect.y - hold_left_click.direction[1]*(i*8) + 4
            if hold_left_click in decoration_group:
                hold_left_click.rect.y -= hold_left_click.image.get_height() -16
                hold_left_click.position.y -= hold_left_click.image.get_height() -16
            if hold_left_click in checkpoint_group:
                hold_left_click.rect.x += 6
                hold_left_click.position.x += 6
                hold_left_click.rect.y += 3
                hold_left_click.position.y += 3


    if editor.tool == 'scale':#scale sprite
        if hold_left_click != None:
            if hold_left_click in block_group or hold_left_click in thin_block_group or hold_left_click in water_group or hold_left_click in rock_group or hold_left_click in coral_group:
                hold_left_click.width = (mouse_pos_x - hold_left_click.rect.x + camera.position.x + scale_offset_x) // 16 * 16 +16
                if hold_left_click.width < 0:
                    hold_left_click.width = 16
            if hold_left_click in block_group or hold_left_click in pipe_group or hold_left_click in water_group or hold_left_click in rock_group or hold_left_click in coral_group:
                hold_left_click.height = (mouse_pos_y - hold_left_click.rect.y + camera.position.y + scale_offset_y) // 16 * 16 + 16
                if hold_left_click.height < 0:
                    hold_left_click.height = 16

            if hold_left_click in block_group:
                hold_left_click.image = make_tiled_image(block_image, hold_left_click.width, hold_left_click.height )
            elif hold_left_click in breakable_block_group:
                hold_left_click.image = make_tiled_image(breakable_block_image, hold_left_click.width, hold_left_click.height )
            elif hold_left_click in thin_block_group:
                hold_left_click.image = make_tiled_image(thin_platform_image, hold_left_click.width, hold_left_click.height )
            elif hold_left_click in pipe_group:
                hold_left_click.image = make_tiled_image(pipe_image, hold_left_click.width, hold_left_click.height )
            elif hold_left_click in rock_group:
                hold_left_click.image = make_tiled_image(rock_image, hold_left_click.width, hold_left_click.height )
            elif hold_left_click in coral_group:
                hold_left_click.image = make_tiled_image(coral_image, hold_left_click.width, hold_left_click.height )
            elif hold_left_click in water_group:
                hold_left_click.image = pygame.Surface((hold_left_click.width, hold_left_click.height))
                hold_left_click.image.fill(pygame.Color(hold_left_click.color))
            hold_left_click.rect = hold_left_click.image.get_rect(topleft=hold_left_click.rect.topleft)

    if editor.tool == 'block' or editor.tool == 'water' or editor.tool == 'rock' or editor.tool == 'coral':#scale block when placed
        if hold_left_click != None:
            hold_left_click.width = (mouse_pos_x - hold_left_click.rect.x + camera.position.x) // 16 * 16 +16
            hold_left_click.height = (mouse_pos_y - hold_left_click.rect.y + camera.position.y) // 16 * 16 + 16
            if hold_left_click.width < 0:
                hold_left_click.width = 16
            if hold_left_click.height < 0:
                hold_left_click.height = 16

            hold_left_click.image = pygame.Surface((hold_left_click.width, hold_left_click.height))
            if hold_left_click in block_group:
                hold_left_click.image = make_tiled_image(block_image, hold_left_click.width, hold_left_click.height )
            if hold_left_click in rock_group:
                hold_left_click.image = make_tiled_image(rock_image, hold_left_click.width, hold_left_click.height )
            if hold_left_click in coral_group:
                hold_left_click.image = make_tiled_image(coral_image, hold_left_click.width, hold_left_click.height )
            if hold_left_click in water_group:
                hold_left_click.image.fill(pygame.Color(hold_left_click.color))
            hold_left_click.rect = hold_left_click.image.get_rect(topleft=hold_left_click.rect.topleft)

    if editor.tool == 'thin block':#scale thin block when placed
        if hold_left_click != None:
            hold_left_click.width = (mouse_pos_x - hold_left_click.rect.x) // 16 * 16 +16
            if hold_left_click.width < 0:
                hold_left_click.width = 16

            hold_left_click.image = make_tiled_image(thin_platform_image, hold_left_click.width, hold_left_click.height )
            hold_left_click.rect = hold_left_click.image.get_rect(topleft=hold_left_click.rect.topleft)

                
    editor.update()
        
    camera.update()

    #render
    screen.fill(BACKGROUND_COLOR)
    for i in range(0, 720, 16):
        pygame.draw.line(screen, (255, 255, 255), (0, i), (900, i))
        pygame.draw.line(screen, (255, 255, 255), (i, 0), (i, 900))
    for sprite in decoration_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in water_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in super_mushroom_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in fire_flower_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in coin_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in power_star_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in show_coin_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in block_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in rock_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in coral_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in item_block_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
        if sprite.item != None:
            screen.blit(sprite.item_image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in breakable_block_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
        if sprite.item != None:
            screen.blit(sprite.item_image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in castle_bridge_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in castle_axe_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in castle_chain_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in fire_box_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in fire_bar_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in thin_block_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in enemy_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in cheepcheep_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in blooper_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in bowser_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in flattened_enemy_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in fire_ball_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in goal_post_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x + 6, sprite.rect.y - camera.position.y))
        screen.blit(flag_pole_top_image, (sprite.rect.x - camera.position.x + 4, sprite.rect.y - camera.position.y -8))
    for sprite in goal_flag_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x + 2, sprite.rect.y - camera.position.y))
    for sprite in goal_base_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in checkpoint_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in pipe_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
        if sprite.direction == 'up':
            screen.blit(pipe_top_image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
        else:
            screen.blit(pipe_bottom_image, (sprite.rect.x - camera.position.x, sprite.rect.y + sprite.height - 16 - camera.position.y))
    for sprite in pirhana_plant_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    if player.invincibility_jitter == False:
        screen.blit(player.image, (player.rect.x - camera.position.x, player.rect.y - camera.position.y))
    screen.blit(menu_backdrop.image, (menu_backdrop.rect.x, menu_backdrop.rect.y))
    for sprite in menu_button_group:
        screen.blit(sprite.image, (sprite.rect.x, sprite.rect.y))
    for sprite in menu_button_group:
        screen.blit(sprite.icon, (sprite.rect.x+8, sprite.rect.y+8))
    if editor.tool != 'select' and editor.tool != 'scale' and hold_left_click == None:
        if mouse_pos_y < 480:
            screen.blit(courser_sprite.image, (mouse_pos_x // 16 * 16, mouse_pos_y // 16 * 16))
            #screen.blit(courser_sprite.image, (mouse_pos_x // 16 * 16, mouse_pos_y // 16 * 16 - courser_sprite.image.get_height() + 16))

    


    

    pygame.display.update()
