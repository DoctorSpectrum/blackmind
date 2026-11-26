label move_location():
    $ renpy.choice_for_skipping()
    $ minds_read = 0
    $ minds_rewound = 0

    if (branch == "a"):
        if (day == 1 and len(days["a"][0]) >= 3):
            jump branch_a_1_4
        elif (day == 2 and len(days["a"][1]) >= 3):
            jump branch_a_2_4
        elif (day == 3 and len(days["a"][2]) >= 3):
            jump branch_a_3_4
        elif (day == 4 and len(days["a"][3]) >= 3):
            jump graves_investigation
    elif (branch == "b"):
        if (len(days["b"][0]) >= 3):
            jump barbara_investigation
    elif (branch == "c"):
        if (day == 2 and len(days["c"][0]) >= 3):
            jump branch_c_2_4
        elif (day == 3 and len(days["c"][1]) >= 3):
            jump branch_c_3_4
        elif (day == 4 and len(days["c"][2]) >= 3):
            jump cat_investigation
    elif (branch == "d"):
        if (day == 3 and len(days["d"][0]) >= 3):
            jump branch_d_3_4
        elif (day == 4 and len(days["d"][1]) >= 3):
            jump eddie_investigation
    elif (branch == "e"):
        if (len(days["e"][0]) >= 3):
            jump branch_e_4_4

    call screen map_navigation() 
