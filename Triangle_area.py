import math


def get_sides():
    sides_number = [1, 2, 3]
    sides = []
    for side in sides_number:
        aux_var = input(f'Type the side {side} of the triangle:  ')
        sides.append(int(aux_var))
    return sides


#using de Heron formula
def area_of_triangle(sides):
    aux_sum = 0
    for side in sides:
        aux_sum += side
    semi_perimeter = aux_sum/2
    area = math.sqrt(semi_perimeter*(semi_perimeter-sides[0])*(semi_perimeter-sides[1])*(semi_perimeter-sides[2]))
    return area


sides = get_sides()
print(area_of_triangle(sides))

