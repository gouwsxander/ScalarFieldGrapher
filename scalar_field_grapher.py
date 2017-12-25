from math import *
from PIL import Image

# Maps pixel (x, y) in image to coordinate (a, b)
def MAP(x, y, scale, origin):
    Cx, Cy = origin
    a = (x - Cx)/scale
    b = -(y - Cy)/scale
    return (a, b)

# Maps value of function to colour output
def sigmoid(z):
    return e**z / (e**z + 1)

# Main function
def main(function, width, height, scale, origin):
    # Creates new RGB image
    img = Image.new("RGB", (width,height))

    # Loops through all pixels in image
    for i in range(width):
        for j in range(height):
            # Convert i,j to coordinate (x,y)
            x, y = MAP(i, j, scale, origin)
            # Evaluates function at (x,y)
            z = function(x,y)

            # Determines colouring of each pixel
            try:
                C = round(sigmoid(z/5)*255)
            except:
                C = 255

            # Writes colour to pixel
            img.putpixel((i,j), (C, C, C))

    # Returns image
    return img

def f(x,y):
    return (y+2)*(y+1)*(y-1) + (x+1)*(x-2)

if __name__ == "__main__":
    sfgraph = main(f,1024,1024,64,(512,512))
    sfgraph.show()
