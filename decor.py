from datetime import datetime


def time_me(f):
    def decorator(*args, **kwargs):
        args_str = ', '.join([repr(x) for x in args])
        kwargs_str = ', '.join(['{}={}'.format(k, repr(v)) for k, v in kwargs.items()])
        start_time = datetime.now()
        res = f(*args, **kwargs)
        print('{}: {}({}, {})'.format(datetime.now() - start_time, f.__name__, args_str, kwargs_str))
        return res
    return decorator



