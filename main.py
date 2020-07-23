print("Congratulations! You have been selected to start a delecious new LIVE TUNA FISH FARM! This is a privilage because there are only a few locations that can hold this fish.")

def fishnumberselection(fish):
  if fish < 5 or fish >=15:
    if fish == 1:
      print("ok it would be better if u got more")
    
    if fish == 2:
      print("ok boomer")

    if fish == 3:
      print("MOOOOOOORE")

    if fish == 4:
      print("MOOOOOOOOOOOOORE")

    if fish == 5:
      print("meh")
    
    if fish >= 15:
      print("THATS TOO MANY BOI'S")

    x = int(input("enter 1-5 fish or more: "))
    fishnumberselection(x)  


  if fish > 5 and fish < 15:
    print("oh yeah baby oh shriplllllle")
  
  return

x = int(input("How many do u want to start out with? "))
fishnumberselection(x)

print("ok now that u have your big bois u should get some bait fish for food, ")


def bfishnumber(bfish):
  if (bfish + x) < 40:
    print('yaaas')
  if (bfish + x) > 40:
    print ("not enough space")


y = int(input("How many bait fish do u want? "))
bfishnumber(y)

print("your tuna seem healthy, great job!")


