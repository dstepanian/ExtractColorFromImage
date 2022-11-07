from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

obj = ColorThief("image.jpg")


#SHOWS THE DOMIANT COLOR {uncomment to run}
# dom_color = obj.get_color(quality = 1)
# plt.imshow([[dom_color]])
# plt.show()


# #SHOWS THE PALLETE OF COLORS
palette = obj.get_palette(color_count = 5, quality = 10)
plt.imshow([[palette [i] for i in range (5)]])
plt.show()


for color in palette:
  print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}") #FOR HEX CODE
  print(colorsys.rgb_to_hls(color[0],color[1],color[2])) #FOR HLS CODE
