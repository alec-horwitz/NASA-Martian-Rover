from rover import *

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
