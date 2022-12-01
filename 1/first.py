
with open("1/input.txt") as f:
  lines = f.readlines()
  count = []
  oneElf = 0
  for line in lines:
     if line.strip():
         oneElf += int(line)
     else:
         count.append(oneElf)
         oneElf = 0
  print(sorted(count)[-1])
  print(sorted(count)[-1] + sorted(count)[-2] + sorted(count)[-3])
  f.close()
  