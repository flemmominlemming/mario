import pygame
import sys, random, math, fractions
import pickle
from spritesheet import SpriteSheet
from maketiledimage import make_tiled_image

pygame.init()
screen_Width = 720
screen_Height = 480
level_width = 4000

SIZE = WIDTH, HEIGHT = screen_Width, screen_Height
FPS = 60
BACKGROUND_COLOR = [pygame.Color(92, 148, 252), pygame.Color(0, 0, 0), pygame.Color(0, 0, 0), pygame.Color(0, 0, 0)]

#full_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode(SIZE)
#full_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#resized_screen = pygame.transform.smoothscale(screen, (screen_Width,screen_Height))
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

scalex = screen.get_width() / screen_Width
scaley = screen.get_height() / screen_Height



clock = pygame.time.Clock()


block_sheet = SpriteSheet('grafik\sprite sheet 3.png')
item_sheet = SpriteSheet('grafik\sprite sheet 2.png')
character_sheet = SpriteSheet('grafik\sprite sheet characters.png')
mario_sheet = SpriteSheet('grafik\sprite sheet mario.png')
enemy_sheet = SpriteSheet('grafik\sprite sheet enemies.png')

star_power_sheet_black = SpriteSheet('grafik\sprite sheet mario star power black.png')
star_power_sheet_red = SpriteSheet('grafik\sprite sheet mario star power red.png')
star_power_sheet_green = SpriteSheet('grafik\sprite sheet mario star power green.png')
star_power_sheet_small_white = SpriteSheet('grafik\sprite sheet small mario star power white.png')

pipe_image = [block_sheet.image_at((0, 151, 32, 8)), block_sheet.image_at((0, 183, 32, 8)), block_sheet.image_at((0, 279, 32, 8)), block_sheet.image_at((0, 151, 32, 8))]
pipe_top_image = [block_sheet.image_at((0, 128, 32, 16), colorkey = (255, 255, 255)), block_sheet.image_at((0, 160, 32, 16), colorkey = (255, 255, 255)), block_sheet.image_at((0, 256, 32, 16), colorkey = (163, 73, 164)), block_sheet.image_at((0, 128, 32, 16), colorkey = (255, 255, 255))]
pipe_bottom_image = []
for sprite in pipe_top_image:
    pipe_bottom_image.append(pygame.transform.flip(sprite, False, True))

flag_pole_image = block_sheet.image_at((263, 144, 2, 16), colorkey = (255, 255, 255))
flag_pole_top_image = block_sheet.image_at((260, 136, 8, 8), colorkey = (255, 255, 255))
goal_base_image = block_sheet.image_at((0, 16, 16, 16), colorkey = (255, 255, 255))
goal_flag_image = item_sheet.image_at((128, 16, 16, 16), colorkey = (255, 255, 255))

item_block_image = block_sheet.image_at((368, 0, 16, 16), colorkey = (255, 255, 255))

empty_item_block_image = [block_sheet.image_at((416, 0, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((416, 32, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((416, 64, 16,16), colorkey = (255, 255, 255)), block_sheet.image_at((416, 96, 16,16), colorkey = (255, 255, 255))]

block_image = [block_sheet.image_at((0, 0, 16, 16), colorkey = (255, 255, 255)), block_sheet.image_at((0, 32, 16, 16), colorkey = (255, 255, 255)), block_sheet.image_at((0, 64, 16, 16), colorkey = (255, 255, 255)), block_sheet.image_at((0, 96, 16, 16), colorkey = (255, 255, 255))]

breakable_block_image = [block_sheet.image_at((16, 0, 16, 16), colorkey = (255, 255, 255)), block_sheet.image_at((16, 32, 16, 16), colorkey = (255, 255, 255)), block_sheet.image_at((16, 64, 16, 16), colorkey = (255, 255, 255)), block_sheet.image_at((16, 96, 16, 16), colorkey = (255, 255, 255))]

water_top_image = block_sheet.image_at((48, 416, 16, 8))

block_piece_topleft_image = [item_sheet.image_at((64, 0, 8, 8), colorkey = (255, 255, 255)), item_sheet.image_at((208, 0, 8, 8), colorkey = (255, 255, 255)), item_sheet.image_at((352, 0, 8, 8), colorkey = (255, 255, 255)), item_sheet.image_at((496, 0, 8, 8), colorkey = (255, 255, 255))]
block_piece_topright_image = [item_sheet.image_at((72, 0, 8, 8), colorkey = (255, 255, 255)), item_sheet.image_at((216, 0, 8, 8), colorkey = (255, 255, 255)), item_sheet.image_at((360, 0, 8, 8), colorkey = (255, 255, 255)), item_sheet.image_at((504, 0, 8, 8), colorkey = (255, 255, 255))]
block_piece_bottomleft_image = [item_sheet.image_at((64, 8, 8, 8), colorkey = (255, 255, 255)), item_sheet.image_at((208, 8, 8, 8), colorkey = (255, 255, 255)), item_sheet.image_at((352, 8, 8, 8), colorkey = (255, 255, 255)), item_sheet.image_at((496, 8, 8, 8), colorkey = (255, 255, 255))]
block_piece_bottomright_image = [item_sheet.image_at((72, 8, 8, 8), colorkey = (255, 255, 255)), item_sheet.image_at((216, 8, 8, 8), colorkey = (255, 255, 255)), item_sheet.image_at((360, 8, 8, 8), colorkey = (255, 255, 255)), item_sheet.image_at((504, 8, 8, 8), colorkey = (255, 255, 255))]

thin_platform_image = [block_sheet.image_at((48, 16, 16, 8)), block_sheet.image_at((48, 48, 16, 8)), block_sheet.image_at((48, 80, 16, 8)), block_sheet.image_at((48, 112, 16, 8))]

fence_image = [block_sheet.image_at((240, 136, 16, 8)), block_sheet.image_at((240, 168, 16, 8)), block_sheet.image_at((240, 264, 16, 8)), block_sheet.image_at((240, 168, 16, 8))]

    

goomba_image_list = [[character_sheet.image_at((296, 187, 16,16), colorkey = (107, 49, 156)), character_sheet.image_at((315, 187, 16,16), colorkey = (107, 49, 156))], [character_sheet.image_at((239, 187, 16,16), colorkey = (107, 49, 156)), character_sheet.image_at((258, 187, 16,16), colorkey = (107, 49, 156))], [character_sheet.image_at((182, 187, 16,16), colorkey = (107, 49, 156)), character_sheet.image_at((201, 187, 16,16), colorkey = (107, 49, 156))], [character_sheet.image_at((182, 187, 16,16), colorkey = (107, 49, 156)), character_sheet.image_at((201, 187, 16,16), colorkey = (107, 49, 156))]]
flattened_goomba = [character_sheet.image_at((277, 195, 16,8), colorkey = (107, 49, 156)), character_sheet.image_at((220, 195, 16,8), colorkey = (107, 49, 156)), character_sheet.image_at((163, 195, 16,8), colorkey = (107, 49, 156)), character_sheet.image_at((163, 195, 16,8), colorkey = (107, 49, 156))]

green_koopa_left_image_list = [[character_sheet.image_at((201, 206, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((182, 206, 16, 24), colorkey = (107, 49, 156))], [character_sheet.image_at((201, 233, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((182, 233, 16, 24), colorkey = (107, 49, 156))], [character_sheet.image_at((201, 233, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((182, 233, 16, 24), colorkey = (107, 49, 156))], [character_sheet.image_at((201, 233, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((182, 233, 16, 24), colorkey = (107, 49, 156))]]
green_koopa_right_image_list = [[character_sheet.image_at((296, 206, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((315, 206, 16, 24), colorkey = (107, 49, 156))], [character_sheet.image_at((296, 233, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((315, 233, 16, 24), colorkey = (107, 49, 156))], [character_sheet.image_at((296, 233, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((315, 233, 16, 24), colorkey = (107, 49, 156))], [character_sheet.image_at((296, 233, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((315, 233, 16, 24), colorkey = (107, 49, 156))]]
green_koopa_shell_image = [character_sheet.image_at((144, 216, 16, 14), colorkey = (107, 49, 156)), character_sheet.image_at((144, 243, 16, 14), colorkey = (107, 49, 156)), character_sheet.image_at((144, 243, 16, 14), colorkey = (107, 49, 156)), character_sheet.image_at((144, 243, 16, 14), colorkey = (107, 49, 156))]
flipped_green_koopa_shell_image = [character_sheet.image_at((353, 216, 16, 14), colorkey = (107, 49, 156)), character_sheet.image_at((353, 216, 16, 14), colorkey = (107, 49, 156)), character_sheet.image_at((353, 216, 16, 14), colorkey = (107, 49, 156)), character_sheet.image_at((353, 216, 16, 14), colorkey = (107, 49, 156))]

red_koopa_left_image_list = [character_sheet.image_at((87, 206, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((68, 206, 16, 24), colorkey = (107, 49, 156))]
red_koopa_right_image_list = [character_sheet.image_at((410, 206, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((429, 206, 16, 24), colorkey = (107, 49, 156))]
red_koopa_shell_image = character_sheet.image_at((30, 216, 16, 14), colorkey = (107, 49, 156))
flipped_red_koopa_shell_image = character_sheet.image_at((467, 215, 16, 14), colorkey = (107, 49, 156))

pirhana_plant_image = [[enemy_sheet.image_at((390, 30, 16, 24), colorkey = (255, 255, 255)), enemy_sheet.image_at((420, 29, 16, 24), colorkey = (163, 73, 164))], [enemy_sheet.image_at((390, 60, 16, 24), colorkey = (255, 255, 255)), enemy_sheet.image_at((420, 60, 16, 24), colorkey = (255, 255, 255))]]

cheepcheep_image_left = [character_sheet.image_at((90, 268 ,15 ,16), colorkey = (107, 49, 156)), character_sheet.image_at((108, 268 ,16 ,16), colorkey = (107, 49, 156))]
cheepcheep_image_right = [character_sheet.image_at((408, 268 ,15 ,16), colorkey = (107, 49, 156)), character_sheet.image_at((389, 268 ,16 ,16), colorkey = (107, 49, 156))]

blooper_image = [character_sheet.image_at((239, 260, 16, 24), colorkey = (107, 49, 156)), character_sheet.image_at((258, 260, 16, 16), colorkey = (107, 49, 156))]

item_block_shimmer_list = [[], [], [], []]
coin_shimmer_list = [[], [], [], []]

fire_ball_list_right = [enemy_sheet.image_at((26, 150, 8, 8), colorkey = (255, 255, 255)), enemy_sheet.image_at((26, 165, 8, 8), colorkey = (255, 255, 255)), enemy_sheet.image_at((41, 150, 8, 8), colorkey = (255, 255, 255)), enemy_sheet.image_at((41, 165, 8, 8), colorkey = (255, 255, 255))]
fire_ball_list_left = []
for image in fire_ball_list_right:
    fire_ball_list_left.append(pygame.transform.flip(image, True, False))

explosion_image_list = [enemy_sheet.image_at((360, 184, 16, 16), colorkey = (255, 255, 255)), enemy_sheet.image_at((390, 184, 16, 16), colorkey = (255, 255, 255)), enemy_sheet.image_at((420, 184, 16, 16), colorkey = (255, 255, 255))]

fire_flower_image = item_sheet.image_at((0, 16, 16,16), colorkey = (255, 255, 255))

power_star_image = [item_sheet.image_at((0, 32, 16,16), colorkey = (255, 255, 255)), item_sheet.image_at((16, 32, 16,16), colorkey = (255, 255, 255)), item_sheet.image_at((32, 32, 16,16), colorkey = (255, 255, 255)), item_sheet.image_at((0, 48, 16,16), colorkey = (255, 255, 255))]

shimmer_frame = 0


#star power vvv
small_mario_standing_left_image = [mario_sheet.image_at((181, 0, 13, 16), colorkey = (255, 255, 255)),
                                              star_power_sheet_green.image_at((181, 0, 13, 16), colorkey = (255, 255, 255)),
                                              star_power_sheet_small_white.image_at((181, 0, 13, 16), colorkey = (255, 255, 255)),
                                              star_power_sheet_red.image_at((181, 0, 13, 16), colorkey = (255, 255, 255)),
                                              star_power_sheet_black.image_at((181, 0, 13, 16), colorkey = (255, 255, 255))]

small_mario_standing_right_image = [mario_sheet.image_at((211, 0, 13, 16), colorkey = (255, 255, 255)),
                                               star_power_sheet_green.image_at((211, 0, 13, 16), colorkey = (255, 255, 255)),
                                               star_power_sheet_small_white.image_at((211, 0, 13, 16), colorkey = (255, 255, 255)),
                                               star_power_sheet_red.image_at((211, 0, 13, 16), colorkey = (255, 255, 255)),
                                               star_power_sheet_black.image_at((211, 0, 13, 16), colorkey = (255, 255, 255))]

tall_mario_standing_left_image = [mario_sheet.image_at((180, 52, 16, 32), colorkey = (255, 255, 255)),
                                             star_power_sheet_green.image_at((180, 52, 16, 32), colorkey = (255, 255, 255)),
                                             star_power_sheet_green.image_at((180, 122, 16, 32), colorkey = (255, 255, 255)),
                                             star_power_sheet_red.image_at((180, 52, 16, 32), colorkey = (255, 255, 255)),
                                             star_power_sheet_black.image_at((180, 52, 16, 32), colorkey = (255, 255, 255))]

tall_mario_standing_right_image = [mario_sheet.image_at((209, 52, 16, 32),colorkey = (255, 255, 255)),
                                              star_power_sheet_green.image_at((209, 52, 16, 32),colorkey = (255, 255, 255)),
                                              star_power_sheet_green.image_at((209, 122, 16, 32), colorkey = (255, 255, 255)),
                                              star_power_sheet_red.image_at((209, 52, 16, 32), colorkey = (255, 255, 255)),
                                              star_power_sheet_black.image_at((209, 52, 16, 32), colorkey = (255, 255, 255))]


small_mario_turning_left_image = [mario_sheet.image_at((60, 0, 14, 16), colorkey = (255, 255, 255)),
                                             star_power_sheet_green.image_at((60, 0, 14, 16), colorkey = (255, 255, 255)),
                                             star_power_sheet_small_white.image_at((60, 0, 14, 16), colorkey = (255, 255, 255)),
                                             star_power_sheet_red.image_at((60, 0, 14, 16), colorkey = (255, 255, 255)),
                                             star_power_sheet_black.image_at((60, 0, 14, 16), colorkey = (255, 255, 255))]

small_mario_turning_right_image = [mario_sheet.image_at((331, 0, 14, 16), colorkey = (255, 255, 255)),
                                              star_power_sheet_green.image_at((331, 0, 14, 16), colorkey = (255, 255, 255)),
                                              star_power_sheet_small_white.image_at((331, 0, 14, 16), colorkey = (255, 255, 255)),
                                              star_power_sheet_red.image_at((331, 0, 14, 16), colorkey = (255, 255, 255)),
                                              star_power_sheet_black.image_at((331, 0, 14, 16), colorkey = (255, 255, 255))]


tall_mario_turning_left_image = [mario_sheet.image_at((329, 52, 16, 32), colorkey = (255, 255, 255)),
                                            star_power_sheet_green.image_at((329, 52, 16, 32), colorkey = (255, 255, 255)),
                                            star_power_sheet_black.image_at((337, 122, 16, 32), colorkey = (255, 255, 255)),
                                            star_power_sheet_red.image_at((329, 52, 16, 32), colorkey = (255, 255, 255)),
                                            star_power_sheet_black.image_at((329, 52, 16, 32), colorkey = (255, 255, 255))]

tall_mario_turning_right_image = [mario_sheet.image_at((59, 52, 16, 32), colorkey = (255, 255, 255)),
                                             star_power_sheet_green.image_at((59, 52, 16, 32), colorkey = (255, 255, 255)),
                                             star_power_sheet_black.image_at((52, 122, 16, 32), colorkey = (255, 255, 255)),
                                             star_power_sheet_red.image_at((59, 52, 16, 32), colorkey = (255, 255, 255)),
                                             star_power_sheet_black.image_at((59, 52, 16, 32), colorkey = (255, 255, 255))]

small_mario_running_left_list = [[mario_sheet.image_at((150, 0, 14, 17), colorkey = (255, 255, 255)), mario_sheet.image_at((121, 0, 12, 17), colorkey = (255, 255, 255)), mario_sheet.image_at((89, 0, 16, 17), colorkey = (255, 255, 255)), mario_sheet.image_at((121, 0, 12, 17), colorkey = (255, 255, 255))],
                                [star_power_sheet_green.image_at((150, 0, 14, 17), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((121, 0, 12, 17), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((89, 0, 16, 17), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((121, 0, 12, 17), colorkey = (255, 255, 255))],
                                [star_power_sheet_small_white.image_at((150, 0, 14, 17), colorkey = (255, 255, 255)), star_power_sheet_small_white.image_at((121, 0, 12, 17), colorkey = (255, 255, 255)), star_power_sheet_small_white.image_at((89, 0, 16, 17), colorkey = (255, 255, 255)), star_power_sheet_small_white.image_at((121, 0, 12, 17), colorkey = (255, 255, 255))],
                                [star_power_sheet_red.image_at((150, 0, 14, 17), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((121, 0, 12, 17), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((89, 0, 16, 17), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((121, 0, 12, 17), colorkey = (255, 255, 255))],
                                [star_power_sheet_black.image_at((150, 0, 14, 17), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((121, 0, 12, 17), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((89, 0, 16, 17), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((121, 0, 12, 17), colorkey = (255, 255, 255))]]

small_mario_running_right_list = [[mario_sheet.image_at((241, 0, 14, 17), colorkey = (255, 255, 255)), mario_sheet.image_at((272, 0, 12, 17), colorkey = (255, 255, 255)), mario_sheet.image_at((300, 0, 16, 17), colorkey = (255, 255, 255)), mario_sheet.image_at((272, 0, 12, 17), colorkey = (255, 255, 255))],
                                [star_power_sheet_green.image_at((241, 0, 14, 17), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((272, 0, 12, 17), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((300, 0, 16, 17), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((272, 0, 12, 17), colorkey = (255, 255, 255))],
                                [star_power_sheet_small_white.image_at((241, 0, 14, 17), colorkey = (255, 255, 255)), star_power_sheet_small_white.image_at((272, 0, 12, 17), colorkey = (255, 255, 255)), star_power_sheet_small_white.image_at((300, 0, 16, 17), colorkey = (255, 255, 255)), star_power_sheet_small_white.image_at((272, 0, 12, 17), colorkey = (255, 255, 255))],
                                [star_power_sheet_red.image_at((241, 0, 14, 17), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((272, 0, 12, 17), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((300, 0, 16, 17), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((272, 0, 12, 17), colorkey = (255, 255, 255))],
                                [star_power_sheet_black.image_at((241, 0, 14, 17), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((272, 0, 12, 17), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((300, 0, 16, 17), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((272, 0, 12, 17), colorkey = (255, 255, 255))]]




tall_mario_running_left_list = [[mario_sheet.image_at((150, 52, 16, 32), colorkey = (255, 255, 255)), mario_sheet.image_at((121, 52, 14, 32), colorkey = (255, 255, 255)), mario_sheet.image_at((90, 53, 16, 32), colorkey = (255, 255, 255)), mario_sheet.image_at((121, 52, 14, 32), colorkey = (255, 255, 255))],
                                           [star_power_sheet_green.image_at((150, 52, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((121, 52, 14, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((90, 53, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((121, 52, 14, 32), colorkey = (255, 255, 255))],
                                           [star_power_sheet_green.image_at((152, 122, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((128, 122, 14, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((102, 122, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((128, 122, 14, 32), colorkey = (255, 255, 255))],
                                           [star_power_sheet_red.image_at((150, 52, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((121, 52, 14, 32), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((90, 53, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((121, 52, 14, 32), colorkey = (255, 255, 255))],
                                           [star_power_sheet_black.image_at((150, 52, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((121, 52, 14, 32), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((90, 53, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((121, 52, 14, 32), colorkey = (255, 255, 255))]]
                                           
                                           

tall_mario_running_right_list = [[mario_sheet.image_at((239, 52, 16, 32), colorkey = (255, 255, 255)), mario_sheet.image_at((270, 52, 14, 32), colorkey = (255, 255, 255)), mario_sheet.image_at((299, 53, 16, 32), colorkey = (255, 255, 255)), mario_sheet.image_at((270, 52, 14, 32), colorkey = (255, 255, 255))],
                                           [star_power_sheet_green.image_at((239, 52, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((270, 52, 14, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((299, 53, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((270, 52, 14, 32), colorkey = (255, 255, 255))],
                                           [star_power_sheet_green.image_at((237, 122, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((263, 122, 14, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((287, 122, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((263, 122, 14, 32), colorkey = (255, 255, 255))],
                                           [star_power_sheet_red.image_at((239, 52, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((270, 52, 14, 32), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((299, 53, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((270, 52, 14, 32), colorkey = (255, 255, 255))],
                                           [star_power_sheet_black.image_at((239, 52, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((270, 52, 14, 32), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((299, 53, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((270, 52, 14, 32), colorkey = (255, 255, 255))]]


tall_mario_crouching_left_image = [mario_sheet.image_at((0, 57, 16, 25), colorkey = (255, 255, 255)),
                                              star_power_sheet_green.image_at((0, 57, 16, 25), colorkey = (255, 255, 255)),
                                              star_power_sheet_green.image_at((0, 127, 16, 25), colorkey = (255, 255, 255)),
                                              star_power_sheet_red.image_at((0, 57, 16, 25), colorkey = (255, 255, 255)),
                                              star_power_sheet_black.image_at((0, 57, 16, 25), colorkey = (255, 255, 255))]

tall_mario_crouching_right_image = [mario_sheet.image_at((389, 57, 16, 25), colorkey = (255, 255, 255)),
                                               star_power_sheet_green.image_at((389, 57, 16, 25), colorkey = (255, 255, 255)),
                                               star_power_sheet_green.image_at((389, 127, 16, 25), colorkey = (255, 255, 255)),
                                               star_power_sheet_red.image_at((389, 57, 16, 25), colorkey = (255, 255, 255)),
                                               star_power_sheet_black.image_at((389, 57, 16, 25), colorkey = (255, 255, 255))]


small_mario_jumping_left_image = [mario_sheet.image_at((29, 0, 16, 16), colorkey = (255, 255, 255)),
                                             star_power_sheet_green.image_at((29, 0, 16, 16), colorkey = (255, 255, 255)),
                                             star_power_sheet_small_white.image_at((29, 0, 16, 16), colorkey = (255, 255, 255)),
                                             star_power_sheet_red.image_at((29, 0, 16, 16), colorkey = (255, 255, 255)),
                                             star_power_sheet_black.image_at((29, 0, 16, 16), colorkey = (255, 255, 255))]

small_mario_jumping_right_image = [mario_sheet.image_at((359, 0, 16, 16), colorkey = (255, 255, 255)),
                                              star_power_sheet_green.image_at((359, 0, 16, 16), colorkey = (255, 255, 255)),
                                              star_power_sheet_small_white.image_at((359, 0, 16, 16), colorkey = (255, 255, 255)),
                                              star_power_sheet_red.image_at((359, 0, 16, 16), colorkey = (255, 255, 255)),
                                              star_power_sheet_black.image_at((359, 0, 16, 16), colorkey = (255, 255, 255))]

tall_mario_jumping_left_image = [mario_sheet.image_at((30, 52, 16, 32), colorkey = (255, 255, 255)),
                                            star_power_sheet_green.image_at((30, 52, 16, 32), colorkey = (255, 255, 255)),
                                            star_power_sheet_green.image_at((27, 122, 16, 32), colorkey = (255, 255, 255)),
                                            star_power_sheet_red.image_at((30, 52, 16, 32), colorkey = (255, 255, 255)),
                                            star_power_sheet_black.image_at((30, 52, 16, 32), colorkey = (255, 255, 255))]

tall_mario_jumping_right_image = [mario_sheet.image_at((359, 52, 16, 32), colorkey = (255, 255, 255)),
                                            star_power_sheet_green.image_at((359, 52, 16, 32), colorkey = (255, 255, 255)),
                                            star_power_sheet_green.image_at((362, 122, 16, 32), colorkey = (255, 255, 255)),
                                            star_power_sheet_red.image_at((359, 52, 16, 32), colorkey = (255, 255, 255)),
                                            star_power_sheet_black.image_at((359, 52, 16, 32), colorkey = (255, 255, 255))]



small_mario_swimming_left_list = [[character_sheet.image_at((78, 44, 16, 16), colorkey = (107, 49, 156)), character_sheet.image_at((62, 44, 16, 16), colorkey = (107, 49, 156))],
                                             [star_power_sheet_green.image_at((90, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((2, 31, 16, 16), colorkey = (255, 255, 255))],
                                             [star_power_sheet_small_white.image_at((90, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_small_white.image_at((2, 31, 16, 16), colorkey = (255, 255, 255))],
                                             [star_power_sheet_red.image_at((90, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((2, 31, 16, 16), colorkey = (255, 255, 255))],
                                             [star_power_sheet_black.image_at((90, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((2, 31, 16, 16), colorkey = (255, 255, 255))]]
                                  
small_mario_swimming_right_list = [[character_sheet.image_at((422, 44, 16, 16), colorkey = (107, 49, 156)), character_sheet.image_at((438, 44, 16, 16), colorkey = (107, 49, 156))],
                                              [star_power_sheet_green.image_at((301, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((389, 31, 16, 16), colorkey = (255, 255, 255))],
                                              [star_power_sheet_small_white.image_at((301, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_small_white.image_at((389, 31, 16, 16), colorkey = (255, 255, 255))],
                                              [star_power_sheet_red.image_at((301, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((389, 31, 16, 16), colorkey = (255, 255, 255))],
                                              [star_power_sheet_black.image_at((301, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((389, 31, 16, 16), colorkey = (255, 255, 255))]]

small_mario_paddling_left_list = [[[mario_sheet.image_at((120, 29, 16, 16), colorkey = (255, 255, 255)), mario_sheet.image_at((150, 29, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_green.image_at((120, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((150, 29, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_small_white.image_at((120, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_small_white.image_at((150, 29, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_red.image_at((120, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((150, 29, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_black.image_at((120, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((150, 29, 16, 16), colorkey = (255, 255, 255))]],
                                              
                                               [[mario_sheet.image_at((180, 29, 16, 16), colorkey = (255, 255, 255)), mario_sheet.image_at((180, 29, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_green.image_at((180, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((180, 29, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_small_white.image_at((180, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_small_white.image_at((180, 29, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_red.image_at((180, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((180, 29, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_black.image_at((180, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((180, 29, 16, 16), colorkey = (255, 255, 255))]]]

small_mario_paddling_right_list = [[[mario_sheet.image_at((271, 29, 16, 16), colorkey = (255, 255, 255)), mario_sheet.image_at((241, 30, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_green.image_at((271, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((241, 30, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_small_white.image_at((271, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_small_white.image_at((241, 30, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_red.image_at((271, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((241, 30, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_black.image_at((271, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((241, 30, 16, 16), colorkey = (255, 255, 255))]],
                                              
                                               [[mario_sheet.image_at((210, 29, 16, 16), colorkey = (255, 255, 255)), mario_sheet.image_at((210, 29, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_green.image_at((210, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((210, 29, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_small_white.image_at((210, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_small_white.image_at((210, 29, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_red.image_at((210, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((210, 29, 16, 16), colorkey = (255, 255, 255))],
                                               [star_power_sheet_black.image_at((210, 29, 16, 16), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((210, 29, 16, 16), colorkey = (255, 255, 255))]]]

tall_mario_swimming_left_list = [[mario_sheet.image_at((180, 86, 16, 32), colorkey = (255, 255, 255)), mario_sheet.image_at((103, 85, 16, 32), colorkey = (255, 255, 255))],
                                           [star_power_sheet_green.image_at((180, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((103, 85, 16, 32), colorkey = (255, 255, 255))],
                                           [star_power_sheet_green.image_at((180, 156, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((103, 155, 16, 32), colorkey = (255, 255, 255))],
                                           [star_power_sheet_red.image_at((180, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((103, 85, 16, 32), colorkey = (255, 255, 255))],
                                           [star_power_sheet_black.image_at((180, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((103, 85, 16, 32), colorkey = (255, 255, 255))]]
                                            
tall_mario_swimming_right_list = [[mario_sheet.image_at((209, 86, 16, 32), colorkey = (255, 255, 255)), mario_sheet.image_at((286, 85, 16, 32), colorkey = (255, 255, 255))],
                                  [star_power_sheet_green.image_at((209, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((286, 85, 16, 32), colorkey = (255, 255, 255))],
                                  [star_power_sheet_green.image_at((209, 156, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((286, 155, 16, 32), colorkey = (255, 255, 255))],
                                  [star_power_sheet_red.image_at((209, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((286, 85, 16, 32), colorkey = (255, 255, 255))],
                                  [star_power_sheet_black.image_at((209, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((286, 85, 16, 32), colorkey = (255, 255, 255))]]

tall_mario_paddling_left_list = [[[mario_sheet.image_at((152, 86, 16, 32), colorkey = (255, 255, 255)), mario_sheet.image_at((78, 85, 16, 32), colorkey = (255, 255, 255))],
                                   [star_power_sheet_green.image_at((152, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((78, 85, 16, 32), colorkey = (255, 255, 255))],
                                   [star_power_sheet_green.image_at((152, 156, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((78, 155, 16, 32), colorkey = (255, 255, 255))],
                                   [star_power_sheet_red.image_at((152, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((78, 85, 16, 32), colorkey = (255, 255, 255))],
                                   [star_power_sheet_black.image_at((152, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((78, 85, 16, 32), colorkey = (255, 255, 255))]],

                                   [[mario_sheet.image_at((127, 86, 16, 32), colorkey = (255, 255, 255)), mario_sheet.image_at((52, 85, 16, 32), colorkey = (255, 255, 255))],
                                    [star_power_sheet_green.image_at((127, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((52, 85, 16, 32), colorkey = (255, 255, 255))],
                                    [star_power_sheet_green.image_at((127, 156, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((52, 155, 16, 32), colorkey = (255, 255, 255))],
                                    [star_power_sheet_red.image_at((127, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((52, 85, 16, 32), colorkey = (255, 255, 255))],
                                    [star_power_sheet_black.image_at((127, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((52, 85, 16, 32), colorkey = (255, 255, 255))]]]

tall_mario_paddling_right_list = [[[mario_sheet.image_at((237, 86, 16, 32), colorkey = (255, 255, 255)), mario_sheet.image_at((311, 85, 16, 32), colorkey = (255, 255, 255))],
                                   [star_power_sheet_green.image_at((237, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((311, 85, 16, 32), colorkey = (255, 255, 255))],
                                   [star_power_sheet_green.image_at((237, 156, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((311, 155, 16, 32), colorkey = (255, 255, 255))],
                                   [star_power_sheet_red.image_at((237, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((311, 85, 16, 32), colorkey = (255, 255, 255))],
                                   [star_power_sheet_black.image_at((237, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((311, 85, 16, 32), colorkey = (255, 255, 255))]],


                                   [[mario_sheet.image_at((262, 86, 16, 32), colorkey = (255, 255, 255)), mario_sheet.image_at((337, 85, 16, 32), colorkey = (255, 255, 255))],
                                    [star_power_sheet_green.image_at((262, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((337, 85, 16, 32), colorkey = (255, 255, 255))],
                                    [star_power_sheet_green.image_at((262, 156, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_green.image_at((337, 155, 16, 32), colorkey = (255, 255, 255))],
                                    [star_power_sheet_red.image_at((262, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_red.image_at((337, 85, 16, 32), colorkey = (255, 255, 255))],
                                    [star_power_sheet_black.image_at((262, 86, 16, 32), colorkey = (255, 255, 255)), star_power_sheet_black.image_at((337, 85, 16, 32), colorkey = (255, 255, 255))]]]


#star power ^^^

for y in range(4):#fetch item blocks from sprite sheet
    for x in range(4):
        item_block_shimmer_list[y].append(item_sheet.image_at((x*16 + y*144, 48, 16,16), colorkey = (255, 255, 255)))
for y in range(4):#fetch coins from sprite sheet
    for x in range(4):
        coin_shimmer_list[y].append(item_sheet.image_at((x*16 + y*144, 64, 16,16), colorkey = (255, 255, 255)))


shimmer_time = pygame.time.get_ticks()
shimmer_time_between_frames = 150
buffer_time = 100

color_palletes = [0, 1, 2, 3]
under_ground_color_palletes = [1, 1, 2, 1]

class General():
    def __init__(self):
        self.level = 1
        self.player_start_position_x = 0
        self.player_start_position_y = 0
        self.level_end_animation = False
        self.enter_pipe = None
        self.entering_pipe = False
        self.color_pallete = color_palletes[self.level - 1]
        self.under_ground_color_pallete = under_ground_color_palletes[self.level - 1]
    def update(self):
        self.color_pallete = color_palletes[self.level - 1]
        self.under_ground_color_pallete = under_ground_color_palletes[self.level - 1]
general = General()

class Player(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Player, self).__init__()

        self.width = 10
        self.height = 12
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(topleft=position)
        self.temp_rect = self.image.get_rect(topleft=position)
        self.image = small_mario_standing_right_image[0]
        self.image_rect = self.image.get_rect(topleft=((position[0] - (self.image.get_width() - self.rect.width) / 2), (position[1] - (self.image.get_height() - self.rect.height) / 2)))
        
        self.hitbox_image = pygame.Surface((self.width, self.height))
        self.hitbox_image.fill(pygame.Color('black'))

        self.jump = False#checks if you have performed a jump
        self.jump_buffer = False
        self.crouch = False
        self.standing = False#checks if you are standing
        self.just_fell = False
        self.wall_slide = False#checks if you are sliding on wall
        self.wall_jump = False#checks if you have performed a wall jump
        self.hold_jump = False
        self.speed = 4
        
        self.tall = False
        self.fire_form = False
        self.star_power = False
        
        self.direction = 'right'
        self.attack_button_pressed = False
        self.jump_button_pressed = False
        self.stuck_jump_button_pressed = False

        self.running_frame = 0
        self.running_sub_frame = 0
        self.swimming_frame = 0
        self.swimming_sub_frame = 0
        self.paddling_frame = 0
        self.paddling_sub_frame = 0
        self.paddling = False

        self.pixel_offset_y = 0
        self.pixel_offset_x = 0

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
        self.star_power_time = None
        self.star_power_duration = 10000
        self.jump_buffer_time = 0
        self.jump_buffer_hold = False#checks if jump button is being held a
        self.cyote_time = 0
        
        self.star_power_frame = 0
        self.star_power_sub_frame = 0

        self.break_point = False
        

    def update(self):
        
        keys = pygame.key.get_pressed()
        #timed events
        self.jump_buffer += 1
        if self.time is not None:
            if pygame.time.get_ticks() - self.time >= self.invincibility_time:
                self.invincibility = False
                self.time = None
                
        if self.star_power_time is not None:
            if pygame.time.get_ticks() - self.star_power_time >= self.star_power_duration:
                self.star_power = False
                self.star_power_time = None

        if self.star_power_time is not None:
            if pygame.time.get_ticks() - self.star_power_time <= self.star_power_duration - 3000:
                self.star_power_sub_frame += 1
                if self.star_power_sub_frame >= 4:
                    self.star_power_sub_frame = 0
                    self.star_power_frame += 1
                    if self.star_power_frame >=5:
                        self.star_power_frame = 0
            elif self.fire_form == True:
                self.star_power_frame = 2
            else:
                self.star_power_frame = 0
        elif self.fire_form == True:
            self.star_power_frame = 2
        else:
            self.star_power_frame = 0
        

        
        if water_collision(self) == True:#water gravity
            
            self.velocity.y += 0.2
            if self.velocity.y >= 2:
                self.velocity.y = 2
            self.rect.y += 1
            if self.velocity.y > 0:
                for block in block_group:
                    if self.rect.colliderect(block):
                        self.standing = True
            self.rect.y -= 1
        else:#normal gravity
            if self.wall_slide == False:
                self.velocity.y = self.velocity.y + 0.75
                if self.velocity.y >= 6:
                    self.velocity.y = 6
            else:
                self.velocity.y = self.velocity.y + 0.5
                if self.velocity.y >= 3:
                    self.velocity.y = 3
        print(self.velocity.y)
        if self.rect.top > screen_Height and self.rect.top < 600:
            dead()
        elif self.rect.top > screen_Height + 640 and self.rect.top < 1240:
            dead()
                
        if keys[pygame.K_ESCAPE]:
            running = False
            pygame.quit()

        if keys[pygame.K_PLUS]:
            self.break_point = True

        if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:#throw fireball
            if self.attack_button_pressed == False:
                if self.fire_form == True:
                    if len(fire_ball_group) < 3:
                        if self.direction == 'left':
                            fire_ball = Fire_ball(position = (self.rect.x, self.rect.y + 16), direction = self.direction)
                        if self.direction == 'right':
                            fire_ball = Fire_ball(position = (self.rect.x + 8, self.rect.y + 16), direction = self.direction)
            self.attack_button_pressed = True
        else:
            self.attack_button_pressed = False
            
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:#move left
            self.direction = 'left'
            if self.rect.x > 0:#makes sure you can't leave the level area
                if water_collision(self):#in water
                    if self.standing == False:
                        self.velocity.x -= 0.1
                        if self.velocity.x <= -2:
                            self.velocity.x = -2
                    else:
                        self.velocity.x -= 0.1
                        if self.velocity.x <= -1:
                            self.velocity.x = -1
                else:#on land
                    if self.standing == True:
                        if self.crouch == False:
                            self.velocity.x -= 0.2
                            if self.velocity.x < -4:
                                self.velocity.x = -4
                    else:#move slower if you are in the air
                        self.velocity.x -= 0.15
                        if self.velocity.x < -4:
                            self.velocity.x = -4
            else:
                self.velocity.x = 0
            if self.crouch == True:
                if player.velocity.x < 0:
                    if self.standing == True:
                        player.velocity.x += 0.25
        
        
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:#move right
            self.direction = 'right'
            if self.rect.x + self.width < level_width:#makes sure you can't leave the level area
                if water_collision(self):#in water
                    if self.standing == False:
                        self.velocity.x += 0.1
                        if self.velocity.x >= 2:
                            self.velocity.x = 2
                    else:
                        self.velocity.x += 0.1
                        if self.velocity.x >= 1:
                            self.velocity.x = 1
                else:#on land
                    if self.standing == True:
                        if self.crouch == False:
                            self.velocity.x += 0.2
                            if self.velocity.x > 4:
                                self.velocity.x = 4
                    else:#move slower if you are in the air
                        self.velocity.x += 0.15
                        if self.velocity.x > 4:
                            self.velocity.x = 4
            else:
                self.velocity.x = 0
            if self.crouch == True:
                if player.velocity.x >= 0:
                    if self.standing == True:
                        player.velocity.x -= 0.25
        
        else:#stand still
            if player.velocity.x > 0:
                if self.standing == True:
                    player.velocity.x -= 0.15#while on the ground
                else:
                    player.velocity.x -= 0.02#while in the air
            if player.velocity.x < 0:
                if self.standing == True:
                    player.velocity.x += 0.15#while on the ground
                else:
                    player.velocity.x += 0.02#while in the air
            if self.velocity.x < 0.15 and self.velocity.x >-0.15:#makes sure velocity.x returns to zero
                self.velocity.x = 0
                    
        if self.rect.x < 0:#if player goes outside the play area
            self.rect.x = 0
        if keys[pygame.K_w] or keys[pygame.K_UP]:#jump
            self.just_fell = False
            if water_collision(self) == True:#in water
                if self.jump_button_pressed == False:
                    self.paddling = True#for animation
                    self.jump_button_pressed = True
                    self.velocity.y -= 5
                    if self.velocity.y < -5:
                        self.velocity.y = -5
            else:#on land
                if self.jump_button_pressed == False or self.jump_buffer <= 4:
                    self.jump_button_pressed = True
                    if self.standing == True or self.cyote_time > 0:
                        self.cyote_time = 0
                        self.jump = True
                        self.velocity.y = -6
                        if self.velocity.x > 0:#jump higher the faster you run
                            self.velocity.y -= self.velocity.x /4
                        if self.velocity.x < 0:#jump higher the faster you run
                            self.velocity.y += self.velocity.x /4
                    elif self.wall_slide == True:#wall jump
                        self.wall_jump = True
                        self.velocity.y = -6
                        if self.velocity.x < 0:
                            self.velocity.x = 4
                        elif self.velocity.x > 0:
                            self.velocity.x = -4
                    elif self.jump_buffer_hold == False:
                        self.jump_buffer_hold = True
                        self.jump_buffer = 0
                if self.jump_button_pressed == True:#hold the jump button to increase jump height
                    if self.velocity.y < 0:
                        self.velocity.y -= 0.50
            for pipe in pipe_group:
                self.rect.top -= 1
                if self.rect.colliderect(pipe.rect):#enter pipe
                    if self.rect.bottom >= pipe.rect.bottom:
                        if self.image_rect.left > pipe.rect.left:
                            if self.image_rect.right < pipe.rect.right:
                                if pipe.warp_destination != None:
                                    general.entering_pipe = True
                                    general.enter_pipe = pipe
                else:
                    self.rect.top += 1
        else:
            self.jump_button_pressed = False
            self.jump_buffer_hold = False
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:#if you press crouch button
            self.crouch = True
            for pipe in pipe_group:
                if pipe.warp_destination != None:#enter pipe
                    self.rect.bottom += 1
                    if self.rect.colliderect(pipe):
                        if self.rect.top < pipe.rect.top:
                            if self.image_rect.left > pipe.rect.left:
                                if self.image_rect.right < pipe.rect.right:
                                    general.entering_pipe = True
                                    general.enter_pipe = pipe
                    else: self.rect.bottom -= 1
        else:#when you release the crouch button
            if self.crouch == True:
                self.crouch = False
                update_hitbox()
                
        for block in all_block_group:#if a block is above you when you release the crouch button
            if block not in pipe_group:#prevents bug when entering pipe
                if self.rect.colliderect(block.rect):
                    if not keys[pygame.K_w] and not keys[pygame.K_UP]:
                        self.stuck_jump_button_pressed = False
                    if block.rect.y <= self.rect.y:
                        if block.thin == False:
                            self.crouch = True
                            self.height = 12
                            if self.tall == True:
                                self.hitbox_image = pygame.Surface((self.width, self.height))
                                self.rect = self.hitbox_image.get_rect(bottomleft=self.rect.bottomleft)
                            if block.rect.collidepoint(player.rect.x, player.rect.y):
                                if not crouch_unstuck_right() == True:
                                    self.rect.x += 1
                            if block.rect.collidepoint(player.rect.x + player.width, player.rect.y):
                                if not crouch_unstuck_left() == True:
                                    self.rect.x -= 1
                            if keys[pygame.K_w] or keys[pygame.K_UP]:
                                if self.stuck_jump_button_pressed == False:
                                    self.stuck_jump_button_pressed = True
                                    if self.standing == True:
                                        self.jump = True
                                        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                                            self.velocity.x -= 0.5
                                        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                                            self.velocity.x += 0.5

        #animation
        if self.tall == False:#while small
            if self.velocity.x > 0:#running right
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:#turn left
                    self.image = small_mario_turning_left_image[self.star_power_frame]
                else:
                    self.image = small_mario_running_right_list[self.star_power_frame][self.running_frame]
                    self.running_sub_frame += self.velocity.x
                    if self.running_sub_frame >= 12:
                        self.running_sub_frame -= self.running_sub_frame
                        self.running_frame += 1
                        if self.running_frame >= 4:
                            self.running_frame = 0
                if self.jump == True:#jumping
                    self.image = small_mario_jumping_right_image[self.star_power_frame]
                
                        
                    
            elif self.velocity.x < 0:#running left
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:#turn right
                    self.image = small_mario_turning_right_image[self.star_power_frame]
                else:
                    self.image = small_mario_running_left_list[self.star_power_frame][self.running_frame]
                    self.running_sub_frame += (-self.velocity.x)
                    if self.running_sub_frame >= 12:
                        self.running_sub_frame -= self.running_sub_frame
                        self.running_frame += 1
                        if self.running_frame >= 4:
                            self.running_frame = 0
                if self.jump == True:#jumping
                    self.image = small_mario_jumping_left_image[self.star_power_frame]



                    
            elif self.velocity.x == 0:#standing still
                if self.direction == 'left':
                    if self.jump == True:
                        self.image = small_mario_jumping_left_image[self.star_power_frame]
                    else:
                        self.image = small_mario_standing_left_image[self.star_power_frame]
                elif self.direction == 'right':
                    if self.jump == True:
                        self.image = small_mario_jumping_right_image[self.star_power_frame]
                    else:
                        self.image = small_mario_standing_right_image[self.star_power_frame]
                self.pixel_offset_x = 2
                        
            if water_collision(self) == True:#swimming
                self.rect.y += 1
                for block in all_block_group:
                    if self.rect.colliderect(block.rect):
                        if self.rect.bottom <= block.rect.bottom:
                            if self.velocity.y >= 0:
                                self.standing = True
                self.rect.y -= 1
                if self.standing == False:
                    if self.direction == 'left':
                        self.image = small_mario_swimming_left_list[self.star_power_frame][self.swimming_frame]
                    else:
                        self.image = small_mario_swimming_right_list[self.star_power_frame][self.swimming_frame]
                    if self.paddling == True:
                        if self.direction == 'left':
                            print(self.paddling_frame, self.star_power_frame, self.swimming_frame)
                            self.image = small_mario_paddling_left_list[self.paddling_frame][self.star_power_frame][self.swimming_frame]
                        else:
                            self.image = small_mario_paddling_right_list[self.paddling_frame][self.star_power_frame][self.swimming_frame]
                    self.swimming_sub_frame += 1
                    if self.swimming_sub_frame > 6:
                        self.swimming_frame += 1
                        self.swimming_sub_frame = 0
                        if self.swimming_frame >= 2:
                            self.swimming_frame = 0
                    if self.paddling == True:
                        self.paddling_sub_frame += 1
                        if self.paddling_sub_frame > 6:
                            self.paddling_frame += 1
                            self.paddling_sub_frame = 0
                            if self.paddling_frame >= 2:
                                self.paddling_frame = 0
                                self.paddling = False

                    
                    
        elif self.tall == True:#while tall
            if self.velocity.x > 0:#running right
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:#turn left
                    self.image = tall_mario_turning_left_image[self.star_power_frame]
                else:
                    self.image = tall_mario_running_right_list[self.star_power_frame][self.running_frame]
                    self.running_sub_frame += self.velocity.x
                    if self.running_sub_frame >= 12:
                        self.running_sub_frame -= self.running_sub_frame
                        self.running_frame += 1
                        if self.running_frame >= 4:
                            self.running_frame = 0
                if self.jump == True:#jumping
                    self.image = tall_mario_jumping_right_image[self.star_power_frame]
            elif self.velocity.x < 0:#running left
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:#turn right
                    self.image = tall_mario_turning_right_image[self.star_power_frame]
                else:
                    self.image = tall_mario_running_left_list[self.star_power_frame][self.running_frame]
                    self.running_sub_frame += (-self.velocity.x)
                    if self.running_sub_frame >= 12:
                        self.running_sub_frame -= self.running_sub_frame
                        self.running_frame += 1
                        if self.running_frame >= 4:
                            self.running_frame = 0
                if self.jump == True:#jumping
                    self.image = tall_mario_jumping_left_image[self.star_power_frame]
            elif self.velocity.x == 0:#standing still
                if self.direction == 'left':
                    if self.jump == True:
                        self.image = tall_mario_jumping_left_image[self.star_power_frame]
                    else:
                        self.image = tall_mario_standing_left_image[self.star_power_frame]
                elif self.direction == 'right':
                    if self.jump == True:
                        self.image = tall_mario_jumping_right_image[self.star_power_frame]
                    else:
                        self.image = tall_mario_standing_right_image[self.star_power_frame]

            if water_collision(self) == True:#swimming
                self.rect.y += 1
                for block in all_block_group:
                    if self.rect.colliderect(block.rect):
                        if self.rect.bottom <= block.rect.bottom:
                            if self.velocity.y >= 0:
                                self.standing = True
                self.rect.y -= 1
                if self.standing == False:
                    if self.direction == 'left':
                        self.image = tall_mario_swimming_left_list[self.star_power_frame][self.swimming_frame]
                    else:
                        self.image = tall_mario_swimming_right_list[self.star_power_frame][self.swimming_frame]
                    if self.paddling == True:
                        if self.direction == 'left':
                            self.image = tall_mario_paddling_left_list[self.paddling_frame][self.star_power_frame][self.swimming_frame]
                        else:
                            self.image = tall_mario_paddling_right_list[self.paddling_frame][self.star_power_frame][self.swimming_frame]
                    self.swimming_sub_frame += 1
                    if self.swimming_sub_frame > 6:
                        self.swimming_frame += 1
                        self.swimming_sub_frame = 0
                        if self.swimming_frame >= 2:
                            self.swimming_frame = 0
                    if self.paddling == True:
                        self.paddling_sub_frame += 1
                        if self.paddling_sub_frame > 6:
                            self.paddling_frame += 1
                            self.paddling_sub_frame = 0
                            if self.paddling_frame >= 2:
                                self.paddling_frame = 0
                                self.paddling = False

            if self.crouch == True:
                if self.direction == 'left':
                    self.image = tall_mario_crouching_left_image[self.star_power_frame]
                elif self.direction == 'right':
                        self.image = tall_mario_crouching_right_image[self.star_power_frame]
            self.image_rect = self.image.get_rect(topleft=((self.rect.left - (self.image.get_width() - self.rect.width) / 2), (self.rect.top - (self.image.get_height() - self.rect.height) / 2)))
       

            
        power_up_collision(self)#power_up_collision
        coin_collision(self)#coin_collision
        
        print(self.standing)
        self.velocity.x = round(self.velocity.x, 2)
        self.velocity.y = round(self.velocity.y, 2)
        self.rect.y += round(self.velocity.y)
        
        breakable_block_collision(self, self.velocity.y)
        item_block_collision(self, self.velocity.y)

        self.rect.y += 1
        for block in (block_group):
            if self.rect.colliderect(block):
                self.cyote_time = 0
        self.rect.y -= 1

        
        if block_collision(self, 0, self.velocity.y) == 'standing':#platform vertical collision
            self.cyote_time = 0
            if not keys[pygame.K_w]:
                self.jump = False
                self.wall_jump = False
                self.wall_slide = False
        elif self.standing == True:
            self.standing = False
            if self.jump == False:
                self.just_fell = True
                if self.cyote_time == 0:
                    self.cyote_time = 1



        #cyote time
        if self.cyote_time < 9 and self.cyote_time >= 1:
            self.cyote_time += 1
        else:
            self.cyote_time = 0

        #run over gaps
        if self.just_fell == True:
            self.just_fell = False
            self.temp_rect.x = self.rect.x + self.velocity.x * 3
            self.temp_rect.y = self.rect.y + self.velocity.y + self.height
            for block in all_block_group:
                if self.temp_rect.colliderect(block.rect):
                    self.rect.bottom = block.rect.top
                    self.velocity.y = 0
                    self.just_fell = True
            
        enemy_collision(self, 0, self.velocity.y)#enemy collision
        player_on_shell_collision(self, self.velocity.y)#shell collision

        update_hitbox()

        self.pixel_offset_x = (self.image.get_width() - self.rect.width) / 2
        if self.running_frame == 0:
            self.pixel_offset_y = 1
        else:
            self.pixel_offset_y = 0


        
        self.rect.x += round(self.velocity.x)   
        
        if general.entering_pipe == False:
            if not block_collision(self, self.velocity.x, 0) == None:#platform horizontal collsion
                if self.wall_slide == False:#makes it easier to wall jump
                    if self.velocity.x > 0:#stops vertical momentum when hitting a wall
                        self.velocity.x = 0.5
                    elif self.velocity.x < 0:
                        self.velocity.x = -0.5
                if self.velocity.y > 0:#starts wall slide
                    if self.standing == False:
                        self.wall_slide = True
            else:
                self.wall_slide = False
            for block in block_removal_group:#destroys breakable blocks
                block.kill()
        
        

class Camera(pygame.sprite.Sprite):
    
    def __init__(self, position):
        super(Camera, self).__init__()

        self.position = pygame.math.Vector2(position)

        self.image = pygame.Surface((screen_Width, screen_Height))
        self.respawn_image = pygame.Surface((screen_Width * 2, screen_Height * 2))
        self.rect = self.image.get_rect(topleft=position)
        self.respawn_rect = self.respawn_image.get_rect(topleft=position)

    def update(self):
        keys = pygame.key.get_pressed()
        
        if player.rect.x >= screen_Width / 2:
            self.position.x = player.rect.x - (screen_Width / 2)
            
        if player.rect.x < screen_Width / 2:
            self.position.x = 0

        self.rect.x = self.position.x
        self.rect.y = self.position.y
        self.respawn_rect.x = self.position.x - screen_Width / 2
        self.respawn_rect.y = self.position.y - screen_Height / 2


class Block(pygame.sprite.Sprite):

    def __init__(self, position, width, height):
        super(Block, self).__init__()
        
        block_group.add(self)
        all_block_group.add(self)
        all_sprite_group.add(self)

        self.breakable = False
        self.thin = False
        self.item_block = False

        self.width = width
        
        self.height = height

        if position.y < 640:
            self.image = make_tiled_image(block_image[general.color_pallete], self.width, self.height )
        else:
            self.image = make_tiled_image(block_image[general.under_ground_color_pallete], self.width, self.height )
        
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        self.bounce_offset = 0

class Item_block(pygame.sprite.Sprite):

    def __init__(self, position, item):
        super(Item_block, self).__init__()
        
        all_block_group.add(self)
        item_block_group.add(self)
        all_sprite_group.add(self)

        self.breakable = False
        self.thin = False
        
        self.item_block = True
        self.item = item
        self.quantity = 1
        
        self.time = None
        self.expiration_time = 3000

        #self.shimmer_frame = 0
        
        self.width = 16
        self.height = 16

        #self.image = pygame.Surface((self.width, self.height))
        self.image = item_block_image
        #self.image = item_block_image
        #self.image.fill(pygame.Color('brown'))
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        self.bounce_offset = 0

    def update(self):
        if self.time is not None:
            if pygame.time.get_ticks() - self.time >= self.expiration_time:
                if self.quantity > 1:
                    self.quantity = 1
                    self.time = None
        if self.quantity > 0:#if not empty
            #if pygame.time.get_ticks() - shimmer_time >= shimmer_time_between_frames:
                
                if shimmer_frame <= 5:
                    if self.position.y < 640:#above ground
                        self.image = item_block_shimmer_list[general.color_pallete][0]
                    else:#under ground
                        self.image = item_block_shimmer_list[general.under_ground_color_pallete][0]
                else:
                    if self.position.y < 640:#under ground
                        self.image = item_block_shimmer_list[general.color_pallete][shimmer_frame -5]
                    else:#under ground
                        self.image = item_block_shimmer_list[general.under_ground_color_pallete][shimmer_frame -5]

class Breakable_block(pygame.sprite.Sprite):

    def __init__(self, position, item):
        super(Breakable_block, self).__init__()
        
        all_block_group.add(self)
        breakable_block_group.add(self)
        all_sprite_group.add(self)

        self.breakable = True
        self.thin = False
        if item == None:
            self.item_block = False
        else:
            self.item_block = True
        
        self.item = item
        self.quantity = 1
        
        self.width = 16
        self.height = 16

        if position.y < 640:#above ground
            self.image = breakable_block_image[general.color_pallete]
        else:
            self.image = breakable_block_image[general.under_ground_color_pallete]
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)
        
        self.animation_frame = 0
        self.bounce_offset = 0


    def update(self):
        if self.animation_frame <= 5:
            self.bounce_offset -= 1
        else:
            self.bounce_offset += 1
        self.animation_frame += 1

        if self.animation_frame >= 10:
            self.animation_frame = 0
            self.bounce_offset = 0
            self.rect.topleft = self.position
            block_bounce_remove_group.add(self)

class Block_piece(pygame.sprite.Sprite):

    def __init__(self, position, corner):
        super(Block_piece, self).__init__()

        block_piece_group.add(self)
        all_sprite_group.add(self)
        
        self.velocity = pygame.math.Vector2(0, 0)

        if position.y < 640:#above ground
            if corner == 'top left':
                self.image = block_piece_topleft_image[general.color_pallete]
                self.velocity.x = -1
                self.velocity.y = -6
            elif corner == 'top right':
                self.image = block_piece_topright_image[general.color_pallete]
                self.velocity.x = 1
                self.velocity.y = -6
            elif corner == 'bottom left':
                self.image = block_piece_bottomleft_image[general.color_pallete]
                self.velocity.x = -2
                self.velocity.y = -3
            elif corner == 'bottom right':
                self.image = block_piece_bottomright_image[general.color_pallete]
                self.velocity.x = 2
                self.velocity.y = -3
        else:#under ground
            if corner == 'top left':
                self.image = block_piece_topleft_image[general.under_ground_color_pallete]
                self.velocity.x = -1
                self.velocity.y = -6
            elif corner == 'top right':
                self.image = block_piece_topright_image[general.under_ground_color_pallete]
                self.velocity.x = 1
                self.velocity.y = -6
            elif corner == 'bottom left':
                self.image = block_piece_bottomleft_image[general.under_ground_color_pallete]
                self.velocity.x = -2
                self.velocity.y = -3
            elif corner == 'bottom right':
                self.image = block_piece_bottomright_image[general.under_ground_color_pallete]
                self.velocity.x = 2
                self.velocity.y = -3

        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

    def update(self):
        #gravity
        self.velocity.y += 0.2

        if self.rect.top > screen_Height and self.rect.top < 600:
            self.kill()
        elif self.rect.top > screen_Height + 640 and self.rect.top < 1240:
            self.kill()

        self.velocity.x = round(self.velocity.x, 2)
        self.velocity.y = round(self.velocity.y, 2)
        self.rect.y += round(self.velocity.y)
        self.rect.x += round(self.velocity.x)
        

class Thin_block(pygame.sprite.Sprite):

    def __init__(self, position, width):
        super(Thin_block, self).__init__()
        
        all_block_group.add(self)
        thin_block_group.add(self)
        all_sprite_group.add(self)

        self.breakable = False
        self.thin = True
        self.item_block = False
        
        self.width = width
        self.height = 8
        if position.y < 640:#above ground
            if general.color_pallete == 2:
                self.image = make_tiled_image(thin_platform_image[general.color_pallete], self.width, self.height, colorkey = (163, 73, 164))
            else:
                self.image = make_tiled_image(thin_platform_image[general.color_pallete], self.width, self.height, colorkey = (255, 255, 255))
            self.fence_image = make_tiled_image(fence_image[general.color_pallete], self.width, self.height, colorkey = (255, 255, 255))
        else:#under ground
            if general.color_pallete == 2:
                self.image = make_tiled_image(thin_platform_image[general.under_ground_color_pallete], self.width, self.height, colorkey = (163, 73, 164))
            else:
                self.image = make_tiled_image(thin_platform_image[general.under_ground_color_pallete], self.width, self.height, colorkey = (255, 255, 255))
            self.fence_image = make_tiled_image(fence_image[general.under_ground_color_pallete], self.width, self.height, colorkey = (255, 255, 255))
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        self.bounce_offset = 0


class Pipe(pygame.sprite.Sprite):

    def __init__(self, position, height, warp_destination, direction, warp_direction):
        super(Pipe, self).__init__()
        pipe_group.add(self)
        all_block_group.add(self)
        all_sprite_group.add(self)
        
        self.breakable = True
        self.thin = False
        self.item_block = False

        self.warp_destination = warp_destination
        self.warp_direction = warp_direction
        
        self.width = 32
        self.height = height

        self.direction = direction

        if position.y < 640:#above ground
            if general.color_pallete == 2:
                self.image = make_tiled_image(pipe_image[general.color_pallete], self.width, self.height, colorkey = (163, 73, 164) )
            else:
                self.image = make_tiled_image(pipe_image[general.color_pallete], self.width, self.height, colorkey = (255, 255, 255) )
        else:#under ground
            if general.under_ground_color_pallete == 2:
                self.image = make_tiled_image(pipe_image[general.under_ground_color_pallete], self.width, self.height, colorkey = (163, 73, 164) )
            else:
                self.image = make_tiled_image(pipe_image[general.under_ground_color_pallete], self.width, self.height, colorkey = (255, 255, 255) )
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        self.bounce_offset = 0

class Water(pygame.sprite.Sprite):

    def __init__(self, position, width, height):
        super(Water, self).__init__()
        
        water_group.add(self)
        all_sprite_group.add(self)
        
        self.width = width
        self.height = height

        self.color = (66, 66, 255)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill (self.color)

        self.wave_image = make_tiled_image(water_top_image, self.width, 8, colorkey = (255, 255, 255) )
        
        self.rect = pygame.Surface ((self.width, self.height)).get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)
        
class Super_mushroom(pygame.sprite.Sprite):

    def __init__(self, position, spawn_counter, direction):
        super(Super_mushroom, self).__init__()

        super_mushroom_group.add(self)
        all_sprite_group.add(self)

        self.width = 16
        self.height = 16
        self.speed = 1
        self.direction = direction
        self.spawn_counter = spawn_counter
        
        #self.image = pygame.Surface((self.width, self.height))
        #self.image.fill(pygame.Color('dark green'))
        self.image = item_sheet.image_at((0, 0, 16,16), colorkey = (255, 255, 255))
        self.rect = self.image.get_rect(bottomleft=position)
        self.position = pygame.math.Vector2(position)

        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):
        if self.spawn_counter >= 16:#gravity
            if water_collision(self) == True:
                self.velocity.y += 0.2
                if self.velocity.y >= 2:
                    self.velocity.y = 2
            else:
                self.velocity.y += 0.5
                if self.velocity.y >= 8:
                    self.velocity.y = 8
            
            if self.rect.top > screen_Height and self.rect.top < 600:
                self.kill()
            elif self.rect.top > screen_Height + 640 and self.rect.top < 1240:
                self.kill()

            if self.rect.left <= 0:
                self.rect.left = 0
                self.direction = 'right'
      
            if self.direction == 'left':
                self.velocity.x = -self.speed
            else:
                self.velocity.x = self.speed

            self.rect.y += self.velocity.y
            block_collision(self, 0, self.velocity.y)#block collision detection y

            self.rect.x += self.velocity.x
            if not block_collision(self, self.velocity.x, 0) == None:#block collision detection x
                if self.velocity.x < 0:
                    self.direction = 'right'
                elif self.velocity.x > 0:
                    self.direction = 'left'  
        if self.spawn_counter < 16:
            self.rect.y -= 1
            self.spawn_counter += 1

class Fire_flower(pygame.sprite.Sprite):

    def __init__(self, position, spawn_counter):
        super(Fire_flower, self).__init__()

        fire_flower_group.add(self)
        all_sprite_group.add(self)

        self.width = 16
        self.height = 16
        
        self.direction = 'left'
        self.spawn_counter = spawn_counter
        
        self.image = fire_flower_image
        self.rect = self.image.get_rect(bottomleft=position)
        self.position = pygame.math.Vector2(position)

        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):
        if self.spawn_counter < 16:#spawn animation
            self.rect.y -= 1
            self.spawn_counter += 1

class Power_star(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Power_star, self).__init__()

        power_star_group.add(self)
        all_sprite_group.add(self)

        self.width = 16
        self.height = 16

        self.direction = 'right'

        self.speed = 2 

        self.image = power_star_image[0]

        self.rect = self.image.get_rect(bottomleft=position)
        self.position = pygame.math.Vector2(position)

        self.velocity = pygame.math.Vector2(0, 0)

        self.spawn_counter = 0
        self.spawn_sub_frame = 0

    def update(self):
        if self.spawn_counter < 16:#spawn animation
            self.rect.y -= 1
            self.spawn_counter += 1
        else:
            #gravity
            self.velocity.y += 0.2
            if self.direction == 'right':
                self.velocity.x = self.speed
            else:
                self.velocity.x = -self.speed
            self.rect.y += self.velocity.y
            if block_collision(self, 0, self.velocity.y) == 'standing':
                self.velocity.y = -3.5
            self.rect.x += self.velocity.x
            if not block_collision(self, self.velocity.x, 0) == None:
                if self.direction == 'right':
                    self.direction = 'left'
                elif self.direction == 'left':
                    self.direction = 'right'

class Fire_ball(pygame.sprite.Sprite):

    def __init__(self, position, direction):
        super(Fire_ball, self).__init__()

        fire_ball_group.add(self)
        all_sprite_group.add(self)

        self.width = 8
        self.height = 8
        
        self.speed = 6
        self.direction = direction

        self.animation_frame = 0
        self.animation_sub_frame = 0

        if self.direction == 'right':
            self.image = fire_ball_list_right[0]
        else:
            self.image = fire_ball_list_left[0]
        self.rect = self.image.get_rect(bottomleft=position)
        self.position = pygame.math.Vector2(position)

        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):
        self.velocity.y = self.velocity.y + 1#gravity
        if self.velocity.y >= 8:
            self.velocity.y = 8

        if self.direction == 'left':
            self.velocity.x = -5
        if self.direction == 'right':
            self.velocity.x = +5
            
        if self.rect.y >= screen_Height + camera.position.y:
            self.kill()
        if self.rect.x < camera.position.x:
            self.kill()
        if self.rect.x > camera.position.x + screen_Width:
            self.kill()


        self.rect.x += self.velocity.x
        if not block_collision(self, self.velocity.x, 0) == None:
            if self.direction == 'left':
                explosion = Explosion(position = (self.rect.x - 8, self.rect.y + 8))
            elif self.direction == 'right':
                explosion = Explosion(position = (self.rect.x, self.rect.y + 8))
            self.kill()

        self.rect.y += self.velocity.y
        if block_collision(self, 0, self.velocity.y) == 'standing':#platform vertical collision
            self.velocity.y = -6


        if fire_ball_collision(self) == True:
            if self.direction == 'left':
                explosion = Explosion(position = (self.rect.x - 8, self.rect.y + 8))
            elif self.direction == 'right':
                explosion = Explosion(position = (self.rect.x, self.rect.y + 8))
            self.kill()     


        self.animation_sub_frame += 1
        if self.animation_sub_frame >= 4:
            self.animation_sub_frame = 0 
            self.animation_frame += 1
            if self.animation_frame >= 4:
                self.animation_frame = 0
        if self.direction == 'left':
            self.image = fire_ball_list_left[self.animation_frame]
        elif self.direction == 'right':
            self.image = fire_ball_list_right[self.animation_frame]

class Explosion(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Explosion, self).__init__()

        explosion_group.add(self)
        all_sprite_group.add(self)

        self.image = explosion_image_list[0]

        self.animation_frame = 0
        self.animation_sub_frame = 0

        self.rect = self.image.get_rect(bottomleft=position)
        self.position = pygame.math.Vector2(position)

    def update(self):
        self.animation_sub_frame += 1
        if self.animation_sub_frame >= 4:
            self.animation_sub_frame = 0 
            self.animation_frame += 1
            if self.animation_frame >= 3:
                self.animation_frame = 0
                self.kill()
            self.image = explosion_image_list[self.animation_frame]
        
    

class Coin(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Coin, self).__init__()

        coin_group.add(self)
        all_sprite_group.add(self)

        self.size = 16

        self.shimmer_frame = 0
        
        self.image = item_sheet.image_at((0, 64, 16,16), colorkey = (255, 255, 255))
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):


        if shimmer_frame <= 5:
            if self.position.y < 640:#above ground
                self.image = coin_shimmer_list[general.color_pallete][0]
            else:#under ground
                self.image = coin_shimmer_list[general.under_ground_color_pallete][0]
        else:
            if self.position.y < 640:#under ground
                self.image = coin_shimmer_list[general.color_pallete][shimmer_frame -5]
            else:#under ground
                self.image = coin_shimmer_list[general.under_ground_color_pallete][shimmer_frame -5]
    

class Show_coin(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Show_coin, self).__init__()

        show_coin_group.add(self)
        all_sprite_group.add(self)

        self.size = 16

        self.spawn_counter = 0
        
        #self.image = pygame.Surface((self.size, self.size))
        #self.image.fill(pygame.Color('yellow'))
        self.image = coin_shimmer_list[general.color_pallete][0]
        self.rect = self.image.get_rect(bottomleft=position)
        self.position = pygame.math.Vector2(position)

        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):
        if self.spawn_counter <= 5:
            self.rect.y -= 4
        else:
            self.rect.y += 4
        self.spawn_counter += 1

        if self.spawn_counter >= 10:
            self.kill()


class Enemy(pygame.sprite.Sprite):

    def __init__(self, position, enemy_type):
        super(Enemy, self).__init__()

        enemy_group.add(self)
        all_sprite_group.add(self)

        self.enemy_type = enemy_type

        self.animation_frame = 0
        
        #hit boxes
        if self.enemy_type == 'goomba':
            self.width = 10
            self.height = 8
        elif self.enemy_type == 'red koopa' or self.enemy_type == 'green koopa':
            self.width = 10
            self.height = 13
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)

        self.position_rect = self.image.get_rect(topleft = position)

        self.hit_box_image = pygame.Surface((self.width, self.height))
        
        self.speed = 1
        self.direction = 'left'
        self.standing = False

        self.go = False
        self.shell = False

        if position.y < 640:#above ground
            if self.enemy_type == 'goomba':
                self.image = goomba_image_list[general.color_pallete][0]
            elif self.enemy_type == 'green koopa':
                self.image = green_koopa_left_image_list[general.color_pallete][0]
            elif self.enemy_type == 'red koopa':
                self.image = red_koopa_left_image_list[0]
            else:
                print(self.enemy_type)
        else:#under ground
            if self.enemy_type == 'goomba':
                self.image = goomba_image_list[general.under_ground_color_pallete][0]
            elif self.enemy_type == 'green koopa':
                self.image = green_koopa_left_image_list[general.under_ground_color_pallete][0]
            elif self.enemy_type == 'red koopa':
                self.image = red_koopa_left_image_list[0]
            else:
                print(self.enemy_type)
        self.hurt_box = self.image.get_rect(topleft = position)
                

            
        self.position = pygame.math.Vector2(position)
        
        

        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):

        if self.rect.colliderect(camera.rect):
            self.go = True
        elif not self.position_rect.colliderect(camera.respawn_rect):
            self.go = False
            self.direction = 'left'
            self.rect.x = self.position.x
            self.rect.y = self.position.y
            
        if self.go == True:
            #gravity
            if water_collision(self) == True:#in water
                self.velocity.y += 0.2
                if self.velocity.y >= 2:
                    self.velocity.y = 2
            else:#on land
                self.velocity.y += 1
                if self.velocity.y >= 6:
                    self.velocity.y = 6

            if self.direction == 'left':
                self.velocity.x = -self.speed
            else:
                self.velocity.x = self.speed

            self.rect.y += self.velocity.y#enemy collision detection y
            self.rect.y += 2
            if block_collision(self, 0, self.velocity.y) == 'standing':
                self.standing = True
            else:
                if self.standing == True:
                    if self.enemy_type == 'red koopa':
                        if self.direction == 'left':#checks if enemy has reached left end of platform
                            self.rect.x += 2
                            self.rect.y -= 1
                            self.direction = 'right'
                        else:#checks if enemy has reached right end of platform
                            self.rect.x -= 2
                            self.rect.y -= 1
                            self.direction = 'left'
                self.standing = False
            self.rect.y -= 2
                    
            self.rect.x += self.velocity.x#enemy collision detection x
            if not block_collision(self, self.velocity.x, 0) == None:#checks if enemy has reached a wall
                if self.velocity.x < 0:
                    self.direction = 'right'
                elif self.velocity.x > 0:
                    self.direction = 'left'

            if enemy_on_enemy_collision(self, self.velocity.x, self.velocity.y) == True:
                if self.velocity.x > 0:
                    self.direction = 'left'
                if self.velocity.x < 0:
                    self.direction = 'right'
            if self.rect.x <= 0:
                self.direction = 'right'
            

            #enemy animation
            if pygame.time.get_ticks() - shimmer_time >= shimmer_time_between_frames:
                if self.enemy_type == 'goomba':
                    if self.animation_frame < len(goomba_image_list[general.color_pallete]) - 1:
                        self.animation_frame += 1
                    else:
                        self.animation_frame = 0
                    if self.position.y < 640:#above ground
                        self.image = goomba_image_list[general.color_pallete][self.animation_frame]
                    else:#under ground
                        self.image = goomba_image_list[general.under_ground_color_pallete][self.animation_frame]
                elif self.enemy_type == 'green koopa':
                    if self.animation_frame < len(green_koopa_left_image_list[general.color_pallete]) - 1:
                        self.animation_frame += 1
                    else:
                        self.animation_frame = 0
                    if self.position.y < 640:#above ground
                        if self.direction == 'left':
                            self.image = green_koopa_left_image_list[general.color_pallete][self.animation_frame]
                        elif self.direction == 'right':
                            self.image = green_koopa_right_image_list[general.color_pallete][self.animation_frame]
                    else:#under ground
                        if self.direction == 'left':
                            self.image = green_koopa_left_image_list[general.under_ground_color_pallete][self.animation_frame]
                        elif self.direction == 'right':
                            self.image = green_koopa_right_image_list[general.under_ground_color_pallete][self.animation_frame]
                elif self.enemy_type == 'red koopa':
                    if self.animation_frame < len(red_koopa_left_image_list) - 1:
                        self.animation_frame += 1
                    else:
                        self.animation_frame = 0
                    if self.direction == 'left':
                        self.image = red_koopa_left_image_list[self.animation_frame]
                    elif self.direction == 'right':
                        self.image = red_koopa_right_image_list[self.animation_frame]
            
            if self.enemy_type == 'red koopa' or self.enemy_type == 'green koopa':
                self.hurt_box.x = self.rect.x - 2
                self.hurt_box.y = self.rect.y - 8
            elif self.enemy_type == 'goomba':
                self.hurt_box.x = self.rect.x - 3
                self.hurt_box.y = self.rect.y - 5


class Flattened_enemy(pygame.sprite.Sprite):

    def __init__(self, position, enemy_type):
        super(Flattened_enemy, self).__init__()

        flattened_enemy_group.add(self)
        all_sprite_group.add(self)

        self.width = 16
        self.height = 4

        if enemy_type == 'goomba':
            if position[1] < 640:#above ground
                self.image = flattened_goomba[general.color_pallete]
            else:#under ground
                self.image = flattened_goomba[general.under_ground_color_pallete]
        elif enemy_type == 'blooper':
            self.image = blooper_image[1]
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)


        self.time = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.time >= 500:
            self.kill()

class Flipped_enemy(pygame.sprite.Sprite):

    def __init__(self, position, image):
        super(Flipped_enemy, self).__init__()

        flattened_enemy_group.add(self)
        all_sprite_group.add(self)

        self.width = 16
        self.height = 16

        self.image = pygame.transform.flip(image, False, True)
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        self.velocity = pygame.math.Vector2(0, 0)
        self.velocity.y = -4

        if self.rect.x < player.rect.x:
            self.direction = 'left'
        else:
            self.direction = 'right'

    def update(self):
        
        #gravity
        self.velocity.y += 0.4
        if self.velocity.y > 4:
            self.velocity.y = 4

        self.rect.y += self.velocity.y
        if self.direction == 'left':
            self.rect.x -= 1
        elif self.direction == 'right':
            self.rect.x += 1

        if self.rect.top >= screen_Height:
            self.kill()

class Shell(pygame.sprite.Sprite):

    def __init__(self, position, colour, respawn_position, bounce):
        super(Shell, self).__init__()

        shell_group.add(self)
        all_sprite_group.add(self)

        self.width = 16
        self.height = 16

        self.speed = 5

        self.colour = colour

        self.go = True


        if colour == 'green':
            if position[1] < 640:#above ground
                self.image = green_koopa_shell_image[general.color_pallete]
            else:#under ground
                self.image = green_koopa_shell_image[general.under_ground_color_pallete]
        else:
            self.image = character_sheet.image_at((30, 216, 16, 14), colorkey = (107, 49, 156))

        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)

        self.respawn_rect = self.image.get_rect(topleft=respawn_position)
        self.respawn_position = pygame.math.Vector2(respawn_position)

        self.velocity = pygame.math.Vector2(0, 0)
        if bounce == True:
            self.velocity.y = -4

    def update(self):#gravity

        if self.rect.colliderect(camera.rect):
            self.go = True
        elif self.respawn_rect.colliderect(camera.respawn_rect):
            pass
        else:
            self.go = False
            self.rect.x = self.position.x
            self.rect.y = self.position.y
            if not self.respawn_rect.colliderect(camera.respawn_rect):
                if self.colour == 'green':
                    enemy = Enemy(position = self.respawn_position, enemy_type = 'green koopa')
                else:
                    enemy = Enemy(position = self.respawn_position, enemy_type = 'red koopa')
                self.kill()

        
        if self.go == True:
            if water_collision(self) == True:#in water
                self.velocity.y += 0.2
                if self.velocity.y >= 2:
                    self.velocity.y = 2
            else:#on land
                self.velocity.y = self.velocity.y + 0.75
                if self.velocity.y >= 6:
                    self.velocity.y = 6

            self.rect.y += self.velocity.y
            
            block_collision(self, 0, self.velocity.y)
            
            self.rect.x += self.velocity.x
            item_block_collision(self, -1)
            if not block_collision(self, self.velocity.x, 0) == None:#checks if enemy has reached a wall
                if self.velocity.x < 0:
                    self.velocity.x = self.speed
                elif self.velocity.x > 0:
                    self.velocity.x = -self.speed

            shell_collision(self)

        
class Pirhana_plant(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Pirhana_plant, self).__init__()

        enemy_group.add(self)
        all_sprite_group.add(self)

        self.enemy_type = 'pirhana plant'

        self.animation_frame = 0

        self.width = 12
        self.height = 10
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)
        self.position_rect = self.image.get_rect(topleft = position)
        self.rect.x += 2
        self.position_rect.x += 2

        self.hitbox_image = pygame.Surface((self.width, self.height))
        
        if position[1] < 640:#above ground
            if general.color_pallete == 0:
                self.image = pirhana_plant_image[0][0]
            else:
                self.image = pirhana_plant_image[1][0]
        else:#under ground
            if general.under_ground_color_pallete == 0:
                self.image = pirhana_plant_image[0][0]
            else:
                self.image = pirhana_plant_image[1][0]
        self.hurt_box = self.image.get_rect()


        self.position = pygame.math.Vector2(position)
        self.position.x += 2
    

        self.go = False
        self.direction = 'up'
        self.sub_frame = 0        

        self.pirhana_delay_time = pygame.time.get_ticks()

        for pipe in pipe_group:
            if self.rect.colliderect(pipe.rect):
                self.pipe = pipe

    def update(self):

        #resets if not on screen
        if self.rect.colliderect(camera.rect):
            if pygame.time.get_ticks() - self.pirhana_delay_time >= 1000:
                if self.direction == 'up':
                    if player.rect.x + player.width < self.rect.x - 12 or player.rect.x > self.rect.x + 24:
                        self.go = True
                elif self.direction == 'down':
                    self.go = True
        elif not self.position_rect.colliderect(camera.respawn_rect):
            self.go = False
            self.direction = 'up'
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]

                
        if pygame.time.get_ticks() - shimmer_time >= shimmer_time_between_frames:
            if self.animation_frame == 0:
                self.animation_frame = 1
            elif self.animation_frame == 1:
                self.animation_frame = 0

        if self.position[1] < 640:#above ground
            if general.color_pallete == 0:
                self.image = pirhana_plant_image[0][self.animation_frame]
            else:
                self.image = pirhana_plant_image[1][self.animation_frame]
        else:#under ground
            if general.under_ground_color_pallete == 0:
                self.image = pirhana_plant_image[0][self.animation_frame]
            else:
                self.image = pirhana_plant_image[1][self.animation_frame]
                
        if self.go == True:
            if self.direction == 'up':
                self.sub_frame += 1
                if self.sub_frame >= 2:
                    self.rect.y -= 1
                    self.sub_frame = 0
                if self.rect.y - 16<= self.pipe.rect.y - 24:
                    self.direction = 'down'
                    self.pirhana_delay_time = pygame.time.get_ticks()
                    self.go = False
            if self.direction == 'down':
                self.sub_frame += 1
                if self.sub_frame >= 2:
                    self.rect.y += 1
                    self.sub_frame = 0
                if self.rect.y - 16 >= self.pipe.rect.y:
                    self.direction = 'up'
                    self.pirhana_delay_time = pygame.time.get_ticks()
                    self.go = False
        self.hurt_box.x = self.rect.x - 2
        self.hurt_box.y = self.rect.y - 14

class Cheepcheep(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Cheepcheep, self).__init__()

        enemy_group.add(self)
        all_sprite_group.add(self)

        self.enemy_type = 'cheepcheep'

        self.animation_frame = 0
        self.animation_sub_frame = 0

        self.bounce = False
        self.bounce_delay = None
        
        #hit boxes
        self.width = 10
        self.height = 6
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)
        self.position_rect = self.image.get_rect(topleft = position)

        self.hit_box_image = pygame.Surface((self.width, self.height))
        
        self.speed = 1
        self.direction = 'left'
        self.standing = False

        self.go = False

        if position.y < 640:#above ground
            self.image = cheepcheep_image_left[0]

        else:#under ground
            self.image = cheepcheep_image_left[0]

        self.hurt_box_image = pygame.Surface((self.image.get_width(), self.image.get_height()))
        self.hurt_box = self.hurt_box_image.get_rect(topleft = position)
        self.position = pygame.math.Vector2(position)

        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):

        if self.rect.colliderect(camera.rect):
            self.go = True
        elif not self.position_rect.colliderect(camera.respawn_rect):
            self.go = False
            self.direction = 'left'
            self.rect.x = self.position.x
            self.rect.y = self.position.y

        if self.go == True:
            #while in water
            if water_collision(self) == True:
                if self.direction =='left':
                    self.velocity.x -= 0.2
                    if self.velocity.x <= -1:
                        self.velocity.x = -1
                else:
                    self.velocity.x += 0.2
                    if self.velocity.x >= 1:
                        self.velocity.x = 1
            #on land
            else:
                self.velocity.y += 1
                if self.velocity.y >= 6:
                    self.velocity.y = 6
                if self.rect.top > screen_Height and self.rect.top < 600:
                    self.kill()
                elif self.rect.top > screen_Height + 640 and self.rect.top < 1240:
                    self.kill()
                if self.velocity.x < 0:
                    self.velocity.x += 0.1
                elif self.velocity.x > 0:
                    self.velocity.x -= 0.1

            self.velocity.x = round(self.velocity.x, 2)
            self.velocity.y = round(self.velocity.y, 2)
            self.rect.y += round(self.velocity.y)#enemy collision detection y
            if block_collision(self, 0, self.velocity.y) == 'standing':
                if self.bounce_delay == None:
                    self.bounce_delay = 0
                if self.bounce_delay != None:
                    self.bounce_delay += 1
                if self.bounce_delay >=64:
                    self.velocity.y -= 6
                    self.bounce = True
                    self.bounce_delay = 0
                elif self.bounce == True:
                    self.velocity.y -= 6
                    self.bounce = False
                    self.bounce_delay = None

            self.rect.x += round(self.velocity.x)#enemy collision detection x
            self.block_direction = block_collision(self, self.velocity.x, 0)
            if self.block_direction == 'right':
                self.direction = 'left'
            elif self.block_direction == 'left':
                self.direction ='right'
            self.hurt_box.x = self.rect.x - 3
            self.hurt_box.y = self.rect.y - 8


            #animation
            self.animation_sub_frame += 1
            if self.animation_sub_frame >= 6:
                self.animation_sub_frame = 0
                self.animation_frame +=1
                if self.animation_frame >= 2:
                    self.animation_frame = 0
            if self.direction == 'left':
                self.image = cheepcheep_image_left[self.animation_frame]
            else:
                self.image = cheepcheep_image_right[self.animation_frame]

class Blooper(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Blooper, self).__init__()

        enemy_group.add(self)
        all_sprite_group.add(self)

        self.enemy_type = 'blooper'

        self.animation_frame = 0

        self.bounce_delay = 0
        
        #hit boxes
        self.width = 10
        self.height = 6
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)
        self.position_rect = self.image.get_rect(topleft = position)

        self.hit_box_image = pygame.Surface((self.width, self.height))
        
        self.speed = 1
        self.direction = 'left'
        self.standing = False

        self.go = False

        if position.y < 640:#above ground
            self.image = blooper_image[0]

        else:#under ground
            self.image = blooper_image[0]

        self.hurt_box_image = pygame.Surface((self.image.get_width(), self.image.get_height()))
        self.hurt_box = self.hurt_box_image.get_rect(topleft = position)
        self.position = pygame.math.Vector2(position)

        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):
        if self.rect.colliderect(camera.rect):
            self.go = True
        elif not self.position_rect.colliderect(camera.respawn_rect):
            self.go = False
            self.direction = 'left'
            self.rect.x = self.position.x
            self.rect.y = self.position.y
        
        
        if self.go == True:
            #gravity
            if water_collision(self) == True:
                self.bounce_delay += 1
                self.velocity.y += 0.2
                if self.velocity.y >= 1:
                    self.velocity.y = 1
                if player.rect.bottom < self.rect.y:
                    if self.velocity.y >= 0:
                        if self.bounce_delay >= 48:
                            self.bounce_delay = 0
                            self.velocity.y = -4
                            if player.rect.right < self.rect.left:
                                self.velocity.x = -2
                            elif player.rect.left > self.rect.right:
                                self.velocity.x = 2
                            else:
                                self.velocity.x = 0
            else:
                self.velocity.y += 1
                if self.velocity.y >= 6:
                    self.velocity.y = 6
            
            if self.velocity.y >= 0:
                self.velocity.x = 0


            self.velocity.x = round(self.velocity.x, 2)
            self.velocity.y = round(self.velocity.y, 2)
            self.rect.y += round(self.velocity.y)#enemy collision detection y
            block_collision(self, 0, self.velocity.y)

            self.rect.x += round(self.velocity.x)#enemy collision detection x
            block_collision(self, self.velocity.x, 0)

            #animation
            if self.velocity.y > 0 and player.rect.bottom < self.rect.top:
                self.image = blooper_image[1]
            else:
                self.image = blooper_image[0]
            
            self.hurt_box_image = pygame.Surface((self.image.get_width(), self.image.get_height()))
            self.hurt_box = self.hurt_box_image.get_rect()
            self.hurt_box.x = self.rect.x - 3
            self.hurt_box.y = self.rect.y - 8


class Flag_pole(pygame.sprite.Sprite):
    
    def __init__(self, position):
        super(Flag_pole, self).__init__()

        goal_post_group.add(self)
        all_sprite_group.add(self)

        self.width = 2
        self.height = 160
        self.image = make_tiled_image(flag_pole_image, self.width, self.height )
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2((position[0] - 6, position[1]))

        self.goal_flag = Goal_flag(position = (self.position[0] - 8, self.position[1] + 8))
        self.goal_base = Goal_base(position = self.position)
    def update(self):
        self.player_flag = Player_flag(position = self.goal_base.position)
        
class Goal_flag(pygame.sprite.Sprite):
    
    def __init__(self, position):
        super(Goal_flag, self).__init__()

        goal_flag_group.add(self)
        all_sprite_group.add(self)

        self.width = 16
        self.height = 16

        self.image = goal_flag_image
        self.rect = self.image.get_rect(topleft=position)
        self.position = pygame.math.Vector2(position)
        
class Player_flag(pygame.sprite.Sprite):
    
    def __init__(self, position):
        super(Player_flag, self).__init__()

        player_flag_group.add(self)
        all_sprite_group.add(self)

        self.width = 16
        self.height = 16

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pygame.Color('black'))
        self.rect = self.image.get_rect(bottomleft=position)
        self.position = pygame.math.Vector2(position)

class Goal_base(pygame.sprite.Sprite):
    
    def __init__(self, position):
        super(Goal_base, self).__init__()

        goal_base_group.add(self)
        all_block_group.add(self)
        all_sprite_group.add(self)

        self.item_block = False
        self.thin = False

        self.width = 16
        self.height = 16
        self.bounce_offset = 0

        self.image = goal_base_image
        self.rect = self.image.get_rect(topleft=position)
        self.rect.y += 144
        self.position = pygame.math.Vector2(position)
        self.position.y += 176
        
def item_block_collision(Self, dy):
    keys = pygame.key.get_pressed()
    for block in all_block_group:
        if Self.rect.colliderect(block.rect):
            if dy < 0:#jump collision
                if block.item_block == True:
                    if block.item != None:
                        block.rect.y -= 3
                        for enemy in enemy_group:
                            if block.rect.colliderect(enemy):
                                if enemy.enemy_type == 'red koopa':
                                    flipped_enemy = Flipped_enemy(position = (enemy.rect.x, enemy.rect.y), image = red_koopa_shell_image)
                                elif enemy.enemy_type =='green koopa':
                                    flipped_enemy = Flipped_enemy(position = (enemy.rect.x, enemy.rect.y), image = green_koopa_shell_image)
                                else:
                                    flipped_enemy = Flipped_enemy(position = (enemy.rect.x, enemy.rect.y), image = enemy.image)
                                enemy.kill()
                        for mushroom in super_mushroom_group:
                            if block.rect.colliderect(mushroom):
                                mushroom.velocity.y = -8
                                if mushroom.direction == 'right':
                                    mushroom.direction = 'left'
                                else:
                                    mushroom.direction = 'right'
                        block.rect.y += 3
                        if block.quantity > 1:
                            if block.time == None:
                                block.time = pygame.time.get_ticks()
                        block.quantity -= 1
                        if block.item == 'fire flower':
                            if player.tall == False:
                                super_mushroom = Super_mushroom(position=(block.rect.bottomleft), spawn_counter = 0, direction = player.direction)
                            else:
                                fire_flower = Fire_flower(position=(block.rect.bottomleft), spawn_counter = 0)
                        elif block.item == 'power star':
                            power_star = Power_star(position = (block.rect.bottomleft))
                        elif block.item == 'coin':
                            coin = Show_coin(position=(block.rect.bottomleft))
                            player.coins += 1
                            player.coin_text = coin_text_font.render(f'{player.coins}', True, (0, 0, 0))
                        if block.quantity == 0:
                            block.item = None
                            block.image = empty_item_block_image[general.color_pallete]

def breakable_block_collision(Self, dy):
    keys = pygame.key.get_pressed()
    for block in breakable_block_group:
        if Self.rect.colliderect(block.rect):
            if dy < 0:#jump collision
                if block.breakable == True:
                    block.rect.y -= 3
                    for enemy in enemy_group:
                        if block.rect.colliderect(enemy):
                            if enemy.enemy_type == 'red koopa':
                                flipped_enemy = Flipped_enemy(position = (enemy.rect.x, enemy.rect.y), image = red_koopa_shell_image)
                            elif enemy.enemy_type =='green koopa':
                                flipped_enemy = Flipped_enemy(position = (enemy.rect.x, enemy.rect.y), image = green_koopa_shell_image)
                            else:
                                flipped_enemy = Flipped_enemy(position = (enemy.rect.x, enemy.rect.y), image = enemy.image)
                            enemy.kill()
                    for mushroom in super_mushroom_group:
                        if block.rect.colliderect(mushroom):
                            mushroom.velocity.y = -3
                            if mushroom.direction == 'right':
                                mushroom.direction = 'left'
                            else:
                                mushroom.direction = 'right'
                    block.rect.y += 3
                    if block.item != None:
                        block_bounce_group.add(block)
                if player.tall == True:
                    if block.breakable == True:
                        if block.item_block == False:
                            block_removal_group.add(block)#assigns blocks for deletion
                            block_piece = Block_piece(block.position, 'top left')
                            block_piece = Block_piece(block.position, 'top right')
                            block_piece = Block_piece(block.position, 'bottom left')
                            block_piece = Block_piece(block.position, 'bottom right')
                else:
                    block_bounce_group.add(block)
    
def block_collision(Self, dx, dy):
    keys = pygame.key.get_pressed()
    for block in all_block_group:
        if Self.rect.colliderect(block.rect):
            if dy > 0:#fall collision
                if Self.rect.y + Self.height < block.rect.y + block.height:
                    Self.rect.bottom = block.rect.top
                    Self.velocity.y = 0
                    Self.standing = True
                    return 'standing'

            if dy < 0:#jump collision
                if block.thin == False:
                    Self.rect.top = block.rect.bottom
                    Self.velocity.y = 0
                    return 'jump'
                
            if dx > 0:#walk right collision
                if block.thin == False:
                    Self.rect.right = block.rect.left
                    return 'right'

            if dx < 0:#walk left collision
                if block.thin == False:
                    Self.rect.left = block.rect.right
                    return 'left'

def enemy_collision(Self, dx, dy):#player-enemy collision
    keys = pygame.key.get_pressed()
    for enemy in enemy_group:
        if Self.rect.colliderect(enemy.hurt_box):
            if Self.star_power == True:
                flipped_enemy = Flipped_enemy(position = (enemy.rect.x, enemy.rect.y), image = enemy.image)
                enemy.kill()
            else:
                if dy > 0:#fall collision
                    if enemy.enemy_type == 'goomba':
                        enemy.kill()
                        if water_collision(Self) == True:
                            Self.velocity.y = -4
                        else:
                            Self.velocity.y = -7
                        flattened_enemy = Flattened_enemy(position = (enemy.rect.x, enemy.rect.y + 3), enemy_type = enemy.enemy_type)
                        Self.rect.bottom = enemy.rect.top
                    if enemy.enemy_type == 'green koopa':
                        shell = Shell(position = (enemy.rect.x, enemy.rect.y), colour = 'green', respawn_position = enemy.position, bounce = False)
                        enemy.kill()
                        if water_collision(Self) == True:
                            Self.velocity.y = -4
                        else:
                            Self.velocity.y = -7
                        Self.rect.bottom = enemy.rect.top
                    if enemy.enemy_type == 'red koopa':
                        shell = Shell(position = (enemy.rect.x, enemy.rect.y), colour = 'red', respawn_position = enemy.position, bounce = False)
                        enemy.kill()
                        if water_collision(Self) == True:
                            Self.velocity.y = -4
                        else:
                            Self.velocity.y = -7
                        Self.rect.bottom = enemy.rect.top
                    if enemy.enemy_type =='blooper':
                        enemy.kill()
                        if water_collision(Self) == True:
                            Self.velocity.y = -4
                        else:
                            Self.velocity.y = -7
                        flattened_enemy = Flattened_enemy(position = (enemy.rect.x, enemy.rect.y + 3), enemy_type = enemy.enemy_type)
                        Self.rect.bottom = enemy.rect.top
                    return 'standing'
                else:
                    if enemy.enemy_type =='blooper':
                        if Self.rect.y < enemy.rect.y:
                            if enemy.velocity.y < Self.velocity.y:
                                enemy.kill()
                                if water_collision(Self) == True:
                                    Self.velocity.y = -4
                                else:
                                    Self.velocity.y = -7
                                flattened_enemy = Flattened_enemy(position = (enemy.rect.x, enemy.rect.y + 3), enemy_type = enemy.enemy_type)
                                Self.rect.bottom = enemy.rect.top
        if Self.rect.colliderect(enemy.rect):
            if Self.star_power == False:
                if not dy > 0:#hurt collision
                    if Self.invincibility == False:
                        if player.fire_form == True:
                            player.fire_form = False
                            player.invincibility = True
                            player.time = pygame.time.get_ticks()#starts invincibility frames
                            
                        elif Self.tall == True:
                            Self.tall = False
                            Self.height = 12
                            player.invincibility = True
                            player.time = pygame.time.get_ticks()#starts invincibility frames
                        else:
                            dead()

def player_on_shell_collision(Self, dy):
    for shell in shell_group:
        if Self.rect.colliderect(shell.rect):
            if Self.star_power == True:
                flipped_enemy = Flipped_enemy(position = (shell.rect.x, shell.rect.y), image = shell.image)
                shell.kill()
                break
            if shell.velocity.x == 0:#if shell is standing still
                if Self.rect.left < shell.rect.left:
                    shell.rect.left = player.rect.right
                    shell.velocity.x = shell.speed
                else:
                    shell.rect.right = player.rect.left
                    shell.velocity.x = -shell.speed
                if dy > 0:#fall collision
                    if player.rect.bottom >= shell.rect.top:
                        Self.rect.bottom = shell.rect.top
                        Self.velocity.y = -7
            else:#if shell is moving
                if dy > 0:#fall collision
                    if player.rect.bottom <= shell.rect.bottom:
                        Self.rect.bottom = shell.rect.top
                        Self.velocity.y = -7
                        shell.velocity.x = 0
                else:
                    if Self.invincibility == False:
                        if Self.star_power == False:
                            if player.fire_form == True:
                                player.fire_form = False
                                Self.image = pygame.Surface((Self.width, Self.height))
                                Self.image.fill(pygame.Color('green'))
                                Self.rect = Self.image.get_rect(topleft=Self.rect.topleft)
                                player.invincibility = True
                                player.time = pygame.time.get_ticks()#starts invincibility frames
                            elif Self.tall == True:
                                Self.tall = False
                                Self.height = 12
                                Self.image = pygame.Surface((Self.width, Self.height))
                                Self.image.fill(pygame.Color('green'))
                                Self.rect = Self.image.get_rect(bottomleft=Self.rect.bottomleft)
                                player.invincibility = True
                                player.time = pygame.time.get_ticks()#starts invincibility frames
                            else:
                                dead()
                        

def enemy_on_enemy_collision(Self, dx, dy):#2 enemies collide
    for enemy in enemy_group:
        if Self.rect.colliderect(enemy.rect):
            
            if dx > 0:#walk right collision
                if not enemy == Self:
                    Self.rect.right = enemy.rect.left
                    return True

            if dx < 0:#walk left collision
                if not enemy == Self:
                    Self.rect.left = enemy.rect.right
                    return True

def fire_ball_collision(Self):
    for enemy in enemy_group:
        if Self.rect.colliderect(enemy.hurt_box):
            #if enemy.enemy_type == 'goomba':
            flipped_enemy = Flipped_enemy(position = (enemy.rect.x, enemy.rect.y), image = enemy.image)
            enemy.kill()
            return True
    for shell in shell_group:
        if Self.rect.colliderect(shell.rect):
            Self.kill()

def shell_collision(Self):
    if Self.velocity.x != 0:#only while shell is moving
        for enemy in enemy_group:
            if Self.rect.colliderect(enemy.rect):
                if enemy != Self:
                    if enemy.enemy_type == 'goomba':
                        flipped_enemy = Flipped_enemy(position = (enemy.rect.x, enemy.rect.y), image = enemy.image)
                    elif enemy.enemy_type == 'green koopa':
                        if camera.position.y < screen_Height:
                            flipped_enemy = Flipped_enemy(position = (enemy.rect.x, enemy.rect.y), image = green_koopa_shell_image[general.color_pallete])
                        else:
                            flipped_enemy = Flipped_enemy(position = (enemy.rect.x, enemy.rect.y), image = green_koopa_shell_image[general.under_ground_color_pallete])
                    elif enemy.enemy_type == 'red koopa':
                        flipped_enemy = Flipped_enemy(position = (enemy.rect.x, enemy.rect.y), image = red_koopa_shell_image)
                    enemy.kill()
        for shell in shell_group:
            if Self.rect.colliderect(shell.rect):#if shell hits another shell
                if shell != Self:
                    if shell.velocity.x < 0:
                        if Self.velocity.x == 0:#if the other shell isn't moving
                            Self.velocity.x = shell.velocity.x
                        shell.velocity.x = shell.speed#if it is moving
                    elif shell.velocity.x > 0:
                        if Self.velocity.x == 0:
                            Self.velocity.x = shell.velocity.x
                        shell.velocity.x = -shell.speed
                    if Self.velocity.x < 0:
                        if shell.velocity.x == 0:
                            shell.velocity.x = Self.velocity.x
                        Self.velocity.x = Self.speed
                    elif Self.velocity.x > 0:
                        if shell.velocity.x == 0:
                            shell.velocity.x = Self.velocity.x
                        Self.velocity.x = -Self.speed
                

def power_up_collision(Self):
    for mushroom in super_mushroom_group:
        if Self.rect.colliderect(mushroom.rect):
            Self.tall = True
            Self.height = 24
            Self.width = 12
            
            mushroom.kill()
            return
    for flower in fire_flower_group:
        if Self.rect.colliderect(flower.rect):
            Self.fire = True
            Self.tall = True
            Self.height = 24
            Self.width = 12
            Self.fire_form = True
            Self.star_power_frame = 2
            
            flower.kill()
            return
    for star in power_star_group:
        if Self.rect.colliderect(star.rect):
            Self.star_power = True
            Self.star_power_time = pygame.time.get_ticks()

            star.kill()
            return
        
def coin_collision(Self):
    for coin in coin_group:
        if Self.rect.colliderect(coin.rect):

            player.coins += 1
            player.coin_text = coin_text_font.render(f'{player.coins}', True, (0, 0, 0))
            
            coin.kill()
            return

def goal_post_collision():
    for goal in goal_post_group:
        if player.rect.colliderect(goal.rect):
            if general.level_end_animation == False:
                goal.update()
            if player.rect.colliderect(goal.goal_base.rect):#check if player has reached bottom of goal_pole
                general.level_end_animation = False
            else:
                general.level_end_animation = True
                
            if general.level_end_animation == True:#while animation is in progress
                player.rect.y += 2
                goal.goal_flag.rect.y += 2
                goal.player_flag.rect.y -= 2
                if goal.goal_flag.rect.colliderect(goal.goal_base.rect):
                    goal.goal_flag.rect.bottom = goal.goal_base.rect.top
                if goal.player_flag.rect.top < goal.rect.top:
                    goal.player_flag.rect.top = goal.rect.top
            if general.level_end_animation == False:#when animation is over
                player.rect.x = general.player_start_position_x
                player.rect.y = general.player_start_position_y
                player.velocity.x = 0
                player.velocity.y = 0
                camera.position.y = 0
                general.level += 1
                general.color_pallete = color_palletes[general.level - 1]
                unload_level()
                load_level()


def warp_animation(pipe):
    if general.entering_pipe == True:#enter warp pipe
        player.velocity.x = 0
        player.velocity.y = 0
        if pipe.direction == 'up':
            player.rect.y += 1
            player.image_rect.y += 1
            if player.image_rect.top >= pipe.rect.top:#when the player has completely entered the pipe
                general.entering_pipe = False
                player.crouch = False
                update_hitbox()
                if pipe.warp_direction == 'up':
                    player.rect.topleft = pipe.warp_destination
                    player.rect.x += 8
                elif pipe.warp_direction == 'down':
                    player.rect.bottomleft = pipe.warp_destination
                    player.rect.x += 8
                    if player.tall == False:
                        player.image_rect = player.image.get_rect(topleft=(player.rect.left - player.pixel_offset_x, player.rect.top + player.pixel_offset_y - 3))
                    else:
                        player.image_rect = player.image.get_rect(topleft=(player.rect.left - player.pixel_offset_x, player.rect.top + player.pixel_offset_y - 7))
                if pipe.warp_destination[1] <= 640:#changes the camera's vertical position
                    camera.position.y = 0
                elif pipe.warp_destination[1] >= 640:
                    camera.position.y = 640
        elif pipe.direction == 'down':
            player.rect.y -= 1
            player.image_rect.y -= 1
            if player.image_rect.bottom <= pipe.rect.bottom:#when the player has completely entered the pipe
                general.entering_pipe = False
                player.crouch = False
                update_hitbox()
                if pipe.warp_direction == 'up':
                    player.rect.topleft = pipe.warp_destination
                    player.rect.x += 8
                elif pipe.warp_direction == 'down':
                    player.rect.bottomleft = pipe.warp_destination
                    player.rect.x += 8
                    if player.tall == False:
                        player.image_rect = player.image.get_rect(topleft=(player.rect.left - player.pixel_offset_x, player.rect.top + player.pixel_offset_y - 3))
                    else:
                        player.image_rect = player.image.get_rect(topleft=(player.rect.left - player.pixel_offset_x, player.rect.top + player.pixel_offset_y - 7))
                if pipe.warp_destination[1] <= 640:#changes the camera's vertical position
                    camera.position.y = 0
                elif pipe.warp_destination[1] >= 640:
                    camera.position.y = 640
                    
    if general.entering_pipe == False:#exit warp pipe
        if pipe.warp_direction == 'up':
            player.rect.y -= 1
            if player.rect.bottom <= pipe.warp_destination[1]:
                general.enter_pipe = None
        elif pipe.warp_direction == 'down':
            player.rect.y += 1
            player.image_rect.y += 1
            if player.image_rect.top >= pipe.warp_destination[1]:
                general.enter_pipe = None

def water_collision(Self):
    for sprite in water_group:
        if Self.rect.colliderect(sprite.rect):
            return True

def update_hitbox():
    if player.tall == True:
        player.height = 24
        player.width = 12
        if player.crouch == True:
            player.height = 12
    else:
        player.height = 12
        player.width = 10
    player.hitbox_image = pygame.Surface((player.width, player.height))
    player.rect = player.hitbox_image.get_rect(bottomleft=player.rect.bottomleft)
    player.hitbox_image.fill(pygame.Color('black'))
    if player.tall == False:
        player.image_rect = player.image.get_rect(topleft=(player.rect.left - player.pixel_offset_x, player.rect.top + player.pixel_offset_y - 3))
    elif player.tall == True:
        player.image_rect = player.image.get_rect(topleft=(player.rect.left - player.pixel_offset_x, player.rect.top + player.pixel_offset_y - 7))
        if player.crouch == True:
            player.image_rect = player.image.get_rect(topleft=(player.rect.left - player.pixel_offset_x, player.rect.top + player.pixel_offset_y - 9))
    player.image_rect_image = pygame.Surface(player.image.get_size())
       

def shimmer():

        if self.quantity > 0:#if not empty
            if pygame.time.get_ticks() - shimmer_time >= shimmer_time_between_frames:
                if self.shimmer_frame < len(item_block_shimmer_list[general.color_pallete]) + 4:
                    self.shimmer_frame += 1
                else:
                    self.shimmer_frame = 0
                if self.shimmer_frame <= 5:
                    if self.position.y < 640:#above ground
                        self.image = item_block_shimmer_list[general.color_pallete][0]
                    else:#under ground
                        self.image = item_block_shimmer_list[general.under_ground_color_pallete][0]
                else:
                    if self.position.y < 640:#above ground
                        self.image = item_block_shimmer_list[general.color_pallete][self.shimmer_frame -5]
                    else:#under ground
                        self.image = item_block_shimmer_list[general.under_ground_color_pallete][self.shimmer_frame -5]

def load_level():
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
        pipe_file = open(f'sprites/level {general.level}//pipe file.pickle', 'rb')
    except FileNotFoundError:
        pipe_file = open(f'sprites/level {general.level}/pipe file.pickle', 'x')
        pipe_file = open(f'sprites/level {general.level}/pipe file.pickle', 'rb')
    try:
        pirhana_plant_file = open(f'sprites/level {general.level}//pirhana plant file.pickle', 'rb')
    except FileNotFoundError:
        pirhana_plant_file = open(f'sprites/level {general.level}/pirhana plant file.pickle', 'x')
        pirhana_plant_file = open(f'sprites/level {general.level}/pirhana plant file.pickle', 'rb')
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
            coin_data = pickle.load(coin_file)
            coin = Coin(position = coin_data[0])
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
            goal_post_data = pickle.load(goal_post_file)
            goal_post = Flag_pole(position = goal_post_data[0])
    except EOFError:
        pass
    try:
        while True:
            pipe_data = pickle.load(pipe_file)
            pipe = Pipe(position = pipe_data[0], height = pipe_data[1], warp_destination = pipe_data[2],direction = pipe_data[3], warp_direction = pipe_data[4])
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
            water_data = pickle.load(water_file)
            water = Water(position = water_data[0], width = water_data[1], height = water_data[2])
    except EOFError:
        pass
    try:
        while True:
            player_position_data = pickle.load(player_position_file)
            player.position = (player_position_data[0])
            player.rect.x = player.position[0]
            player.rect.y = player.position[1]
    except EOFError:
        pass

    
def unload_level():
    for sprite in all_sprite_group:
        sprite.kill()

def crouch_unstuck_left():
        for block in all_block_group:
            if block.rect.collidepoint(player.rect.x, player.rect.y):
                return True

def crouch_unstuck_right():
    for block in all_block_group:        
        if block.rect.collidepoint(player.rect.x + player.width, player.rect.y):
            return True

def dead():
    player.tall = False
    player.fire_form = False
    player.height = 12
    player.image = pygame.Surface((player.width, player.height))
    player.image.fill(pygame.Color('green'))
    player.rect = player.image.get_rect(bottomleft=player.rect.bottomleft)
    player.velocity.x = 0
    player.velocity.y = 0
    camera.position.y = 0
    unload_level()
    load_level()
    print('død')

#create groups 
all_sprite_group = pygame.sprite.Group()

item_block_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
all_block_group = pygame.sprite.Group()
breakable_block_group = pygame.sprite.Group()
block_piece_group = pygame.sprite.Group()
block_bounce_group = pygame.sprite.Group()
thin_block_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
pirhana_plant_group = pygame.sprite.Group()
flattened_enemy_group = pygame.sprite.Group()
flipped_enemy_group = pygame.sprite.Group()
super_mushroom_group = pygame.sprite.Group()
fire_flower_group = pygame.sprite.Group()
power_star_group = pygame.sprite.Group()
power_up_group = pygame.sprite.Group()
fire_ball_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
show_coin_group = pygame.sprite.Group()
goal_post_group = pygame.sprite.Group()
goal_flag_group = pygame.sprite.Group()
player_flag_group = pygame.sprite.Group()
goal_base_group = pygame.sprite.Group()
shell_group = pygame.sprite.Group()

block_removal_group = pygame.sprite.Group()
block_bounce_remove_group = pygame.sprite.Group()


coin_text_font = pygame.font.SysFont('freesansbold.ttf', 30)

player = Player(position=(screen_Width / 2, 220))

load_level()

general = General()
camera = Camera (position=(player.position.x  - screen_Width / 2, 0))



running = True
while running:
    clock.tick(FPS)
    Mouse_x, Mouse_y = pygame.mouse.get_pos()
    for e in pygame.event.get():#button inputs
        if e == pygame.QUIT:
            Running = False
        if e.type == pygame.KEYDOWN and e.type == pygame.K_ESCAPE:
            running = False
            
    if general.level_end_animation == False:
        if general.enter_pipe == None:
            player.update()
        else:
            warp_animation(general.enter_pipe)
    goal_post_collision()
    
    if player.invincibility == True:
        if player.invincibility_jitter == False:
            player.invincibility_jitter = True
        elif player.invincibility_jitter == True:
            player.invincibility_jitter = False
    if player.invincibility == False:
        player.invincibility_jitter = False
        
    enemy_group.update()
    pirhana_plant_group.update()
    shell_group.update()
    flattened_enemy_group.update()
    flipped_enemy_group.update()
    super_mushroom_group.update()
    fire_flower_group.update()
    power_star_group.update()
    
    fire_ball_group.update()
    explosion_group.update()
    
    show_coin_group.update()
    block_piece_group.update()
    
    block_bounce_group.update()
    for block in block_bounce_remove_group:#remove from bounce list when animation is over
        block_bounce_group.remove(block)
    block_bounce_remove_group.empty()
    
    item_block_group.update()
    coin_group.update()
    if pygame.time.get_ticks() - shimmer_time >= shimmer_time_between_frames:
        shimmer_time =  pygame.time.get_ticks()
        if shimmer_frame < len(item_block_shimmer_list[general.color_pallete]) + 4:
            shimmer_frame += 1
        else:
            shimmer_frame = 0
                    
    
    camera.update()
        

    #render
    if player.rect.y < 640:#above ground
        screen.fill(BACKGROUND_COLOR[general.color_pallete])
    else:#under ground
        screen.fill(BACKGROUND_COLOR[general.under_ground_color_pallete])
    for sprite in water_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
        screen.blit(sprite.wave_image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y - 8))
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
    for sprite in all_block_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y + sprite.bounce_offset))
    for sprite in thin_block_group:
        screen.blit(sprite.fence_image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y - 8))
    for sprite in enemy_group:
        if sprite.enemy_type == 'red koopa' or sprite.enemy_type == 'green koopa':
            screen.blit(sprite.image, (sprite.rect.x - camera.position.x - 2, sprite.rect.y - camera.position.y - 8))
        elif sprite.enemy_type == 'goomba':
            screen.blit(sprite.image, (sprite.rect.x - camera.position.x - 3, sprite.rect.y - camera.position.y - 5))
        elif sprite.enemy_type == 'pirhana plant':
            screen.blit(sprite.image, (sprite.rect.x - camera.position.x - 2, sprite.rect.y - camera.position.y - 14))
        elif sprite.enemy_type == 'cheepcheep':
            screen.blit(sprite.image, (sprite.rect.x - camera.position.x - 3, sprite.rect.y - camera.position.y - 8))
        elif sprite.enemy_type == 'blooper':
            screen.blit(sprite.image, (sprite.rect.x - camera.position.x - 3, sprite.rect.y - camera.position.y - 8))
        else:
            screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in shell_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in flattened_enemy_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in fire_ball_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in goal_post_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
        screen.blit(flag_pole_top_image, (sprite.rect.x - camera.position.x - 3, sprite.rect.y - camera.position.y -8))
    for sprite in goal_flag_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in player_flag_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    for sprite in goal_base_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
    if player.invincibility_jitter == False:
        if player.tall == False:
            screen.blit(player.image, (player.rect.x - camera.position.x - player.pixel_offset_x, player.rect.y - camera.position.y - 3 + player.pixel_offset_y))
        elif player.tall == True:
            if player.crouch == False:
                screen.blit(player.image, (player.rect.x - camera.position.x - player.pixel_offset_x, player.rect.y - camera.position.y - 7 + player.pixel_offset_y))
            elif player.crouch == True:
                screen.blit(player.image, (player.rect.x - camera.position.x - 2, player.rect.y - camera.position.y - 9))
    for sprite in pipe_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
        if sprite.direction == 'up':
            if sprite.position.y < 640:#above ground
                screen.blit(pipe_top_image[general.color_pallete], (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
            else:#under ground
                screen.blit(pipe_top_image[general.under_ground_color_pallete], (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))
        else:
            if sprite.position.y < 640:#above ground
                screen.blit(pipe_bottom_image[general.color_pallete], (sprite.rect.x - camera.position.x, sprite.rect.y + sprite.height - 16 - camera.position.y))
            else:#under ground
                screen.blit(pipe_bottom_image[general.under_ground_color_pallete], (sprite.rect.x - camera.position.x, sprite.rect.y + sprite.height - 16 - camera.position.y))
    for sprite in explosion_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x , sprite.rect.y - camera.position.y))
    for sprite in block_piece_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x , sprite.rect.y - camera.position.y))

    for x in range(len(fence_image)):
        screen.blit(fence_image[x], (0, x * 32))

    for sprite in power_up_group:
        screen.blit(sprite.image, (sprite.rect.x - camera.position.x, sprite.rect.y - camera.position.y))

    

    screen.blit(player.coin_text, (8,0))


    pygame.display.update()
