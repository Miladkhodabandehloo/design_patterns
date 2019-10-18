from functools import wraps


def hi(function):
    wraps(function)

    def decorator():
        ret = function()
        return "hi " + ret

    return decorator


@hi
def test():
    return "test"


print(test())
