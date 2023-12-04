import regex as re

def clean(a):
    if a == "one":
        return "1"
    elif a == "two":
        return "2"
    elif a == "three":
        return "3"
    elif a == "four":
        return "4"
    elif a == "five":
        return "5"
    elif a == "six":
        return "6"
    elif a == "seven":
        return "7"
    elif a == "eight":
        return "8"
    elif a == "nine":
        return "9"
    else:
        return a
def clean_with_overlap(input, no_text=False):
    with open(input,"r") as my_text:
        content = my_text.readlines()
        if no_text:
            regex=("[0-9]")
        else:
            regex=("one|two|three|four|five|six|seven|eight|nine|[0-9]")
        r = re.compile(regex)
        count=0
        for line in content:
            match=r.findall(line, overlapped=True)
            res = [match[0],match[-1]]
            res_clean = [clean(a) for a in res]
            result =res_clean[0] + res_clean[-1]
            count+= int(result)
        print(count)

clean_with_overlap("input2")
clean_with_overlap("input2", no_text=True)


