import random
import string
def genfilename(size):
    return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(size))