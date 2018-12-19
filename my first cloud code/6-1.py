import easygui

flavor = easygui.choicebox("what is your favorite flavor ??",choices = ['vanilla','chocolate','strawberry'])

easygui.msgbox("you choose;"+flavor)
