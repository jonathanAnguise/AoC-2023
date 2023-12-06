import re
def check_game(input, max_red=12, max_green=13, max_blue=14):
    with open(input, "r") as f:
        index = 0
        res = 0
        res2 = 0
        regex_red = "(\d+) red"
        regex_green = "(\d+) green"
        regex_blue = "(\d+) blue"
        rr = re.compile(regex_red)
        rg = re.compile(regex_green)
        rb = re.compile(regex_blue)
        lines = f.readlines()
        for line in lines:
            max_red = 0
            max_green = 0
            max_blue = 0
            index += 1
            are_sets_valid =  []
            sets = line.split(";")
            for set in sets:
                count_red = sum([int(match) for match in re.findall(rr, set)])
                count_green = sum([int(match) for match in re.findall(rg, set)])
                count_blue = sum([int(match) for match in re.findall(rb, set)])
                if count_blue > max_blue:
                    max_blue = count_blue
                if count_green > max_green:
                    max_green = count_green
                if count_red > max_red:
                    max_red = count_red
                if not (count_red <= max_red and count_green <= max_green and count_blue <= max_blue):
                    are_sets_valid.append(False)
                    break
                else:
                    are_sets_valid.append(True)
            if False in are_sets_valid:
                continue
            else:
                res+= index
            res2 += (max_blue * max_green * max_red)
        print(res)
        print(res2)

check_game("input1")

