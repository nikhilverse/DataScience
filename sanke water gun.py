#Snake water gun game
import random

rand_no = random.randint(1,3)

def win(user,computer):
#snake vs gun
    if user=="g" and computer=="s":
        return True
    elif user=="s" and computer=="g":
        return False
#water vs snake
    if user=="s" and computer=="w":
        return True
    elif user=="w" and computer=="s":
        return False
#gun vs water
    if user=="g" and computer=="w":
        return True
    elif user=="w" and computer=="g":
        return False

print("Computer's turn : Snake(s) , Water(w), gun(g)")
if rand_no==1:
    computer="s"
elif rand_no==2:
    computer="w"
else:
    computer="g"

user = input("Your turn : Snake(s) , Water(w), gun(g) : ").lower()
result = win(user,computer)
print(f"You choose : {user}")
print(f"computer choose : {computer}")
if result is None:
    print("DRAW!")
elif(result):
    print("you win!")
else:
    print("yu lose!")