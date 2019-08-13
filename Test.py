import unittest
from Marcher import Marcher
from Map import Map


#   The weight between two pixels is the euclidean distance between
#   the (R,G,B) values of the 2 pixels. (If we think of them as vectors)
def similar_colour(mp, a, b):
    pa = mp.pixels[a]
    pb = mp.pixels[b]
    dst = (pa[0]-pb[0])**2 + (pa[1]-pb[1])**2 + (pa[2]-pb[2])**2
    return (dst ** 0.5 + 0.01)


#   The weight between two pixels is simply how close pixel (b) is from
#   the colour white (255, 255, 255).
def how_white(mp, a, b):
    pb = mp.pixels[b]
    dst = (255-pb[0])**2 + (255-pb[1])**2 + (255-pb[2])**2
    return ((dst/100.0) ** 0.5) + 0.01


class TestMarcher(unittest.TestCase):

    def test_One(self):
        inp = Map("images/water.ppm")
        cost = Marcher.findPath(inp, similar_colour)
        inp.outputPath()
        self.assertAlmostEqual(cost, 1280.8152597, 5)

    def test_Maze(self):
        inp = Map("images/maze.ppm")
        cost = Marcher.findPath(inp, how_white)
        inp.outputPath()
        self.assertAlmostEqual(cost, 12.3999999, 5)

    def test_Maze_Big(self):
        inp = Map("images/bigmaze.ppm")
        cost = Marcher.findPath(inp, how_white)
        inp.outputPath()
        self.assertAlmostEqual(cost, 8.6199999, 5)

    def test_Gradient_One(self):
        inp = Map("images/grad.ppm")
        cost = Marcher.findPath(inp, similar_colour)
        inp.outputPath()
        self.assertAlmostEqual(cost, 278.7514937, 5)

    def test_Gradient_Two(self):
        inp = Map("images/grad.ppm")
        cost = Marcher.findPath(inp, how_white)
        inp.outputPath()
        self.assertAlmostEqual(cost, 2168.3216577, 5)


if __name__ == "__main__":
    unittest.main()
