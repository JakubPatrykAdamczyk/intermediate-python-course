import random

def main():
  # print('You rolled a die')
  dice_roll=int(input('how many dice\n'))
  dice_size=int(input("how big dice\n"))
  dice_sum=0
  for i in range(0,dice_roll):
    roll=random.randint(1,6)
    dice_sum+=roll
    if roll==1:
      print(f"critcial fail you roll {roll}")
    elif roll==6:
      print(f"critcial succes you roll {roll}")
    else:
      print(f'You rolled a {roll}')
    
  print(f"total roll {dice_sum}")

if __name__== "__main__":
  main()