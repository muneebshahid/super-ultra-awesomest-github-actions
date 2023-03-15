from glob import glob


def test_func(x):
    return x + 1


def test_print_dir_contents(dir_: str):
    contents = glob(dir_ + "/*")
    for content in contents:
        print(content)


def test_func3(x):
    return x + 9
