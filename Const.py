WINDOW_W = 800
WINDOW_H = 448
FPS = 100

# Player physics
GRAVITY = 0.08

# 左右键加速度
SPEED_INCREASE_RATE = 0.038

SPEED_INCREASE_RATE_FAST = 5

# 左右键减速度：如果没有按方向键，会减速
SPEED_DECREASE_RATE = 0.018
# SPEED_DECREASE_RATE = 0.038

# 正常跳跃系数
JUMP_POWER = 4.8

FALL_MULTIPLIER = 2.0

# 不长按空格，掉落速度 = gravity * low_jump_multiplier
LOW_JUMP_MULTIPLIER = 3.0

MAX_MOVE_SPEED = 2.0
MAX_FASTMOVE_SPEED = 3.0
MAX_FALL_SPEED = 5.5


# icons tiled id

# 黄色问号 - 出coin
QUESTION_ICON_ID = 246

# 砖块
BRICK_ID = 247

# 粉色问号 - 出蘑菇\戒指
QUESTION_SPECIAL_ID = 248

import os
file_path = os.path.abspath(__file__)
file_path = os.path.dirname(file_path)
file_path = os.path.join(file_path, 'materials/')


TMX_FILE = os.path.join(file_path, 'worlds/W11_ver113.tmx')

# FLAG POSITION -> 32*方格id

FLAG_X = 220

FLAG_X_POS = 7040
# FLAG_X_POS = 832
FLAG_Y_POS = 48

# HOME POSITION -> 方格id
HOME_X = 246
HOME_Y = 12

# 红毯坐标*32 =  5250
RED_CARPET = 5250


# 红毯平坦坐标 （186，5）
RED_CARPET_FLAT_X = 186



RED_CARPET_FLAT_X_POS = 5952


# 加速起始&结束坐标 - 红毯？188-230
SPEED_INCREASE_RATE_FAST_START = 6016
SPEED_INCREASE_RATE_FAST_END = 7360