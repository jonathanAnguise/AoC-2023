answer = 0
with open("input2") as f:
   lines = f.read().strip().split("\n")

for line in lines:
    res = 0
    lin = line.split()
    set_delimiter = line.split().index("|")
    set1 = set(line.split()[2:set_delimiter])
    set2 = set(line.split()[set_delimiter+1:])
    len_set = len(set1 & set2)
    res=2**(len_set - 1) if len_set > 0 else 0
        
    answer+=res
print(answer)
