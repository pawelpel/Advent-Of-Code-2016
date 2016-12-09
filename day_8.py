"""--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an implementation
of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard
(no problem; there was one on a nearby desk).
Then, it displays a code on a little screen, and you type that code on a keypad.
Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed.
After a few minutes, you've taken everything apart and figured out how it works.
Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions
for the screen; these instructions are your puzzle input.
The screen is 50 pixels wide and 6 pixels tall, all of which start off,
and is capable of three somewhat peculiar operations:

rect AxB turns on all of the pixels in a rectangle at the top-left of
the screen which is A wide and B tall.

rotate row y=A by B shifts all of the pixels in row A (0 is the top row)
right by B pixels. Pixels that would fall off the right end
appear at the left end of the row.

rotate column x=A by B shifts all of the pixels in column A (0 is the left column)
down by B pixels. Pixels that would fall off the bottom appear at the top of the column.

For example, here is a simple sequence on a smaller screen:

rect 3x2 creates a small rectangle in the top-left corner:

###....
###....
.......
rotate column x=1 by 1 rotates the second column down by one pixel:

#.#....
###....
.#.....
rotate row y=0 by 4 rotates the top row right by four pixels:

....#.#
###....
.#.....
rotate column x=1 by 1 again rotates the second column down by one pixel,
causing the bottom pixel to wrap back to the top:

.#..#.#
#.#....
.#.....
As you can see, this display technology is extremely powerful,
and will soon dominate the tiny-code-displaying-screen market.
That's what the advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display:
after you swipe your card, if the screen did work, how many pixels should be lit?
"""

import re
import curses
import time
from collections import deque


def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    with open('day_8_data.txt', 'r') as data:
        BLANK = ' '
        LIGHT = 'X'

        pattern_rotate = re.compile(r'(\w+) (\w)=(\d+) by (\d+)')
        pattern_rect = re.compile(r'(\d+)x(\d+)')

        displayer = [[BLANK for x in range(50)] for x in range(6)]

        for da in data:

            if da.startswith('rect'):
                m = re.search(pattern_rect, da)
                X, Y = int(m.group(1)), int(m.group(2))

                for di in range(Y):
                    for d in range(X):
                            displayer[di][d] = LIGHT

            elif da.startswith('rotate'):
                m = re.search(pattern_rotate, da)

                axis = m.group(2)
                which = int(m.group(3))
                by = int(m.group(4))

                if axis == 'x':
                    tmp = deque([])
                    for row in range(len(displayer)):
                        x = displayer[row][which]
                        tmp.append(x)

                    tmp.rotate(by)

                    for row in range(len(displayer)):
                        displayer[row][which] = tmp[row]

                elif axis == 'y':

                    tmp = deque(displayer[which])
                    tmp.rotate(by)
                    displayer[which] = tmp

            i = 0
            for d in displayer:
                stdscr.addstr(i, 0, BLANK.join(d))
                i += 1
            time.sleep(0.1)
            stdscr.refresh()

        time.sleep(3)
        curses.echo()
        curses.nocbreak()
        curses.endwin()

        counter = 0
        for di in displayer:
            for d in di:
                if d == LIGHT:
                    counter += 1
        return counter


if __name__ == '__main__':

    print('\n\nThere are {} lights\n\n'.format(main()))


"""
    There are 119 lights
"""


