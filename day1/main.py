import re

def elves_trebuchet_solver(input):
    with open(input) as my_text:
        content = my_text.readlines()

    my_regex1 = r".*?(\d).*(\d).*$"
    my_regex2 = r"todo"
    for line in content:
