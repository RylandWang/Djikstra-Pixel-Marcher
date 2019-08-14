from Map import Map

def similar_colour(mp, a, b):
    '''
    Colored weight function.
    Given Map mp, calculates euclidean distance between RGB of pixel a and b.
    '''
    #   The weight between two pixels is the euclidean distance between
    #   the (R,G,B) values of the 2 pixels. (If we think of them as vectors)
    pa = mp.pixels[a]
    pb = mp.pixels[b]
    dst = (pa[0]-pb[0])**2 + (pa[1]-pb[1])**2 + (pa[2]-pb[2])**2
    return (dst ** 0.5 + 0.01)

def how_white(mp, a, b):
    '''
    Black and white image weight function.
    Given Map mp, calculates euclidean distance of pixel b from white's RGB.
    '''
    #   The weight between two pixels is simply how close pixel (b) is from
    #   the colour white (255, 255, 255).
    pb = mp.pixels[b]
    dst = (255-pb[0])**2 + (255-pb[1])**2 + (255-pb[2])**2
    return ((dst/100.0) ** 0.5) + 0.01