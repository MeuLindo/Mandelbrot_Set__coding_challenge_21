maxval = 0.45
minval = -0.45

def setup():
    size(1000,1000)
    pixelDensity(1)
    
    maxiterations = 100
    loadPixels()
    
    for x in range(0, width):
        for y in range(0,height):
            
            a = map(x-500, 0, width, minval, maxval)
            b = map(y, 0, height, maxval, minval)
            
            ca = a
            cb = b
            n = 0
            z = 0
            
            while n < maxiterations:
                
                aa = a*a - b*b
                bb = 2 * a * b
                
                a = aa + ca
                b = bb + cb
                
                #print(abs(a + b), "                                     {}                                                 ".format(n))
                
                if abs(a + b) > 16:
                    break
                
                n += 1
                
                # Colorizações diferentes
                acender = map(n, 0, maxiterations, 0, 255)
                #acender = (n * 16) % 255
                #acender = 200
                
                if n == maxiterations:
                    acender = 0
            
            pix = (x + y * width)
            
            pixels[pix] = color(acender)
        
    updatePixels()
