from typing import List

LEFTHAND = set(['q', 'w', 'e', 'r', 't', 'a', 's',
                'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'])
RIGHTHAND = set(['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'])


def left_right() -> List[str]:
    works = []
    for i in open('/usr/share/dict/words'):
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


def one_hand() -> str:
    works = []
    for i in open('/usr/share/dict/words'):
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
    print_words(left_right())
    print_words(one_hand())
