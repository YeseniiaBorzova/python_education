
"""Trying to implement simple python functions"""


def list_benefits():

    """This function returns list of hardcoded strings"""

    strings = ["More organized code", "More readable code", "Easier code reuse",
               "Allowing programmers to share and connect code together"]
    return strings


def build_sentence(benefit):

    """This function adds phrase is a benefit to your string"""

    return benefit + " is a benefit of functions!"


def name_the_benefits_of_functions():

    """This function checks work of two functions:
    list_benefits() and build_sentence()"""

    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


name_the_benefits_of_functions()
