"""
--- Day 6: Signals and Noise ---

Something is jamming your communications with Santa.
Fortunately, your signal is only partially jammed, and protocol in situations
like this is to switch to a simple repetition code to get the message through.

In this model, the same message is sent repeatedly. You've recorded
the repeating message signal (your puzzle input), but the data seems
quite corrupted - almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each position.
For example, suppose you had recorded the following messages:

eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
The most common character in the first column is e;
in the second, a;
in the third, s, and so on.
Combining these characters returns the error-corrected message, easter.

Given the recording in your puzzle input, what is the error-corrected
version of the message being sent?
"""

from collections import Counter


def main():
    main_counter = [[] for _ in range(8)]

    message = ''

    with open('day_6_data.txt', 'r') as data:
        for da in data:
            da = da.replace('\n','')
            i = 0
            for d in da:
                main_counter[i].append(d)
                i += 1

    for m in main_counter:
        c = Counter(m)
        message += c.most_common(1)[0][0]

    return message


if __name__ == '__main__':
    print('The message is: {}'.format(main()))

"""
    The message is: qoclwvah
"""
