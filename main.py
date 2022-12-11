from room import Room
from graph import Graph
from termcolor import colored
from colorama import init

init(autoreset = True)

# Create the rooms
room0 = Room("room0")
room1 = Room("room1")
room2 = Room("room2")
room3 = Room("room3")
room4 = Room("room4")
room5 = Room("room5")
room6 = Room("room6")
room7 = Room("room7")

# Create the edges
room0.setDoors(room1, None, None, None)
room1.setDoors(room2, room4, room0, None)
room2.setDoors(None, None, room1, room3)
room3.setDoors(None, room2, None, None)
room4.setDoors(room7, room5, None, room1)
room5.setDoors(None, None, room6, room4)
room6.setDoors(room5, None, None, None)
room7.setDoors(None, None, room4, None)

# Create the graph
dungeonMap = Graph([room0, room1, room2, room3, room4, room5, room6, room7])

# Actual Game
# Track if the player has been in a room before to alter text.
complete0 = False
complete1 = False
complete2 = False
seen3 = False
complete4 = False
complete5 = False
complete6 = False
hasKey = False

gamePlaying = True
while (gamePlaying):
    # Events for specific rooms.
    # Room 0
    if (dungeonMap.currentRoom.name == "room0"):
        if (complete0):
            print("* This is where you first woke up. There was nothing to do but move forward.")
        else:
            print("* You open your eyes, but it isn't much different from being asleep. It is pitch black all around, you can't see a thing.")
            input("(Press enter to continue.)")
            print("* Suddenly you feel a vibration on your wrist. You bring your wrist towards your face and notice a watch with very faintly glowing text.")
            input("...")
            print(colored("Welcome.", "green"))
            input("...")
            print(colored("This watch will be your guide through this dark cavern. It will tell you where doors are located, and nothing more.", "green"))
            input("...")
            print(colored("Good luck.", "green"))
            print(colored("Move between rooms by typing the cardinal direction you wish to go in. You can also type just the first letter.", "yellow"))
            complete0 = True

    # Room 1
    if (dungeonMap.currentRoom.name == "room1"):
        if (complete1):
            print("* This is the first room you moved to after waking up. There didn't seem to be anything to do here.")
        else:
            print("* You still can't see a thing. Part of you wants to go back to the previous room where you know it's safe,\nbut the sane part of you knows that is not an option.")
            complete1 = True

    # Room 2
    if (dungeonMap.currentRoom.name == "room2"):
        if (complete2 and hasKey):
            print("* You can faintly hear the two-fingered fiend to the West mumbling to itself.")
        elif (complete2):
            print("* You can hear an ominous snarling noise accompanied by the occasional jangle of a keychain coming from the West.")
        else:
            print("* You suddenly get goosebumps, as a growling sound unlike any you've ever heard can be heard faintly from the room to the West.\nAfter calming down a bit, you can pick out the sound of keys jangling.")
            complete2 = True

    # Room 3
    if (dungeonMap.currentRoom.name == "room3"):
        if (hasKey):
            print(colored("What more do you want from me? Get out of here.", "red"))
        else:
            print("* Inside the room are three pairs of glowing, pure white eyes. The glow faintly illuminates a face, but not enough to make out any details. The beast notices your presence, and speaks.")
            input("...")
            if (seen3):
                print(colored("Back again? If you wish to lose to me once again, go ahead!", "red"))
                input("...")
            else:
                seen3 = True
                print(colored("Hello, trapped one. Here to take my key I assume?", "red"))
                input("...")
                print(colored("I won't be giving it up easy. If you want this key, you'll have to beat me in a little game of rock, paper, scissors!", "red"))
                input("...")
            print(colored("We go on shoot. Ready? Rock, paper, scissors, SHOOT!", "red"))
            RPS = input("* What will you play?:  ")
            if (RPS.lower() == "rock"):
                print(colored("Heh. Rock. I threw paper. Sorry. Better luck text time.", "red"))
                if (complete6):
                    input("...")
                    print("* You recall the message you saw on the tablet. You know you couldn't have lost.")
                    input("...")
                    yorn = input("* Will you confront the beast? (Y/N):  ")
                    if (yorn.lower() == "y" or yorn.lower == "yes"):
                        print("* You tell the monster that he's lying, and that you know you won the game.")
                        input("...")
                        print(colored("Is that so? In that case, what did I throw?", "red"))
                        input("...")
                        RPS2 = input("* Did the monster throw rock, paper, or scissors?:  ")
                        if (RPS2.lower() == "rock"):
                            print(colored("Whatever. Then we tied. Better luck next time!", "red"))
                            dungeonMap.kickedEast()
                        elif (RPS2.lower() == "paper"):
                            print(colored("Of course! That's what I already said! Better luck next time!", "red"))
                            dungeonMap.kickedEast()
                        elif (RPS2.lower() == "scissors"):
                            print(colored("How... I-I don't know what you mean. How do you know I threw scissors?", "red"))
                            input("...")
                            answer = input("* How do you know the monster threw scissors?:  ")
                            if (("two finger" in answer) or ("2 finger" in answer)):
                                print(colored("You weren't supposed to be able to see! How did you possibly know that? Whatever, I care not. Take the key and go.", "red"))
                                input("...")
                                print("* You open your hand and extend it towards the beast. A moment later you feel a cold metal object placed in your palm. You grip the key, turn around, and leave the room.")
                                hasKey = True
                                dungeonMap.goEast()
                            else:
                                print(colored("As I expected. You have no proof. Get out of here.", "red"))
                                dungeonMap.kickedEast()
                        else:
                            print(colored("Ha! That isn't an option. Sorry. Better luck next time!", "red"))
                            dungeonMap.kickedEast()
                    elif (yorn.lower() == "n" or yorn.lower() == "no"):
                        dungeonMap.kickedEast()
                    else:
                        print(colored("Get out of here already!", "red"))
                        dungeonMap.kickedEast()
                else:
                    dungeonMap.kickedEast()
            elif (RPS.lower() == "paper"):
                print(colored("Heh. Paper. I threw scissors. Sorry. Better luck next time!", "red"))
                dungeonMap.kickedEast()
            elif (RPS.lower() == "scissors"):
                print(colored("Heh. Scissors. I threw Rock. Sorry. Better luck next time!", "red"))
                dungeonMap.kickedEast()
            else:
                print(colored("Ha! That isn't an option. Sorry. Better luck next time!", "red"))
                dungeonMap.kickedEast()


    # Room 4
    if (dungeonMap.currentRoom.name == "room4"):
        if (complete4 and complete6):
            print("* There is a faint, yet hopefully light shinign from the North. You can vaguely make out the beeping of the tablet you found to the East.")
        elif (complete4):
            print("* There is faint, yet hopeful light shining from the North and an electronic beep coming from the East.")
        else:
            print("* You notice an incredibly faint light shining from the North. Could it be a way out? Although quiet, you can make out the sound of an electronic beep coming from the East.")
            complete4 = True

    # Room 5
    if (dungeonMap.currentRoom.name == "room5"):
        if (complete5 and complete6):
            print("* You can still hear the tablet beeping to the South.")
        elif (complete5):
            print("* You can still hear the beeping coming from the South.")
        else:
            print("* The beeping you heard in the previous room has grown louder. It is clear that it is coming from the South.")
            complete5 = True

    # Room 6
    if (dungeonMap.currentRoom.name == "room6"):
        if (complete6 and hasKey):
            print("* This is where you found the tablet that guided you to defeat the beast and retrieve the key.")
        elif (complete6):
            print("* This is where you found the mysterious tablet with a description of a horrible beast that only has two fingers and cannot make a fist.")
        else:
            print("* As you near the center of the room, the beep gets even louder. As you get closer to the noise you feel your foot hit something. You bend down to pick it up.")
            print("As soon as you touch it, word light up a screen revealing it to be a tablet. It reads:")
            input("...")
            print(colored("If you have found this, then you have found yourself in the same situation I was in. The key to escape this place is kept by a horrible beast in the Northwestern corner.", "magenta"))
            input("...")
            print(colored("The beast will make you play a game to receive the key, but it does not play fair. Even if you win, it will insist you have lost, as it knows you cannot see.", "magenta"))
            input("...")
            print(colored("To get the key, you must expose its lie. The beast cannot make a fist and only has two fingers. Use this information to claim the key and escape. - M", "magenta"))
            input("...")
            print("* The screen shuts off and you are engulfed in darkness again.")
            complete6 = True
    # Room 7
    if (dungeonMap.currentRoom.name == "room7"):
        if (hasKey):
            gamePlaying = False
            break
        else:
            print("* The light that you saw from the previous room has grown clearer. It outlines a door. In the faint glow, you can barely make out a padlock on the door.\nYou try to force the door, but it's of no use. You will need a key to proceed any further.")

    # Moving to another room.
    print(colored(dungeonMap.printStatus(dungeonMap.currentRoom), "green"))
    direction = input(colored("Where will you go?   ", "green"))
    if (direction.lower() == "north" or direction.lower() == "n"):
        dungeonMap.goNorth()
    elif (direction.lower() == "east" or direction.lower() == "e"):
        dungeonMap.goEast()
    elif (direction.lower() == "south" or direction.lower() == "s"):
        dungeonMap.goSouth()
    elif (direction.lower() == "north" or direction.lower() == "w"):
        dungeonMap.goWest()
    else:
        print(colored("Invalid Input. Please type 'North', 'East', 'South', or 'West'.", "yellow"))

print("* With the key in hand you approach the door. You insert the key into the lock and pull open the door. The light is blinding, but you step through.")
input("...")
print("* You can't see, but you can feel the sun beating down on you and the chriping of birds.")
input("...")
print("You made it out.")
input("...")
print(colored("THE END", "blue"))
    
