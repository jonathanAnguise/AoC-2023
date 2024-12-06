<<<<<<< HEAD
with open("input2") as f:
   lines =  f.read().strip().split('\n')
my_dict = {i:0 for i in range(len(lines))}
print(my_dict)

for i,line in enumerate(lines):
  my_dict[i] += 1
  first, rest = line.split('|')
  rest_list = rest.split()
  card_list = first.split(':')[1].split()
  card_nums = [int(x) for x in card_list]
  rest_nums = [int(x) for x in rest_list]
  val = len(set(card_nums) & set(rest_nums))
  for j in range(val):
    my_dict[i+1+j] += my_dict[i]
print(sum(my_dict.values()))
=======
answer = 0
with open("input2") as f:
   lines = f.read().strip().split("\n")

res2_list = [ [0] for _ in range(len(lines))]

for i,line in enumerate(lines):
    res = 0
    lin = line.split()
    set_delimiter = line.split().index("|")
    set1 = set(line.split()[2:set_delimiter])
    set2 = set(line.split()[set_delimiter+1:])
    len_set = len(set1 & set2)
    print(len_set)
    for j in range(i+1, i+len_set+1):
        res2_list[i].append(j)

score = [1 for _ in range(len(lines))]

for i in range(len(lines)-1, -1, -1):
    for j in res2_list[i]:
        score[i] += score[j]

print(sum(score)/2)
>>>>>>> 5fa92a1 (day4: Finish part2)
