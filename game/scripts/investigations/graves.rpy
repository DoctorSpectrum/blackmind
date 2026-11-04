label graves_investigation:
    $ current_thought_block = "mind_read_graves"
    if (branch == "a"):
        if (day == 1):
            jump graves_a_1
        elif (day == 2):
            jump graves_a_2
        elif (day == 3):
            jump graves_a_3
        elif (day == 4):
            jump graves_a_4
    
    return

label graves_a_1:

    scene detective_office with slow_dissolve
    $ swap_sprites("graves_intimidating", slow_dissolve)
    $ current_thought = "graves_thought_01"
    show screen psychic_powers

    return

label graves_a_2:
    return

label graves_a_3:
    return

label graves_a_4:
    return