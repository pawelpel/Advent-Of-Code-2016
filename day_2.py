"""
--- Day 2: Bathroom Security ---

You arrive at Easter Bunny Headquarters under cover of darkness. However,
you left in such a rush that you forgot to use the bathroom! Fancy office
buildings like this one usually have keypad locks on their bathrooms,
so you search the front desk for the code.

"In order to improve security," the document you find says,
"bathroom codes will no longer be written down. Instead, please memorize and
follow the procedure below to access the bathrooms."

The document goes on to explain that each button to be pressed can be
found by starting on the previous button and moving to adjacent buttons
on the keypad: U moves up, D moves down, L moves left, and R moves right.
Each line of instructions corresponds to one button, starting at the previous
button (or, for the first line, the "5" button); press whatever button you're
on at the end of each line. If a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out the code
as you walk to the bathroom. You picture a keypad like this:

1 2 3
4 5 6
7 8 9
Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD
You start at "5" and move up (to "2"), left (to "1"), and left
(you can't, and stay on "1"), so the first button is 1.
Starting from the previous button ("1"), you move right twice (to "3") and then
down three times (stopping at "9" after two moves and ignoring the third),
ending up with 9.
Continuing from "9", you move left, up, right, down, and left, ending with 8.
Finally, you move up four times (stopping at "2"), then down once, ending with 5.
So, in this example, the bathroom code is 1985.

"""

input_raw = """
LURLLLLLDUULRDDDRLRDDDUDDUULLRLULRURLRRDULUUURDUURLRDRRURUURUDDRDLRRLDDDDLLDURLDUUUDRDDDLULLDDLRLRRRLDLDDDDDLUUUDLUULRDUDLDRRRUDUDDRULURULDRUDLDUUUDLUDURUURRUUDRLDURRULURRURUUDDLRLDDDDRDRLDDLURLRDDLUDRLLRURRURRRURURRLLRLDRDLULLUDLUDRURDLRDUUDDUUDRLUDDLRLUDLLURDRUDDLRURDULLLUDDURULDRLUDLUDLULRRUUDDLDRLLUULDDURLURRRRUUDRUDLLDRUDLRRDUDUUURRULLDLDDRLUURLDUDDRLDRLDULDDURDLUUDRRLDRLLLRRRDLLLLURDLLLUDRUULUULLRLRDLULRLURLURRRDRLLDLDRLLRLULRDDDLUDDLLLRRLLLUURLDRULLDURDLULUDLRLDLUDURLLLURUUUDRRRULRDURLLURRLDLRLDLDRRUUDRDDDDDRDUUDULUL
RRURLURRULLUDUULUUURURULLDLRLRRULRUDUDDLLLRRRRLRUDUUUUDULUDRULDDUDLURLRRLLDLURLRDLDUULRDLLLDLLULLURLLURURULUDLDUDLUULDDLDRLRRUURRRLLRRLRULRRLDLDLRDULDLLDRRULRDRDUDUUUDUUDDRUUUDDLRDULLULDULUUUDDUULRLDLRLUUUUURDLULDLUUUULLLLRRRLDLLDLUDDULRULLRDURDRDRRRDDDLRDDULDLURLDLUDRRLDDDLULLRULDRULRURDURRUDUUULDRLRRUDDLULDLUULULRDRDULLLDULULDUDLDRLLLRLRURUDLUDDDURDUDDDULDRLUDRDRDRLRDDDDRLDRULLURUDRLLUDRLDDDLRLRDLDDUULRUDRLUULRULRLDLRLLULLUDULRLDRURDD
UUUUUURRDLLRUDUDURLRDDDURRRRULRLRUURLLLUULRUDLLRUUDURURUDRDLDLDRDUDUDRLUUDUUUDDURRRDRUDDUURDLRDRLDRRULULLLUDRDLLUULURULRULDRDRRLURULLDURUURDDRDLLDDDDULDULUULLRULRLDURLDDLULRLRRRLLURRLDLLULLDULRULLDLRULDDLUDDDLDDURUUUURDLLRURDURDUUDRULDUULLUUULLULLURLRDRLLRULLLLRRRRULDRULLUURLDRLRRDLDDRLRDURDRRDDDRRUDRLUULLLULRDDLDRRLRUDLRRLDULULRRDDURULLRULDUDRLRUUUULURLRLRDDDUUDDULLULLDDUDRLRDDRDRLDUURLRUULUULDUDDURDDLLLURUULLRDLRRDRDDDUDDRDLRRDDUURDUULUDDDDUUDDLULLDRDDLULLUDLDDURRULDUDRRUURRDLRLLDDRRLUUUDDUUDUDDDDDDDLULURRUULURLLUURUDUDDULURDDLRDDRRULLLDRRDLURURLRRRDDLDUUDR
URLLRULULULULDUULDLLRDUDDRRLRLLLULUDDUDLLLRURLLLLURRLRRDLULRUDDRLRRLLRDLRRULDLULRRRRUUDDRURLRUUDLRRULDDDLRULDURLDURLRLDDULURDDDDULDRLLUDRULRDDLUUUDUDUDDRRUDUURUURLUUULRLULUURURRLRUUULDDLURULRRRRDULUDLDRLLUURRRLLURDLDLLDUDRDRLLUDLDDLRLDLRUDUULDRRLLULDRRULLULURRLDLUUDLUDDRLURDDUDRDUDDDULLDRUDLRDLRDURUULRRDRUUULRUURDURLDUDRDLLRUULUULRDDUDLRDUUUUULDDDDDRRULRURLLRLLUUDLUDDUULDRULDLDUURUDUDLRULULUULLLLRLULUDDDRRLLDRUUDRLDDDRDDURRDDDULURDLDLUDDUULUUURDULDLLULRRUURDDUDRUULDLRLURUDLRDLLLDRLDUURUDUDRLLLDDDULLUDUUULLUUUDLRRRURRRRRDUULLUURRDUU
UDULUUDLDURRUDDUDRDDRRUULRRULULURRDDRUULDRLDUDDRRRRDLRURLLLRLRRLLLULDURRDLLDUDDULDLURLURUURLLLDUURRUUDLLLUDRUDLDDRLRRDLRLDDDULLRUURUUUDRRDLLLRRULDRURLRDLLUDRLLULRDLDDLLRRUDURULRLRLDRUDDLUUDRLDDRUDULLLURLRDLRUUDRRUUDUDRDDRDRDDLRULULURLRULDRURLURLRDRDUUDUDUULDDRLUUURULRDUDRUDRULUDDULLRDDRRUULRLDDLUUUUDUDLLLDULRRLRDDDLULRDUDRLDLURRUUDULUDRURUDDLUUUDDRLRLRLURDLDDRLRURRLLLRDRLRUUDRRRLUDLDLDDDLDULDRLURDURULURUDDDUDUULRLLDRLDDDDRULRDRLUUURD
"""

input_formatted = input_raw.strip().split('\n')


def came_to(direction, c_b, keypad_):
    cb = c_b

    try:
        c_b_div_3 = (c_b-1)//3
        c_b_i = keypad_[c_b_div_3].index(c_b)
        if direction == 'L':
            c_b = keypad_[c_b_div_3][c_b_i-1 if c_b_i > 0 else 0]
        if direction == 'R':
            c_b = keypad_[c_b_div_3][c_b_i+1 if c_b_i < 3 else 3]
        if direction == 'U':
            c_b = keypad_[c_b_div_3-1 if c_b_div_3 > 0 else 0][c_b_i]
        if direction == 'D':
            c_b = keypad_[c_b_div_3+1 if c_b_div_3 < 3 else 3][c_b_i]

    except IndexError as e:
            # print('NOBODY CARE : )')
            c_b = cb

    return c_b


def  solve(input_):

    keypad = [[1,2,3],
              [4,5,6],
              [7,8,9]]

    cur_button = 5
    code = []

    for line in input_:
        for l in line:
            cur_button = came_to(l, cur_button, keypad)
        code.append(cur_button)

    return code


def main():

    bathroom_code = solve(input_formatted)
    print("The bathroom code is {}".format(''.join(map(lambda x: str(x), bathroom_code))))


if __name__ == '__main__':

    main()


""" solution 19636 """






























