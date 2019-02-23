import argparse

parser = argparse.ArgumentParser()


def add_arguments(array):
    for argument in array:
        parser.add_argument("--{}".format(argument))
    args = parser.parse_args()
    return args

