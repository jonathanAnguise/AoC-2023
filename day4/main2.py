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
