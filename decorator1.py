#function decorator

import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs): #should contain the number of arguments the function has
        print('start')
        result=func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@start_end_decorator
def add(x):
    return x+5

def main():
    result=add(5)
    print(result)

    print(help(add))
    print(add.__name__)

if __name__ == "__main__":
    main()