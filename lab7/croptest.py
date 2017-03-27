#!/usr/bin/env python
 
from PIL import Image
import grabber



pic = Image.open('picture','r')
#cropped = pic.crop((255,350,350,175))
half_width = pic.size[0]/2
half_height = pic.size[1]/2
cropped = pic.crop((half_width-300,half_height-60,half_width+20,half_height+100))
#cropped.save("cropped.png")

cropped_list = list(cropped.getdata())
print cropped_list[1:100]
