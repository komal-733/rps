import random
def play(user,win,lose,draw):
  
  comp=random.choice(["rock","paper","scissor"])
  
  if user == "rock":
    if comp == "rock":
      result = "draw"
      draw += 1
    elif comp == "paper":
      result = "lose"
      lose += 1
    else:
      result = "win"
      win += 1
      
  elif user == "paper":
    if comp == "rock":
      result = "win"
      win += 1
    elif comp == "paper":
      result = "draw"
      draw += 1
    else:
      result = "lose"
      lose += 1
      
  else:
    if comp == "scissor":
      result = "draw"
      draw += 1
    elif comp == "rock":
      result = "lose"
      lose += 1
    else:
      result = "win"
      win += 1
      
  return [result,win,lose,draw,comp]

print("Let's play".center(50))

choice=1
w=l=d=0
while(choice):
  user=input("\nEnter rock paper scissor\n")
  r,w,l,d,c=play(user,w,l,d)
  print(f"Computer choose : {c}")
  print(f"\nYou {r}\n")
  print(f"win = {w}\t lose = {l} draw = {d}")
  choice=int(input("1: continue\t\t0: exit\n"))