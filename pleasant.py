import sys
from typing import List
from typing.io import TextIO

LEFTHAND = frozenset('12345qwertasdfgzxcvb')


def left_right(dictionary: TextIO) -> List[str]:
    works = []
    for word in dictionary:
        word = word.lower().strip()
        left = word[0] in LEFTHAND
        for c in word[1:]:
            if (c in LEFTHAND) == left:
                break
            else:
                left = not left
        else:
            works.append(word)
    return works


def one_hand(dictionary: TextIO) -> List[str]:
    works = []
    for word in dictionary:
        word = word.lower().strip()
        left = word[0] in LEFTHAND
        for c in word[1:]:
            if (c in LEFTHAND) != left:
                break
        else:
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
