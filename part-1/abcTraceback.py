def a():
    print
    b()  # Call b()


def b():
    print('Start of b()')
    c()  # Call c()


def c():
    print('Start of c()')
    42 / 0


a()
