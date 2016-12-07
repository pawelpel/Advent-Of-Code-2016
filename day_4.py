"""--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms.
Of course, the list is encrypted and full of decoy data, but the instructions
to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes)
followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters
in the encrypted name, in order, with ties broken by alphabetization.
For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters
are a (5), b (3), and then a tie between x, y, and z, which are listed
alphabetically.

a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters
are all tied (1 of each), the first five are listed alphabetically.

not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.
"""

import re
import operator
import string
from collections import Counter


def check_room(room):
    real = False

    name, sector_id, checksum = get_rooms_data(room)

    def own_cmp(a,b):
        if string.ascii_lowercase.index(b[0]) > string.ascii_lowercase.index(a[0]):
            if a[1] == b[1]:
                return -1
        return 0

    c = Counter(name)

    m_c = c.most_common()
    m_c.sort(own_cmp)

    l_more_than_1 = ''.join(x[0] for x in m_c if x[1] > 1)
    l_less_than_2 = ''.join(sorted((x[0] for x in m_c if x[1] < 2)))

    my_check = l_more_than_1[:len(checksum)] + l_less_than_2[:len(checksum)-len(l_more_than_1[:len(checksum)])]

    if checksum == my_check:
        real = True

    # print("{:80} is{} a real room".format(room.replace('\n',''), ' not' if not real else ''))
    return real, sector_id


def get_rooms_data(room):

    m = re.match('([a-z-]+)(\d+)\[([a-z]+)\]', room)

    name = m.group(1).replace('-','')
    sector_id = m.group(2)
    checksum = m.group(3)

    return name, sector_id, checksum


def main():
    sum_of_ids = 0

    with open('day_4_data.txt', 'r') as room_list:
        for room in room_list:

            ys, addition = check_room(room)
            if ys:
                sum_of_ids += int(addition)

    print('Sum of valid rooms\' ids is {}'.format(sum_of_ids))



if __name__ == '__main__':
    main()

    def test():
        check_room('aaaaa-bbb-z-y-x-123[abxyz]')
        check_room('a-b-c-d-e-f-g-h-987[abcde]')
        check_room('not-a-real-room-404[oarel]')
        check_room('totally-real-room-200[decoy]')

