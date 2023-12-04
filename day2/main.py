import re
def check_game(input, max_red=12, max_green=13, max_blue=14):
    with open(input, "r") as f:
        index = 0
        res = 0
        regex_red = "(\d+) red"
        regex_green = "(\d+) green"
        regex_blue = "(\d+) blue"
        rr = re.compile(regex_red)
        rg = re.compile(regex_green)
        rb = re.compile(regex_blue)
        lines = f.readlines()
        for line in lines:
            index += 1
            sets = line.split(";")
            #to continue here 
            count_red = sum([ int(match) for match in re.findall(rr, line)])
            count_green = sum([ int(match) for match in re.findall(rg, line)])
            count_blue = sum([ int(match) for match in re.findall(rb, line)])
            print(line)
            print(index, count_red, count_green, count_blue)
            
            if count_red <= max_red and count_green <= max_green and count_blue <= max_blue:
                res+= index
                print(f"{res:>20}")

        print(res)






check_game("input1")

