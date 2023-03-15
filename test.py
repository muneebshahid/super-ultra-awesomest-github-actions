from glob import glob


def test_func(x):
    return x + 1


def test_print_dir_contents(dir_: str):
    contents = glob(dir_ + "/*")
    for content in contents:
        print(content)


def do_random_stuff():
    from random import randint

    return randint(0, 100)


def setup_os():
    import os

    os.environ["TEST"] = "test"
