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
            are_sets_valid =  []
            sets = line.split(";")
            for set in sets:
                count_red = sum([int(match) for match in re.findall(rr, set)])
                count_green = sum([int(match) for match in re.findall(rg, set)])
                count_blue = sum([int(match) for match in re.findall(rb, set)])
                if not (count_red <= max_red and count_green <= max_green and count_blue <= max_blue):
                    are_sets_valid.append(False)
                    break
                else:
                    are_sets_valid.append(True)
            if False in are_sets_valid:
                continue
            else:
                res+= index
        print(res)

check_game("input1")

