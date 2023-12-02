import re

def elves_trebuchet_solver(input):
    with open(input) as my_text:
        content = my_text.readlines()

    #my_regex1 = r".*?(\d).*(\d).*$"
    #my_regex2 = r"todo"
    res=0
    for line in content:
        numbers_array = [char for char in content if char.isdigit()]
        
        res_array = numbers_array[0] + numbers_array[-1]
        if len(numbers_array)>=1:




