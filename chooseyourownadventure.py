print('''
      __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'   
             '\/'

Welcome to Treasure Island my nig!
Your mission is to find the treasure and spend it on the bitches down at the club.
But alas you've arrived at a crossroad.
''')

direction = input('Do you want to go left or right, my nigga?\n')
#this is to determine the direction left or right


if direction.lower() == "left":
    print('You come to a big ass lake. "That is one big ass lake", you remark outloud to yourself for some odd reason.')
#if user types left it should go to the next input in the sequence    
    wait_or_swim = input("Do you swim like a man or wait like a pussy?\n")
    if wait_or_swim.lower() == "wait":
                print("You decided to wait like the giant pussy you are and three magical doors appear in front of you." )
                #next line is to choose from the three doors
                three_doors = input('The doors are labeled: "He/Him", "They/Them", and "Xe/Xim".\nWhich door do you go through?\n')
                if three_doors.lower() == "he/him":
                    print("You win!")
                else:
                    print("God smites you for being a filthy infidel. YOU LOSE!")
    else:
                print("You get in the water and you are immediately molested to death by oily, gay mermen. YOU LOSE! (your innocence)")
#which way western man?
else:
    print("You fall into a hole and break your leg and shit your pants and die from dysentery and God sends you to hell and your parents\nhate you and your dog hates you and your boss hates you and")
#this is simply a barrier for the next code, less confusing that way me thinks
    



    