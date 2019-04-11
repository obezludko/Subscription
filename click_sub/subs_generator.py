import random

"""This script generate pseudo random subs,
   that will be used in click get request
"""


def generate_sub(sub_gen='sub value'):
    sub_gen = str(sub_gen)
    random_int = random.randint(1, 9999999)
    random_sub = str(random_int) \
                 + ' ' + sub_gen + \
                 ' ' + str(random_int)
    return random_sub
