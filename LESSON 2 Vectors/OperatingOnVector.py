import numpy as np

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

def vectorPlus(vector1, vector2):
    arr1 = np.array(vector1.coordinates)
    arr2 = np.array(vector2.coordinates)
    return arr1 + arr2


def vectorMinus(vector1, vector2):
    arr1 = np.array(vector1.coordinates)
    arr2 = np.array(vector2.coordinates)    
    return arr1 - arr2

def vectorScalar(scalar, vector2):
    arr1 = np.array(vector2.coordinates)     
    return arr1 * scalar


my_vector1 = Vector([8.218, -9.341])
my_vector2 = Vector([-1.129, 2.111])

my_vector3 = Vector([7.119, 8.215])
my_vector4 = Vector([-8.223, 0.878])

my_vector5 = Vector([1.671, -1.012, -0.318])



print(vectorPlus(my_vector1, my_vector2))
print(vectorMinus(my_vector3, my_vector4))
print(vectorScalar(7.41, my_vector5))
