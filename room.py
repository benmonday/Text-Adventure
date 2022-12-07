class Room:
    def __init__(self, name):
        self.name = name
        self.north = None
        self.east = None
        self.south = None
        self.west = None

    def setDoors(self, north, east, south, west):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
