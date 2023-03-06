from math import sqrt, pi

print("""
1. Napisati kod koji za date katete a i b (a<b) pravouglog trougla 
računa površinu i zapreminu tijela koje se dobija rotacijom 
trougla oko manje katete.
""")


def cone_square_volume(a: float, b: float) -> object:
    """površinu i zapreminu tijela koje se dobija rotacijom trougla oko manje katete"""
    # be sure a<b
    if (a > b):
        c = a
        a = b
        b = c

    cone_hypotenuse = sqrt((a*a)+(b*b))

    # cone square =  pi*a*a + pi*a*coneHypotenuse
    cone_square = pi*a*(a+cone_hypotenuse)

    # cone volume = b * pi * a * a / 3
    cone_volume = b*pi*a*a/3

    return {
        'cone_square': cone_square,
        'cone_volume': cone_volume
    }


for data in [[1, 2], [3, 4]]:
    print(f'Triangle legs: {data[0]},{data[1]}')
    obj = cone_square_volume(data[0], data[1])
    print(
        f" Cone surface square: {round(obj['cone_square'],1)}, volume {round(obj['cone_volume'],1)}")
