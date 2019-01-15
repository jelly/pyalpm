import resource
import gc

from pyalpm import Handle
from pycman.config import init_with_config


def memory():
    gc.collect()
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f'memory {r}')
    return r


def alpm_things():
    #h = init_with_config('/etc/pacman.conf')
    a = 0
    h = Handle('/', '/var/lib/pacman')


def main():
    old = memory()
    alpm_things()
    new = memory()
    print(new-old)


if __name__ == "__main__":
    main()
