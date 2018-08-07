import sys
from typing import List
from typing.io import TextIO

LEFTHAND = set(
    ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
)
RIGHTHAND = set(['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'])


def left_right(dictionary: TextIO) -> List[str]:
    works = []
    for i in dictionary:
        word = i.strip()
        if word[0] in LEFTHAND:
            hand = LEFTHAND
        else:
            hand = RIGHTHAND
        found = True
        for letter in word:
            if letter in hand:
                if hand == LEFTHAND:
                    hand = RIGHTHAND
                else:
                    hand = LEFTHAND
            else:
                found = False
                break
        if found:
            works.append(word)
    return works


def one_hand(dictionary: TextIO) -> List[str]:
    works = []
    for i in dictionary:
        word = i.strip()
        if word[0] in LEFTHAND:
            hand = LEFTHAND
        else:
            hand = RIGHTHAND
        found = True
        for letter in word:
            if letter not in hand:
                found = False
                break
        if found:
            works.append(word)
    return works


def print_words(words: List[str]) -> None:
    words.sort(key=len)
    for word in words:
        if len(word) >= 4:
            print(word)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(f'usage: {sys.argv[0]} /path/to/dict')
        sys.exit(-1)
    for dictionary in sys.argv[1:]:
        print_words(left_right(open(dictionary)))
        print_words(one_hand(open(dictionary)))
