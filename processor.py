import random
import string


class UrlProcessor(object):
    def generate(self, size=7):
        letters = string.ascii_lowercase
        numbers = string.digits
        l = letters + numbers
        url = ''.join(random.choice(l) for _ in range(size))
        return url