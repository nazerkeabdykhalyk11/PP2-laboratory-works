import math

def volume_of_sphere (r):
    volume = 4/3 * math.pi * r**3

    print(volume)

volume_of_sphere(int(input(f'Enter radius of the sphere: ')))
