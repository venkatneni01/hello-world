import modulea
from modulea import dummy_b, dummy_int
from dummy_pkg.dummy_modulea import dummy_func

if __name__ == '__main__':
    modulea.dummy_a()
    dummy_b()
    dummy_func()