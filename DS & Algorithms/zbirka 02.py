from math import sqrt, pi

print(
    """

1. Napisati kod koji za date katete a i b (a<b) pravouglog trougla 
računa površinu i zapreminu tijela koje se dobija rotacijom 
trougla oko manje katete.
""")


def coneSquareAndVolume(a: float, b: float) -> object:
    # be sure a<b
    if (a > b):
        c = a
        a = b
        b = c

    coneHypotenuse = sqrt((a*a)+(b*b))

    # cone square =  pi*a*a + pi*a*coneHypotenuse
    coneSquare = pi*a*(a+coneHypotenuse)

    # cone volume = b * pi * a * a / 3
    coneVolume = b*pi*a*a/3

    return {
        'coneSquare': coneSquare,
        'coneVolume': coneVolume
    }


for data in [[1, 2], [3, 4]]:
    print(f'Triangle legs: {data[0]},{data[1]}')
    obj = coneSquareAndVolume(data[0], data[1])
    print(
        f" Cone surface square: {round(obj['coneSquare'],1)}, volume {round(obj['coneVolume'],1)}")
