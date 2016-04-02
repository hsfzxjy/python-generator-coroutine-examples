from sleep import sleep
import runner


def task(name):
    print(name, 1)
    yield sleep(1)
    print(name, 2)
    yield sleep(2)
    print(name, 3)

if __name__ == '__main__':
    runner.run((task('hsfzxjy'), task('Jack')))
