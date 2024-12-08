res = 0

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

def is_safe(report):
    variation = report[1] > report[0]
    if variation:
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            if not 1 <= diff <= 3:
                return False
        return True
    else:
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            if not -1 >= diff >= -3:
                return False
        return True

def is_dampered_safe(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True
    return False

for line in lines:
    report = [int(i) for i in line.split()]
    res += is_dampered_safe(report)

print(res)
