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
BACKGROUND_COLOR = [pygame.Color(92, 148, 252), pygame.Color(0, 0, 0), pygame.Color(0, 0, 0), pygame.Color(0, 0, 0)]

screen = pygame.display.set_mode(SIZE)
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)



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

empty_item_block_image = block_sheet.image_at((144, 112, 16,16), colorkey = (255, 255, 255))

block_image = [block_sheet.image_at((0, 0, 16, 16), colorkey = (255, 255, 255)), block_sheet.image_at((0, 32, 16, 16), colorkey = (255, 255, 255)), block_sheet.image_at((0, 64, 16, 16), colorkey = (255, 255, 255)), block_sheet.image_at((0, 96, 16, 16), colorkey = (255, 255, 255))]

breakable_block_image = [block_sheet.image_at((16, 0, 16, 16), colorkey = (255, 255, 255)), block_sheet.image_at((16, 32, 16, 16), colorkey = (255, 255, 255)), block_sheet.image_at((16, 64, 16, 16), colorkey = (255, 255, 255)), block_sheet.image_at((16, 96, 16, 16), colorkey = (255, 255, 255))]

thin_platform_image = item_sheet.image_at((80, 64, 16, 8))

goomba_image_list = [character_sheet.image_at((296, 187, 16,16), colorkey = (107, 49, 156)), character_sheet.image_at((315, 187, 16,16), colorkey = (107, 49, 156))]

green_koopa_left_image_list = [character_sheet.image_at((201, 206, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((182, 206, 16, 24), colorkey = (107, 49, 156))]

red_koopa_left_image_list = [character_sheet.image_at((87, 206, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((68, 206, 16, 24), colorkey = (107, 49, 156))]

pirhana_plant_image = enemy_sheet.image_at((390, 30, 15, 24), colorkey = (255, 255, 255))

cheepcheep_image = character_sheet.image_at((90, 268 ,15 ,16), colorkey = (107, 49, 156))
blooper_image = character_sheet.image_at((239, 260, 16, 24), colorkey = (107, 49, 156))


item_block_shimmer_list = [[block_sheet.image_at((368, 0, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 0, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 0, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 0, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 0, 16,16), colorkey = (255, 255, 255))],
                           [block_sheet.image_at((368, 32, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 32, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 32, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 32, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 32, 16,16), colorkey = (255, 255, 255))],
                            [block_sheet.image_at((368, 64, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 64, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 64, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 64, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 64, 16,16), colorkey = (255, 255, 255))],
                            [block_sheet.image_at((368, 96, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 96, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 96, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 96, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((368, 96, 16,16), colorkey = (255, 255, 255))],
]

coin_shimmer_list = [item_sheet.image_at((0, 64, 16,16), colorkey = (255, 255, 255)), item_sheet.image_at((0, 64, 16,16), colorkey = (255, 255, 255)), item_sheet.image_at((0, 64, 16,16), colorkey = (255, 255, 255)), item_sheet.image_at((0, 64, 16,16), colorkey = (255, 255, 255)), item_sheet.image_at((0, 64, 16,16), colorkey = (255, 255, 255))]

fire_flower_image = item_sheet.image_at((0, 16, 16,16), colorkey = (255, 255, 255))

power_star_image = [item_sheet.image_at((0, 32, 16,16), colorkey = (255, 255, 255)), item_sheet.image_at((16, 32, 16,16), colorkey = (255, 255, 255)), item_sheet.image_at((32, 32, 16,16), colorkey = (255, 255, 255)), item_sheet.image_at((0, 48, 16,16), colorkey = (255, 255, 255))]


small_mario_standing_right_image = character_sheet.image_at((277, 44, 12, 16), colorkey = (107, 49, 156))

for y in range(4):#fetch item blocks from sprite sheet
    for x in range(3):
        item_block_shimmer_list[y].append(block_sheet.image_at((368 + x*16, x * 32, 16,16), colorkey = (255, 255, 255)))
for x in range(3):#fetch coins from sprite sheet
    coin_shimmer_list.append(item_sheet.image_at((0 + x*16, 64, 16,16), colorkey = (255, 255, 255)))



class General():
    def __init__(self):
        self.level = 1
        self.level_mode = 1
        self.color_pallete = 1
general = General()

class Level():
    def __init__(self):
        
        self.level_width = level_width

        self.color_pallete = color_pallete

level_width = []
color_palletes = [0, 1, 2, 3]

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

        if self.tool == 'block' or self.tool == 'coin' or self.tool == 'enemy':
            self.icon = icon
        else:
            self.icon = pygame.Surface((16, 16))
            self.icon.fill(icon)
            
    def update(self):
        if editor.tool == 'block':
            self.icon = block_image[general.color_pallete]
        elif editor.tool == 'thin block':
            self.icon = item_sheet.image_at((80, 64, 16, 8), colorkey = (255, 255, 255))
        elif editor.tool == 'item block':
            self.icon = item_block_image
        elif editor.tool == 'breakable block':
            self.icon = breakable_block_image[general.color_pallete]
        elif editor.tool == 'goomba':
            self.icon = goomba_image_list[0]
        elif editor.tool == 'green koopa':
            self.icon = green_koopa_left_image_list[0]
        elif editor.tool == 'red koopa':
            self.icon = red_koopa_left_image_list[0]
        elif editor.tool == 'pirhana plant':
            self.icon = pirhana_plant_image
        elif editor.tool == 'cheepcheep':
            self.icon = cheepcheep_image
        elif editor.tool == 'blooper':
            self.icon = blooper_image
        elif editor.tool == 'coin':
            self.icon = coin_shimmer_list[0]
        elif editor.tool == 'fire flower':
            self.icon = fire_flower_image
        elif editor.tool == 'power star':
            self.icon = power_star_image[0]
        elif editor.tool == 'pipe up':
            self.icon = pipe_top_image
        elif editor.tool == 'pipe down':
            self.icon = pipe_bottom_image
        elif editor.tool == 'water':
            self.icon = pygame.Surface((16, 16))
            self.icon.fill(pygame.Color('blue'))
        
menu_backdrop = Menu_backdrop()
menu_items = ['select', 'block', 'coin', 'enemy', 'goal post', 'connect pipes', 'scale']
menu_icons = [pygame.Color('black'), block_image[general.color_pallete], goomba_image_list[0], coin_shimmer_list[0], pygame.Color('red'), pygame.Color('black'), pygame.Color('black')]
        
try:
    block_file = open(f'sprites/level {general.level}/block file.pickle', 'rb')
except FileNotFoundError:
    filename = f'sprites/level {general.level}/block file.pickle'#creates new folder
    os.makedirs(os.path.dirname(filename), exist_ok=True)#creates new folder
    block_file = open(f'sprites/level {general.level}/block file.pickle', 'x')
    block_file = open(f'sprites/level {general.level}/block file.pickle', 'rb')
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
    enemy_file = open(f'sprites/level {general.level}//enemy file.pickle', 'rb')
except FileNotFoundError:
    enemy_file = open(f'sprites/level {general.level}/enemy file.pickle', 'x')
    enemy_file = open(f'sprites/level {general.level}/enemy file.pickle', 'rb')
try:
    pirhana_plant_file = open(f'sprites/level {general.level}//pirhana plant file.pickle', 'rb')
except FileNotFoundError:
    pirhana_plant_file = open(f'sprites/level {general.level}/pirhana plant file.pickle', 'x')
    pirhana_plant_file = open(f'sprites/level {general.level}/pirhana plant file.pickle', 'rb')
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
    water_file = open(f'sprites/level {general.level}//water file.pickle', 'rb')
except FileNotFoundError:
    water_file = open(f'sprites/level {general.level}/water file.pickle', 'x')
    water_file = open(f'sprites/level {general.level}/water file.pickle', 'rb')
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
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if self.s_pressed == False:
                self.s_pressed = True
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
                    self.selected_sprite.kill()
                    self.selected_sprite = None
                    self.delete_is_pressed = True
        else:
            self.delete_is_pressed = False

        if keys[pygame.K_ESCAPE]:
            on_closing()

        if keys[pygame.K_1]:
            self.category = 'select'
            self.tool = 'select'
            for sprite in menu_button_group:#returns preveiously selected button to white
                sprite.image.fill(pygame.Color('white'))
            menu_button_list[0].image.fill(pygame.Color(100, 100, 100))#turns selected button grey
        if keys[pygame.K_2]:
            #self.tool = 'block'
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
            self.category = 'scale'
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
            self.category = 'goal post'
            self.tool = 'goal post'
            courser_sprite.image = pygame.Surface((4, 96))
            courser_sprite.image.fill(pygame.Color('blue'))
            for sprite in menu_button_group:
                sprite.image.fill(pygame.Color('white'))
            menu_button_list[4].image.fill(pygame.Color(100, 100, 100))
        if keys[pygame.K_6]:
            self.category = 'connect pipes'
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

    def update(self):
        if editor.tool == 'block':
            self.image = block_image[general.color_pallete]
        elif editor.tool == 'thin block':
            self.image = item_sheet.image_at((80, 64, 16, 8), colorkey = (255, 255, 255))
        elif editor.tool == 'item block':
            self.image = item_block_image
        elif editor.tool == 'breakable block':
            self.image = breakable_block_image[general.color_pallete]
        elif editor.tool == 'goomba':
            self.image = goomba_image_list[0]
        elif editor.tool == 'green koopa':
            self.image = green_koopa_left_image_list[0]
        elif editor.tool == 'red koopa':
            self.image = red_koopa_left_image_list[0]
        elif editor.tool == 'pirhana plant':
            self.image = pirhana_plant_image
        elif editor.tool == 'cheepcheep':
            self.image = cheepcheep_image
        elif editor.tool == 'blooper':
            self.image = blooper_image
        elif editor.tool == 'coin':
            self.image = coin_shimmer_list[0]
        elif editor.tool == 'fire flower':
            self.image = fire_flower_image
        elif editor.tool == 'power star':
            self.image = power_star_image[0]
        elif editor.tool == 'pipe up':
            self.image = pipe_top_image
        elif editor.tool == 'pipe down':
            self.image = pipe_bottom_image
        elif editor.tool == 'water':
            self.image = pygame.Surface((16, 16))
            self.image.fill(pygame.Color('blue'))
    

def on_closing():
    with open(f'sprites/level {general.level}/block file.pickle', 'wb') as handle:
        for sprite in block_group:
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
    with open(f'sprites/level {general.level}/pipe file.pickle', 'wb') as handle:
        for sprite in pipe_group:
            pickle.dump([sprite.position, sprite.height, sprite.warp_position, sprite.direction, sprite.warp_direction], handle)
        handle.close()
    with open(f'sprites/level {general.level}/enemy file.pickle', 'wb') as handle:
        for sprite in enemy_group:
            pickle.dump([sprite.position, sprite.enemy_type], handle)
        handle.close()
    with open(f'sprites/level {general.level}/pirhana plant file.pickle', 'wb') as handle:
        for sprite in pirhana_plant_group:
            pickle.dump([sprite.position], handle)
        handle.close()
    with open(f'sprites/level {general.level}/cheepcheep file.pickle', 'wb') as handle:
        for sprite in cheepcheep_group:
            pickle.dump([sprite.position], handle)
        handle.close()
    with open(f'sprites/level {general.level}/blooper file.pickle', 'wb') as handle:
        for sprite in blooper_group:
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
    with open(f'sprites/level {general.level}/level settings.pickle', 'wb') as handle:
        pickle.dump([general.color_pallete], handle)
        handle.close()
    running = False
    pygame.quit()
                
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

        self.base_image = block_image
        self.image = make_tiled_image(block_image[general.color_pallete], self.width, self.height )
        
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        sprite_replace_check(self)

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
            self.item = 'coin'
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
        
        self.width = 16
        self.height = 16


        self.image = breakable_block_image[general.color_pallete]

        
        
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)
        self.animation_frame = 0

        sprite_replace_check(self)

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
        
        self.base_image = pipe_image
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

        self.base_image = thin_platform_image
        self.image = make_tiled_image(thin_platform_image, self.width, self.height, colorkey = (255, 255, 255) )
        self.rect = pygame.Surface ((self.width, 16)).get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        sprite_replace_check(self)

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

class Power_star(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Power_star, self).__init__()

        power_star_group.add(self)

        self.direction = 'right'

        self.speed = 3

        self.image = power_star_image[0]

        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        self.velocity = pygame.math.Vector2(0, 0)


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
                sprite.quantity = 1
                coin_group.remove(self)
                sprite.image.fill(pygame.Color('orange'))
                self.kill()
        for sprite in breakable_block_group:
            if self.rect.colliderect(sprite):
                sprite.item = 'coin'
                sprite.quantity = 1
                coin_group.remove(self)
                sprite.image.fill(pygame.Color(100, 100, 100))
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

class Pirhana_plant(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Pirhana_plant, self).__init__()

        pirhana_plant_group.add(self)
        all_sprite_group.add(self)

        self.animation_frame = 0

        self.width = 16
        self.height = 24
        
        self.image = pirhana_plant_image
        
        self.rect = self.image.get_rect(topleft = position)

        self.position = pygame.math.Vector2(position)

class Cheepcheep(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Cheepcheep, self).__init__()

        cheepcheep_group.add(self)
        all_sprite_group.add(self)

        self.animation_frame = 0

        self.width = 16
        self.height = 16
        
        self.image = cheepcheep_image
        
        self.rect = self.image.get_rect(topleft = position)

        self.position = pygame.math.Vector2(position)

class Blooper(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Blooper, self).__init__()

        blooper_group.add(self)
        all_sprite_group.add(self)

        self.enemy_type = 'blooper'

        self.animation_frame = 0
        
        self.width = 16
        self.height = 16
        
        self.image = blooper_image
        
        self.rect = self.image.get_rect(topleft = position)

        self.position = pygame.math.Vector2(position)

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
        self.rect.y += 176
        self.position = pygame.math.Vector2(position)
        self.position.y += 176

def sprite_replace_check(Self):
    for sprite in all_sprite_group:
        if Self.rect.colliderect(sprite):
            if Self != sprite:
                if sprite not in water_group:
                    sprite.kill()

#create groups 
all_sprite_group = pygame.sprite.Group()

item_block_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
thin_block_group = pygame.sprite.Group()
breakable_block_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
pirhana_plant_group = pygame.sprite.Group()
cheepcheep_group = pygame.sprite.Group()
blooper_group = pygame.sprite.Group()
flattened_enemy_group = pygame.sprite.Group()
flipped_enemy_group = pygame.sprite.Group()
super_mushroom_group = pygame.sprite.Group()
fire_flower_group = pygame.sprite.Group()
power_star_group = pygame.sprite.Group()
fire_ball_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
show_coin_group = pygame.sprite.Group()
goal_post_group = pygame.sprite.Group()
goal_flag_group = pygame.sprite.Group()
goal_base_group = pygame.sprite.Group()
menu_button_group = pygame.sprite.Group()
menu_icon_group = pygame.sprite.Group()

player_list = []
menu_button_list = []

block_list = ['block', 'thin block', 'item block', 'breakable block', 'pipe up', 'pipe down', 'water']
enemy_list = ['goomba', 'green koopa', 'red koopa', 'pirhana plant', 'cheepcheep', 'blooper']
item_list = ['coin', 'fire flower', 'power star']

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
        pirhana_plant_data = pickle.load(pirhana_plant_file)
        pirhana_plant = Pirhana_plant(position = pirhana_plant_data[0])
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
        water_data = pickle.load(water_file)
        water = Water(position = water_data[0], width = water_data[1], height = water_data[2])
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
camera = Camera(position = (player.position.x - screen_Width / 2, player.position.y))
for x in range(len(menu_items)):
    menu_button = Menu_button(position = (16 + x*64 , 496), tool = menu_items[x], icon = menu_icons[x])


running = True
while running:
    clock.tick(FPS)
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    print(mouse_pos_x + camera.position.x, mouse_pos_y + camera.position.y)
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
                    courser_sprite.update()
                    if editor.category == 'blocks':
                        menu_button_list[1].update()
                    if editor.category == 'enemies':
                        menu_button_list[2].update()
                    if editor.category == 'items':
                        menu_button_list[3].update()
                    
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
                    courser_sprite.update()
                    if editor.category == 'blocks':
                        menu_button_list[1].update()
                    if editor.category == 'enemies':
                        menu_button_list[2].update()
                    if editor.category == 'items':
                        menu_button_list[3].update()
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
                    if editor.tool == 'thin block':
                        thin_block = Thin_block(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), width = 16)
                        hold_left_click = thin_block
                    if editor.tool == 'item block':
                        item_block = Item_block(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), item = None)
                    if editor.tool == 'breakable block':
                        breakable_block = Breakable_block(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), item = None)
                    if editor.tool == 'fire flower':
                        fire_flower = Fire_flower(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'power star':
                        power_star = Power_star(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'coin':
                        coin = Coin(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'goomba':
                        enemy = Enemy(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), enemy_type = 'goomba')
                    if editor.tool == 'green koopa':
                        enemy = Enemy(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), enemy_type = 'green koopa')
                    if editor.tool == 'red koopa':
                        enemy = Enemy(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), enemy_type = 'red koopa')
                    if editor.tool == 'pirhana plant':
                        for pipe in pipe_group:
                            if editor.rect.colliderect(pipe.rect):
                                pirhana_plant = Pirhana_plant(position = (pipe.rect.x + 8, pipe.rect.y))
                    if editor.tool == 'cheepcheep':
                        cheepcheep = Cheepcheep(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'blooper':
                        blooper = Blooper(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'goal post':
                        goal_post = Goal_post(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y))
                    if editor.tool == 'pipe up':
                        pipe = Pipe(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), height = 48, warp_position = None, direction = 'up', warp_direction = None)
                    if editor.tool == 'pipe down':
                        pipe = Pipe(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), height = 48, warp_position = None, direction = 'down', warp_direction = None)
                    if editor.tool == 'water':
                        water = Water(position = (mouse_pos_x // 16 * 16 + camera.position.x, mouse_pos_y // 16 * 16 + camera.position.y), width = 16, height = 16)
                        hold_left_click = water
                    if editor.tool == 'select':
                        for sprite in all_sprite_group:#selects sprite you click on
                            if editor.rect.colliderect(sprite):
                                hold_left_click = sprite
                                editor.selected_sprite = sprite
                                print(f'selected item: {sprite}')
                                left_click_offset_x = (mouse_pos_x // 16 * 16) - hold_left_click.rect.x + camera.position.x
                                left_click_offset_y = (mouse_pos_y // 16 * 16) - hold_left_click.rect.y + camera.position.y
                                break
                            else:
                                editor.selected_sprite = None#deselect sprite
                    if editor.tool == 'scale':
                        for sprite in all_sprite_group:#select sprite for size scaling
                            if editor.rect.colliderect(sprite):
                                print('test')
                                hold_left_click = sprite
                                left_click_offset_x = (mouse_pos_x // 16 * 16) - hold_left_click.rect.x
                                left_click_offset_y = (mouse_pos_y // 16 * 16) - hold_left_click.rect.y
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
                    for coin in coin_group:
                        if coin.rect.colliderect(block):
                            block.item = 'coin'
                            block.quantity = 1
                            coin.kill()
                    for power_star in power_star_group:
                        if power_star.rect.colliderect(block):
                            block.item = 'power star'
                            block.quantity = 1
                            power_star_group.remove(power_star)
                            power_star.kill()
                for block in breakable_block_group:#add item to item block
                    for fireflower in fire_flower_group:
                        if fireflower.rect.colliderect(block):
                            block.item = 'fire flower'
                            block.quantity = 1
                            fire_flower_group.remove(fireflower)
                            fireflower.kill()
                    for coin in coin_group:
                        if coin.rect.colliderect(block):
                            block.item = 'coin'
                            block.quantity = 1
                            coin.kill()
                    for power_star in power_star_group:
                        if power_star.rect.colliderect(block):
                            block.item = 'power star'
                            block.quantity = 1
                            power_star_group.remove(power_star)
                            power_star.kill()
            
    if editor.tool == 'select':
        if hold_left_click != None:#drag mouse to move sprites
            hold_left_click.rect.x = editor.rect.x // 16 * 16 - left_click_offset_x
            hold_left_click.position.x = editor.rect.x // 16 * 16 - left_click_offset_x
            hold_left_click.rect.y = editor.rect.y // 16 * 16 - left_click_offset_y
            hold_left_click.position.y = editor.rect.y // 16 * 16 - left_click_offset_y
            
                    
                
                
    if editor.tool == 'scale':#scale sprite
        if hold_left_click != None:
            if hold_left_click in block_group or hold_left_click in thin_block_group or hold_left_click in water_group:
                hold_left_click.width = (mouse_pos_x - hold_left_click.rect.x + camera.position.x) // 16 * 16 + 16 + left_click_offset_x
                if hold_left_click.width < 0:
                    hold_left_click.width = 16
            if hold_left_click in block_group or hold_left_click in pipe_group or hold_left_click in water_group:
                hold_left_click.height = (mouse_pos_y - hold_left_click.rect.y + camera.position.y) // 16 * 16 + 16 + left_click_offset_y
                if hold_left_click.height < 0:
                    hold_left_click.height = 16

            if hold_left_click in water_group:
                hold_left_click.image = pygame.Surface((hold_left_click.width, hold_left_click.height))
                hold_left_click.image.fill(pygame.Color(hold_left_click.color))
                hold_left_click.rect = hold_left_click.image.get_rect(topleft=hold_left_click.rect.topleft)
            elif hold_left_click in block_group or hold_left_click in thin_block_group or hold_left_click in pipe_group:
                hold_left_click.image = make_tiled_image(hold_left_click.base_image, hold_left_click.width, hold_left_click.height, colorkey = (255, 255, 255))
                hold_left_click.rect = hold_left_click.image.get_rect(topleft=hold_left_click.rect.topleft)
    if editor.tool == 'block' or editor.tool == 'water':#scale block when placed
        if hold_left_click != None:
            hold_left_click.width = (mouse_pos_x - hold_left_click.rect.x + camera.position.x) // 16 * 16 +16
            hold_left_click.height = (mouse_pos_y - hold_left_click.rect.y + camera.position.y) // 16 * 16 + 16
            if hold_left_click.width < 0:
                hold_left_click.width = 16
            if hold_left_click.height < 0:
                hold_left_click.height = 16


            if hold_left_click in block_group:
                hold_left_click.image = make_tiled_image(block_image[general.color_pallete], hold_left_click.width, hold_left_click.height )
                hold_left_click.rect = hold_left_click.image.get_rect(topleft=hold_left_click.rect.topleft)
            elif hold_left_click in water_group:
                print('test')
                hold_left_click.image.fill(pygame.Color(hold_left_click.color))
                hold_left_click.rect = hold_left_click.image.get_rect(topleft=hold_left_click.rect.topleft)

    if editor.tool == 'thin block':#scale thin block when placed
        if hold_left_click != None:
            hold_left_click.width = (mouse_pos_x - hold_left_click.rect.x) // 16 * 16 +16
            if hold_left_click.width < 0:
                hold_left_click.width = 16

            hold_left_click.image = pygame.Surface((hold_left_click.width, hold_left_click.height))
            hold_left_click.rect = hold_left_click.image.get_rect(topleft=hold_left_click.rect.topleft)
            hold_left_click.image = make_tiled_image(thin_platform_image, hold_left_click.width, hold_left_click.height, colorkey = (255, 255, 255))

                
    editor.update()
        
    camera.update()


    #render
    screen.fill(BACKGROUND_COLOR[general.color_pallete])
    for i in range(0, 720, 16):
        pygame.draw.line(screen, (255, 255, 255), (0, i), (900, i))
        pygame.draw.line(screen, (255, 255, 255), (i, 0), (i, 900))
    for sprite in water_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in super_mushroom_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in fire_flower_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in coin_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in show_coin_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in block_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in item_block_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
        if sprite.item == 'fire flower':
            screen.blit(fire_flower_image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
        elif sprite.item == 'power star':
            screen.blit(power_star_image[0], (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in breakable_block_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in thin_block_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in enemy_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in cheepcheep_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in blooper_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in flattened_enemy_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in fire_ball_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in goal_post_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x + 6, sprite.rect.y - camera.position.y))
        screen.blit(flag_pole_top_image, (sprite.rect.x - camera.position.x + 4, sprite.rect.y - camera.position.y -8))
        screen.blit(goal_flag_image, (sprite.rect.x - camera.position.x + -6, sprite.rect.y - camera.position.y +8))
        screen.blit(goal_base_image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y + sprite.height - 16))
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
    if editor.selected_sprite != None:
        screen.blit(editor.selected_sprite.image, (0, 0))
    screen.blit(menu_backdrop.image, (menu_backdrop.rect.x, menu_backdrop.rect.y))
    for sprite in menu_button_group:
        screen.blit(sprite.image, (sprite.rect.x, sprite.rect.y))
    for sprite in menu_button_group:
        screen.blit(sprite.icon, (sprite.rect.x+8, sprite.rect.y+8))
    if editor.tool != 'select' and editor.tool != 'scale' and hold_left_click == None:
        if mouse_pos_y < 480:
            screen.blit(courser_sprite.image, (mouse_pos_x // 16 * 16, mouse_pos_y // 16 * 16))

    #removes glitch phantom blocks
    for block in block_group:
        if block.height <= 7 :
            block.kill()

    


    

    pygame.display.update()
