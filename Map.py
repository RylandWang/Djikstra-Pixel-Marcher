from PIL import Image
from os import makedirs, path

class Map:
    """
    This class store image data
    """

    def __init__(self, filePath):
        with open(filePath, 'rb') as img_handle:
            self.fileName = path.basename(filePath)
            self.img = Image.open(img_handle)
            (self.sx, self.sy) = self.img.size
            self.pixels = self.img.load()
            self.path = []

    def outputPath(self):
        """
        Outputs an image with the name Path-<fileName> (in the 'output' folder) which displays the path 
        stored in self.path. The path is coloured green, with pixels at start being a brighter green 
        and towards the end being a darker green. 
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
        gradient formed along the path in self.path[].
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