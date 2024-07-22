

def cutom_exceptions():

    try:
        custom_int = 5
        if custom_int / 1:
           print(custom_int)
        spam = spam * 5
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print('else')
    finally:
        print('kkdfff')


if __name__ == '__main__':
    cutom_exceptions()