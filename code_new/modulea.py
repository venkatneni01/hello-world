dummy_int = 56
dummy_str = 'dummy_str'
dummy_bool = True
dummy_float = 12.6

def dummy_a():
    print('dummy_a')
    dummy_int1 = 11
    global dummy_int
    print(dummy_int1)
    print(dummy_int)
    dummy_int = 69
    print(dummy_int)
    # print('hello world')

def dummy_b():
    print('dummy_b')
    print(dummy_int)

if __name__ == '__main__':
    dummy_b()
    dummy_a()
    