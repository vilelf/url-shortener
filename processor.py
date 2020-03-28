import os
import random
import string


class UrlProcessor(object):
    def generate(self, size=7):
        letters = string.ascii_lowercase
        numbers = string.digits
        l = letters + numbers
        short = ''.join(random.choice(l) for _ in range(size))
        url = os.path.join(os.environ['ROOT_URL'], short)
        return url
