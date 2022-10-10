import random
import string


def link_generator(link):
    letters = string.ascii_lowercase
    lst = []
    for i in range(5):
        lst.append(random.choice(letters))
    short_link = ''.join(lst)
    return [link, short_link]
