from rover import *
from pprint import pprint # for printing the map
import sys      # for forcefully exiting this program

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
    print("X: " + str(rover.x_axis))
    print("Y: " + str(rover.y_axis))
    print("Direction: " + str(rover.direction))
    pprint(rover.map)

    move_instr = raw_input('\nEnter series of instructions telling the rover how to explore the plateau. \n "L" and "R" means spin 90 degrees left or right respectively, without moving from its current spot. \n "M" means move forward one grid point, and maintain the same heading. There should be no spaces between instruction characters (i.e. "MRMMLMLMMMRM"): ')

    rover.moves(move_instr)

    print("X: " + str(rover.x_axis))
    print("Y: " + str(rover.y_axis))
    print("Direction: " + str(rover.direction))
    pprint(rover.map)
