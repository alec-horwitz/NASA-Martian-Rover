from pprint import pprint # for printing the map
import sys      # for forcefully exiting this program


COMPASS = ["N", "E", "S", "W"]     # for defining what the possible directions are

def main():
    print("===================================================")
    print("=== Welcome to the NASA Martian Rover Simulator ===")
    print("===================================================")
    print("\n\n\n------SYSTEM TEST COMMENCING------")
    test_rover()
    print("\n\n\n----LUNCHING TERMINAL INTERFACE----")
    terminal_interface()

def test_rover():
    # lunches some simple automated tests
    rover = Rover(7, 9, 3, 4, "N")
    rover.land()

    testArray = [[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]

    if rover.map == testArray:
        print("[PASSED]: landed a rover in a big map")
    else:
        print("[FAILED]: Unable to land rover in big map")

    rover.moves("MMMMMLMMMMLMMMMMMMMMLMMMMMMMLMMMMMMMMMLMMMMMMMRRMMMMMMMRMMMMMMMMMRMMMMMMMRMMMMMMMMMRMMMMMMM")

    testArray = [[0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]

    if rover.map == testArray:
        print("[PASSED]: Move rover around in big map")
    else:
        print("[FAILED]: Unable to move rover around in big map")

    rover = Rover(0, 0, -1, -1, "N")
    rover.land()

    testArray = [[0]]

    if rover.map == testArray:
        print("[PASSED]: landed a rover outside a small map")
    else:
        print("[FAILED]: Unable to land rover outside small map")

    rover.moves("MRM")

    testArray = [[1]]

    if rover.map == testArray:
        print("[PASSED]: Move rover into small map")
    else:
        print("[FAILED]: Unable to move rover into small map")

def terminal_interface():
    # lunches a terminal interface with some error handling
    print("\n\n\n=== Define map boundaries ===")
    dementions = raw_input('Enter numbers for the max X value and max Y value seperated by a single space (i.e. "6 9"): ')
    dementions = dementions.split(" ")

    print("\n\n\n=== Define this rovers landing zone ===")
    current_pos = raw_input('Enter numbers for the starting X value, starting Y value, and a capital letter representing one of the four cardinal compass points seperated by spaces (i.e. "2 4 N"): ')
    current_pos = current_pos.split(" ")
    if (not((int(current_pos[0]) < int(dementions[0])) and (int(current_pos[1]) < int(dementions[1])) and (int(current_pos[0]) > -1) and (int(current_pos[1]) > -1))):
        print("WARNING: The rover is on route to land outside of the map!\n This means the rover will not be visable untill you move it into the veiw of the map!")
        ans = raw_input("\nDo you want to abort the mission?(y/n): ")
        if ans == "y":
            sys.exit()
    rover = Rover(dementions[0], dementions[1], current_pos[0], current_pos[1], current_pos[2])

    rover.land()

    print("\n\n\n=== The rover has landed and is now awaiting instuction ===")
    print("X: ", rover.x_axis)
    print("Y: ", rover.y_axis)
    print("Direction: ", rover.direction)
    pprint(rover.map)

    move_instr = raw_input('\nEnter series of instructions telling the rover how to explore the plateau. \n "L" and "R" means spin 90 degrees left or right respectively, without moving from its current spot. \n "M" means move forward one grid point, and maintain the same heading. There should be no spaces between instruction characters (i.e. "MRMMLMLMMMRM"): ')


    rover.moves(move_instr)

    print("X: ", rover.x_axis)
    print("Y: ", rover.y_axis)
    print("Direction: ", rover.direction)
    pprint(rover.map)







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
        self.make_map([self.max_x, self.max_y])

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


        # Puts rover on the map if it landed on it
        if ((self.y_axis < len(map)) and (self.x_axis < len(map)) and (self.y_axis > -1) and (self.x_axis > -1)):
            map[-((self.y_axis)+1)][self.x_axis] = 1

        self.map = map

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
        if ((self.y_axis < len(self.map)) and (self.x_axis < len(self.map)) and (self.y_axis > -1) and (self.x_axis > -1)):
            self.map[-((self.y_axis)+1)][self.x_axis] = 0

        if self.direction == "N":
            if self.y_axis < (len(self.map)-1):
                self.y_axis = self.y_axis + 1
            # else:
            #     print("!!!INVALID_MOVEMENT: At a Y value of "+str(self.y_axis)+" Moving further north would move you off the map!!!")
        elif self.direction == "S":
            if self.y_axis > 0:
                self.y_axis = self.y_axis - 1
            # else:
            #     print("!!!INVALID_MOVEMENT: At a Y value of "+str(self.y_axis)+" Moving further South would move you off the map!!!")
        elif self.direction == "E":
            if self.x_axis < (len(self.map[0])-1):
                self.x_axis = self.x_axis + 1
            # else:
            #     print("!!!INVALID_MOVEMENT: At a X value of "+str(self.x_axis)+" Moving further East would move you off the map!!!")
        elif self.direction == "W":
            if self.x_axis > 0:
                self.x_axis = self.x_axis - 1
            # else:
            #     print("!!!INVALID_MOVEMENT: At a X value of "+str(self.x_axis)+" Moving further West would move you off the map!!!")

        if ((self.y_axis < len(self.map)) and (self.x_axis < len(self.map)) and (self.y_axis > -1) and (self.x_axis > -1)):
            self.map[-((self.y_axis)+1)][self.x_axis] = 1

    def turn_direction(self, num):
        # turns the rover left or right given a number
        direction_index = COMPASS.index(self.direction)
        if direction_index+num < len(COMPASS):
            self.direction = COMPASS[direction_index+num]
        else:
            self.direction = COMPASS[0]


if __name__ == '__main__':
  main()
