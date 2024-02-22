# Quinton Nelson
# 2/21/2024
# This file contains color values depending on the value of the tile

#Dictionary for color values based on the value of the tile
TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (237, 207, 114),
    128: (237, 204, 97),
    256: (237, 200, 80),
    512: (237, 197, 63),
    1024: (237, 194, 46),
    2048: (237, 191, 29),
    4096: (237, 188, 12),
    8192: (237, 185, 0),
    16384: (237, 182, 0),
    32768: (237, 179, 0),
    65536: (237, 176, 0),
    131072: (237, 173, 0),
    262144: (237, 170, 0),
    524288: (237, 167, 0),
    1048576: (237, 164, 0)
}


#Calculate color of text based on the brightness of the background
def get_font_color(background_color):
    # Calculate the brightness of the background color using the formula: 0.299*R + 0.587*G + 0.114*B
    brightness = 0.299 * background_color[0] + 0.587 * background_color[1] + 0.114 * background_color[2]

    if brightness > 125:
        return (0, 0, 0) # Dark font color
    else:
        return (255, 255, 255)  # Light font color
