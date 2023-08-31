import imageio
import math
from collections import defaultdict
from pprint import pp

filepath = 'zoe_eric_stitch.png'

margin_left = 8
margin_right = 8
margin_top = 8
margin_bottom = 24

box_width = 7.5
line_width = 1

num_stitches_x = 140
num_stitches_y = 140
stitches_width = 1182
stitches_height = 1182


# y first, then x
stitch = imageio.v3.imread(filepath)


image_y, image_x, _z = stitch.shape

stitch_count = 0
color_counts = defaultdict(int)

for i in range(num_stitches_x):
    for j in range(num_stitches_y):
        y = math.floor(margin_top + line_width + box_width/2 + j * (stitches_height / num_stitches_y))
        x = math.floor(margin_left + line_width + box_width/2 + i * (stitches_width / num_stitches_x))
        if list(stitch[y][x]) != [255, 255, 255, 255]:
            stitch_count += 1
            color_counts[tuple(stitch[y][x])] += 1
        stitch[y][x] = [255, 0, 0, 255]

imageio.imsave('output.png', stitch)

print(f'stitch count is {stitch_count}')
pp(color_counts)
