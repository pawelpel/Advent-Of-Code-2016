"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways
and office furniture that makes up this part of Easter Bunny HQ.
This must be a graphic design department; the walls are covered
in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes,
but... 5 10 25? Some of these aren't triangles.
You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than
the remaining side. For example, the "triangle" given above is impossible,
because 5 + 10 is not larger than 25.

"""
import re


def check_trianlge(sides):
    x, y, z = list(map(lambda x: int(x), sides))
    return (x + y > z) and (x + z > y) and (z + y > x)


def solve(data_):

    counter = 0
    for edges in data_:
        matched = re.match(r'[ ]+(\d+)[ ]+(\d+)[ ]+(\d+)', edges)
        if check_trianlge(matched.groups()):
            counter += 1
    return counter


def main():
    with open('day_3_data.txt','r') as data:
        possieble_triangle = solve(data)
        print('There are {} possible triangels'.format(str(possieble_triangle)))


if __name__ == '__main__':
    main()

"""
    There are 993 possible triangels
"""
