import re

def clean_with_overlap(input)
    with open(input,"r") as my_text:
        content = my_text.readlines()
    return content

def elves_trebuchet_solver(input):
        res=0
        for line in clean_with_overlap(input):
            numbers_array = "".join(filter(str.isdigit, line))
            res_str = str(numbers_array[0])+ str(numbers_array[-1])
            res+=int(res_str)
    return res

#print(elves_trebuchet_solver("input2"))




