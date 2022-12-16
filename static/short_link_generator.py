import random
import string


def link_generator(link):
    letters = string.ascii_letters
    digits = '1234567890'
    lst = []
    for i in range(3):
        lst.append(random.choice(letters))
        lst.append(random.choice(digits))
    random.shuffle(lst)
    short_link = ''.join(lst)
    return [link, short_link]
