def relative_view(player, target, *args):
    x, y, width, height = player
    tx, ty = target
    cx = tx - x
    cy = ty - y

    args_array = [(x + cx, y + cy, width, height)]
    for arg in args:
        elements_array = []
        for element in arg:
            ex, ey, e_width, e_height = element
            elements_array.append((ex + cx, ey + cy, e_width, e_height))

        args_array.append(elements_array)

    return tuple(args_array)
