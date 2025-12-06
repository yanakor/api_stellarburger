import random
import string

def generate_password(lenght):
    case = string.ascii_letters
    random_string = ''.join(random.choice(case) for _ in range(lenght))
    return random_string
