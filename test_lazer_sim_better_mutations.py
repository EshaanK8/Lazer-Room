from math import gcd

# Helper Functions
# @profile
def smallest_vec(vec):
    '''
        ((int))->(int)
        'Normalizes' a vector to its smallest possible integer
        components (compared to actual normalization, this is much
        more accurate as it uses ints not floats). Because it is
        used only for comparing if two vectors have the same
        direction, this is all that is needed.
    '''
    div = gcd(vec[0], vec[1])
    if div == 0:
        return tuple(vec)
    return (vec[0]//div, vec[1]//div)

# @profile
def distance(vec1, vec2):
    '''
        ((int), (int))->num
        Simple Pythagorean theorem implementation to determine
        the distance between two vectors on a plane.
    '''
    return ((vec1[0]-vec2[0])**2 + (vec1[1]-vec2[1])**2)**0.5