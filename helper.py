import pygame
from pytmx.util_pygame import load_pygame
from Const import *
# from PIL import Image

# 在窗口中显示图片
pygame.init()
screen = pygame.display.set_mode((256, 256))
tmx_data = load_pygame(TMX_FILE)
layer_num = 0
tileID_lst = []
for layer in tmx_data.visible_layers:
    for y in range(tmx_data.height):
        for x in range(tmx_data.width):

                # Getting pygame surface
            image = tmx_data.get_tile_image(x, y, layer_num)

                    # It's none if there are no tile in that place
            if image is not None:
                tileID = tmx_data.get_tile_gid(x, y, layer_num)
                if tileID not in tileID_lst:
                    tileID_lst.append(tileID)
                screen.blit(image, (0, 0))
                pygame.display.flip()
                
                img_name = 'temp_pic_full_tileID_x_y_layernum/img' + '_' + str(tileID)  + '_' + str(x)+ '_' + str(y)+ '_' + str(layer_num) + '.png'
                pygame.image.save(image,img_name)
    layer_num += 1