# This function accepts numbers of tower's floors.

def tower_builder(n_floors):
    floors = []
    number_of_symbols = (n_floors * 2 - 1) // 2
    number_of_stars = 0
    for current_floor in range(n_floors):
        floor = ""
        for first_part in range(number_of_symbols):
            if first_part < number_of_symbols - number_of_stars:
                floor += " "
            else:
                floor += "*"
        floor += "*"
        for second_part in range(number_of_symbols):
            if second_part < number_of_stars:
                floor += "*"
            else:
                floor += " "
        floors.append(floor)
        print(floor)
        number_of_stars += 1
    return floors
