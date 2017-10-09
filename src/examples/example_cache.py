from functools import lru_cache
from urllib.error import HTTPError
from urllib.request import urlopen

@lru_cache(maxsize=32)
def get_pep(num):
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urlopen(resource) as s:
            return s.read()
    except HTTPError:
        return 'Not Found'

if __name__ == '__main__':
    for n in [8, 290, 308, 320]*2 + [9991]:
        pep = get_pep(n)
        print(n, len(pep))

    print(get_pep.cache_info())
