

def custom_lam():
    # lambda arguments: expression

    funct1 = lambda x: x * 2

    funct2 = lambda x, y: x * y

    funct3 = lambda x, y: x * y if x == 5 else x + y

    


    print(funct1(2))

    print(funct2(5, 6))

    print(funct3(5, 6))

    print(funct3(6, 5))


if __name__ == '__main__':
    custom_lam()