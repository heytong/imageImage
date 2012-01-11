import os,Image,ImageDraw
from math import sqrt

DEFAULT_PATH = os.path.dirname(__file__)
img_file     = os.path.join(DEFAULT_PATH,"2.jpg").replace("\\","/")
img          = Image.open(img_file).convert("RGB")
width,height = img.size

img1         = Image.new( "RGB",(width,height),(255,255,255) )
draw = ImageDraw.Draw(img1)
#sobel operator
for i in range(width):
    for j in range(height):
        #r,g,b = img.getpixel((i,j))
        g_v = g_h = 0
        v0 = h0 = v1 = h1 = v2 = h2 = 0
        for k in range(i-1,i+2):
            
            for L in range(j-1,j+2):

                if k >=0 and L >= 0 and k < width and L < height:
                    pixel = img.getpixel((k,L))
                    r,g,b = pixel
                    if k == i - 1:
                        if L == j:
                            g_v = -2
                        else:
                            g_v = -1
                    if k == i + 1:
                        if L == j:
                            g_v = 2
                        else:
                            g_v = 1
                    if k == i:
                        g_v = 0
                    if L == j - 1:
                        if k == i:
                            g_h = 2
                        else:
                            g_h = 1
                    if L == j + 1:
                        if k == i:
                            g_h = -2
                        else:
                            g_h = -1
                    if L == j:
                        g_h = 0
                    v0 += r * g_v
                    h0 += r * g_h
                    v1 += g * g_v
                    h1 += g * g_h
                    v2 += b * g_v
                    h2 += b * g_h                    
                    #aa += () * g_v
        R   = int(sqrt( v0*v0 + h0*h0 ))
        G   = int(sqrt( v1*v1 + h1*h1 ))
        B   = int(sqrt( v2*v2 + h2*h2 ))
        """
        if R > 128 and G > 128 and B > 128:
            R = G = B = 255
        else :
            R = G = B = 0
        """
        draw.point( (i,j), (R,G,B) )
img1.convert("L")
img1.show()
#img1 show