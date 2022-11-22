import random
from colorama import Fore, Back, Style

# CREATOR --> MARTIN BARRIOS

# GITHUB  --> Marrtyb15

green = Fore.GREEN
red = Fore.RED
off = Style.RESET_ALL


list=[[1,2,3],[4,5,6],[7,8,9]]

player = " O "
ai = " X "
block = False
turn = player
count = 0

#{}dictionary- key & value
table = {"1": '   ',
         "2": '   ', 
         "3": '   ', 
         "4": '   ', 
         "5": '   ', 
         "6": '   ', 
         "7": '   ', 
         "8": '   ',
         "9": '   '
        }
table_example = {"1": ' 1 ',
         "2": ' 2 ', 
         "3": ' 3 ', 
         "4": ' 4 ', 
         "5": ' 5 ', 
         "6": ' 6 ', 
         "7": ' 7 ', 
         "8": ' 8 ',
         "9": ' 9 '
        }



def switch_color(pos1, pos2, pos3, color):
    if color == player:
      color = green
    else:
      color = red
    table[pos1] = color + table[pos1] + off
    table[pos2] = color + table[pos2] + off
    table[pos3] = color + table[pos3] + off
  # print_table()
    
  

def reset_table(t): 
  for i in t:
    t[i] = "   "


def print_table(tab):
  # if win == None:
    print("")
    print(tab['1'] + "|" + tab['2'] + "|" +tab['3'])
    print("---+---+---")
    print(tab['4'] + "|" + tab['5'] + "|" +tab['6'])
    print("---+---+---")
    print(tab['7'] + "|" + tab['8'] + "|" +tab['9'])
    print("")

  # elif win == "top-row":
  #   print("")
  #   print(table['1'] + "|" + table['2'] + "|" +table['3'])
  #   print("---+---+---")
  #   print(table['4'] + "|" + table['5'] + "|" +table['6'])
  #   print("---+---+---")
  #   print(table['7'] + "|" + table['8'] + "|" +table['9'])
  #   print("")


  



def ai_check():
  global block
  global count

  #UNCOMMENT FOR EXTRA HARD
  
  if count != 0 and table["5"] == "   ":
    return "5"
  
  
  #top row
  if table["1"] == table["2"] != "   " and table["3"] == "   " :
    # block = True
    return "3"
  elif table["1"] == table["3"] != "   " and table["2"] == "   ":
    # block = True
    return "2"
  elif table["2"] == table["3"]!= "   "  and table["1"] == "   ":
    # block = True
    return "1"

  #middle row
  if table["4"] == table["5"] != "   " and table["6"] == "   ":
    # block = True
    return "6"
  elif table["4"] == table["6"] != "   " and table["5"] == "   ":
    # block = True
    return "5"
  elif table["6"] == table["5"] != "   " and table["4"] == "   ":
    # block = True
    return "4"

  #bottom row
  if table["7"] == table["8"] != "   " and table["9"] == "   ":

    # block = True
    return "9"
  elif table["7"] == table["9"] != "   " and table["8"] == "   ":
    # block = True
    return "8"
  elif table["8"] == table["9"] != "   " and table["7"] == "   ":
    # block = True
    return "7"
    
  # left column
  if table["1"] == table["4"] != "   " and table["7"] == "   ":
    # block = True
    return "7"

    
  elif table["1"] == table["7"] != "   " and table["4"] == "   ":
    # block = True
    return "4"
  elif table["4"] == table["7"] != "   " and table["1"] == "   ":
    # block = True
    return "1"

  #middle column
  if table["2"] == table["5"] != "   " and table["8"] == "   ":
    # block = True
    return "8"
  elif table["2"] == table["8"] != "   " and table["5"] == "   ":
    # block = True
    return "5"
  elif table["5"] == table["8"] != "   " and table["2"] == "   ":
    # block = True
    return "2"
    
  #right column
  if table["3"] == table["6"] != "   " and table["9"] == "   ":
    # block = True
    return "9"
  elif table["3"] == table["9"]  != "   " and table["6"] == "   ":
    # block = True
    return "6"
  elif table["6"] == table["9"] != "   " and table["3"] == "   ":
    # block = True
    return "3"
  
  #diagonal left to top right
  if table["7"] == table["5"] != "   " and table["3"] == "   ":
    # block = True
    return "3"
  elif table["7"] == table["3"] != "   " and table["5"] == "   ":
    # block = True
    return "5"
  elif table["3"] == table["5"] != "   " and table["7"] == "   ":
    # block = True
    return "7"
    
  #diagonal left to bottom right
  if table["1"] == table["5"] != "   "and table["9"] == "   ":
    # block = True
    return "9"
  elif table["1"] == table["9"] != "   "and table["5"] == "   ":
    # # block = True
    return "5"
  elif table["5"] == table["9"] != "   "and table["1"] == "   ":
    # # block = True
    return "1"
    
print_table(table_example)



def game():
  global block
  global player
  global ai 
  global turn 
  global count
  
  while True:
    character = input("Would you like to be X or O :").upper()
    if character == "X":
      player = " X "
      ai = " O "
      break
    elif character == "O":
      player = " O "
      ai = " X "
      break
    else: continue
    



  first = random.randrange(2)
  if first == 1:
    turn = player
  else: 
    turn = ai
  
  while True:
    if turn == player:
      try:
        position = input( "Enter a position :")
        if position == "q":
          break
        elif table[position] == "   ":
          print(table[position]) #=====
          table[position] = turn
          count += 1
          print_table(table)
        else: continue
      except:
        continue
    elif turn == ai:
      input("Press Enter...")
      while True:
        position = str(random.randrange(1,10))
        x = ai_check()
        try:
          # print("---",x)
          if x != None:       #--------
           
            table[x] = turn
            count += 1
            # block = False
            print_table(table)
            break  
          elif table[position] == "   ":
            table[position] = turn
            count += 1
            print_table(table)
            break
          else: 
            continue
            
        except:
          continue
  
  
    
    if table["1"] == table["2"] == table["3"] != "   ":    #!=not
      print(turn, "wins")
      switch_color("1", "2", "3",  turn)
      break
      
    elif table["4"] == table["5"] == table["6"] != "   ":    
      print(turn, "wins")
      switch_color("4", "5", "6",  turn)
      break
      
    elif table["7"] == table["8"] == table["9"] != "   ":    
      print(turn, "wins")
      switch_color("7", "8", "9", turn)
      break
  
    elif table["1"] == table["4"] == table["7"] != "   ":    
      print(turn, "wins")
      switch_color("1", "4", "7", turn)
      break
  
    elif table["2"] == table["5"] == table["8"] != "   ":    
      print(turn, "wins")
      switch_color("2", "5", "8",  turn)
      break
  
    elif table["3"] == table["6"] == table["9"] != "   ":
      print(turn, "wins")
      switch_color("3", "6", "9",turn)
      break
  
    elif table["1"] == table["5"] == table["9"] != "   ":
      print(turn, "wins")
      switch_color("1", "5", "9", turn)
      break
  
    elif table["3"] == table["5"] == table["7"] != "   ":
      print(turn, "wins")
      switch_color("3", "5", "7", turn)
      break

    if count == 9:
      print("It's a cat's game")
      break
    
    
    if turn == ai:
      turn = player
    elif turn == player:
      turn = ai
  print_table(table)

game()
while True:
  again = input("\nWould you like to play again y/n...").upper()
  if again == "Y" or again == "YES":
    reset_table(table)
    count = 0
    game()
  elif again == "N" or again == "NO":
    break

# Error handling
#try and except 
#when anytho other than a valid integer is input the game crashes 
# json files
# file handling 

#---------------------------NOTE-----------------------------------------
# I made the ai smarter by chagning the condition
# I did this by removing some code and nothing else
# Instead of checking if the two adjecent values are equal to the player variable it now checks if the values are equal to one another.
# It stills checks if the third value is equal to 3 spaces (vacant).
# If the conditions are met the ai will place make its next move there

# now that we are only checking if the adjacent values are equal to one another it is possible that both those values are the ai moves and the ai will move the the third position to get three in a row and win. 

#ADD if space taken print board and change color of position. 