def getRangeElf(num1:str,num2:str):
  finalRange = set()
  for i in range(int(num1),int(num2)+1):
    finalRange.add(i)
  return finalRange

with open("4/input.txt") as f:
  pairs = 0
  lines = f.readlines()
  for line in lines:
    numList = line.split(",")
    numListFinal = []
    for num in numList:
      oneElf = num.split("-")
      for num in oneElf:
        numListFinal.append(num)
    finalList1 = getRangeElf(numListFinal[0],numListFinal[1])
    finalList2 = getRangeElf(numListFinal[2],numListFinal[3])
    z = finalList1.intersection(finalList2)
    intersection = len(z)
    len1 = len(finalList1)
    len2 = len(finalList2)
    if(intersection == len2 or intersection == len1):
      pairs+=1
 
  print(pairs)