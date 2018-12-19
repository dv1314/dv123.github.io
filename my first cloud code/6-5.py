import random, easygui
secret = random.randint(1,99)
guess = 0
tries = 0
easygui.msgbox("""Aha,DV,hou are you these days??? please enter an interger .""")
while guess != secret and tries < 6:
    guess = easygui.integerbox("what is your guess ??,dv")
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + "is too low,you stubid !!!")
    elif guess > secret:
        easygui.msgbox(str(guess) + "is too high,you are a fool!!")
    tries = tries + 1
if guess == secret:
    easygui.msgbox("oh you are so cute!!!you got it!!!")
else:
    easygui.msgbox("you are a stubid!!!")
