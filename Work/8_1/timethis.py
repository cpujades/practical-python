# timethis.py


def timethis(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__module__}.{func.__name__}: {end - start}")

        return result

    return wrapper
