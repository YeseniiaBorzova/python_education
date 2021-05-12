
"""Working with functions with multiple arguments"""


# edit the functions prototype and implementation
def foo(a, b, c, *args):

    """This function returns amount od *args"""

    return len(args)


def bar(a, b, c, **kwargs):

    """This function checks whether magic number equals 7 or not"""

    return kwargs["magic_number"] == 7


if foo(1, 2, 3, 4) == 1:
    print("Good.")

if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")

if not bar(1, 2, 3, magic_number=6):
    print("Great.")

if bar(1, 2, 3, magic_number=7):
    print("Awesome!")
