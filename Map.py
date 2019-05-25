from PIL import Image
from os import makedirs, path

#################################################################
#                                                               #
#    You should ONLY be submitting Marcher.py on Markus,        #
#    and so you should not be changing any of the logic here    #
#    as part of it. If you feel like you need to add any        #
#    temporay variables to debug, thats OK, but make            #
#    sure your solution only depends on this file as it was     #
#    in the starter code.                                       #
#                                                               #
#################################################################


class Map:
    """
    This class is used to store the image in memory. It has the following fields:

    - fileName : Name of the image opened

    - img : The image object (used to output)

    - pixels : The 2D array containing pixel data. You will be using this for weights. 
                Each element is a 3-tuple representing the (R,G,B) values. Each of these 
                is an integer between 0 and 255.

                For example, if the pixel at (5,3) is Red,
                  pixels[(5,3)] = (255,0,0)

                Or, other notation you should be familiar with:
                  pixels[5][3][0] = 255   # Red
                  pixels[5][3][2] = 0     # Blue
                  pixels[5][3][3] = 0     # Green

    - sx, sy : The x and y dimensions of the image. Remember that the top left pixel (start) 
               is at (0,0). x increases as you go right, and y increases as you go down. The 
               bottom right pixel (target) is located at (sx-1, sy-1)

    - path : Initialized to be an empty array, but you need to add in the pixels along the 
             leastenergy path in here to have it output correctly. Each element in this should 
             be a tuple of (x,y) coordinates in order of the path you have found.

             For example:
             path = [(0,0), (0,1), (1,1), ... , (sx-1, sy-1)]

             Means your path found starts at (0,0), then goes to (0,1), then to (1,1), etc.
    """

    def __init__(self, filePath):
        with open(filePath, 'rb') as img_handle:
            self.fileName = path.basename(filePath)
            self.img = Image.open(img_handle)
            (sx, sy) = self.img.size
            self.pixels = self.img.load()
            self.path = []
            self.sx = sx
            self.sy = sy

    def outputPath(self):
        """
        Outputs an image with the name Path-<fileName> (in the 'output' folder) which displays the path 
        stored in self.path. The path is coloured green, with pixels at start being a brighter green 
        and towards the end being a darker green. 

        You will not be submitting this file, so feel free to change this to show more information
        on the image. (Displaying the pixels you've already 'finished' may help)
        """
        if self.path == []:
            print('Nothing in path. Skipping output...')
            return

        makedirs('output', exist_ok=True)
        # Scaling factor to gradually change colour
        ptImg = self.img.copy()
        ptPix = ptImg.load()
        l = 120.0 / len(self.path)
        for i, coords in enumerate(self.path):
            ptPix[coords] = (0, 255-int(i*l), 0)
        ptImg.save('output/Path-'+self.fileName)
        ptImg.close()

    def outputGradient(self):
        """
        Outputs an image with the name Grad-<fileName> (in the 'output' folder) which displays the 
        gradient formed along the path in self.path[]. Use this to help you complete and test the 
        'all_colour_weight()' function. Make sure that no colour is repeated!

        Another interesting exercise (on your own time) would be to try and come up with weight 
        functions that give you cooler gradients - how would you get the smoothest gradient? The 
        most colourful? The possibilities are endless! (Share your cool gradients with us!)
        """

        if self.path == []:
            print('Nothing in path. Skipping output...')
            return

        makedirs('output', exist_ok=True)
        grImg = Image.new('RGB', (len(self.path), len(self.path)))
        grPix = grImg.load()
        for i in range(len(self.path)):
            for j in range(len(self.path)):
                grPix[(i, j)] = self.pixels[self.path[i]]
        grImg.save('output/Grad-'+self.fileName)
        grImg.close()
