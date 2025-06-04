import pygame
def make_tiled_image( image, width, height, colorkey = None):
    x_cursor = 0
    y_cursor = 0

    tiled_image = pygame.Surface( ( width, height ) )#.convert()
    while ( y_cursor < height ):
        while ( x_cursor < width ):
            tiled_image.blit( image, ( x_cursor, y_cursor ) )
            x_cursor += image.get_width()
        y_cursor += image.get_height()
        x_cursor = 0
    if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            tiled_image.set_colorkey(colorkey, pygame.RLEACCEL)
    return tiled_image
