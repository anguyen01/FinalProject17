from random import randint

item = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
scene1 = []
inventory = {"gun": 0, "flashlight": 0, "water": 0, "cloak": 0, "fried meme dinner": 0, "knife": 0, "crippling depression": 0, "communist manifesto": 0, "bomb": 0, "crowbar": 0, "strange paper": 0, "matches": 0, "vegetals": 0}


# Picks a random scenario
def scene():
    x = randint(1, 30)
    if x == 1:
        scene1()
    elif x == 2:
        scene2()
    elif x == 3:
        scene3()
    elif x == 4:
        scene4()
    elif x == 5:
        scene5()
    elif x == 6:
        scene6()
    elif x == 7:
        scene7()
    elif x == 8:
        scene8()
    elif x == 9:
        scene9()
    elif x == 10:
        scene10()
    elif x == 11:
        scene11()
    elif x == 12:
        scene12()
    elif x == 13:
        scene13()
    elif x == 14:
        scene14()
    elif x == 15:
        scene15()
    elif x == 16:
        scene16()
    elif x == 17:
        scene17()
    elif x == 18:
        scene18()
    elif x == 19:
        scene19()
    elif x == 20:
        scene20()
    elif x == 21:
        scene21()
    elif x == 22:
        scene22()
    elif x == 23:
        scene23()
    elif x == 24:
        scene24()
    elif x == 25:
        scene25()
    elif x == 26:
        scene26()
    elif x == 27:
        scene27()
    elif x == 28:
        scene28()
    elif x == 29:
        scene29()
    elif x == 30:
        scene30()

# Adds an item
def obt():
    x = randint(1, 13)
    if x == 1:
        if inventory["gun"] == 1:
            obt()
        else:
            inventory["gun"] == 1
            print("Gun obtained!")
    elif x == 2:
        if inventory["flashlight"] == 1:
            obt()
        inventory["flashlight"] = 1
        print("Flashlight obtained!")
    elif x == 3:
        if inventory["water"] == 1:
            obt()
        inventory["water"] = 1
        print("Water obtained!")
    elif x == 4:
        if inventory["cloak"] == 1:
            obt()
        inventory["cloak"] = 1
        print("Cloak obtained!")
    elif x == 5:
        if inventory["fried meme dinner"] == 1:
            obt()
        inventory["fried meme dinner"] = 1
        print("Fried meme dinner obtained!")
    elif x == 6:
        if inventory["knife"] == 1:
            obt()
        inventory["knife"] = 1
        print("Knife obtained!")
    elif x == 7:
        if inventory["crippling depression"] == 1:
            obt()
        inventory["crippling depression"] = 1
        print("Crippling depression obtained!")
    elif x == 8:
        if inventory["communist manifesto"] == 1:
            obt()
        inventory["communist manifesto"] = 1
        print("Communist Manifesto obtained!")
    elif x == 9:
        if inventory["bomb"] == 1:
            obt()
        inventory["bomb"] = 1
        print("Bomb obtained!")
    elif x == 10:
        if inventory["crowbar"] == 1:
            obt()
        inventory["crowbar"] = 1
        print("Crowbar obtained!")
    elif x == 11:
        if inventory["strange paper"] == 1:
            obt()
        inventory["strange paper"] = 1
        print("Strange paper obtained!")
    elif x == 12:
        if inventory["matches"] == 1:
            obt()
        inventory["matches"] = 1
        print("Matches obtained!")
    elif x == 13:
        if inventory["vegetals"] == 1:
            obt()
        inventory["vegetals"] = 1
        print("Vegetals obtained!")

# Removes an item
def rem():
    x = randint(1, 13)
    if x == 1:
        inventory["gun"] = 0
        print("Gun lost!")
    elif x == 2:
        inventory["flashlight"] = 0
        print("Flashlight lost!")
    elif x == 3:
        inventory["water"] = 0
        print("Water lost!")
    elif x == 4:
        inventory["cloak"] = 0
        print("Cloak lost!")
    elif x == 5:
        inventory["fried meme dinner"] = 0
        print("Fried meme dinner lost!")
    elif x == 6:
        inventory["knife"] = 0
        print("Knife lost!")
    elif x == 7:
        inventory["crippling depression"] = 0
        print("Crippling depression lost!")
    elif x == 8:
        inventory["communist manifesto"] = 0
        print("Communist Manifesto lost!")
    elif x == 9:
        inventory["bomb"] = 0
        print("Bomb lost!")
    elif x == 10:
        inventory["crowbar"] = 0
        print("Crowbar lost!")
    elif x == 11:
        inventory["strange paper"] = 0
        print("Strange paper lost!")
    elif x == 12:
        inventory["matches"] = 0
        print("Matches lost!")
    elif x == 13:
        inventory["vegetals"] = 0
        print("Vegetals lost!")

# Asks the player if they want to restart after dying
def res():
    print("You have died.")
    response = input("Would you like to restart the game? ").lower()
    if response == "yes":
        run_game()
    elif response == "no":
        print("Ending game.")
        exit()

# Runs the game
def run_game():
    response = input("Welcome to Survival. In this game, you are a survivor in the wastelands. Your goal is to survive for 15 turns.\nAnswer choices are capitalized. Are you ready to play? ").lower()
    if response == "yes":
        print("Good. Let the game begin.")
    else:
        print("Tough.")
    for x in range(1,16):
        print(f"Turn {x}")
        scene()
        print(" ")
    print("You have survived!")
    exit()

# Defines every scenerio
def scene1():
    print("You have died of dysentery.")
    res()

def scene2():
    response = input("You are relaxing in your camp when you suddenly hear voices. You look outside to see a small group of bandits.\nDo you Defend or Hide? ").lower()
    if response == "defend":
        if inventory["gun"] == 1:
            print("You draw your gun and fire. You see a body fall to the ground and the other bandits running away.")
        else:
            print("You try your best to fend off the invaders, but you are eventually overpowered and killed.")
            res()
    elif response == "hide":
            print("You hide as the bandits rummage through your camp. You are safe, but the same can’t be said for your supplies.")
            rem()
    else:
        print("Invalid response. Try again.")
        scene2()

def scene3():
    response = input("As you wander the wasteland, you stumble upon an abandoned house. Do you Search the house or Ignore it? ").lower()
    if response == "search":
        if inventory["flashlight"] == 1:
            print("Using your flashlight, you rummage through the house. Huzzah! You found some items.")
            obt()
            obt()
        else:
            print("You try your best to search through, but it’s too dark. You can only find one item.")
            obt()
    elif response == "ignore":
        print("You don’t know what’s inside, and you aren’t going to find out. You decide to keep walking.")
    else:
        print("Invalid response. Try again.")
        scene3()

def scene4():
    response = input("While camping, you hear a strong wind. You look to find the source of the sound and find a dust storm\nheading your way. Do you take Shelter or Run? ").lower()
    if response == "shelter":
        if inventory["cloak"] == 1:
            print("You quickly pull out your cloak and cover yourself in it. The storm scrapes past you uncomfortably, but you’re ok for the most part.")
        else:
            print("You fling yourself onto the ground. The dust passes over you without any harm. But some of your items are destroyed.")
            rem()
            rem()
    elif response == "run":
        print("You attempt to run from the storm, but the storm sweeps by faster than your feet can take you.")
        res()
    else:
        print("Invalid response. Try again.")
        scene4()

def scene5():
    response = input("A man walks to your camp asking for supplies. You can’t help but notice his strange hairstyle.\nDo you Help the man, Refuse to help, or Insult his hair? ").lower()
    if response == "help":
        if inventory["water"] == 1:
            print("You give the man some supplies, including a bottle of water. The man is gureatoful for your help and gives you many items in return.")
            obt()
            obt()
            obt()
        else:
            print("You lack supplies but try your best to help the man. The man thanks you for your help and gives you some items.")
            obt()
            obt()
    elif response == "refuse":
        print("You could easily help the man out. But you refuse. The man leaves.")
    elif response == "insult":
        print("What did you say about his hair?! The man angrily punches you with a surprising amount of force. You shortly black out.")
        res()
    else:
        print("Invalid response. Try again.")
        scene5()

def scene6():
    response = input("During your travels, you find a plate of spaghetti laying on a table out in the open. Do you\nEat the spaghetti, Ignore it, or Inspect it? ").lower()
    if response == "eat":
        print("You pick up the fork and take a bite. It’s delicious. Suddenly, you hear a voice cry out behind you. ‘SOMEBODY TOUCHA MY SPAGHETT!’ Before you can turn around, your vision becomes dark.")
        res()
    elif response == "ignore":
        print("It’s obviously a trap. You continue to travel, leaving the spaghetti untouched.")
    elif response == "inspect":
        print("The plate of spaghetti is very suspicious. To find out its secrets, you punch it with all your might. Surprise! An item drops out of it. Somehow.")
        obt()
    else:
        print("Invalid response. Try again.")
        scene6()

def scene7():
    response = input("As you wander the land, you hear a sudden click as you take a step. An object springs up from the ground\nand explodes, sending what appears to be emeralds flying towards you. Do you Deflect the emeralds or Duck? ").lower()
    if response == "deflect":
        print("What!? There’s no way! No one can just deflect the emerald splash!")
    elif response == "duck":
        print("As you duck down, some of your items fall out of your pack. The emeralds easily pierce through them.")
        rem()
        rem()
    else:
        print("Invalid response. Try again.")
        scene7()

def scene8():
    response = input("As you wander in a building, you hear a rumble as the ground begins to shake. Suddenly, parts of the building\nbegin to collapse. Do you run to the Door or the Window? ").lower()
    if response == "door":
        if inventory["knife"] == 1:
            print("You run to the door, but your leg gets caught up in some wires. You quickly pull out your knife, cut through the wire,\nand escape the building.")
        else:
            print("You run to the door, but your leg gets caught up in some wires. You try to untangle your leg, but you are ultimately\ncrushed under the rubble.")
            res()
    elif response == "window":
        print("You run to the window, but an item falls out of your pack and is lost in the rubble.")
        rem()
    else:
        print("Invalid response. Try again.")
        scene8()

def scene9():
    response = input("A man approaches you during your travels. He asks you about your opinion on communism. Do you Agree or Disagree? ").lower()
    if response == "agree":
        if inventory["communist manifesto"] == 1:
            print("You pull out your copy of the Communist Manifesto. He sees that you are a man of culture as well and leaves you be.")
        else:
            print("You proclaim your love of communism, but he does not believe you. He proceeds to strangle you to death.")
            res()
    elif response == "disagree":
        print("You argue that death is a preferable alternative to communism. The man deems you a heretic and strangles you to death.")
        res()
    else:
        print("Invalid response. Try again.")
        scene9()

def scene10():
    response = input("You hear a strange voice call out to you. Do you Look towards the source, Run away, or try a Different option? ").lower()
    if response == "look":
        print("You look behind and see a small tank with a skull on it rushing towards you. As it approaches you, it immediately explodes.")
        res()
    elif response == "run":
        print("As you run away, many of your items fall out of your pack. You are too busy running away to care.")
        rem()
        rem()
        rem()
    elif response == "different":
        if inventory["matches"] == 1:
            print("You take out a match and start a fire nearby. The strange looking tank is drawn towards it.\nAs it is busy looking at the fire, you make your escape.")
            res()
        else:
            print("You try to start a fire, but have nothing to ignite. The tank approaches you and explodes.")
    else:
        print("Invalid response. Try again.")
        scene10()

def scene11():
    response = input("You wander an empty house. As you enter one of the rooms, you find a noose hanging from the ceiling.\nYou don’t know why, but you want to come closer. Do you walk Closer or Leave? ").lower()
    if response == "closer":
        print("You feel compelled to get closer to the noose. You slip it over your head. Everything around you becomes dark.")
        res()
    elif response == "leave":
        print("You fight back the forces and leave the room.")
    else:
        print("Invalid response. Try again.")
        scene11()

def scene12():
    response = input("In the middle of the night, you find a man standing under a streetlight. You don’t know why, but his appearance is very\nMENACING. Do you Watch the man or RUN AWAY? ").lower()
    if response == "watch":
        print("You continue to stare at the man. The man sprints towards you and lunges. He bites into your neck and starts to drink your blood.")
        res()
    elif response == "run":
        print("You were trained for scenarios like this. You even had a family technique. And that’s for you to rUN FOR YOUR LIFE.")
    else:
        print("Invalid response. Try again.")
        scene12()

def scene13():
    response = input("You wake up to find yourself tied to a chair. You are surrounded by men wearing yellow and black shirts. One of the men comes forward. He opens his mouth. 'According to all known laws of aviation…' ").lower()
    if response == "there is no way a bee should be able to fly. its wings are too small to get its fat little body off the ground. the bee, of course, flies anyway because bees don’t care what humans think is impossible.":
        print("The men are impressed by your knowledge and decide to release you.")
    else:
        print("The men are disgusted by your lack of culture and decide to end your life.")
        res()

def scene14():
    response = input("You hear distant screaming. You run towards a building and peer through a window. You see a man tied to a chair\nwith several men surrounding him. Do you Break in, Sneak in, or take a Different option? ").lower()
    if response == "break in":
        if inventory["gun"] == 1:
            print("You charge in, guns blazing, and fire at the men. You somehow manage to kill them all. After freeing the hostage,\nhe gives you an item in return.")
            obt()
        else:
            print("You charge in and are immediately gunned down.")
            res()
    elif response == "sneak in":
        if inventory["knife"] == 1:
            print("You sneak in and manage to take out all of the men silently. After freeing the hostage, he gives you a(n) <item> in return.")
            obt()
        else:
            print("You sneak into the building, but a man spots you and guns you down.")
            res()
    elif response == "different":
        if inventory["bomb"] == 1:
            print("You take your bomb out from your backpack. After lighting the fuze, you lob the bomb into the building. After a few seconds, you hear an explosion. You walk away triumphantly.\nYou don’t need to extract the hostage if the hostage is dead.")
        else:
            print("You reach into your bag to get the bomb before you realize that you’re not that operator. Grumpily, you walk away from the building.")
    else:
        print("Invalid response. Try again.")
        scene14()

def scene15():
    response = input("You find a bar in the middle of nowhere. You walk in and approach the bartender. You order a Nuka Cola because this is a G-rated workspace\nand those under the age of 21 are not legally allowed to consume alcohol. The bartender looks at you incredulously and asks who you are. ").lower()
    if response == "hey, i’m al capone, the famous mobster most people think that i’m a robber, but that’s not true. hey, don’t worry i will not kill you unless you give me a reason to they know that i’ve killed four, but they don’t know about anymore and i grew up poor now i’m making bank at my bootleg bar and i-i-i-i-i won’t stop unless the prohibition drops so next time that i ask you to go do something for me i expect you to just do it not for you to disagree. because getting rid of you that would be so easy remember i’m al capone and this is my speakeasy":
        print("The bartender is surprised and immediately apologizes for his rudeness. He quickly pours you a Nuka Cola and gives you\nmany itemsfor your travels.")
        obt()
        obt()
        obt()
    elif response == "cuck":
        print("The bartender is insulted by your rudeness. He shoots you in the face.")
        res()
    else:
        print("The bartender is still unsure of who you are and tells you to leave.")

def scene16():
    response = input("You find a poker table out in the middle of nowhere. A man is sitting there, asking you for a game. He says the loser gives up their soul.\nDo you Play or Refuse? ").lower()
    if response == "play":
        response = input("You decide to sit down for a game. The man smirks and deals out the cards. You pick up your hand. It’s so bad, you are certain that you’ve just contracted AIDS.\nYou are very sure that the man has rigged the game. Do you try to Bluff or do you Leave? ").lower()
        if response == "bluff":
            if inventory["crippling depression"] == 1:
                print("The man believes that you are bluffing, but your crippling depression hides all of your emotions. The man decides to fold and you win the game.")
            else:
                print("The man sees through your bluff and calls you out. You lose the game and your soul.")
                res()
        elif response == "leave":
            if inventory["gun"] == 1:
                print("You both reveal your cards. He has a four of a kind, kings, and a 5. However, you reveal your hand, which is a gun. You shoot the man and leave.")
            else:
                print("You both reveal your cards. He has a four of a kind, kings, and a 5. However, you have a high card, 7. You lose the game and your soul.")
                res()
        else:
            print("Invalid response. Try again.")
            scene16()
    elif response == "refuse":
        print("You don’t have time for a game of poker and walk off.")
    else:
        print("Invalid response. Try again.")
        scene16()

def scene17():
    response = input("You find an injured man lying on the ground. He is wearing some sort of black uniform. Do you Attack the man or do Something else? ").lower()
    if response == "attack":
        print("You attack the man, but he uses the force to knock you back. Your vision begins to darken.")
        res()
    elif response == "something":
        print("You ask him if he wants to do the dance for old time’s sake. He has no idea what you’re talking about, but YEAH! After all,\nyou’re feeling like a star. They can’t stop your shine. You’re loving Cloud City. Your head’s in the sky. You’re Solo. You’re Han Solo. You’re Han Solo. You’re Han Solo, Solo.")
    else:
        print("Invalid response. Try again.")
        scene17()

def scene18():
    response = input("You enter a nearby forest to hunt when you hear growling in the distance. You turn around and see a bear looking at you. Do you Attack the bear or Run away? ").lower()
    if response == "attack":
        if inventory["gun"] == 1:
            print("You shoot the bear.")
        elif inventory["knife"] == 1:
            print("You stab the bear.")
        else:
            print("You punch the bear. The bear mauls you to death.")
            res()
    elif response == "run":
        print("You run as fast as you can. After a while, you turn around. The bear is nowhere in sight.")
        scene18()

def scene19():
    response = input("You find a locked safe. Do you Open it or Leave it alone? ").lower()
    if response == "open":
        if inventory["crowbar"] == 1:
            print("Congratulations! You’ve just won the “Jeff and Paul Award for Excellence in Shopping Centers”.\nActually, the crowbar snaps in two.\nJust kidding!\nYou find many items in the safe.")
            obt()
            obt()
            obt()
        else:
            print("You fail to open the safe.")
    elif response == "leave":
        print("It’s too much work. You decide to leave it be.")
    else:
        print("Invalid response. Try again.")
        scene19()

def scene20():
    response = input("You feel some drops of rain fall onto your shoulder. More and more raindrops fall. Soon, you hear a loud boom and see a bright flash.\nDo you Stay outside or Run inside? ").lower()
    if response == "stay":
        print("Against your better judgement, you decide to stay outside. As you expected, you are struck by lightning.")
        res()
    elif response == "run":
        print("You run inside a nearby building and wait for the storm to clear.")
    else:
        print("Invalid response. Try again.")
        scene20()

def scene21():
    response = input("A man walks up behind you with a gun pointed at you. He hands you a costume and orders you to do the green alien dance perfectly.\nYou put on the outfit and proceed to perform the dance, but you do not remember how many times you are supposed to adjust your glasses. How many times do you adjust your glasses? ").lower()
    if response == "12":
        print("You adjust your glasses 12 times, the correct amount (Yes, I counted). The man is pleased and gives you some items.")
        obt()
        obt()
    else:
        print("You adjust your glasses the incorrect amount of times. The man is disappointed with your performance and shoots you.")

def scene22():
    response = input("During the night, you hear voices. You are unsure where they are coming from. Do you Breathe or take a different option? ").lower()
    if response == "nico nico nii":
        print("With the power of Nico Yazawa, The Voice in your head ceases.")
    elif response == "breathe":
        if inventory["crippling depression"] == 1:
            print("You begin to panic before you realize that you have crippling depression. The voices cease.")
        else:
            print("You try your best to relax, but the voices continue. In a fit of panic, you destroy an item.")
            rem()
    else:
        print("Your efforts to calm yourself fail. In a fit of panic, you destroy an item.")
        rem()

def scene23():
    response = input("You hear the distant wail of a car. You turn around to and see what appears to be an Archduke riding in a taxi. You’re sure that he has a lot of supplies.\nDo you try to Assassinate the Archduke or Leave? ").lower()
    if response == "assassinate":
        if inventory["knife"] == 1:
            response = input("You pull out your knife and try to kill the archduke. However, the taxi drives off and you miss. Do you Assassinate again or just Leave? ").lower()
            if response == "assassinate":
                response = input("You try to kill the archduke again but he drives off. Do you Try again or Leave? ").lower()
                if response == "assassinate":
                    response = input("Again, you stab in the archdukes direction, but you are just short. You angrily storm off. You then notice the archduke and the taxi driver exit the taxi.\nDo you Assassinate again or Leave? ").lower()
                    if response == "assassinate":
                        print("You slowly creep up on the archduke and stab him nine times. The taxi driver, for some reason, dabs to the beat of your stabs, before realizing that the archduke is dead.")
                    elif response == "leave":
                        print("You decide killing him is too much effort.")
                    print("Invalid response. Try again.")
                    scene23()
                elif response == "leave":
                    print("You decide killing him is too much effort.")
                print("Invalid response. Try again.")
                scene23()
            elif response == "leave":
                print("You decide killing him is too much effort.")
            print("Invalid response. Try again.")
            scene23()
        else:
            print("You approach the taxi. The taxi driver notices you and shoots you.")
            res()
    elif response == "leave":
        print("You decide killing him is too much effort.")
    else:
        print("Invalid response. Try again.")
        scene23()

def scene24():
    response = input("You come across a building. As you enter, you find a soldier huddled over a telegraph. He doesn't seem to know what he's doing.\nDo you Help the man or Leave? ").lower()
    if response == "help":
        if inventory["strange paper"] == 1:
            print("Luckily for the soldier, as a communications engineer ;) you happen to have one of those left as you take out the strange paper.\nYou tell the soldier that all he has to do is tap tap, easy as that. The soldier is grateful for your help and gives you some items in return.")
            obt()
            obt()
        else:
            print("You try to help, but you have no knowledge of a telegraph. The soldier thanks you for your help anyways. He gives you an item for your attempt.")
            obt()
    elif response == "leave":
        print("You are unsure how to use the device. You refuse to help, as you believe that you’ll make things worse.")
    else:
        print("Invalid response. Try again.")
        scene24()

def scene25():
    response = input("While inside a building, you feel the ground shake. You’ve never experienced one first-hand, but you are very sure that you’re in the middle of an earthquake.\nDo you run to the Door or Drop to the ground? ").lower()
    if response == "door":
        print("You run to the doorframe, thinking that you are safe. Soon, however, the frame collapses, pinning you to the ground.")
        res()
    elif response == "drop":
        print("You drop to the ground and hide under the table. Soon, the earthquake passes.")
    else:
        print("Invalid response. Try again.")
        scene25()

def scene26():
    response = input("You wake up to find a bomb next to you. Do you Cut the wires or Run away? ").lower()
    if response == "cut":
        if inventory["knife"] == 1:
            response == input("You pull out your knife. Do you cut the Red wire, Blue wire, Green wire, or Yellow wire? ").lower()
            if response == "red":
                print("You cut the red wire. The bomb is disarmed.")
            elif response == "blue":
                print("You cut the blue wire. The bomb explodes.")
                res()
            elif response == "yellow":
                print("You cut the yellow wire. The bomb explodes.")
                res()
            elif response == "green":
                print("You cut the green wire. The bomb explodes.")
                res()
        else:
            print("You have no knife to cut the wires with. The bomb explodes.")
            res()
    elif response == "run":
        print("You run away from your camp, leaving an item behind. The bomb explodes.")
        rem()
    else:
        print("Invalid response. Try again.")
        scene26()

def scene27():
    response = input("The night turns out to be colder than you expected. You’ll most likely freeze to death if you don’t do something. Do you start a Fire or Huddle for warmth? ").lower()
    if response == "fire":
        if inventory["matches"] == 1:
            print("You light a match and throw it into a pile of tinder. It isn’t much, but it’ll keep you alive.")
        else:
            print("You don’t have anything to start a fire with. You eventually succumb to the elements.")
            res()
    elif response == "huddle":
        if inventory["cloak"] == 1:
            print("You take out your cloak and wrap it around yourself. It isn’t much, but it’ll keep you alive.")
        else:
            print("You don’t have anything to keep yourself warm with. You eventually succumb to the elements.")
            res()
    else:
        print("Invalid response. Try again.")
        scene27()

def scene28():
    response = input("The day turns out to be hotter than you expected. You’ll most likely die of heat stroke if you don’t do something. Do you Drink some water or Cover yourself? ").lower()
    if response == "drink":
        if inventory["water"] == 1:
            print("You drink some water. You’re still thirsty, but you’ll probably be fine.")
        else:
            print("You have nothing to drink. You eventually succumb to the elements.")
            res()
    elif response == "cover":
        if inventory["cloak"] == 1:
            print("You use your cloak to shade yourself from the sun. It’s uncomfortable, but you’ll survive.")
        else:
            print("You have nothing to shade yourself from the sun with. You eventually succumb to the elements.")
            res()
    else:
        print("Invalid response. Try again.")
        scene28()

def scene29():
    response = input("A rare pepe approaches you, asking where his foond is. Do you Feed the rare pepe or Drive him away? ").lower()
    if response == "feed":
        if inventory["fried meme dinner"] == 1:
            if inventory["vegetals"] == 1:
                print("He tastes a vegetal. He is ANGERY. He kills you.")
                res()
            else:
                print("You have his steank with NO VEGETAL as he asked. cool and good. He gives you an item as payment.")
                obt()
        else:
            print("You do not have his steank. He is disappointed.")
    elif response == "drive":
        print("You drive the rare pepe away. He is disappointed.")
    else:
        print("Invalid response. Try again.")
        scene29()

def scene30():
    response = input("You wake up to find rats all over your camp. Do you Attack the rats or Defend your supplies? ").lower()
    if response == "attack":
        if inventory["gun"] == 1:
            print("You hunt all of the rats and successfully kill all of them.")
        elif inventory["knife"] == 1:
            print("You hunt all of the rats and successfully kill all of them.")
        elif inventory["bomb"] == 1:
            print("You light the fuze and throw it at the rats. Unsurprisingly, all of them die, including yourself.")
            res()
        else:
            print("You chase after the rats but fail to kill them. They destroy an item.")
            rem()
    elif response == "defend":
        if inventory["gun"] == 1:
            print("You protect your supplies but fail to fend off the rats. They destroy an item.")
            rem()
        elif inventory["knife"] == 1:
            print("You protect your supplies but fail to fend off the rats. They destroy an item.")
            rem()
        elif inventory["bomb"] == 1:
            print("You light the fuze and throw it at the rats. Unsurprisingly, all of them die, including yourself.")
            res()
        else:
            print("You try to protect your supplies but fail to fend off the rats. They destroy some of your items.")
            rem()
            rem()
    else:
        print("Invalid response. Try again.")
        scene30()