"""
--- Day 7: Internet Protocol Version 7 ---

While snooping around the local network of EBHQ, you compile a list of IP
addresses (they're IPv7, of course; IPv6 is much too limited).
You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA.
An ABBA is any four-character sequence which consists of a pair of two
different characters followed by the reverse of that pair, such as xyyx or abba.
However, the IP also must not have an ABBA within any hypernet sequences,
which are contained by square brackets.

For example:

abba[mnop]qrst supports TLS (abba outside square brackets).

abcd[bddb]xyyx does not support TLS (bddb is within square brackets,
even though xyyx is outside square brackets).

aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior
characters must be different).

ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets,
even though it's within a larger string).

How many IPs in your puzzle input support TLS?
"""
import re


def main():
    counter = 0

    with open('day_7_data.txt', 'r') as data:
        for da in data:

            is_found_in_brackets = False
            is_found_in_text = False

            pattern = re.compile(r'(\w)(\w)\2\1')

            da = da.replace('\n', '')
            in_brackets = re.findall(r'\[(\w+)\]', da)

            for i in in_brackets:
                s = re.search(pattern, i)
                if s is not None:
                    if s.group(0)[0] != s.group(0)[1]:
                        is_found_in_brackets = True
                        break
                da = da.replace('['+i+']', ' ')

            if is_found_in_brackets:
                continue

            da = da.split(' ')

            for x in da:
                found = re.search(pattern, x)
                if found is not None:
                    if found.group(0)[0] != found.group(0)[1]:
                        is_found_in_text = True
                        break

            if is_found_in_text:
                counter += 1

    return counter


if __name__ == '__main__':
    print('There are {} IPs which support TLS'.format(main()))



"""
    There are 105 IPs which support TLS
"""
