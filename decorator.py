# function decorator


def start_end_decorator(func):
    def wrapper(
        *args, **kwargs
    ):  # should contain the number of arguments the function has
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result

    return wrapper


@start_end_decorator
def print_name():
    print("alec")


@start_end_decorator
def add(x):
    return x + 5


def main():
    print_name()
    result = add(5)
    print(result)


if __name__ == "__main__":
    main()
