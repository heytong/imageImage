#!/usr/bin/env python
import os,Image,ImageDraw
default_path    =   os.path.dirname(__file__)
img_file        =   os.path.join(default_path, "test1.jpg").replace("\\","")
img             =   Image.open(img_file).convert("L")
width,height    =   img.size
img1            =   Image.new("RGB", (width,height), (0,0,0))
draw            =   ImageDraw.Draw(img1)

'''
def  crop( y, x, s[3][3] ):
    for m in range(-1,2):
        for n in range(-1,2):
            if y + m > 0 and y + m < height and x + n > 0 and x + n < width:
                s[1+m][1+n] =   img.getpixel( (y + m, x + n) )  
'''
a = [[0 for col in range(5)] for row in range(5)]
jump = 1
while(jump):
    jump = 0    
    for I in range(2,width-2):
        for J in range(2,height-2):
            if img.getpixel((I,J)) ==0:
                continue            
            #a = [[0 for col in range(5)] for row in range(5)]
            for M in range(-2,2):
                for N in range(-2,2):
                    if I + M > 0 and I + M < width and J + N > 0 and J + N < height:
                        if img.getpixel((I+M, J+N)) >= 128:
                            a[2+M][2+N]   =   255
                        else:
                            a[2+M][2+N]   =   0
                        #a[2+M][2+N]   =   0                   
            if a[2][2] == 0:
                continue                        
            #condition 1
            ncount = 0
            for M in range(1,4):
                for N in range(1,4):
                    if a[M][N] == 255:
                        ncount+=1
            #drop a[2][2]
            ncount-=1            
            if ncount < 2 or ncount > 6:
                draw.point((I,J),(255,255,255))
                continue
            #condition 2
            ncount = 0
            if a[1][2] ==255 and a[1][1] ==0:
                ncount+=1
            if a[1][1] ==255 and a[2][1] ==0:
                ncount+=1
            if a[2][1] ==255 and a[3][1] ==0:
                ncount+=1
            if a[3][1] ==255 and a[3][2] ==0:
                ncount+=1
            if a[3][2] ==255 and a[3][3] ==0:
                ncount+=1
            if a[3][3] ==255 and a[2][3] ==0:
                ncount+=1
            if a[2][3] ==255 and a[1][3] ==0:
                ncount+=1
            if a[1][3] ==255 and a[1][2] ==0:
                ncount+=1
            if ncount != 1:
                  draw.point((I,J),(255,255,255))
                  continue
            #condition 3
            if a[1][2]*a[2][1]*a[2][3]!=0:
                ncount = 0
                if a[0][2]==255 and a[0][1]==0:
                    ncount+=1   
                if a[0][1]==255 and a[1][1]==0:
                    ncount+=1 
                if a[1][1]==255 and a[2][1]==0:   
                    ncount+=1  
                if a[2][1]==255 and a[2][2]==0:
                    ncount+=1  
                if a[2][2]==255 and a[2][3]==0:  
                    ncount+=1 
                if a[2][3]==255 and a[1][3]==0:
                    ncount+=1  
                if a[1][3]==255 and a[0][3]==0:
                    ncount+=1   
                if a[0][3]==255 and a[0][2]==0:
                    ncount+=1
                if ncount == 1:
                    draw.point((I,J),(255,255,255))
                    continue
            #condition 4
            if a[1][2]*a[2][1]*a[3][2]!=0:
                ncount = 0
                if a[1][1]==255 and a[1][0]==0:
                    ncount+=1   
                if a[1][0]==255 and a[2][0]==0:
                    ncount+=1 
                if a[2][0]==255 and a[3][0]==0:   
                    ncount+=1  
                if a[3][0]==255 and a[3][1]==0:
                    ncount+=1  
                if a[3][1]==255 and a[3][2]==0:  
                    ncount+=1 
                if a[3][2]==255 and a[2][2]==0:
                    ncount+=1  
                if a[2][2]==255 and a[1][2]==0:
                    ncount+=1   
                if a[1][2]==255 and a[1][1]==0:
                    ncount+=1
                if ncount  == 1:
                    draw.point((I,J),(255,255,255))
                    continue
            draw.point((I,J),(0,0,0))
            jump = 0
#second loop
'''
b = [[0 for col in range(3)] for row in range(3)]
jump2 = 1
while(jump2):
    jump2 = 0    
    for I in range(0,width):
        for J in range(0,height):
            if img.getpixel((I,J)) ==0:
                continue            
            #a = [[0 for col in range(5)] for row in range(5)]
            for M in range(-1,2):
                for N in range(-1,2):
                    if I + M >= 0 and I + M < width and J + N >= 0 and J + N < height:
                        a[1+M][1+N]   =   img.getpixel((I+M, J+N))                        
                        #a[2+M][2+N]   =   0                   
            if a[1][1] ==0:
                continue                        
            #condition 1
            ncount = 0
            for M in range(0,2):
                for N in range(0,2):
                    if a[M][N] ==255:
                        ncount+=1
            #drop a[1][1]
            ncount-=1            
            if ncount < 2 or ncount > 6:
                draw.point((I,J),(255,255,255))
                continue
            #condition 2
            ncount = 0
            if a[0][0] ==255 and a[1][1] ==0:
                ncount+=1
            if a[1][1] ==255 and a[2][1] ==0:
                ncount+=1
            if a[2][1] ==255 and a[3][1] ==0:
                ncount+=1
            if a[3][1] ==255 and a[3][2] ==0:
                ncount+=1
            if a[3][2] ==255 and a[3][3] ==0:
                ncount+=1
            if a[3][3] ==255 and a[2][3] ==0:
                ncount+=1
            if a[2][3] ==255 and a[1][3] ==0:
                ncount+=1
            if a[1][3] ==255 and a[1][2] ==0:
                ncount+=1
            if ncount != 1:
                  draw.point((I,J),(255,255,255))
                  continue
            #condition 3
            if a[1][2]*a[2][1]*a[2][3]!= 0:
                ncount = 0
                if a[0][2]==255 and a[0][1]==0:
                    ncount+=1   
                if a[0][1]==255 and a[1][1]==0:
                    ncount+=1 
                if a[1][1]==255 and a[2][1]==0:   
                    ncount+=1  
                if a[2][1]==255 and a[2][2]==0:
                    ncount+=1  
                if a[2][2]==255 and a[2][3]==0:  
                    ncount+=1 
                if a[2][3]==255 and a[1][3]==0:
                    ncount+=1  
                if a[1][3]==255 and a[0][3]==0:
                    ncount+=1   
                if a[0][3]==255 and a[0][2]==0:
                    ncount+=1
                if ncount == 1:
                    draw.point((I,J),(255,255,255))
                    continue
            #condition 4
            if a[1][2]*a[2][1]*a[3][2]!=0:
                ncount = 0
                if a[1][1]==255 and a[1][0]==0:
                    ncount+=1   
                if a[1][0]==255 and a[2][0]==0:
                    ncount+=1 
                if a[2][0]==255 and a[3][0]==0:   
                    ncount+=1  
                if a[3][0]==255 and a[3][1]==0:
                    ncount+=1  
                if a[3][1]==255 and a[3][2]==0:  
                    ncount+=1 
                if a[3][2]==255 and a[2][2]==0:
                    ncount+=1  
                if a[2][2]==255 and a[1][2]==0:
                    ncount+=1   
                if a[1][2]==255 and a[1][1]==0:
                    ncount+=1
                if ncount  == 1:
                    draw.point((I,J),(255,255,255))
                    continue
            draw.point((I,J),(0,0,0))
            jump2 = 0
'''
#show
img1.show()
#img1.save("./test2.jpg")
            
            
            
            
            

                
                
            
            