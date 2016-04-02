#! /usr/bin/python3


def printer():

    counter = 0
    while True:
        string = (yield)
        print('[{0}] {1}'.format(counter, string))
        counter += 1

if __name__ == '__main__':
    p = printer()
    next(p)
    p.send('Hi')
    p.send('My name is hsfzxjy.')
    p.send('Bye!')
