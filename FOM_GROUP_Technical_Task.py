# Написать декоратор который позволит вызывать функцию с альтернативными названиями параметров:
# Написать декоратор который кеширует любую функцию,
# если эта функция уже вызывалась с такими параметрами


def cache_results(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper


if __name__ == '__main__':
    add_two(a=4, b=5)