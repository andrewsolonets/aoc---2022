
# first star
with open("2/input.txt") as f:
  lines = f.readlines()
  score = 0
  for line in lines:
    move = line.strip()
    if(move[0] == "A" and move[2] == "Z" ):
      # print("rock vs scissors - lost")
      score+=3
    if(move[0] == "A" and move[2] == "Y"):
      # print("rock vs paper - won")
      score+=8
    if(move[0] == "A" and move[2] == "X"):
      # print("rock vs rock - draw")
      score+=4
    if(move[0] == "B" and move[2] == "X"):
      # print("paper vs rock - lost")
      score+=1
    if(move[0] == "B" and move[2] == "Z"):
      # print("paper vs scissors - won")
      score+=9
    if(move[0] == "B" and move[2] == "Y"):
      # print("paper vs paper - draw")
      score+=5
    if(move[0] == "C" and move[2] == "X"):
      # print("scissors vs rock - won")
      score+=7
    if(move[0] == "C" and move[2] == "Y"):
      # print("scissors vs paper - lost")
      score+=2
    if(move[0] == "C" and move[2] == "Z"):
      # print("scissors vs scissors - draw")
      score+=6
  print(score)

pointsForOutcome = {
  "X":0,
  "Y":3,
  "Z":6
}

moveSecond = {
  "X":2,
  "Y":1,
  "Z":0
}

pointsForSigns = {
  "rock":1,
  "paper":2,
  "scissors":3
}

rightMove = {
  "A": ["paper","rock","scissors"],
  "B": ["scissors","paper","rock"],
  "C":["rock","scissors","paper"]
}

print(rightMove["A"][0])



# second star
with open("2/input.txt") as f:
  lines = f.readlines()
  score = 0
  for line in lines:
    move = line.strip()
    curMoveIndex = rightMove[move[0]][moveSecond[move[2]]]
    cur = pointsForSigns[curMoveIndex] + pointsForOutcome[move[2]]
    score+=cur
  print(score)
    


# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
  
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock

# Scoring: shape (1 for X (Rock), 2 for Y (Paper), and 3 for Z(Scissors)) + outcome (0 if you lost, 3 if the round was a draw, and 6 if you won) 

# A for Rock, B for Paper, and C for Scissors you: X for Rock, Y for Paper, and Z for Scissors