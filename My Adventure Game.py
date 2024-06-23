name = input("type your name :-) \n~~>")
print("welcome",name,"to my adventure world")
ans = input('You hav to run away from tiger he is chasing you; now the way is divide into two different path chose \na) LEFT \nb) RIGHT\n').lower()

if ans == "a":
    ans = input('you have come to river, now you have 2 options\n a) go from brige \n b) go by swimming \n==>').lower()
    if ans == 'a':
        ans == input("you walk for many hours now you again have two option\na) climb mountain\nb) go form the cave\n ~~> ").lower()
        if (ans == 'a'):
            print('''the tiger could'nt climb the mountain you are safe now {^_^} :)''')
        elif (ans == 'b'):
            print('you get eaten by lion inside the cave :( \n you died...:(')
        else:
            print('invalide option.. plz try again,..')
    elif ans == 'b':
        print("OPPS you are eaten by CROCODILE :( \n You died..")
    else:
        print('invalide option, plz try again..')
elif ans == "b":
    ans = input("you again meet two different path \na) go left\nb) go right \n ==>").lower()
    if(ans == 'a'):
        print('dead-end,bad luck :( you died..')
    elif(ans == 'b'):
        print("Now you are safe now you got your friend and your firend have gun")
    else:
        print('invalide option, plz try again..')
else:
        print('invalide option, plz try again..')

print('thank you for playing game\n Hope you like the game have a great day..(^_^)')