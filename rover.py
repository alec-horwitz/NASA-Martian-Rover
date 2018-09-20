COMPASS = ["N", "E", "S", "W"]     # for defining what the possible directions are

class Rover(object):
    """A Class for making rover objects"""
    def __init__(self, max_x, max_y, start_x, start_y, start_direction):
        self.x_axis = int(start_x)
        self.y_axis = int(start_y)
        self.direction = str(start_direction)
        self.max_x = int(max_x)
        self.max_y = int(max_y)
        self.map = None

    def land(self):
        # makes map generate with a 1 for the rovers location and 0s for every other location
        self.map = self.make_map([self.max_x, self.max_y])
        self.toggle_map_pos() # Puts rover on the map if it landed on it

    def make_map(self, dementions, fill = None):
        # this function was originally designed for the possibility
        # of an array of more then 2 dementions
        # this is why it accepts a dementions array for it to parse through
        if fill == None:
            fill = 0

        map = [fill for i in xrange(int(dementions[0])+1)]
        dementions.remove(dementions[0])

        while len(dementions) > 0:
            map = [map[:] for j in xrange(int(dementions[0])+1)]
            dementions.remove(dementions[0])

        return map

    def moves(self, instructions):
        # reads through each char in the instructions
        # and sends it to be parsed by the move function
        for char in instructions:
            self.move(char)

    def move(self, char):
        # determins next movement
        # and sends cammand to the appropriate function
        if char == "L":
            self.turn_direction(-1)
        elif char == "R":
            self.turn_direction(1)
        elif char == "M":
            self.move_direction()


    def move_direction(self):
        # move rover in the direction it is facing
        # if rover is in the map don't let it leave
        self.toggle_map_pos()

        if self.direction == "N":
            if self.y_axis < (len(self.map)-1):
                self.y_axis = self.y_axis + 1
        elif self.direction == "S":
            if self.y_axis > 0:
                self.y_axis = self.y_axis - 1
        elif self.direction == "E":
            if self.x_axis < (len(self.map[0])-1):
                self.x_axis = self.x_axis + 1
        elif self.direction == "W":
            if self.x_axis > 0:
                self.x_axis = self.x_axis - 1

        self.toggle_map_pos()

    def toggle_map_pos(self):
        if self.within_map():
            if (self.map[-((self.y_axis)+1)][self.x_axis]):
                self.map[-((self.y_axis)+1)][self.x_axis] = 0
            else:
                self.map[-((self.y_axis)+1)][self.x_axis] = 1

    def within_map(self):
        within_max_x = self.x_axis < len(self.map[0])
        within_max_y = self.y_axis < len(self.map)

        within_min_x = self.x_axis > -1
        within_min_y = self.y_axis > -1

        x_within_map = within_max_x and within_min_x
        y_within_map = within_max_y and within_min_y

        xy_within_map = x_within_map and y_within_map

        return xy_within_map

    def turn_direction(self, num):
        # turns the rover left or right given a number
        direction_index = COMPASS.index(self.direction)
        if direction_index+num < len(COMPASS):
            self.direction = COMPASS[direction_index+num]
        else:
            self.direction = COMPASS[0]
