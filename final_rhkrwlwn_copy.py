import csv
f = open("result.csv", "r", encoding="utf-8")

def test_func(*args):
    print(len(args))


class TestClass:
    def __init__(self, *args):
        self.args = args

        for arg in range(len(args)):
            globals()