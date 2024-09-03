import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print(f"Time take by function {end_time - start_time}")

    return wrapper()


@time_decorator
def test_ui_1():
    print("Add a function, time taken by this fucntion")
    time.sleep(2) # wait for 2 seconds


@time_decorator
def test_ui_2():
    print("Add a function, time taken by this fucntion")
    time.sleep(5)
