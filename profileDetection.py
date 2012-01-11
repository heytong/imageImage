#!/usr/bin/env python
import os,Image,ImageDraw

DEFAULT_PATH    =   os.path.dirname(__file__)
img_file        =   os.path.join(DEFAULT_PATH,"sssss.jpg").replace("\\","/")
img             =   Image.open(img_file).convert("L")
width,height    =   img.size
img1            =   Image.new("RGB",(width,height),(255,255,255))
draw            =   ImageDraw.Draw(img1)

for I in range(width):
    for J in range(height):
        L = img.getpixel( ( I, J ) )
        if L >= 128:
            draw.point( ( I, J ), (255,255,255) )
        else:
            draw.point( ( I, J ), (0,0,0) )
img1.show()
'''
for I in range(width):
    for J in range(height):
        r0,g0,b0 = img.getpixel( ( I, J ) )
        #print r0,g0,b0
        x = y = 0
        for K in range(I-1,I+2):
            for L in range(J-1,J+2):
                if K >= 0 and L >=0 and K < width and L < height:
                    r,g,b = img.getpixel( ( K, L) )
                    #print r,g,b
                    #if I != K and J != L:
                    if abs(r0-r) < 55 and abs(g0-g) < 55 and abs(b0-b) < 55:
                        x+=1       
        #print x
        if x == 9:
            draw.point( (I, J), (255,255,255) )
        else:
            draw.point( (I, J), (0,0,0) )
img1.show()
'''
