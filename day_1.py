"""
--- Day 1: No Time for a Taxicab ---

Santa's sleigh uses a very high-precision clock to guide its movements,
and the clock's oscillator is regulated by stars. Unfortunately,
the stars have been stolen... by the Easter Bunny. To save Christmas,
Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available
on each day in the advent calendar; the second puzzle is unlocked when
you complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere.
"Near", unfortunately, is as close as you can get - the instructions
on the Easter Bunny Recruiting Document the Elves intercepted start here,
and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates
(where you just landed) and face North. Then, follow the provided sequence:
either turn left (L) or right (R) 90 degrees, then walk forward the given
number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though,
so you take a moment and work out the destination. Given that you can only
walk on the street grid of the city,
how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.

How many blocks away is Easter Bunny HQ?

    N
W       E
    S
"""

input_raw = """
L5, R1, R4, L5, L4, R3, R1, L1, R4, R5, L1, L3, R4, L2, L4, R2, L4,
L1, R3, R1, R1, L1, R1, L5, R5, R2, L5, R2, R1, L2, L4, L4, R191, R2, R5,
R1, L1, L2, R5, L2, L3, R4, L1, L1, R1, R50, L1, R1, R76, R5, R4, R2, L5,
L3, L5, R2, R1, L1, R2, L3, R4, R2, L1, L1, R4, L1, L1, R185, R1, L5, L4,
L5, L3, R2, R3, R1, L5, R1, L3, L2, L2, R5, L1, L1, L3, R1, R4, L2, L1,
L1, L3, L4, R5, L2, R3, R5, R1, L4, R5, L3, R3, R3, R1, R1, R5, R2, L2,
R5, L5, L4, R4, R3, R5, R1, L3, R1, L2, L2, R3, R4, L1, R4, L1, R4, R3,
L1, L4, L1, L5, L2, R2, L1, R1, L5, L3, R4, L1, R5, L5, L5, L1, L3, R1,
R5, L2, L4, L5, L1, L1, L2, R5, R5, L4, R3, L2, L1, L3, L4, L5, L5, L2,
R4, R3, L5, R4, R2, R1, L5
"""


def fromat_input(input_raw_):
    return input_raw_.strip().replace('\n', ' ').split(', ')


def roatate(LR, cur_direction_, directions_):
    if LR == 'L':
        if cur_direction_ == 'W':
            cur_direction_ = 'S'
        else:
            cur_direction_ = directions_[directions_.index(cur_direction_)-1]

    if LR == 'R':
        if cur_direction_ == 'S':
            cur_direction_ = 'W'
        else:
            cur_direction_ = directions_[directions_.index(cur_direction_)+1]

    return cur_direction_


def solve(input_):

    directions = ['W', 'N', 'E', 'S']
    cur_direction = directions[1]

    #              X  Y      X - vertical, Y - horizontal
    blocks_away = [0, 0]

    for i in input_:
        where = i[:1]
        blocks = int(i[1:])
        cur_direction = roatate(where, cur_direction, directions)

        if cur_direction == 'W':
            blocks_away[1] += -blocks
        if cur_direction == 'N':
            blocks_away[0] += blocks
        if cur_direction == 'E':
            blocks_away[1] += blocks
        if cur_direction == 'S':
            blocks_away[0] += -blocks

    return blocks_away[0]+blocks_away[1]


def main():

    number_of_bloks_away = solve(fromat_input(input_raw))

    print('Ester Bunny is {} blocks away!'.format(number_of_bloks_away))

    return number_of_bloks_away


if __name__ == '__main__':
    main()

"""
    Ester Bunny is 242 blocks away!
"""






