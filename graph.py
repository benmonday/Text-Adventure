from room import Room

class Graph:
    def __init__(self, rooms):
        self.rooms = rooms
        self.currentRoom = rooms[0]

    def getCurrentRoom(self):
        return self.currentRoom

    def setCurrentRoom(self, room):
        self.currentRoom = room

    def goNorth(self):
        if (self.currentRoom.north != None):
            self.setCurrentRoom(self.currentRoom.north)
            print("\n* You move through the door to the North.")
            self.printStatus(self.currentRoom)
        else:
            print("There is no door to the North.")

    def goEast(self):
        if (self.currentRoom.east != None):
            self.setCurrentRoom(self.currentRoom.east)
            print("\n* You move through the door to the East.")
            self.printStatus(self.currentRoom)
        else:
            print("There is no door to the East.")

    def goSouth(self):
        if (self.currentRoom.south != None):
            self.setCurrentRoom(self.currentRoom.south)
            print("\n* You move through the door to the South.")
            self.printStatus(self.currentRoom)
        else:
            print("There is no door to the South.")

    def goWest(self):
        if (self.currentRoom.west != None):
            self.setCurrentRoom(self.currentRoom.west)
            print("\n* You move through the door to the West.")
            self.printStatus(self.currentRoom)
        else:
            print("There is no door to the West.")

    def kickedEast(self):
        self.setCurrentRoom(self.currentRoom.east)
        print("* You feel a sudden force hit your chest as you are thrown backwards out of the room.")
            

    def printStatus(self, room):
        options = "You shouldn't see me"
        # Count the number of availible directions
        directions = []
        if (room.north != None):
            directions.append("North")
        if (room.east != None):
            directions.append("East")
        if (room.south != None):
            directions.append("South")
        if (room.west != None):
            directions.append("West")

        # Format a string to return
        if (len(directions) == 1):
            options = "\nThere is a door to the " + directions[0] + "."
        if (len(directions) == 2):
            options = "\nThere are doors to the " + directions[0] + " and " + directions[1] + "."
        if (len(directions) == 3):
            options = "\nThere are doors to the " + directions[0] + ", " + directions[1] + ", and " + directions[2] + "."
        return options



