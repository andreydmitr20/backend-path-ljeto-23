""" Homework 'zbirka 02'"""
from tkinter import *
from math import sqrt, pi, sin, cos, tan

print("""
1. Napisati kod koji za date katete a i b (a<b) pravouglog trougla
računa površinu i zapreminu tijela koje se dobija rotacijom
trougla oko manje katete.
""")


def cone_square_volume(aaa: float, bbb: float) -> object:
    """površinu i zapreminu tijela koje se dobija rotacijom trougla oko manje katete"""
    # be sure a<b
    if aaa > bbb:
        _ = aaa
        aaa = bbb
        bbb = _

    cone_hypotenuse = sqrt((aaa**2)+(bbb**2))

    # cone square =  pi*a*a + pi*a*coneHypotenuse
    cone_square = pi*aaa*(aaa+cone_hypotenuse)

    # cone volume = b * pi * a * a / 3
    cone_volume = (bbb*pi*aaa*aaa)/3

    return {
        'cone_square': cone_square,
        'cone_volume': cone_volume
    }


for data1 in [[1, 2], [3, 4]]:
    print(f'Triangle legs: {data1[0]},{data1[1]}')
    obj = cone_square_volume(data1[0], data1[1])
    print(
        f" Cone surface square: {round(obj['cone_square'],1)}, volume {round(obj['cone_volume'],1)}")


print("""
5. Dati su realni brojevi x, y,α, β, a i b.
 Napisati kod koji izračunava sljedeće izraze:
""")


def calc_abcde(data: dict) -> float:
    """calculate"""
    try:
        match data['letter']:
            case 'a':
                return ((data['x']**3) / 3) -\
                    (3*(data['y']**2)) +\
                    ((data['x']+1)/((2*data['y'])+3))
            case 'b':
                return (-5)*sqrt(data['x']+(sqrt(data['y'])))
            case 'c':
                return 1+(1/(2+(1/(3+(1/4)))))
            case 'd':
                return 3*sin(2*data['alfa'])*cos(2*data['beta']) -\
                    (5*(tan(data['alfa']+data['beta']) ** 2))
            case 'e':
                return sqrt((data['a']**2) +
                            (data['b']**2) -
                            (2*data['a']*data['b']*sin(data['alfa'])))
    except ZeroDivisionError:
        return None

    return None


for data1 in [
    {'letter': 'a', 'x': 1, 'y': 2},
    {'letter': 'b', 'x': 3, 'y': 4},
    {'letter': 'c'},
    {'letter': 'd', 'alfa': 7, 'beta': 8},
    {'letter': 'e', 'a': 9, 'b': 10, 'alfa': 1},
]:
    print(f'Input data: {data1}')
    print(f"result: {calc_abcde(data1)}")


print("""
10.  Napisati kod koji za kvadratnu jednačinu  ax2 + bx + c =0
ispituje da li ima realna rješenja
""")


def quadratic_equation_decision(data: dict) -> dict:
    """quadratic equation decision"""
    if data['a'] == 0:
        if data['b'] == 0:
            return {}
        else:
            if data['c'] == 0:
                return {'root1': 0}
            else:
                return {'root1': (-data['c'])/data['b']}

    discriminant = (data['b']**2)-(4*data['a']*data['c'])

    if discriminant < 0:
        return {}

    if discriminant == 0:
        return {'root1': (-data['b'])/(2*data['a'])}

    sqrt_of_discriminant = sqrt(discriminant)
    return {
        'root1': (-data['b']-sqrt_of_discriminant)/(2*data['a']),
        'root2': (-data['b']+sqrt_of_discriminant)/(2*data['a'])
    }


for data1 in [
    {'a': 0, 'b': 2, 'c': 10},
    {'a': -4, 'b': 28, 'c': -49},
    {'a': -6, 'b': 0, 'c': 54},
    {'a': 1, 'b': -1, 'c': 0},
    {'a': 3, 'b': -4, 'c': 94},
    {'a': 0, 'b': -4, 'c': 0},
    {'a': 0, 'b': 0, 'c': 0},
]:
    print(f'Input data: {data1}')
    print(
        f"result: {quadratic_equation_decision(data1)}")

print("""
17.  Napisati kod koji za date realni brojeve x i y provjerava da li tačka sa
koordinatama (x,y) pripada osjenčenom dijelu ravni. 
Centar oba kruga je u tački (0,0), poluprečnici su im 
redom 4 i 6, dok je prava data jednačinom x-y-4=0. 
Podsjetite se da je krug skup tačaka u 
ravni koje su na rastojanju r od date tačke tj. centra kruga. 
Štampati poruku „Pripada“ ili „Ne pripada“. 
""")


def is_point_inside_shaded_parts(data: dict) -> bool:
    """determine if point inside shaded parts"""
    # radius
    radius1 = data['radius1']
    radius2 = data['radius2']
    if radius2 < radius1:
        _ = radius1
        radius1 = radius2
        radius2 = _

    px0 = data['x']
    py0 = data['y']

    if px0 == 0:
        # part 1
        if 0 <= py0 <= radius2:
            return True
        elif py0 == -radius1:
            return True

    elif px0 > 0:
        if px0 <= radius1:
            if py0 >= 0:
                # part 2
                if py0 <= radius1:
                    return px0 <= sqrt((radius1**2)-(py0**2))
            else:
                # part 3
                py0 = abs(py0)
                if py0 <= radius1:
                    if px0 <= sqrt((radius1**2)-(py0**2)):
                        return (px0 + py0) >= radius1
        elif px0 <= radius2:
            # part 4
            if 0 <= py0:
                px2 = 0
                if py0 <= radius2:
                    px2 = sqrt((radius2**2)-(py0**2))
                    if radius1 <= px0 <= px2:
                        if py0 <= (px0-radius1):
                            return True
    else:
        # px0 < 0

        # only part1
        if py0 >= 0:
            px1 = 0
            if py0 <= radius1:
                px1 = sqrt((radius1**2)-(py0**2))
            px2 = 0
            if py0 <= radius2:
                px2 = sqrt((radius2**2)-(py0**2))
            return px1 <= abs(px0) <= px2

    return False


for data1 in [
    {'radius1': 4, 'radius2': 6, 'x': -1, 'y': 5},
    {'radius1': 4, 'radius2': 6, 'x': -4.5, 'y': 1},
    {'radius1': 4, 'radius2': 6, 'x': 0, 'y': 6},
    {'radius1': 4, 'radius2': 6, 'x': 0, 'y': -6.1},
    {'radius1': 4, 'radius2': 6, 'x': 1, 'y': 1.1},
    {'radius1': 4, 'radius2': 6, 'x': 0, 'y': -4},
    {'radius1': 4, 'radius2': 6, 'x': 2.1, 'y': -1.8},
    {'radius1': 4, 'radius2': 6, 'x': 2, 'y': -2},
    {'radius1': 4, 'radius2': 6, 'x': 5, 'y': 1},
    {'radius1': 4, 'radius2': 6, 'x': 5, 'y': 1.1},
    {'radius1': 4, 'radius2': 6, 'x': 3, 'y': 3},
    {'radius1': 4, 'radius2': 6, 'x': 5, 'y': 0.5},
]:
    print(f'Input data: {data1}')
    print(
        f"result: {'Pripada' if is_point_inside_shaded_parts(data1) else 'Ne pripada'}")

# test in 2d graphics
win = Tk()
win.title("Task 17 graphics test")
RADIUS1 = 100
RADIUS2 = 200
CANVAS_WIDTH = 800


def convert_x(xxx: int):
    """ convert x"""
    return xxx+(CANVAS_WIDTH//2)


def convert_y(yyy: int):
    """ convert y"""
    return (CANVAS_WIDTH//2)-yyy


c = Canvas(win,
           width=CANVAS_WIDTH,
           height=CANVAS_WIDTH)
c.pack(expand=YES, fill=BOTH)

c.create_oval(convert_x(-RADIUS1), convert_y(-RADIUS1),
              convert_x(RADIUS1), convert_y(RADIUS1))
c.create_oval(convert_x(-RADIUS2), convert_y(-RADIUS2),
              convert_x(RADIUS2), convert_y(RADIUS2))

for x in range(-(CANVAS_WIDTH//2), CANVAS_WIDTH//2):
    for y in range(-(CANVAS_WIDTH//2), CANVAS_WIDTH//2):
        if is_point_inside_shaded_parts(
            {
                'radius1': RADIUS1,  # CANVAS_WIDTH//4,
                'radius2': RADIUS2,  # CANVAS_WIDTH//3,
                'x': x,
                'y': y
            }
        ):
            c.create_line(
                convert_x(x), convert_y(y),
                convert_x(x+1), convert_y(y),
                fill='blue'
            )

mainloop()
