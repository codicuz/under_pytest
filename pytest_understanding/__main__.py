import pytest_understanding as pu

def main():
    g = pu.SomeClass()

    print(g.greatings())
    print(g.greatings('Bob'))


if __name__ == '__main__':
    main()