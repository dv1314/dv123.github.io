import easygui,random
secret = random.randint(1,99)
guess = 0
tries = 0
easygui.msgbox("""kadsdaa""")
while guess != secret and tries < 6:
    guess = easygui.integerbox("sdaasd")
    if not guess:break
    if guess < secret:
        easygui.msgbox(str(guess) + "is too low,you stubid!!,dv")
    elif guess > secret:
        easygui.msgbox(str(guess) + "is too high,dsfssdf")
    tries = tries + 1
if guess == secret:
    easygui.msgbox("dfsdfs")
else:
    easygui.msgbox("sda" + str(secret))
