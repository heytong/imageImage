import os,Image,ImageDraw
from math import sqrt

DEFAULT_PATH = os.path.dirname(__file__)
img_file     = os.path.join(DEFAULT_PATH,"1.jpg").replace("\\","/")
img          = Image.open(img_file).convert("RGB")
width,height = img.size

img1         = Image.new( "RGB",(width,height),(255,255,255) )
draw = ImageDraw.Draw(img1)
#prewitt operator
for i in range(width):
    for j in range(height):
        #r,g,b = img.getpixel((i,j))
        g_v = g_h = 0
        r0 = r1 = g0 = g1 = b0 = b1 = 0
        for k in range(i-1,i+2):
            
            for L in range(j-1,j+2):

                if k >=0 and L >= 0 and k < width and L < height:
                    pixel = img.getpixel((k,L))
                    r,g,b = pixel
                    if k == i - 1:
                        g_v = -1
                    if k == i + 1:
                        g_v = 1
                    if k == i:
                        g_v = 0
                    if L == j - 1:
                        g_h = 1
                    if L == j + 1:
                        g_h = -1
                    if L == j:
                        g_h = 0
                    r0 += r * g_v
                    r1 += r * g_h
                    g0 += g * g_v
                    g1 += g * g_h
                    b0 += b * g_v
                    b1 += b * g_h                    
                    #aa += () * g_v
        R   = int(sqrt( r0*r0 + r1*r1 ))
        G   = int(sqrt( g0*g0 + g1*g1 ))
        B   = int(sqrt( r0*r0 + r1*r1 ))        
        draw.point( (i,j), (R,G,B) )        
img1.show()
#img1 show