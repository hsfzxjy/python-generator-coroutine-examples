from functools import wraps
from future import Future


def _next(gen, future, value=None):

    try:
        try:
            yielded_future = gen.send(value)
        except TypeError:
            yielded_future = next(gen)

        yielded_future.set_callback(lambda value: _next(gen, future, value))
    except StopIteration as e:
        future.done(e.value)


def coroutine(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        future = Future()

        gen = func(*args, **kwargs)
        _next(gen, future)
        return future

    return wrapper
