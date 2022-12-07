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
complete3 = False
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
        if (complete2 and complete3):
            print("* You can faintly hear the two-fingered fiend to the West mumbling to itself.")
        elif (complete2):
            print("* You can hear an ominous snarling noise accompanied by the occasional jangle of a keychain coming from the West.")
        else:
            print("* You suddenly get goosebumps, as a growling sound unlike any you've ever heard can be heard faintly from the room to the West.\nAfter calming down a bit, you can pick out the sound of keys jangling.")
            complete2 = True

    # Room 3
    if (dungeonMap.currentRoom.name == "room3"):
        print("This is room 3.")

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
        if (complete6 and complete3):
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
            print(colored("To get the key, you must expose it's lie. The beast cannot make a fist and only has two fingers. Use this information to claim the key and escape. - M", "magenta"))
            input("...")
            print("* The screen shuts off and you are engulfed in darkness again.")
            complete6 = True
    # Room 7
    if (dungeonMap.currentRoom.name == "room7"):
        if (hasKey):
            print("* With the key in hand you approach the door. You insert the key into the lock and pull open the door. You step through.")
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
        print(colored("Invalid Input", "red"))

print("you reached the end of the game")
    
