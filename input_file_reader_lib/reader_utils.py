"""
Random utilities that are used throughout the input reader libraries
"""


def untested_warning(keyword, option="blank"):
    """
    Prints out a warning for the given command
    command -- String
    """
    if option == "blank":
        print("Warning "+keyword+" is completely untested")
    else:
        print("Warning option "+option+" of "+keyword+" is completely untested")
    return


def missed_option(keyword, option):
    """
    Prints out warning for a missed option
    """
    print("Error missed option "+option+" of keyword "+keyword)
    return


def missed_keyword(keyword):
    """
    Prints out warning for a missed option
    """
    print("Error missed keyword "+keyword)
    return
