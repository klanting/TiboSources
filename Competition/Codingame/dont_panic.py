elevator_dict = {}
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevator_dict.update({elevator_floor: elevator_pos})
elevator_dict.update({exit_floor: exit_pos})
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])
    clone_pos = int(inputs[1])
    direction = inputs[2]
    elevator_pos = elevator_dict.get(clone_floor, 0)
    if direction == "LEFT":
        check_pos = clone_pos-1
    else:
        check_pos = clone_pos+1
    current_distance = abs(clone_pos - elevator_pos)
    distance = abs(check_pos - elevator_pos)
    if (current_distance < distance) and not (distance < 2):
        print("BLOCK")
    else:
        print("WAIT")
