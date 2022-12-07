from room import Room
from graph import Graph
from termcolor import colored

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

# Lore and info dump
print("* You open your eyes, but it isn't much different from being asleep. It is pitch black all around, you can't see a thing.")
input("(Press enter to continue.)")
print("* Suddenly you feel a vibration on your wrist. You bring your wrist towards your face and notice a watch with very faintly glowing text.")
input()
print(colored("Welcome.", "green"))

# Actual Game
# Track if the player has been in a room before to alter text.
complete0 = False
complete1 = False
complete2 = False
complete3 = False
complete4 = False
complete5 = False
complete6 = False
complete7 = False

gamePlaying = True
while (gamePlaying):
    # Events for specific rooms.
    # Room 0
    if (dungeonMap.currentRoom.name == "room0"):
        if (complete0):
            print("* This is where you first woke up. There was nothing to do but move forward.")
        else:
            print("This is the starting room.")

    # Room 1
    if (dungeonMap.currentRoom.name == "room1"):
        if (complete1):
            print("* This is the first room you moved to after waking up. There didn't seem to be anything to do here.")
        else:
            print("* You still can't see a thing. Part of you wants to go back to the previous room where you know it's safe,\nbut the sane part of you knows that is not an option.")
            complete1 = True

    # Room 2
    if (dungeonMap.currentRoom.name == "room2"):
        if (complete2):
            print("* You can hear an ominous snarling noise accompanied by the occasional jangle of a keychain coming from the West.")
        elif (complete2 and complete3):
            print("* You can faintly hear the two-fingered fiend to the West mumbling to itself.")
        else:
            print("* You suddenly get goosebumps, as a growling sound unlike any you've ever heard can be heard faintly from the room to the West.\nAfter calming down a bit, you can pick out the sound of keys jangling.")
            complete2 = True

    # Room 3
    if (dungeonMap.currentRoom.name == "room3"):
        print("This is room 3.")

    # Room 4
    if (dungeonMap.currentRoom.name == "room4"):
        print("This is room 4.")

    # Room 5
    if (dungeonMap.currentRoom.name == "room5"):
        print("This is room 5.")

    # Room 6
    if (dungeonMap.currentRoom.name == "room6"):
        print("This is room 6.")
        
    # Room 7
    if (dungeonMap.currentRoom.name == "room7"):
        print("This is room 7.")

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


    
