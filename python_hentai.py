import timg
import os
import sys
import r34

data = os.get_terminal_size()
width = data.columns
height = data.lines

#downloada shit in doba filename
filename = r34.save_img(sys.argv[1:])
print(sys.argv)

#nardi shit za img showing
obj = timg.Renderer()
obj.load_image_from_file(filename)
obj.resize(width, height)
obj.render(timg.Ansi24HblockMethod)