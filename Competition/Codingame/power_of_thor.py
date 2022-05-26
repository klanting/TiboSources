import sys
import math

# Solve this puzzle by writing the shortest code.
# Whitespaces (spaces, new lines, tabs...) are counted in the total amount of chars.
# These comments should be burnt after reading!

# lx: the X position of the light of power
# ly: the Y position of the light of power
# tx: Thor's starting X position
# ty: Thor's starting Y position
lx, ly, tx, ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The level of Thor's remaining energy, representing the number of moves he can still make.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    """klanting here: we check which direction is the closest to the end-point and we move to it"""

    directions = {"N": (tx, ty - 1),
                  "NE": (tx + 1, ty - 1),
                  "E": (tx + 1, ty),
                  "SE": (tx + 1, ty + 1),
                  "S": (tx, ty + 1),
                  "SW": (tx - 1, ty + 1),
                  "W": (tx - 1, ty),
                  "NW": (tx - 1, ty - 1)}

    last_distance = math.sqrt((lx - tx) ** 2 + (ly - ty) ** 2)
    last_key = None

    for key, value in directions.items():
        nx, ny = value
        distance = math.sqrt((lx - nx) ** 2 + (ly - ny) ** 2)
        if distance < last_distance:
            last_distance = distance
            last_key = key

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(last_key)
    tx, ty = directions.get(last_key)
