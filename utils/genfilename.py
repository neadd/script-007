"""Service module for filename generation"""
import random
import string


def genfilename(size):
    """ generate file name if <size> alphanumeric chars""" 
    return ''.join(random.choice(string.ascii_letters+string.digits)
                   for _ in range(size))
