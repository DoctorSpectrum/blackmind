screen debug():
    default action = None
    default label_jump = ""
    default timeline_branch_selected = "a"
    default new_boolean = ""

    modal True
    zorder 100
    style_prefix "debug"

    frame:
        xfill True
        yfill True
        background Solid("#F2EE29")

        if (action == None):
            vbox:
                xalign 0.5
                yalign 0.2

                text _("DEBUG"):
                    font "gui/Decade__.ttf"
                    size 60

                textbutton _("Label Jump"):
                    action SetScreenVariable("action", "label_jump")

                textbutton _("Variable Controls"):
                    action SetScreenVariable("action", "variable_controls")

                textbutton _("Timeline"):
                    action SetScreenVariable("action", "timeline")
                
                textbutton _("Booleans"):
                    action SetScreenVariable("action", "booleans")

                #textbutton _("Test Map Jump"):
                #    action [
                #        Hide("debug"),
                #        SetVariable("progress_convo", False),
                #        Show("map_navigation")
                #    ]

                #textbutton _("Test Upgrading Psychic Abilities"):
                #    action [
                #        Hide("debug"),
                #        Show("upgrades_screen")
                #    ]

                #textbutton _("Test Flow Chart"):
                #    action [
                #        Hide("debug"),
                #        Show("flow_chart")
                #    ]
        elif (action == "label_jump"):
            hbox:
                xalign 0.5
                yalign 0.2
                spacing 10

                text _("Label Name:")
                input:
                    value ScreenVariableInputValue("label_jump")

            key "K_RETURN":
                action [
                    Hide("debug"),
                    Jump(label_jump)
                ]

        elif (action == "variable_controls"):
            vbox:
                xalign 0.5
                yalign 0.2
                spacing 10
                
                vbox:
                    spacing 25
                    hbox:
                        spacing 10
                        text _("Branch:"):
                            yoffset 5
                        hbox:
                            textbutton _("A"):
                                action SetVariable("branch", "a")
                            textbutton _("B"):
                                action SetVariable("branch", "b")
                            textbutton _("C"):
                                action SetVariable("branch", "c")
                            textbutton _("D"):
                                action SetVariable("branch", "d")
                            textbutton _("E"):
                                action SetVariable("branch", "e")
                            textbutton _("F"):
                                action SetVariable("branch", "f")
                            textbutton _("G"):
                                action SetVariable("branch", "g")

                    hbox:
                        spacing 10
                        text _("Day:"):
                            yoffset 5
                        hbox:
                            textbutton _("1"):
                                action SetVariable("day", 1)
                            textbutton _("2"):
                                action SetVariable("day", 2)
                            textbutton _("3"):
                                action SetVariable("day", 3)
                            textbutton _("4"):
                                action SetVariable("day", 4)
        
        elif (action == "timeline"):
            vbox:
                xalign 0.1
                yalign 0.2
                spacing 25
                label _("BRANCH"):
                    text_font "gui/Decade__.ttf"
                vbox:
                    spacing 10
                    textbutton _("A"):
                        action SetScreenVariable("timeline_branch_selected", "a")
                    textbutton _("B"):
                        action SetScreenVariable("timeline_branch_selected", "b")
                    textbutton _("C"):
                        action SetScreenVariable("timeline_branch_selected", "c")
                    textbutton _("D"):
                        action SetScreenVariable("timeline_branch_selected", "d")
                    textbutton _("E"):
                        action SetScreenVariable("timeline_branch_selected", "e")

            vbox:
                xalign 0.5
                yalign 0.2
                spacing 10
                
                vbox:
                    spacing 25

                    hbox:
                        spacing 10
                        if (timeline_branch_selected == "a"):
                            text _("Day 1:"):
                                yoffset 5
                        elif (timeline_branch_selected in ["b", "e"]):
                            text _("Day 4:"):
                                yoffset 5
                        elif (timeline_branch_selected == "c"):
                            text _("Day 2:"):
                                yoffset 5
                        elif (timeline_branch_selected == "d"):
                            text _("Day 3:"):
                                yoffset 5
                        textbutton _("Barbara"):
                            action (AddToSet(days[timeline_branch_selected][0], "barbara") if not person_visited("barbara", timeline_branch_selected, 0) else RemoveFromSet(days[timeline_branch_selected][0], "barbara"))
                            selected person_visited("barbara", timeline_branch_selected, 0)
                        textbutton _("Cat"):
                            action (AddToSet(days[timeline_branch_selected][0], "cat") if not person_visited("cat", timeline_branch_selected, 0) else RemoveFromSet(days[timeline_branch_selected][0], "cat"))
                            selected person_visited("cat", timeline_branch_selected, 0)
                        textbutton _("Eddie"):
                            action (AddToSet(days[timeline_branch_selected][0], "eddie") if not person_visited("eddie", timeline_branch_selected, 0) else RemoveFromSet(days[timeline_branch_selected][0], "eddie"))
                            selected person_visited("eddie", timeline_branch_selected, 0)
                        textbutton _("Graves"):
                            action (AddToSet(days[timeline_branch_selected][0], "graves") if not person_visited("graves", timeline_branch_selected, 0) else RemoveFromSet(days[timeline_branch_selected][0], "graves"))
                            selected person_visited("graves", timeline_branch_selected, 0)

                    if (timeline_branch_selected in ["a", "c", "d"]):
                        hbox:
                            spacing 10
                            if (timeline_branch_selected == "a"):
                                text _("Day 2:"):
                                    yoffset 5
                            elif (timeline_branch_selected == "c"):
                                text _("Day 3:"):
                                    yoffset 5
                            elif (timeline_branch_selected == "d"):
                                text _("Day 4:"):
                                    yoffset 5
                            textbutton _("Barbara"):
                                action (AddToSet(days[timeline_branch_selected][1], "barbara") if not person_visited("barbara", timeline_branch_selected, 1) else RemoveFromSet(days[timeline_branch_selected][1], "barbara"))
                                selected person_visited("barbara", timeline_branch_selected, 1)
                            textbutton _("Cat"):
                                action (AddToSet(days[timeline_branch_selected][1], "cat") if not person_visited("cat", timeline_branch_selected, 1) else RemoveFromSet(days[timeline_branch_selected][1], "cat"))
                                selected person_visited("cat", timeline_branch_selected, 1)
                            textbutton _("Eddie"):
                                action (AddToSet(days[timeline_branch_selected][1], "eddie") if not person_visited("eddie", timeline_branch_selected, 1) else RemoveFromSet(days[timeline_branch_selected][1], "eddie"))
                                selected person_visited("eddie", timeline_branch_selected, 1)
                            textbutton _("Graves"):
                                action (AddToSet(days[timeline_branch_selected][1], "graves") if not person_visited("graves", timeline_branch_selected, 1) else RemoveFromSet(days[timeline_branch_selected][1], "graves"))
                                selected person_visited("graves", timeline_branch_selected, 1)

                    if (timeline_branch_selected in ["a", "c"]):
                        hbox:
                            spacing 10
                            if (timeline_branch_selected == "a"):
                                text _("Day 3:"):
                                    yoffset 5
                            elif (timeline_branch_selected == "c"):
                                text _("Day 4:"):
                                    yoffset 5
                            textbutton _("Barbara"):
                                action (AddToSet(days[timeline_branch_selected][2], "barbara") if not person_visited("barbara", timeline_branch_selected, 2) else RemoveFromSet(days[timeline_branch_selected][2], "barbara"))
                                selected person_visited("barbara", timeline_branch_selected, 2)
                            textbutton _("Cat"):
                                action (AddToSet(days[timeline_branch_selected][2], "cat") if not person_visited("cat", timeline_branch_selected, 2) else RemoveFromSet(days[timeline_branch_selected][2], "cat"))
                                selected person_visited("cat", timeline_branch_selected, 2)
                            textbutton _("Eddie"):
                                action (AddToSet(days[timeline_branch_selected][2], "eddie") if not person_visited("eddie", timeline_branch_selected, 2) else RemoveFromSet(days[timeline_branch_selected][2], "eddie"))
                                selected person_visited("eddie", timeline_branch_selected, 2)
                            textbutton _("Graves"):
                                action (AddToSet(days[timeline_branch_selected][2], "graves") if not person_visited("graves", timeline_branch_selected, 2) else RemoveFromSet(days[timeline_branch_selected][2], "graves"))
                                selected person_visited("graves", timeline_branch_selected, 2)

                    if (timeline_branch_selected == "a"):
                        hbox:
                            spacing 10
                            text _("Day 4:"):
                                yoffset 5
                            textbutton _("Barbara"):
                                action (AddToSet(days[timeline_branch_selected][3], "barbara") if not person_visited("barbara", timeline_branch_selected, 3) else RemoveFromSet(days[timeline_branch_selected][3], "barbara"))
                                selected person_visited("barbara", timeline_branch_selected, 3)
                            textbutton _("Cat"):
                                action (AddToSet(days[timeline_branch_selected][3], "cat") if not person_visited("cat", timeline_branch_selected, 3) else RemoveFromSet(days[timeline_branch_selected][3], "cat"))
                                selected person_visited("cat", timeline_branch_selected, 3)
                            textbutton _("Eddie"):
                                action (AddToSet(days[timeline_branch_selected][3], "eddie") if not person_visited("eddie", timeline_branch_selected, 3) else RemoveFromSet(days[timeline_branch_selected][3], "eddie"))
                                selected person_visited("eddie", timeline_branch_selected, 3)
                            textbutton _("Graves"):
                                action (AddToSet(days[timeline_branch_selected][3], "graves") if not person_visited("graves", timeline_branch_selected, 3) else RemoveFromSet(days[timeline_branch_selected][3], "graves"))
                                selected person_visited("graves", timeline_branch_selected, 3)
        elif (action == "booleans"):
            vbox:
                xalign 0.5
                yalign 0.2
                spacing 25

                text _("BOOLEANS")

                hbox:
                    spacing 5
                    text _("Add:")
                    input:
                        value ScreenVariableInputValue("new_boolean")

                vbox:
                    spacing 10
                    for boolean in booleans:
                        textbutton _(boolean):
                            action RemoveFromSet(booleans, boolean)

                key "K_RETURN":
                    action [
                        Function(add_boolean, new_boolean),
                        SetScreenVariable("new_boolean", "")
                    ]

        textbutton _("RETURN"):
            background Frame("gui/frame.png")
            xalign 0.0
            yalign 1.0
            xoffset 10
            yoffset -10
            action (Hide("debug") if action is None else SetScreenVariable("action", None))

style debug_text:
    color "#000"
style debug_button_text:
    selected_underline True
    selected_color "#000"

screen psychic_powers():
    default icon_hint = None

    zorder 20

    if (reading_mind or rewound_mind):
        null
    else:
        frame:
            background None
            xalign 1.0
            yalign 0.0
            yoffset 40
            xoffset -5
            xsize 275
            ysize 82

            frame:
                background Frame("gui/button/button_idle.png")
                padding (10, 10, 10, 10)
                xalign 0.5

                hbox:
                    spacing 20

                    #image "gui/icons/psychic_icon_idle.png":
                    #    at transform:
                    #        zoom 0.5

                    imagebutton:
                        auto "gui/icons/mind_read_icon_%s.png"
                        yalign 0.5
                        action [
                            SetLocalVariable("icon_hint", None),
                            (Call("mind_read_effects", from_current=True) if (max_mind_reads == None or minds_read < max_mind_reads) else NullAction()),
                        ]
                        hovered SetLocalVariable("icon_hint", "mind_read")
                        unhovered SetLocalVariable("icon_hint", None)

                    if (check_boolean("mind_wipe_available")):
                        imagebutton:
                            auto "gui/icons/mind_wipe_icon_%s.png"
                            yalign 0.5
                            action [
                                SetLocalVariable("icon_hint", None),
                                (Call("mind_wipe_pause", from_current=True) if (max_rewinds == None or minds_rewound < max_rewinds) else NullAction())
                            ]
                            hovered SetLocalVariable("icon_hint", "mind_wipe")
                            unhovered SetLocalVariable("icon_hint", None)

                    if (check_boolean("future_sight_available")):
                        imagebutton:
                            auto "gui/icons/future_sight_icon_%s.png"
                            action [
                                SetLocalVariable("icon_hint", None),
                                (Call("future_sight", from_current=False) if (check_boolean("call_future_sight")) else Show("future_sight"))
                            ]
                            hovered SetLocalVariable("icon_hint", "future_sight")
                            unhovered SetLocalVariable("icon_hint", None)
            
            if (icon_hint != None):
                frame:
                    background Frame("gui/namebox.png", xsize=120, ysize=25)
                    xalign 0.5
                    yoffset 15
                    xsize 120
                    ysize 25
                    at transform:
                        rotate 3
                        alpha 0.0
                        linear 0.1:
                            alpha 1.0

                    text _("Read Mind" if icon_hint == "mind_read" else ("Rewind Mind" if icon_hint == "mind_wipe" else "Future Sight")):
                        color "#000"
                        xalign 0.5
                        yalign 0.5
                        size 15

    
        key ["K_1", "pad_dpleft_press"]:
            action [
                SetLocalVariable("icon_hint", None),
                (Call("mind_read_effects", from_current=True) if (max_mind_reads == None or minds_read < max_mind_reads) else NullAction()),
            ]

        if (check_boolean("mind_wipe_available")):
            key ["K_2", "pad_dpup_press"]:
                action [
                    SetLocalVariable("icon_hint", None),
                    (Call("mind_wipe_pause", from_current=True) if (max_rewinds == None or minds_rewound < max_rewinds) else NullAction())
                ]

        if (check_boolean("future_sight_available")):
            key ["K_3", "pad_dpright_press"]:
                action [
                    SetLocalVariable("icon_hint", None),
                    (Call("future_sight", from_current=False) if (check_boolean("call_future_sight")) else Show("future_sight"))
                ]

screen psychic_splash(details):
    timer details["time"]:
        action Hide("psychic_splash")

    frame:
        xfill True
        yfill True
        background Solid ("#00000066")

        text _(details["line"]):
            color "#F2EE29"
            font "gui/twoweekendgo-bold.otf"
            xalign 0.025
            yalign 0.25
            size 96
            at fade_side_to_side(-10) 
            at transform:
                rotate -5

        frame:
            background Solid("#F2EE29")
            style "title_half_card_right"
            at transform:
                yoffset -1080
                linear 0.25:
                    yoffset -5

        image "images/menu/jack_menu.png":
            xalign 1.0
            yalign 1.0

            at transform:
                alpha 0.0
                zoom 0.75
                crop (103, 0, 1397, 1300)
                xoffset 100
                yoffset 1000

                linear 0.25:
                    alpha 1.0
                    yoffset 10
    
    if (not config.developer):
        key "K_TAB":
            action NullAction()

screen psychic_read():
    if False:   #Check for Lloyd/Jack
        timer 2.25:
            action Hide("psychic_read")

        image "images/menu/ring.png":
            at ring_mind_read_expand(0, 200)
    else:
        timer 3.25:
            action Hide("psychic_read")
    
        frame:
            background None
            xfill True
            yfill True
            at transform:
                rotate 5

            image Solid("#F2EE29"):
                ysize 2
                xsize 1
                xanchor 0.0
                ypos -300
                xpos -225
                at transform:
                    linear 0.25:
                        xsize 1920
                    pause 1.25
                    xsize 0
            image Solid("#F2EE29"):
                ysize 2
                xsize 1
                xanchor 1.0
                xpos 1700
                ypos -300
                at transform:
                    pause 1.5
                    xsize 1920
                    linear 1.75:
                        xsize 0

screen psychic_wipe():
    timer 2.5:
        action Hide("psychic_wipe")

    if False:
        image "images/menu/ring.png":
            at ring_mind_rewind_pause(0, 200)
    else:
        image "gui/icons/nail.png":
            xalign 0.5
            yalign 0.0
            yoffset -200
            at transform:

                linear 0.25:
                    yoffset 400
                pause 0.5
                linear 0.25:
                    alpha 0.0

        image "gui/icons/nail.png":
            xalign 0.25
            yalign 0.6
            at transform:
                rotate -135
                alpha 0.0
                pause 0.2

                linear 0.25:
                    #alpha 1.0
                    yoffset -345
                    xoffset 430
                pause 0.5
                linear 0.25:
                    alpha 0.0

        image "gui/icons/nail.png":
            xalign 0.75
            yalign 0.6
            at transform:
                #zoom 0.75
                rotate 135
                alpha 0.0
                pause 0.4

                linear 0.25:
                    #alpha 1.0
                    yoffset -345
                    xoffset -430
                pause 0.5
                linear 0.25:
                    alpha 0.0

screen future_sight(returnable=False, fadein=True, fadeout=True):
    modal True
    zorder 105
    default viewing = "current"
    default info = get_future_sight_info()

    frame:
        xfill True
        yfill True
        background Solid ("#00000066")

    frame:
        background Solid("#000")
        xalign 0.5
        yalign 0.5
        xsize 1440
        ysize 840

        if (fadein):
            at transform:
                on show:
                    xoffset 500
                    alpha 0.0
                    linear 0.35:
                        xoffset 0
                        alpha 1.0
        if (fadeout):
            at transform:
                on hide:
                    xoffset 0
                    linear 0.35:
                        xoffset 500
                        alpha 0.0

        frame:
            background Image("gui/future_sight_frame.png")

            xalign 0.5
            yalign 0.5
            xsize 1400
            ysize 800

            hbox:
                frame:
                    background None
                    xsize 0.33
                    image "images/sprites/" + info["picture"]:
                        xoffset 15
                        yoffset -18
                        at transform:
                            zoom 0.205
                            matrixcolor TintMatrix("#000")
                            alpha (0.0 if fadein else 0.8)

                            pause (0.4 if fadein else 0.0)
                            linear 0.25:
                                alpha 0.8
                    image "images/sprites/" + info["picture"]:
                        at transform:
                            zoom 0.2

                frame:
                    background None
                    xsize 865

                    vbox:
                        yoffset 50
                        spacing 20
                        text _(info["description"]):
                            color "#000"
                            xalign 0.0
                            yalign 0.5

                        if (check_boolean("future_sight_types")):
                            hbox:
                                spacing 25
                                textbutton _("CURRENT"):
                                    style "future_sight_type_button"
                                    selected viewing == "current"
                                    action SetScreenVariable("viewing", "current")

                                textbutton _("GENERAL"):
                                    style "future_sight_type_button"
                                    selected viewing == "general"
                                    action [
                                        (Show("modal_popup", message="These keywords may or may not be present in the current scene. Reading the corresponding thought will unlock more information about this character.", option_actions=[Hide("modal_popup")]) if not check_boolean("future_sight_general_message") else NullAction()),
                                        Function(add_boolean, "future_sight_general_message"),
                                        SetScreenVariable("viewing", "general")
                                    ]

                                textbutton _("HISTORY"):
                                    style "future_sight_type_button"
                                    selected viewing == "history"
                                    action [
                                        (Show("modal_popup", message="Information you discover about this character will be displayed here.", option_actions=[Hide("modal_popup")]) if not check_boolean("future_sight_history_message") else NullAction()),
                                        Function(add_boolean, "future_sight_history_message"),
                                        SetScreenVariable("viewing", "history")
                                    ]

                        vbox:
                            style_prefix "future_sight_checkbox"
                            if (viewing == "current"):
                                for current in info["current"]:
                                    hbox:
                                        frame:
                                            text _(current["keyword"])
                                        frame:
                                            style ("future_sight_checkbox_checked" if current["discovered"] else "future_sight_checkbox")
                            elif (viewing == "general"):
                                for general in info["general"]:
                                    hbox:
                                        frame:
                                            text _(general["keyword"])
                                        frame:
                                            style ("future_sight_checkbox_checked" if general["discovered"] else "future_sight_checkbox")
                            elif (viewing == "history"):
                                text _(get_future_sight_history(person=info["person"]))

                    textbutton _("RETURN"):
                        style "yellow_button"
                        xalign 0.5
                        yalign 0.925
                        hover_background Frame("gui/button/button_hover_allblack.png")
                        action [
                            Hide("future_sight"),
                            (Return() if returnable else Hide("future_sight"))
                        ]

        frame:
            background None
            ysize 75
            xsize 480
            yoffset -170
            xoffset -30
            at transform:
                rotate -25

            text _(info["title"]):
                color "#F2EE29"
                font "gui/Decade__.ttf"
                xalign 0.2
                yalign 0.5
                size 50
                yoffset 5

    if (check_boolean("future_sight_types")):
        key "pad_leftshoulder_press":
            if (viewing == "general"):
                action SetScreenVariable("viewing", "current")
            elif (viewing == "history"):
                action [
                    (Show("modal_popup", message="These keywords may or may not be present in the current scene. Reading the corresponding thought will unlock more information about this character.", option_actions=[Hide("modal_popup")]) if not check_boolean("future_sight_general_message") else NullAction()),
                    Function(add_boolean, "future_sight_general_message"),
                    SetScreenVariable("viewing", "general")
                ]
        key "pad_rightshoulder_press":
            if (viewing == "current"):
                action [
                    (Show("modal_popup", message="These keywords may or may not be present in the current scene. Reading the corresponding thought will unlock more information about this character.", option_actions=[Hide("modal_popup")]) if not check_boolean("future_sight_general_message") else NullAction()),
                    Function(add_boolean, "future_sight_general_message"),
                    SetScreenVariable("viewing", "general")
                ]
            elif (viewing == "general"):
                action [
                    (Show("modal_popup", message="Information you discover about this character will be displayed here.", option_actions=[Hide("modal_popup")]) if not check_boolean("future_sight_history_message") else NullAction()),
                    Function(add_boolean, "future_sight_history_message"),
                    SetScreenVariable("viewing", "history")
                ]
            

style future_sight_type_button:
    selected_background Frame("gui/button/button_squareish.png")
    left_padding 10
    right_padding 10
    top_padding 12

style future_sight_type_button_text:
    color "#000"
    font "gui/chubhand.ttf"
    hover_underline True

style future_sight_checkbox_frame:
    xsize 755
    ysize 60
    background "gui/keyword_frame.png"

style future_sight_checkbox_text:
    color "#000"
    xalign 0.5
    yalign 0.5

style future_sight_checkbox:
    xsize 60
    ysize 60
    background "gui/keyword_checkbox.png"
style future_sight_checkbox_checked is future_sight_checkbox:
    background "gui/keyword_checkbox_checked.png"

screen map_navigation(destinations):
    default xpos = 0
    default ypos = 0
    default fade_delay = 1
    default selected_destination = None

    timer 1.0:
        action SetScreenVariable("fade_delay", 0)

    frame:
        background Solid("#D1CE21")
        xalign 0.5
        yalign 0.5
        xsize 1920
        ysize 1080

        text _("SELECT YOUR DESTINATION"):
            font "gui/Decade__.ttf"
            color "#000"
            size 80
            xalign 0.5
            yalign 0.05
            at trans_fade(0.5, 0.5), fade_side_to_side(-300, 0.25)

        hbox:
            xalign 0.5
            yalign (0.7 if selected_destination == None else 0.5)
            spacing 100

            if (selected_destination == None):
                vbox:
                    ysize 751
                    xsize 640
                    vbox:
                        yalign 0.5
                        xalign 0.5
                        spacing 25
                        for i, destination in enumerate(destinations):
                            textbutton _(destination["label"]):
                                style "destination_button"
                                xsize 500
                                action [
                                    SetScreenVariable("selected_destination", destination),
                                    SetScreenVariable("xpos", 0),
                                    SetScreenVariable("ypos", 0),
                                ]
                                hovered [
                                    SetScreenVariable("xpos", destination["xcoord"]),
                                    SetScreenVariable("ypos", destination["ycoord"])
                                ]
                                selected False
                                at trans_fade(fade_delay, 1.0), fade_side_to_side(-200, fade_delay)
                    #textbutton _("SAVE GAME"):
                    #    xalign 0.5
                    #    yalign 1.0
                    #    text_color "#000"
                    #    text_font "gui/Decade__.ttf"
                    #    text_hover_underline True
                    #    action ShowMenu("saves_list", title="SAVE")
                    #    at trans_fade(1.5, 1.0)

                frame:
                    xsize 640
                    ysize 763
                    background Frame("images/map.png")
                    at trans_fade(fade_delay, 1.0), fade_side_to_side(200, fade_delay)

                    frame:
                        style "map_y_coord"
                        xpos 0
                        at transform:
                            ease 1.0:
                                xpos xpos

                    frame: 
                        style "map_x_coord"
                        ypos 0
                        at transform:
                            ease 1.0:
                                ypos ypos
            else:
                vbox:
                    xalign 0.5
                    yoffset 25
                    spacing 35
                    
                    vbox:
                        spacing 10

                        text _(selected_destination["label"]):
                            color "#000"
                            font "gui/chubhand.ttf"
                            size 72
                            at trans_fade(0.25, 0.5), fade_side_to_side(-50, 0.25)

                        frame:
                            xsize 864
                            ysize 486
                            xoffset 180
                            background Frame("images/backgrounds/venue_exterior.png" if selected_destination["key"] == "venue" else "images/backgrounds/restaurant_night.png")
                            at trans_fade(0.25, 0.5), fade_side_to_side(50, 0.25)

                    hbox:
                        at trans_fade(0.25, 0.5), fade_up_down(50, 0.25)
                        spacing 50
                        frame:
                            background None
                            xsize 900

                            if (selected_destination["key"] == "venue"):
                                text _("Isn’t there some small underground place near here that plays jazz or one of those made-up music genres? They’ve got to have some booze there...people wouldn’t go there if they didn’t have any."):
                                    style "destination_description"
                            elif (selected_destination["key"] == "restaurant"):
                                text _("Do they have chips at this place? I kind of want chips now...Oh, I know! I’ll trick them into thinking they have chips if they don’t, and make them make some for me!"):
                                    style "destination_description"

                        vbox:
                            xsize 200
                            spacing 15
                            yoffset 5
                
                            textbutton _("CONFIRM"):
                                style "destination_option"
                                #Again, worry about making this more dynamic later
                                action Jump("prologue_music_venue" if selected_destination["key"] == "venue" else "prologue_restaurant")
                            textbutton _("RETURN"):
                                style "destination_option"
                                action SetScreenVariable("selected_destination", None)
            

style map_y_coord:
    xmaximum 2
    yfill True
    background Solid("#000")

style map_x_coord:
    ymaximum 2
    xfill True
    background Solid("#000")

style destination_button is yellow_button:
    padding (10, 30, 10, 30)

style destination_button_text is yellow_button_text:
    font "gui/chubhand.ttf"
    yoffset 5
    size 54

style destination_option is yellow_button:
    xsize 250
    xalign 0.5

style destination_option_text is yellow_button_text:
    font "gui/chubhand.ttf"
    size 44
    yoffset 4

style destination_description:
    color "#000"
    size 34

screen locked_message(message):
    frame:
        background Frame("gui/textbox.png")
        padding (50, 50, 50, 50)
        xalign 0.5
        yalign 0.9
        at transform:
            alpha 0.0
            xoffset -50
            linear 0.3:
                alpha 1.0
                xoffset 0

        text _(message):
            text_align 0.5
            color "#000"
            xalign 0.5
            yalign 0.5
            size 25

screen upgrades_screen():
    default selected = None

    frame:
        xsize 1400
        ysize 800
        xalign 0.5
        yalign 0.5
        padding (50, 50, 50, 50)

        background Solid("#F2EE29")

        text _("Psychic Upgrades"):
            xalign 0.5
            yalign 0.0

        vbox:
            yalign 0.4

            hbox:
                text _("Mind Reads")
                textbutton _(str(3)):
                    action NullAction()
                textbutton _(str(4)):
                    action (NullAction() if max_mind_reads != 3 else SetScreenVariable("selected", "mr_4"))
                textbutton _(str(5)):
                    action (NullAction() if max_mind_reads != 4 else SetScreenVariable("selected", "mr_5"))
                textbutton _(str(6)):
                    action (NullAction() if max_mind_reads != 5 else SetScreenVariable("selected", "mr_6"))

            hbox:
                text _("Rewinds")
                textbutton _(str(1)):
                    action NullAction()
                textbutton _(str(2)):
                    action (NullAction() if max_rewinds != 1 else SetScreenVariable("selected", "rw_2"))
                textbutton _(str(3)):
                    action (NullAction() if max_rewinds != 2 else SetScreenVariable("selected", "rw_3"))
                textbutton _(str(4)):
                    action (NullAction() if max_rewinds != 3 else SetScreenVariable("selected", "rw_4"))

            hbox:
                text _("Future Visions")
                textbutton _(str(0)):
                    action NullAction()
                textbutton _(str(1)):
                    action (NullAction() if max_flash_forwards != 0 else SetScreenVariable("selected", "fv_1"))
                textbutton _(str(2)):
                    action (NullAction() if max_flash_forwards != 1 else SetScreenVariable("selected", "fv_2"))
                textbutton _(str(3)):
                    action (NullAction() if max_flash_forwards != 2 else SetScreenVariable("selected", "fv_3"))

        #Deffo throw some flavour text in somewhere, and at the bottom do a "You will be able to do X Y times" or whatever

        if (selected != None):
            textbutton _("Confirm"):
                xalign 0.5
                yalign 1.0
                action [        #Prolly a better way to do this - should I set two variables on the textbuttons?
                    (SetVariable("max_mind_reads", 4) if selected == "mr_4" else NullAction()),
                    (SetVariable("max_mind_reads", 5) if selected == "mr_5" else NullAction()),
                    (SetVariable("max_mind_reads", 6) if selected == "mr_6" else NullAction()),
                    (SetVariable("max_rewinds", 2) if selected == "rw_2" else NullAction()),
                    (SetVariable("max_rewinds", 3) if selected == "rw_3" else NullAction()),
                    (SetVariable("max_rewinds", 4) if selected == "rw_4" else NullAction()),
                    (SetVariable("max_flash_forwards", 1) if selected == "fv_1" else NullAction()),
                    (SetVariable("max_flash_forwards", 2) if selected == "fv_2" else NullAction()),
                    (SetVariable("max_flash_forwards", 3) if selected == "fv_3" else NullAction()),
                    Hide("upgrades_screen"),
                    Show("debug")
                ]

screen flow_chart():
    tag menu
    default zoom_level = 1.0
    default offset = 10
    default zooming_in = False
    default zooming_out = False
    default scrolling_up = False
    default scrolling_down = False
    default active_control = None
    default show_content = False
    default loaded_node = None

    timer 1.2:
        action SetScreenVariable("show_content", True)

    use game_menu("FLOW\n CHART", 88):

        if (zooming_in):
            timer (0.01):
                action SetScreenVariable("zoom_level", zoom_level + 0.01 if zoom_level < 1 else 1)
                repeat True
        
        if (zooming_out):
            timer (0.01):
                action SetScreenVariable("zoom_level", zoom_level - 0.01 if zoom_level > 0.25 else 0.25)
                repeat True

        if (scrolling_up):
            timer (0.01):
                action SetScreenVariable("offset", offset - 2 if offset > -350 else -350)
                repeat True
        
        if (scrolling_down):
            timer (0.01):
                action SetScreenVariable("offset", offset + 2 if offset < 350 else 350)
                repeat True

        #Mouse wheel up/down should scroll it up/down
                    
        if (show_content):
            #text _(str(offset))
            frame:
                xfill True
                yfill True
                xalign 0.5
                yalign 0.5
                background None

                at trans_fade(0.0, 0.5)
                at transform:
                    yoffset offset
                    zoom zoom_level

                vbox:
                    hbox:
                        xsize 960
                        spacing 0

                        frame:
                            background None
                            xalign 0.0
                            xsize 0

                            text _("PROLOGUE"):
                                color "#000"
                                font "gui/chubhand.ttf"
                                size 96
                        
                        vbox:
                            xalign 1.0
                            yoffset 60
                            xsize 98
                            spacing 10

                            frame: 
                                background Solid("#000")
                                xsize 70
                                ysize 70
                                padding (6, 6, 6, 6)
                                at transform:
                                    rotate -45

                                imagebutton:
                                    idle Solid("#F2EE29")
                                    hover Solid("#D1CE21")
                                    action SetScreenVariable("loaded_node", "prologue_1")
                                        
                            image Solid("#000"):
                                xsize 5
                                ysize 125
                                xalign 0.5

                            frame: 
                                background Solid("#000")
                                xsize 70
                                ysize 70
                                padding (6, 6, 6, 6)
                                at transform:
                                    rotate -45

                                imagebutton:
                                    idle Solid("#F2EE29")
                                    hover Solid("#D1CE21")
                                    action SetScreenVariable("loaded_node", "prologue_2")

                            image Solid("#000"):
                                xsize 5
                                ysize 125
                                xalign 0.5
                        
                    image Solid("#000"):
                        xsize 1700
                        ysize 5
                    
                    hbox:
                        xsize 960
                        ysize 600
                        spacing 0

                        frame:
                            background None
                            xalign 0.0
                            xsize 400

                            text _("DAY 1"):
                                color "#000"
                                font "gui/chubhand.ttf"
                                size 96
                                yoffset 10
                        
                        vbox:
                            xalign 1.0
                            yoffset 60
                            xsize 98
                            spacing 10

                            frame: 
                                background Solid("#000")
                                xsize 70
                                ysize 70
                                padding (6, 6, 6, 6)
                                at transform:
                                    rotate -45

                                #image Solid("#F2EE29")

                            #image Solid("#000"):
                            #    xsize 5
                            #    ysize 125
                            #    xalign 0.5

                            #frame: 
                            #    background Solid("#000")
                            #    xsize 70
                            #    ysize 70
                            #    padding (6, 6, 6, 6)
                            #    at transform:
                            #        rotate -45

                                #image Solid("#F2EE29")

                            #image Solid("#000"):
                            #    xsize 5
                            #    ysize 125
                            #    xalign 0.5
                            
                            #frame: 
                            #    background Solid("#000")
                            #    xsize 70
                            #    ysize 70
                            #    padding (6, 6, 6, 6)
                            #    at transform:
                            #        rotate -45

                                #image Solid("#F2EE29")
                                        
                            #image Solid("#000"):
                            #    xsize 5
                            #    ysize 125
                            #    xalign 0.5
                        
                    image Solid("#000"):
                        xsize 1700
                        ysize 5


                    #textbutton _("End of Day #1" if renpy.can_load(str(game_id) + "_A_01_03") else "-"):
                    #    action (NullAction() if not renpy.can_load(str(game_id) + "_A_01_03") else [
                            #Function(renpy.log, days),
                    #        Function(renpy.load, str(game_id) + "_A_01_03")
                    #    ])
                    #textbutton _("End of Day #2" if renpy.can_load(str(game_id) + "_A_02_03") else "-"):
                    #    action (NullAction() if not renpy.can_load(str(game_id) + "_A_02_03") else [
                            #Function(renpy.log, days),
                    #        Function(renpy.load, str(game_id) + "_A_02_03")
                    #    ])
                    #textbutton _("End of Day #3" if renpy.can_load(str(game_id) + "_A_03_03") else "-"):
                    #    action (NullAction() if not renpy.can_load(str(game_id) + "_A_03_03") else [
                            #Function(renpy.log, days),
                    #        Function(renpy.load, str(game_id) + "_A_03_03")
                    #    ])
                    #textbutton _("End of Day #4" if renpy.can_load(str(game_id) + "_A_04_03") else "-"):
                    #    action (NullAction() if not renpy.can_load(str(game_id) + "_A_04_03") else [
                            #Function(renpy.log, days),
                    #        Function(renpy.load, str(game_id) + "_A_04_03")
                    #    ])

                if (loaded_node is not None):
                    use node_selected_display(loaded_node)

            vbox:
                xalign 0.98
                yalign 0.62
                spacing 30

                vbox:
                    spacing 2
                    xalign 0.5

                    imagebutton:
                        auto "gui/arrow_up_%s.png"
                        #hover "gui/arrow_up_hover.png"
                        if (active_control == "down"):
                            keysym "mousedown_1"
                            alternate_keysym "mouseup_1"
                        action SetScreenVariable("scrolling_down", True)
                        alternate SetScreenVariable("scrolling_down", False)
                        hovered SetScreenVariable("active_control", "down")
                        unhovered SetScreenVariable("active_control", None)

                    imagebutton:
                        auto "gui/arrow_down_%s.png"
                        if (active_control == "up"):
                            keysym "mousedown_1"
                            alternate_keysym "mouseup_1"
                        action SetScreenVariable("scrolling_up", True)
                        alternate SetScreenVariable("scrolling_up", False)
                        hovered SetScreenVariable("active_control", "up")
                        unhovered SetScreenVariable("active_control", None)

                hbox:
                    spacing 5
                    xalign 0.5

                    imagebutton:
                        auto "gui/icons/zoom_out_%s.png"
                        if (active_control == "zoom_out"):
                            keysym "mousedown_1"
                            alternate_keysym "mouseup_1"
                        action SetScreenVariable("zooming_out", True)
                        alternate SetScreenVariable("zooming_out", False)
                        hovered SetScreenVariable("active_control", "zoom_out")
                        unhovered SetScreenVariable("active_control", None)
                    imagebutton:
                        auto "gui/icons/zoom_in_%s.png"
                        if (active_control == "zoom_in"):
                            keysym "mousedown_1"
                            alternate_keysym "mouseup_1"
                        action SetScreenVariable("zooming_in", True)
                        alternate SetScreenVariable("zooming_in", False)
                        hovered SetScreenVariable("active_control", "zoom_in")
                        unhovered SetScreenVariable("active_control", None)

        #Ensure that the timeline won't flow over the title by rendering a duplicate on top of it
        frame:
            style "bottom_left_frame"
            at menu_bottom_left_slide, trans_fade(1.5, 0.01)

        text _("FLOW\n CHART"):
            font "gui/Decade__.ttf"
            size 88
            color "#F2EE29"
            xalign 0.0125
            yalign 0.95
            at trans_fade(1.5, 0.01)

screen node_selected_display(loaded_node):
    zorder 100
    frame:
        #xsize 400
        ysize 200
        padding (10, 10, 10, 10)

        at transform:
            xsize 0
            ease 0.5:
                xsize 400

        if (loaded_node == "prologue_1"):
            xpos 980
            ypos 50

            text _("prologue_1 text"):
                style "node_active_text"
                at trans_fade(0.6, 0.5)
                
        elif (loaded_node == "prologue_2"):
            xpos 980
            ypos 300

            text _("Jack chose to go to the Restaurant. While there, he had a psychic vision of an attack that would be happening soon."):
                style "node_active_text"
                at trans_fade(0.6, 0.5)
            
        hbox:
            yalign 0.9
            xsize 380
            at trans_fade(1.1, 0.5)
            textbutton _("Jump"):
                xalign 0.0
                style "yellow_button"
                text_font "gui/chubhand.ttf"
                text_yoffset 2
                action NullAction()

            textbutton _("Back"):
                xalign 1.0
                style "yellow_button"
                text_font "gui/chubhand.ttf"
                text_yoffset 2
                action SetScreenVariable("loaded_node", None)

style node_active_text:
    color "#000"
    size 18

screen saves_list(title="LOAD"):
    tag menu
    default hover_row = None
    default selected_save = None
    default show_content = False

    timer 1.2:
        action SetScreenVariable("show_content", True)

    use game_menu(title, 96, Return() if title == "SAVE" else None):

        if (show_content):
            vbox:
                yalign 0.25
                at trans_fade(0.0, 0.5)

                for i in range(15):
                    frame:
                        style_prefix "save_row"
                        background Solid("#F2EE29" if (hover_row is not i and selected_save is not i) else "#000")
                        xoffset ((i * 50) -400 if i > 9 else 65)

                        if (renpy.can_load("1-" + str(i + 1))):     #Will prolly need to fix this up when I add in proper save functionality
                            hbox:
                                spacing 0

                                textbutton _(renpy.slot_json("1-" + (str(i + 1))).get('_save_name', '')):
                                    text_color ("#F2EE29" if hover_row == i or selected_save == i else "#000")
                                    text_underline selected_save == i
                                    hovered SetScreenVariable("hover_row", i)
                                    unhovered SetScreenVariable("hover_row", None)
                                    xsize 525
                                    action SetScreenVariable("selected_save", i)
                                textbutton _(add_date_suffix(FileTime(i + 1, format="%d")) + FileTime(i + 1, format=_("{#file_time}%B %Y, %H:%M"), empty=_("empty slot"))):
                                    text_color ("#F2EE29" if hover_row == i or selected_save == i else "#000")
                                    text_underline selected_save == i
                                    hovered SetScreenVariable("hover_row", i)
                                    unhovered SetScreenVariable("hover_row", None)
                                    action SetScreenVariable("selected_save", i)
                        else:
                            hbox

                    image Solid("#3B3B3B"):
                        xsize 875
                        ysize 2
                        xoffset ((i * 50) -400 if i > 9 else 65)

            frame:
                style_prefix "save_details"
                background None #Solid("#FFFC5E")
                xalign 0.69
                yalign 0.135
                xsize 450
                ysize 525

                vbox:
                    xsize 450
                    spacing 50
                    if (title == "SAVE" and find_next_save() != "0"):
                        textbutton _("NEW SAVE"):
                            style "light_yellow_button_small"
                            action Show("save_name", filename=default_save_name()) 
                            xsize 240
                            ysize 45
                            text_font "gui/chubhand.ttf"
                            text_yoffset 3
                            text_size 40
                            text_selected_color "#000"
                            text_hover_color "#FFFC5E"
                            xalign 0.5
                            padding (40, 25, 40, 25)
                    if (selected_save is not None):
                        vbox:
                            spacing 20

                            add FileScreenshot(selected_save + 1):
                                xalign 0.5

                            text _(renpy.slot_json("1-" + (str(selected_save + 1))).get('_save_name', '')):
                                style "save_name"
                            text _("Prologue"):
                                style "save_details"
                            text _(add_date_suffix(FileTime(selected_save + 1, format="%d", empty=(0))) + FileTime(selected_save + 1, format=_("{#file_time}%B %Y, %H:%M"))):
                                style "save_date"

                            hbox:
                                xfill True
                                spacing 5
                                box_align 0.5
                                if (title == "LOAD"):
                                    textbutton _("Load"):
                                        style "light_yellow_button_small"
                                        action (Function(renpy.load, "1-" + str(selected_save + 1)))
                                        xsize 120
                                        text_font "gui/chubhand.ttf"
                                        text_yoffset 2
                                        text_size 28
                                else:
                                    textbutton _("Save"):
                                        style "light_yellow_button_small"
                                        action Show("modal_popup", message="Are you sure you want to overwrite this save?", option_labels=["Yes", "No"], option_actions=[[Function(renpy.save, "1-" + str(selected_save + 1), renpy.slot_json("1-" + (str(selected_save + 1))).get('_save_name', '')), Hide("modal_popup")], Hide("modal_popup")])
                                        xsize 120
                                        text_font "gui/chubhand.ttf"
                                        text_yoffset 2
                                        text_size 28
                                textbutton _("Delete"):
                                    style "light_yellow_button_small"
                                    action ([FileDelete(selected_save + 1), SetScreenVariable("selected_save", None)])
                                    text_font "gui/chubhand.ttf"
                                    text_yoffset 2
                                    text_size 28
                
style bottom_left_frame:
    background Solid("#000")
    xsize 850
    ysize 400
    xalign 0.0
    yalign 0.8
    xoffset -750

style top_right_frame:
    background Solid("#000")
    xsize 1050
    ysize 500
    xalign 1.0
    yalign 0.0
    xoffset 1200
    yoffset 300

style bottom_right_frame:
    background Solid("#000")
    xsize 1050
    ysize 500
    xalign 1.0
    yalign 1.0
    xoffset 1250

style save_row_hbox:
    xsize 863
    ysize 36

style save_row_button_text:
    size 20

style save_details_vbox:
    spacing 10

style save_name:
    color "#000"
    xalign 0.5
    text_align 0.5
    size 35

style save_details:
    color "#000"
    xalign 0.5
    text_align 0.5
    size 24

style save_date is save_details:
    size 20

style light_yellow_button is yellow_button:
    background Frame("gui/button/button_light_idle.png")
    hover_background Frame("gui/button/button_light_hover.png")

style light_yellow_button_text is yellow_button_text:
    hover_color "#FFFC5E"

style light_yellow_button_small is light_yellow_button:
    padding (20, 5, 20, 5)

style light_yellow_button_small_text is light_yellow_button_text

screen modal_base(short=True):
    modal True
    zorder 200

    frame:
        xfill True
        yfill True
        background Solid ("#f2ef2973")
        at trans_fade(0.0, 0.5)

        frame:
            background Solid("#000000")
            xsize 940
            ysize (490 if short else 980)
            xalign 0.5
            yalign 0.5

            frame:
                background Solid("#F2EE29")
                xsize 900
                ysize (450 if short else 940)
                xalign 0.5
                yalign 0.5

                vbox:
                    xalign .5
                    yalign .5
                    spacing 45

                    transclude

screen modal_popup(message, option_labels=["OK"], option_actions=[Return()], short=True):
    modal True
    zorder 110
    use modal_base(short):
        label _(message):
            style "confirm_prompt"
            text_color "#000"
            xalign 0.5

        hbox:
            xalign 0.5
            yalign 1.0
            #yoffset 70

            for (i, label) in enumerate(option_labels):
                textbutton _(label):
                    action option_actions[i]
                    style "yellow_button"
                    hover_background Frame("gui/button/button_hover_allblack.png")

    if (len(option_labels) == 1):
        key ["K_ESCAPE", "K_RETURN", "K_SPACE", "pad_a_press"]:
            action option_actions[0]

screen save_name(filename):
    modal True
    default input_variable = (filename if len(filename) > 0 else '')

    use modal_base:
        text "Save File Name":
            font "gui/chubhand.ttf"
            color "#000"
            size 50
            xalign 0.5

        vbox:
            spacing 2
            ysize 50

            input:
                yalign 0.5
                xmaximum 700
                value ScreenVariableInputValue('input_variable')
                length 40
                exclude "\[\{"
            frame:
                background Solid("#000")
                ysize 2
                xsize 700

        hbox:
            xsize 700
            textbutton _("Cancel"):
                xalign 0.0
                text_hover_underline True
                action [
                    Hide("save_name"),
                ]

            textbutton _("Save"):
                xalign 1.0
                text_hover_underline True
                action [
                    Function(renpy.save, find_next_save(), input_variable if len(input_variable) > 0 else default_save_name()),
                    Hide("save_name"),
                ]

    key "K_RETURN":
        action [
            Function(renpy.save, find_next_save(), input_variable if len(input_variable) > 0 else default_save_name()),
            Hide("save_name"),
        ]

screen pause_menu():
    tag menu
    
    frame:
        background Solid("#000")
        style "title_half_card"
    frame:
        background Solid("#F2EE29")
        style "title_half_card_right"

    frame:
        background Solid("#F2EE29")
        style "title_half_card"
        at title_card_slide("down")

    frame: 
        background Solid("#000")
        style "title_half_card_right"
        at title_card_slide("up")

    vbox:
        xalign 0.5
        yalign 0.05
        spacing 0

        at trans_fade(0.5, 0.5)

        text _("{color=#000}BLACK{/color}{color=#F2EE29}MIND{/color}"):
            font "gui/Decade__.ttf"
            size 90
            xoffset -18
        text _("{color=#000}PSYCHIC SOCIAL{/color}{color=#F2EE29} SIMULATOR{/color}"):
            font "gui/chubhand.ttf"
            size 18
            xalign 0.5
            yalign 0.25
            xoffset -30
            kerning 12.6

    vbox:
        xalign 0.3
        yalign 0.55
        spacing 50
        at trans_fade(1.0, 0.5), fade_side_to_side(-1000, 0.5)
        textbutton _("Locked"): #"Flow Chart"):
            style "yellow_button_on_yellow"
            #action ShowMenu("flow_chart")
            action (Show("modal_popup", message="This function is disabled during the demo", option_actions=[Hide("modal_popup")]) if clickable_button() else NullAction())
        textbutton _("Locked"): #"Characters"):
            style "yellow_button_on_yellow"
            #action ShowMenu("characters")
            action (Show("modal_popup", message="This function is disabled during the demo", option_actions=[Hide("modal_popup")]) if clickable_button() else NullAction())
        #textbutton _("Load"):
        #    style "yellow_button_on_yellow"
        #    action (ShowMenu("saves_list") if clickable_button() else NullAction())
        textbutton _("Return"):
            style "yellow_button_on_yellow"
            action (Return() if clickable_button() else NullAction())
        textbutton _("Main Menu"):
            style "yellow_button_on_yellow"
            action (MainMenu() if clickable_button() else NullAction())

    vbox:
        xalign 0.775
        yalign 0.75
        spacing 50
        at trans_fade(1.0, 0.5), fade_side_to_side(1000, 0.5)
        #textbutton _("Locked"): #Psychic Powers"):
        #    style "black_button_on_black"
            #action ShowMenu("upgrades_screen")
        #    action (Show("modal_popup", message="This function is disabled during the demo", option_actions=[Hide("modal_popup")]) if clickable_button() else NullAction())
        textbutton _("Locked"): #Notes"):
            style "black_button_on_black"
            #action ShowMenu("notes")
            action (Show("modal_popup", message="This function is disabled during the demo", option_actions=[Hide("modal_popup")]) if clickable_button() else NullAction())
        textbutton _("Settings"):
            style "black_button_on_black"
            action (ShowMenu("preferences") if clickable_button() else NullAction())
        textbutton _("Help"):
            style "black_button_on_black"
            action (ShowMenu("help") if clickable_button() else NullAction())
        textbutton _("Quit Game"):
            style "black_button_on_black"
            action (Quit() if clickable_button() else NullAction())

    #use cash_money("pause_menu")

style yellow_button_on_yellow:
    background Frame("gui/button/button_idle.png")
    hover_background Frame("gui/button/button_idle.png")
    padding (80, 20, 80, 20)
    xsize 486

style yellow_button_on_yellow_text:
    color "#000"
    font "gui/chubhand.ttf"
    hover_underline True
    size 65
    yoffset 5
    xalign 0.5

style black_button_on_black is yellow_button_on_yellow:
    background Frame("gui/button/button_hover.png")
    hover_background Frame("gui/button/button_hover.png")
    padding (80, 20, 80, 20)
    xsize 603

style black_button_on_black_text is yellow_button_on_yellow_text:
    color "#F2EE29"

screen chapter_breaks(title, paragraph):
    default can_continue = False

    timer 2.75:
        action SetScreenVariable("can_continue", True)

    frame:
        background Solid("#000")
        style "title_half_card"
    frame:
        background Solid("#F2EE29")
        style "title_half_card_right"

    frame:
        background Solid("#F2EE29")
        style "title_half_card"
        at title_card_slide("down")

    frame: 
        background Solid("#000")
        style "title_half_card_right"
        at title_card_slide("up")

    vbox:
        xalign 0.98
        yalign 0.2
        at trans_fade(0.5, 0.5), fade_side_to_side(100)

        text _("BLACKMIND"):
            font "gui/Decade__.ttf"
            size 150
            color "#F2EE29"

        text _("PSYCHIC SOCIAL SIMULATOR"):
            font "gui/chubhand.ttf"
            color "#F2EE29"
            size 38
            kerning 20

    text _("OPEN YOUR THIRD EYE"):    
        color "#000"
        xalign 0.035
        yalign 0.05
        size 20
        at trans_fade(1.25, 1.5), fade_side_to_side(-50, 0.75)

    vbox:
        xalign 0.05
        yalign 0.6
        spacing 50
        xmaximum 700
        
        text _(title):
            color "#000"
            font "gui/chubhand.ttf"
            size 100
            xoffset -10
            at trans_fade(1.25, 1.5), fade_side_to_side(-100, 0.75)

        text _(paragraph):
            color "#000"
            at trans_fade(2.0, 1.5), fade_side_to_side(-100, 1.5)

    if (can_continue):
        text _("Press any key to continue"):
            color "#F2EE29"
            xalign 0.98
            yalign 0.95
            at transform:
                alpha 0.0
                linear 1.0:
                    alpha 1.0
                linear 0.5:
                    alpha 0.0
                repeat

        use any_key(Return())
    
    key "mouseup_3":
        action NullAction()

screen calendar(day, section, sections=4):
    frame: 
        background None
        xsize 600
        ysize 80

        xpos 270
        ypos -550
        
        at transform:
            rotate -40
        
        image Solid("#000"):
            xsize 50
            xanchor 1.0
            at transform:
                linear 0.5:
                    xsize 600
    
    frame:
        background None
        xsize 600
        ysize 80
        
        ypos -225
        xpos -80
        at transform:
            rotate -30

        image Solid("#F2EE29"):
            xsize 50
            at transform:
                linear 0.5:
                    xsize 600

        text _(day):
            yalign 0.5
            yoffset 3
            xalign 0.15
            color "#000"
            font "gui/chubhand.ttf"
            size 50

            at transform:
                xoffset -400
                pause 0.25
                linear 0.5:
                    xoffset 0

        hbox:
            xalign (0.6 if sections == 4 else 0.5)
            yalign 0.5
            spacing 5
            at transform:
                xoffset 400
                pause 0.25
                linear 0.5:
                    xoffset 0

            for i in range(sections):
                frame: 
                    background Solid("#000")
                    xsize 20
                    ysize 20
                    padding (3, 3, 3, 3)
                    at transform:
                        rotate -45

                    if (i <= section - 1):
                        image Solid("#F2EE29")

screen conversation_history(initial_expanded = False, show_button = True, initial_opened=False):
    default expanded = initial_expanded
    default opened = initial_opened

    if (show_button and renpy.get_screen("say")):
        textbutton _("HISTORY" if not expanded else "HIDE"):
            style "yellow_button"
            text_font "gui/chubhand.ttf"
            text_yoffset 2

            xalign 0.96
            yalign 0.8
            xsize 195
            action [
                SetScreenVariable("expanded", expanded == False),
                SetScreenVariable("opened", True),
            ]
            selected False
            text_selected_color "#F2EE29"
            text_hover_color "#F2EE29"

    if (opened):
        frame:
            background None
            xsize 500
            ysize 650
            yalign 0.415
            xalign 0.95
            xoffset 60

            image Solid("#000"):
                yanchor 1.0
                yoffset 630
                if (expanded):
                    at transform:
                        ysize 0
                        linear 0.5:
                            ysize 650
                else:
                    at transform:
                        ysize 650
                        linear 0.5:
                            ysize 0

            image Solid("#F2EE29"):
                yanchor 1.0
                yoffset 625
                ysize 640
                xoffset 5
                xsize 480

                if (expanded):
                    at transform:
                        ysize 0
                        linear 0.5:
                            ysize 640
                else:
                    at transform:
                        ysize 640
                        linear 0.5:
                            ysize 0

            side ("c r"):
                area (-20, 10, 500, 540)
                if (expanded):
                    viewport id "history_viewport":
                        draggable True 
                        mousewheel True
                        arrowkeys not renpy.get_screen("choice")
                        yadjustment ui.adjustment()
                        yinitial 1.0
                    
                        vbox:
                            for i, h in enumerate(_history_list[0:len(_history_list) - 1 if not renpy.get_screen("choice") else len(_history_list)]):
                                if (h.who and _history_list[i - 1] is not None and _history_list[i - 1].who and _history_list[i - 1].who is not h.who):
                                    label h.who:
                                        style "history_who"
                                        at trans_fade(0.5, 0.5)
                                elif (i == 0 and h.who):
                                    label h.who:
                                        style "history_who"
                                        at trans_fade(0.5, 0.5)
                                if (h.what == "__breakpoint__"):
                                    image "gui/icons/mind_wipe_icon_idle.png":
                                        xoffset 45
                                        yoffset -10
                                        at trans_fade(0.5, 0.5)
                                        at transform:
                                            zoom 0.75
                                else:
                                    text _(h.what + "\n"):
                                        color (h.what_args["color"] if "color" in h.what_args else "#000")
                                        if ("color" in h.what_args and h.what_args["color"] == "#F2EE29"):
                                            outlines [ (4, "#000005", 0, 0) ]
                                        xoffset 50
                                        xmaximum 400
                                        size 20
                                        at trans_fade(0.5, 0.5)
                else:
                    null
                if (len(_history_list) - 1 > 0 and expanded):
                    vbar: 
                        value YScrollValue("history_viewport")
                        xsize 10
                        xoffset 15
                        base_bar "#000"
                        thumb "gui/bar/history_scrollbar_thumb.png"
                        if (expanded):
                            at trans_fade(0.5, 0.5)
                else:
                    null

            if (progress_convo and expanded and check_boolean("show_convo_progress")):
                vbox:
                    xalign 0.5
                    yalign 0.95
                    spacing 5
                    at trans_fade(0.5, 0.5)

                    bar: 
                        style "convo_progress_bar"
                        value AnimatedValue(convo_progress, convo_length, 1.0, (convo_progress - 1 if progress_convo else convo_progress))

                    if (config.developer):
                        text _(str(convo_progress) + "/" + str(convo_length)):
                            color "#000"
                            xalign 0.5
                            size 15

style history_who is label

style history_who_text is label_text:
    bottom_padding 15
    xoffset 35

style convo_progress_bar:
    left_bar Frame("gui/bar/progress_bar_left.png", gui.vbar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/progress_bar_right.png", gui.vbar_borders, tile=gui.bar_tile)
    xmaximum 450
    ysize 30

screen mobile_articles():
    default article = None
    default read_articles = []

    frame:
        background Solid("#F2EE29")
        xalign 0.5
        yalign 0.5
        xsize 1600
        ysize 800

        if (article == None):
            vbox:
                xalign 0.8
                yalign 0.1

                text _("This should be of interest to you.")
                
                # Clicking on both of these should append them to an array of articles we've read
                textbutton _("https://localnewspaper.com/articles/man-shot"):
                    action [
                        (AddToSet(read_articles, 0) if 0 not in read_articles else NullAction()),
                        SetScreenVariable("article", 0)
                    ]
                textbutton _("https://localnewspaper.com/articles/another-man-shot"):
                    action [
                        (AddToSet(read_articles, 1) if 1 not in read_articles else NullAction()),
                        SetScreenVariable("article", 1)
                    ]

        else:
            side ("c r"):
                area (0, 0, 1145, 625)
                viewport id "article_viewport":
                    draggable True 
                    mousewheel True
                    arrowkeys True
                    
                    vbox:
                        style_prefix "article"
                        spacing 20
                        if (article == 0):
                            text _("Police confirm early-hours shooting in city"):
                                size 42
                            text _("Police have confirmed the death via gunshot wound of a local man, Charles Eisenhardt, at approximately 2 AM this morning. Although a neighbour – who preferred to remain anonymous – was nearby and responded to Eisenhardt’s cries for help, they were unable to reach him in time to save him.")
                            text _("“It’s very distressing to have this happen,” Constable Clive Pugh said in a statement to the press. “By all accounts he was a kind and nurturing man.”")
                            text _("Further statements indicated that a motivation for the act is unknown, and that there are currently no known suspects.")
                            text _("Police are urging anyone with information to come forward.")
                        elif (article == 1):
                            text _("Police investigating unknown killing in city’s south end"):
                                size 42
                            image "images/backgrounds/apartment_day.png"

                            text _("A man in his 40s has been fatally shot in the south-western regions of the city. The body was found at approximately 5 AM this morning.")
                            text _("The police confirmed the identity of the victim, Mortimer “Morty” Telemachus, in a statement this morning. “We’re urging locals to be careful when travelling at night,” continued the statement.")
                            text _("The police have revealed that they believe this to be related to the death of Charles Eisenhardt, another gunshot victim from several days ago, who died in a similar manner. No relationship or similarities between the two men are currently known.")
                            text _("If you or somebody you know has information related to the crime, please contact the police. All information given is confidential.")
                        elif (article == 2):
                            text _("{i}Star-Bot: Legend of the Stellar Six{/i} series begins filming, studio confirms"):
                                size 42
                            text _("Shooting has officially begun on Netflix’s upcoming series {i}Star-Bot: Legend of the Stellar Six{/i}, an official report confirmed. The live-action reboot of the cult classic cartoon is expected to take roughly three months to shoot, with a further three months scheduled for post-production.")
                            text _("“The first day of shooting’s always interesting,” said lead actor Davis Tomino, “since you often start out with a quieter scene to get a feel for your character. But here, [[director] Lucas Burbank clearly knows what we should prioritise, and so we’ve started out with a fight scene between Star-Bot and...well, you’ll have to watch and find out, won’t you?”")
                            text _("Fan response to the rebooted series has thus far largely been negative, with many viewing it as a soulless cash grab. “Why do we even need a reboot? The original series did everything it set out to do, and ended perfectly. There’s nothing that this series can meaningfully bring to the table,” read one popular comment on the show’s subreddit.")
                            text _("“What are the odds that it’ll be a twelve-episode season, but Star-Bot won’t actually appear until the nineth [[sic] or tenth episode?” read another.")
                            text _("{i}Star-Bot: Legend of the Stellar Six{/i} is currently scheduled to debut in April.")
                        elif (article == 3):
                            text _("Mystery woman interrupts tech conference"):
                                size 42
                            text _("{i}Titans of Tech{/i}, the annual conference run by software giant COEUS, was interrupted today by a pirate broadcaster during the opening presentation.")
                            text _("Attendees report that for roughly fifteen seconds the presentation was interrupted by an unknown woman, who hijacked the stream with what appeared to be a live broadcast of herself. The unknown woman urged consumers to stop buying COEUS products, and appeared to be warning viewers of something before control was regained of the stream. The woman wore a disguise and so far remains unidentified, although she did appear to have green hair.")
                            text _("COEUS officials have thus far responded quite calmly. “This is clearly some university student who thinks they’re being funny,” said one. “It’s nothing to be concerned about; it’s hardly on the same level as the Max Headroom signal hijackings. That being said, we would very much like to find this woman, so if anyone does have any information about where we can find her, please contact us immediately.”")
                            text _("Further statements later emphasised that the hijacking was only possible due to security exploits in outdated software. COEUS declined to comment when asked to clarify whether their own software was being used for the broadcast.")

                        text _("POPULAR ARTICLES")
                        if (article != 2):
                            textbutton _("{i}Star-Bot: Legend of the Stellar Six{/i} series begins filming, studio confirms"):
                                action [
                                    (AddToSet(read_articles, 2) if 2 not in read_articles else NullAction()),
                                    SetScreenVariable("article", 2)
                                ]
                        if (article != 3):
                            textbutton _("Mystery woman interrupts tech conference"):
                                action [
                                    (AddToSet(read_articles, 3) if 3 not in read_articles else NullAction()),
                                    SetScreenVariable("article", 3)
                                ]
                vbar value YScrollValue("article_viewport")
        
        # Either once we hit back or once we've scrolled to the bottom of the articles we return
        textbutton _("Back"):
            action (SetScreenVariable("article", None) if 0 not in read_articles or 1 not in read_articles else Return())

style article_text:
    color "#000"

screen read_pdf(full_file=False):
    frame:
        style_prefix "pdf_file"
        background Solid("#F2EE29")
        xalign 0.5
        yalign 0.5
        xsize 1600
        ysize 800

        side ("c r"):
            area (0, 0, 1145, 625)
            viewport id "pdf_viewport":
                draggable True 
                mousewheel True
                arrowkeys True
                
                vbox:
                    text _("From as far back as the 1930s, theories about the existence of extrasensory perception have been put forth. Scientific experiments have been performed to detect such abilities, but have never conclusively proved their existence.")
                    text _("Although many believe that these abilities are pseudoscience, they are wrong. There are people with extrasensory perception who live among us today.")
                    text _("My name is Sergei Maskelyne, and with the assistance of my friends Charles Eisenhardt and Morty Telemachus, I have been conducting research into people with these abilities for the last five years. These notes comprise the extent of my research thus far, and have been compiled so that if anything should happen to me, others can follow in my footsteps.")

                    text _("OPENING YOUR THIRD EYE"):
                        style "pdf_heading"
                    text _("Although there are several means by which a person may unlock their potential and gain psychic abilities, they are difficult to verify. It appears that what works for one person may not necessarily work for others, and the same method may not unlock identical powers between two people. I am as of yet unable to determine why exactly this is, beyond some speculation that the small variations in genetic makeup are enough to affect the exact abilities a person is granted.")
                    text _("I should begin with a description of how my own abilities were unlocked. I had been travelling through the Amazon jungle for several weeks. At the time I was a biologist, and was looking for samples of certain butterflies ({i}Caligo idomeneus{/i}, {i}Hamadryas arinome{/i}, {i}Semomesia capanea{/i}, among others). We were making our way out of the Amazon; the trip was to wrap up within a few days.")
                    text _("That was the plan, anyway. But the best-laid plans of mice and men often go awry. I was travelling with my crew down the river when we were beset by a heavy storm. We were washed further downstream than intended and separated in the currents. I was able to make my way to the shore, and in something of a panic, stumbled through the jungle in search of another human being.")
                    text _("I don’t know where exactly I was. Everything was dark, and I lost my bearings quite swiftly. The weather buffeted me about, making it impossible to find any navigational aids. I thought that I would be dead of exposure by morning. I wished only to send some sort of signal to warn others not to come and find me; to focus on their own survival and to abandon me as a lost cause. I had lost all hope, and was fearful of dragging others down with me.")
                    text _("Then, I found it. A monolithic stone tower, built by some ancient community of humans. Visibility was low in the weather, and I’ll admit that I was exhausted by this time. I’d been wandering around the jungle for hours after a lengthy day of travel. But despite my fatigue, despite the weather, I would still make the same claim today that I did when I first told this story. That the tower stretched infinitely up into the sky, an impossible distance beyond what the human eye could see.")
                    text _("The diameter of the tower itself was itself gigantic. I walked around its edge for many hours more, seeking an entrance so that I could shelter within during the storm. The resurgence of hope which had initially come to me upon finding the tower was just as soon diminished, replaced with a stronger sense of despair. The only positive that had come of finding the tower was the knowledge that it would serve as a natural waypoint; that others would not have to wander the jungle for days in order to confirm my death.")
                    text _("My morbid thoughts were eventually proven premature, however. Although I could have sworn that I had circled the entirety of the outside of the tower at least twice, I stumbled upon an entrance into it. Perhaps I had simply missed it, between my fatigue and the absence of light. Or perhaps there was another reason for the lack of an entrance...")
                    text _("Whatever the reason, I collapsed into the tower. It was a brutal thing constructed with raw blocks of stone, with nothing in the way of comfort. I was more than fine with that – I had a shelter from the storm, a sanctuary throughout the night. Simply lying down upon the rocky floor and getting a few winks of sleep would have been sufficient.")
                    text _("And yet my curiosity was getting the better of me. What was this gigantic stone tower? How had such a construct been created without collapsing under its own weight? Why had I never heard of such a thing while preparing for my trip? I ventured further into the darkness of the tower. I knew that the answers would likely forever remain a mystery to me, but I had to at least attempt to find them.")
                    text _("I have already mentioned that the circumference of the tower took me hours to walk around. One would think, then, that I would be prepared for how long it would take me to traverse the interior of the tower. I was not, and to be perfectly honest, I could not say how long it took me. At times it seemed as though I had been walking for days, wondering when I would see a wall, or some other construct within the tower. At other times I felt as though it had barely been a few minutes, that any confusion about how much time had passed had been the product of a tired and confused brain.")
                    text _("However long it took me, I did eventually find something within the tower. It was fairly easy to spot it once I was close enough – a light shone upon it from somewhere up high. Where that light came from, and how it was able to shine unbroken when I could still hear the whistle of the wind and rain outside, are questions that I cannot answer.")
                    text _("It was a statue, a humanoid figure sitting upon a throne. Whether the figure represented a god, king, or something else, I could not say. The closer I got to it – the more I focused on it – the more difficult I found it to comprehend its features. A pounding had begun in my head by now, and my vision was blurring. Attempting to identify features of the statue had me seeing double, the images swaying back and forth before me. My headache worsened more and more, and eventually I collapsed. I couldn’t maintain my balance, let alone my vision. Darkness closed in on me, the last thing I had seen being the ominous visage of the statue.")
                    text _("Once again, I cannot say how much time passed. I had long ago lost any devices which could have told me what hour it was, and even if I hadn’t, I somehow doubt that their claims would match my experience. All that I can say is that at some point, I regained consciousness. The pounding in my head was still present, but in comparison with what I had experienced prior to falling unconscious, it may as well have been nothing.")
                    text _("I picked myself up from the stone floor. The storm had blown itself out, and I could hear a twittering birdsong. There was no reason to stay within the tower – it had sheltered me as I had hoped it would, and I wasn’t going to discover any of its secrets. I knew the last to be a fact, for the statue which I had seen before falling unconscious was gone.")
                    text _("I left the tower – in much shorter a time than I would have thought it would take – and found myself with a new dilemma. I may have survived the night, but I was still lost deep within the Amazon jungle, away from my crew and civilisation. Out of the frying pan and into the fire, as they say.")
                    text _("How then, was I able to navigate my way out of the jungle and return home? How was I able to survive the deadly wildlife, the dangerous climate, of the jungle? Was it as simple as encountering the remainder of my crew within the next hour, and resuming our plans to return home?")
                    text _("If only.")
                    text _("What happened next should sound like some fantastic story, but if you’re reading this, then I’ve clearly trusted you to believe me. What happened next was that the pounding in my head intensified once more, to the level it had been at when I had approached the mysterious statue within the tower. I tried to concentrate, to control my breathing and hopefully cease it.")
                    text _("Instead what happened was I received a vision. I saw myself standing elsewhere, in a different part of the jungle. I could only have seen the vision for a scant few seconds, yet it was perfectly imprinted upon my mind. I couldn’t have forgotten it if I wanted to.")
                    text _("Although somewhat shaky, I decided that I should try to find the place that I had seen. It was as good a plan as any, and I was curious as to what I had seen. Was it even a real place? I walked away from the tower, choosing to move in the direction that I believed the river to be.")
                    text _("It didn’t take long, however, before I realised that something was wrong. There was a sensation in my mind that something was wrong. That I should walk the way that I was. Despite my best efforts to ignore it, the feeling persisted, until I eventually decided to change directions once more. At first the sensation disappeared, but it wasn’t too long before it came back again.")
                    text _("That was how the next three days went. I would travel in a single direction as best I could, until the sensation of wrongness returned. At that point I would choose a random direction and move in it, changing direction immediately if the sensation persisted. For water I drank from puddles and off leaves as required, trusting it to be rainwater and thus safe to drink. For food I simply didn’t bother. I hardly had the survival skills to trap or hunt any animals, and I couldn’t be certain that any plants would be safe to eat.")
                    text _("After three days of travel, stopping only when I was physically unable to, I reached the place that I had seen in my vision. At first I thought that it was pointless, that there was nothing for me there but more greenery and dangers, but shortly afterwards a group different to mine passed through. Needless to say, they were able to feed and hydrate me, and eventually help me return to civilisation. I was the only one of my team to do so.")
                    text _("No other person that I’ve spoken to has ever heard of the tower I encountered in the Amazon jungle, nor has anybody been able to identify the civilisation that the statue was carved by, let alone what the statue itself was. Were it not for the abilities that I was granted, I would be tempted to write the whole thing off as the hallucinations of a stressed body.")
                    text _("But I know better.")
                    text _("Other than the statue, there are several other ways to gain extrasensory abilities that I have confirmed. The first is to simply be born the child of a psychic. Historical records that I’ve unearthed have shown signs of psychic powers passing down a lineage, although it appears that they get weaker with each generation until they eventually disappear altogether. I suspect that lingering remnants of these abilities are what lead to phenomena such as gut feelings or prophetic dreams in ordinary people, although both Charles and Morty disagree with me.")
                    text _("The third way to gain psychic powers that I’m aware of is to be near a person with such abilities as they die. Others that I have spoken to claim to have been near people that regularly showed uncanny insight and odd abilities as they died, and each of them gained their powers shortly afterwards.")
                    text _("My theory is that whatever energy enables a person to access their abilities, it can only be held within a human brain. Once the life is gone from somebody, that energy must move to the nearest brain. (Is it possible that there is some sentience to the energy? It sounds ridiculous, and yet...) I have no evidence of extrasensory abilities acquired in this way diminishing over time, the way that they do when passed down bloodlines, but there is little confirmed data to work with. If only there were some way to test this further...")
                    text _("These are the three ways that one can acquire psychic powers that I’m aware of. Given that two of them involve inheritance, the natural question then is: do all such powers ultimately derive from the statue that I encountered? I could not say for certain. I’ve encountered several historical records of missing or confiscated statues, but none from the region where I encountered it. (I need to do further research into other artifacts. No description for The Sampo exists; could the statue be related?)")
                    text _("Although these are the three ways that I have confirmed that one can gain extrasensory abilities, there are rumours and unconfirmed stories of other ways. The most recurring one is of a certain technological company looking into brain implants which would grant psychic powers to the recipient. I need to keep an eye on them...")

                    text _("THE AWAKENED"):
                        style "pdf_heading"
                    text _("The following is a list of known psychics. To maintain anonymity, codenames have been used.")
                    text _("    {font=DejaVuSans.ttf}•{/font} THE EX-PROFESSOR\n    {font=DejaVuSans.ttf}•{/font} THE SPOONBENDER\n    {font=DejaVuSans.ttf}•{/font} FORGETTABLE NPC\n    {font=DejaVuSans.ttf}•{/font} THE CIRCUS RUNAWAY\n    {font=DejaVuSans.ttf}•{/font} THE PEEPER\n    {font=DejaVuSans.ttf}•{/font} MOTHER’S BOY\n    {font=DejaVuSans.ttf}•{/font} CRYO ORGANS\n    {font=DejaVuSans.ttf}•{/font} GAS MASK PROPHET")

                    text _("EXTRASENSORY ABILITIES"):
                        style "pdf_heading"
                    text _("From my research, I have discovered that the following abilities may be present in someone who has awakened their psychic powers. I’ve never encountered more than three within a single person, although it is possible that some of them may be different manifestations of the same power.")
                    text _("A single ability can be more or less powerful depending upon the individual; I’ve found it easiest to classify them within three broad levels where distinctions are known. Any figures given are averages for that level. Some have reported experiencing intermittent spikes of power with their abilities; whether this is a sign that all psychics could awaken their abilities to the third level with practice and training, or whether it’s a sign of something else, is unknown. Attempts to push one’s abilities beyond their natural limit usually result only in pain; there have even been records of abilities becoming damaged or stunted by trying to push them too far.")
                    text _("Several powers, most notably telepathy, can be blocked by the Yellow Square Defence, even should the target not have any telepathic talent of their own.")

                    if (full_file):
                        text _("TELEPATHY"):
                            style "pdf_subheading"
                        text _("Also known as mind-reading. A person with telepathic ability can reach out their minds to others and discover the thoughts and memories within their heads. How these thoughts are presented to the telepath appears to depend on the individual; some telepaths report receiving “fuzzy” or “blurred” thoughts when using their ability, while for others what they receive could not be any clearer.")
                        text _("The form thoughts are received in can also vary; a telepath may receive a thought as a string of text, images – either literal or metaphorical – or a strong emotion. Likely forms beyond these exist too.")
                        text _("A level one telepath can only read the surface thoughts of a person; what they’re currently thinking of. Particularly weak telepaths may require eye contact or touch in order to utilise their ability.")
                        text _("A level two telepath can delve deeper below the surface thoughts of a person; they can read subconscious ideas and emotions which the target may be unaware of. There are rumours of level two telepaths being affected by the subconsciousness which they read, absorbing the ideas and emotions and believing them to be their own.")
                        text _("Level three telepaths are virtually unheard of. They can not only read the surface and subconscious thoughts of a person, they can read and filter the thoughts of multiple minds at once. A level three telepath can delve deeply into a person’s memory and read all that they can recall; they could also follow a train of thought back to its origin.")

                        text _("PUPPETEERING"):
                            style "pdf_subheading"
                        text _("Also known as mind control. A person with the ability to puppeteer can control another using their thoughts, words, or both, depending upon the individual. Lower-level puppeteers can be thwarted fairly easily by people with strong enough wills and who are able to think for themselves; they recognise that their actions are not matching up with their intentions and can break the connection through force of will. For this reason I believe most users of LLMs to be highly vulnerable to puppeteers.")
                        text _("A level one puppeteer is often limited by how close they are to their target, and usually require touching them or speaking to them directly in order to utilise their ability. A level one puppeteer’s control is limited – they may be able to make their target react to certain trigger words they’ve implanted, or alter their emotions, but rarely can do more than that.")
                        text _("A level two puppeteer has much more control over their target; they can effectively possess somebody and control their actions. Whether or not the target is aware that their actions are not their own, or whether they are a prisoner within their own body, appears to depend upon the puppeteer themselves and how their ability manifests.")
                        text _("Level three puppeteers are only theoreticals; I have yet to encounter any or read of any confirmed cases of them. I speculate that a level three puppeteer would be able to effortlessly control multiple people around them without their control being broken; it’s also possible that the controlled would believe their actions to be their own, no matter how anathematic they are to them.")

                        text _("TELEKINESIS"):
                            style "pdf_subheading"
                        text _("Telekinesis is the ability to move objects using one’s mind. Some telekinetics show an affinity for particular materials; they find it easier to move and keep track of, for example, objects that are completely metal, or water. Others have little difficulty with multiple small objects but strain to move larger objects of comparable mass, or vice versa. The differing levels of telekinetics vary only in the amount of mass or objects that they can move, and the distance at which their power works.")
                        text _("A level one telekinetic can typically move up to 5 kilograms of mass without difficulty; if this is distributed through multiple objects 30 appears to be the maximum number that can be controlled. These telekinetics can affect objects up to roughly a 15-metre radius, centred on themselves.")
                        text _("A level two telekinetic’s limits are around 100 kilograms of mass, or up to 200 objects. Their range extends to around 200 metres.")
                        text _("The highest volume of mass recorded being manipulated by a level three telekinetic’s abilities was one tonne, although it wasn’t moved particularly far. I would estimate that 800 kilograms is more comfortably the upper limit of a level three’s abilities. The range of a level three telekinetic’s abilities is about 500 metres, although I question whether this is due to limitations of vision. Could a level three telekinetic using binoculars or something similar manipulate objects over a larger distance?")

                        text _("PRECOGNITION"):
                            style "pdf_subheading"
                        text _("Also known as future sight; the ability to see potential futures. Despite my best efforts I’ve been unable to confirm whether the future a precognitive sees is set in stone, or if it’s possible for it to be changed. Precognitives seem to have the most difficulty in manifesting their power when they wish it; I speculate that this is because their power only works once the majority of their sight cannot be changed.")
                        text _("A level one precognitive may not even be aware of their abilities, as they often manifest in a vague sense of words or feelings. When these precognitives experience the future they’ve foreseen they often get a sense of déjà vu, not recognising how their abilities work. A level one precognitive may also see brief flashes of images, but this is less common.")
                        text _("Level two precognitives will almost always see the future as visions. They may or may not be present in the vision themselves; this appears to be something that varies depending upon the individual. The intensity of these visions tends to be such that the precognitive is able to recall the image or images they see perfectly, without any flaws or difficulty.")
                        text _("No known level three precognitives have been discovered. I speculate that a level three precognitive would not only receive visions of the future, but that they could act within it and see the outcome of individual actions. Alternatively, it is possible that they would be able to identify how the visions they see came about; the chain of events which lead to those scenes.")

                        text _("PYROKINESIS"):
                            style "pdf_subheading"
                        text _("The ability to control and manipulate heat and flames with the power of one’s mind. Contrary to the common depictions in popular media, being a pyrokinetic does not make one any more hot-headed, impulsive, or angry than average.")
                        text _("Level one pyrokinetics are rarely aware of their abilities, although they may find themselves drawn to sources of heat or fires more than the average person. They can typically heat up things that they are in contact with and control their heat distribution. It’s possible that cases of spontaneous human combustion are the result of these pyrokinetics not knowing how to control their abilities, although I admit that this is speculation.")
                        text _("A level two pyrokinetic can control flames to a certain extent, moving them around and increasing or decreasing their heat or presence. Many pyrokinetics at this level are similarly unaware of their abilities, using them without recognising what they are doing.")
                        text _("Level three pyrokinetics are what one likely thinks of when it comes to pyrokinesis; they are able to cause fire to ignite spontaneously. While there are no records of any pyrokinetics being able to create flame larger than the average campfire, such a limitation rarely matters: the fire spreads naturally and consumes what it can, growing in the process.")

                        text _("ASTRAL PROJECTION"):
                            style "pdf_subheading"
                        text _("Astral projection is the ability for one to separate their consciousness from their body and move around; removing the ghost from the machine, as it were. While the person’s consciousness is on its own the body typically slumps to the floor and appears to be unconscious or sleeping.")
                        text _("Although the body continues its functions such as breathing on its own, the longer that a person astrally projects, the more difficult they will find returning to their body to be. Even returning successfully after too long may result in the person finding it difficult to control their body, with extreme cases leaving the person in a coma.")
                        text _("At level one of astral projection, the consciousness can move around outside of the body with conventional movement. The consciousness generally cannot be perceived by non-psychics or interact with objects. The consciousness typically cannot move too far from the body; the maximum recorded range for a level one projector is fifty metres.")
                        text _("At the second level of astral projection the consciousness can travel much further, with ranges measured in the range of kilometres. The consciousness can generally pass through some objects but still cannot manipulate them. In addition, the consciousness is less restricted in movement; projectors typically fly or float to travel. The consciousness still typically cannot be seen by non-psychics, but they can make themselves be heard.")
                        text _("The third level of astral projection allows the consciousness to move much farther and faster than the previous levels; while speeds were previously typically similar to what a person would be able to physically achieve, at this level the projection can move at the speed of thought. The projector can also control whether others can perceive them or not, and can pass through virtually any substance.")

                        text _("MEMORY ALTERATION"):
                            style "pdf_subheading"
                        text _("Often mistaken for the ability to wipe or “rewind” minds due to the manifestation of the ability at the lowest level. Psychics who can alter memories are similar to puppeteers in that they manipulate others, but while puppeteers manipulate the body, these psychics manipulate the mind.")
                        text _("At the first level these psychics can delete recent memories from the minds of their targets. The disorientation that occurs to the target typically results in them overlooking any minor discrepancies. For instance, if a book was on a table and then placed in a bookshelf before the target had their memories deleted, the target would assume that it hadn’t previously been on the table, provided they weren’t interacting with it.")
                        text _("Psychics at the second level of this ability have a finer control over the techniques available. While they can still delete memories they can be more selective in what they make the target forget, and can delete memories from further back. In addition, they can make minor alterations to existing memories, such as making a target believe that another person was present in a memory, or that something different was said in a conversation.")
                        text _("In my opinion the third level of memory alteration is one of the deadliest psychic powers. At this level the psychic can not only delete and alter memories with much greater control, they can create new memories in the target’s mind with ease. Thankfully the Yellow Square Defence can provide some safety against even this level, but one has to let their guard down eventually...")

                        text _("PSYCHOMETRY"):
                            style "pdf_subheading"
                        text _("A rare talent, psychometry is the ability to read the history of an object. More often than not touch is essential in this ability; while other psychic abilities may become easier or slightly more powerful when touching the subject, it is often required to utilise psychometry.")
                        text _("The first level of psychometry allows the psychic to touch an object and get a sense for who has recently touched or been near it. The psychic may get an image of the person or persons, or they may get a sense for that person’s unique mental patterns.")
                        text _("The second level of psychometry gives a stronger sense of not only who has recently interacted with the object, but of the item’s own history and where it has recently been. This typically takes the form of visions, although they may not always be in chronological order.")
                        text _("The third level of psychometry allows the psychic to read an item’s history and its possessors as far back as possible. It is recommended, however, that the psychic limit themselves to no more than a few years; the human brain is ill-equipped to sort and filter through so much information, and looking too far can result in comas or even brain death.")
                        
                        text _("SCANNING"):
                            style "pdf_subheading"
                        text _("A scanner is a psychic with the ability to detect the psychic energy of others. That is to say, if they are in the vicinity of other psychics, they can detect their presence. From my understanding most scanners have their ability constantly active, with no way to turn it off at their leisure.")
                        text _("At the first level, a scanner is limited in their ability. They can detect psychic energy in roughly a one-block radius, but not where it is concentrated. If a level one scanner were in a room with five other people, one of whom was a psychic, the scanner would know that there was a psychic nearby, but not who it was. Were there a second psychic five houses down the road, the scanner would be able to estimate that there was more than one psychic in the area, but could not be certain where they were – they could be in the same room as them, they could not.")
                        text _("Second-level scanners are able to detect psychic energy over a larger area, comparable to a moderately-sized city. At this level scanners no longer have the issue of their level one counterparts; they can detect which individuals within their area are psychic.")
                        text _("At the third level, scanners are able to detect psychic energy over an even wider area, comparable to a 5000 kilometre radius. They can still detect which individuals have psychic abilities, and when in their proximity, they can get a sense for what exactly those abilities might be.")

                        text _("CIBOPATHY"):
                            style "pdf_subheading"
                        text _("See reports #1 - #60 of {i}Chew{/i}, by John Layman and Rob Guillory.")

                        text _("THE TRUTH UNCOVERED?"):
                            style "pdf_heading"
                        text _("I have mentioned previously that a psychic’s abilities can experience brief spikes in level, but recent research has shown me a new way to increase power. After cross-referencing information in several books that I trust, I’ve come to a hypothesis: whatever energy is tapped into when using one’s abilities, access is limited by the number of psychics in the area.")
                        text _("For example, say that there is n amount of energy in an area, and there are ten psychics that live there. Each one would be able to tap into n10 energy, or 10% of n. If, however, five of them left the area, or died, there would only be five remaining psychics. They would each now be able to tap into n5 energy, or 20% of n. Each of them would find the range of their abilities doubled, although it may take some time for their brains to acclimatise to the change in energy; their abilities wouldn’t instantly increase.")
                        text _("While this has interesting implications for the ways in which psychics’ abilities work, there is more to be discovered yet. While it wouldn’t be apparent to a casual reader, cross-referencing further information between the books points to some sinister implications. I may have found some hints as to what the statue I once encountered truly was...but I’m not certain that I like the answers.")
                        text _("For now I’ve asked my partner to remove the books, lest somebody else find the information before I can determine how dangerous it may or may not be. Thankfully the topics of the books are fairly niche, and only by studying it from multiple angles can the truth be glimpsed.")
                        text _("I’ll provide an update as soon as possible...if I deem the knowledge safe to share...")
        
            vbar value YScrollValue("pdf_viewport")
        
        # Replace this with scrolling revealing stuff and returning
        textbutton _("Done"):
            xalign 1.0
            yalign 1.0
            action Return()

style pdf_file_text:
    color "#000"

style pdf_heading:
    color "#000"
    size 42

style pdf_subheading is pdf_heading:
    size 30

screen cash_money(style="left_small"):
    zorder 20

    if (style == "left_small"):
        frame:
            background Solid("#F2EE29")
            xsize 200
            ysize 50
            xalign 0.0
            yalign 0.3
            at transform:
                on show:
                    xoffset -200
                    ease 0.5:
                        xoffset 0
                on hide:
                    ease 0.5:
                        xoffset -200

            text _("$" + str(f'{money:.2f}')):
                color "#000"
                xalign 0.5
                yalign 1.0
                font "gui/twoweekendgo-bold.otf"
                size 32
    elif (style == "right_large"):
        frame:
            background Solid("#F2EE29")
            xsize 225
            ysize 75
            xalign 1.0
            yalign 0.3
            xoffset 200
            at transform:
                on show:
                    xoffset 0
                    ease 0.5:
                        xoffset -200
                on hide:
                    ease 0.5:
                        xoffset 200

            text _("$" + str(f'{money:.2f}')):
                color "#000"
                xalign 0.5
                yalign 0.5
                font "gui/twoweekendgo-bold.otf"
                size 46
    elif (style == "pause_menu"):
        frame:
            background Solid("#F2EE29")
            xsize 225
            ysize 75
            xalign 1.0
            yalign 0.2
            xoffset 200
            at transform:
                on show:
                    alpha 0.0
                    pause 1.6
                    xoffset 0
                    
                    parallel:
                        linear 1.0:
                            alpha 1.0
                    parallel:
                        ease 0.5:
                            xoffset -200
                on hide:
                    ease 0.5:
                        xoffset 200

            text _("$" + str(f'{money:.2f}')):
                color "#000"
                xalign 0.5
                yalign 0.5
                font "gui/twoweekendgo-bold.otf"
                size 46


screen gallery():
    tag menu
    default hover_item = None
    default viewing_cg = None
    default viewing_index = 0
    default show_content = False

    if (not show_content):
        timer 1.2:
            action SetScreenVariable("show_content", True)

    if (viewing_cg is not None and show_content):
        image ("images/cgs/" + cg_index_unlocked(viewing_cg)[viewing_index]["file"]):
            at transform:
                alpha 0.0
                linear 0.25 alpha 1.0
            xsize 1920
            ysize 1080

        if (viewing_index > 0 and cg_index_unlocked(viewing_cg)[viewing_index - 1]["locked"] == False):
            imagebutton:
                auto "gui/nav_arrow_%s_left.png"
                action SetScreenVariable("viewing_index", viewing_index - 1)
                xalign 0.0
        if (len(cg_index_unlocked(viewing_cg)) > viewing_index + 1 and cg_index_unlocked(viewing_cg)[viewing_index + 1]["locked"] == False):
            imagebutton:
                auto "gui/nav_arrow_%s_right.png"
                action SetScreenVariable("viewing_index", viewing_index + 1)
                xalign 1.0

        frame:
            background Solid("#F2EE29")
            xsize 100
            ysize 40
            xalign 0.5
            yalign 1.0
            at transform:
                yoffset 100
                linear 0.25:
                    yoffset 0

            textbutton _("BACK"):
                xalign 0.5
                yalign 0.5
                text_color "#000"
                text_font "gui/chubhand.ttf"
                text_hover_underline True
                action [SetScreenVariable("show_content", False),
                        SetScreenVariable("hover_item", None), 
                        SetScreenVariable("viewing_cg", None)]

        key "pad_b_press":
            action [SetScreenVariable("show_content", False),
                    SetScreenVariable("hover_item", None), 
                    SetScreenVariable("viewing_cg", None)]
            capture True
    else:
        use game_menu("GALLERY", 80, ShowMenu("main_menu", initialised=True, extras=True)):
            if(show_content):
                grid 1 4:
                    xalign 0.5
                    yalign 0.5
                    spacing 10
                    at trans_fade(0.0, 0.5)

                    for i in range(4):
                        if (i < 1):
                            frame:
                                background Solid("#3B3B3B")
                                xsize 320
                                ysize 179

                                button:
                                    background Frame("images/cgs/" + cg_index_unlocked(i)[0]["file"] if len(cg_index_unlocked(i)) > 0 else "images/cgs/locked.png")
                                    action ([
                                            SetScreenVariable("viewing_cg", i),
                                            SetScreenVariable("viewing_index", 0)
                                        ] if len(cg_index_unlocked(i)) > 0 else NullAction())
                                    #focus_mask True
                                    hovered SetScreenVariable("hover_item", i)
                                    unhovered SetScreenVariable("hover_item", None)
                                    at transform:
                                        on hover:
                                            matrixcolor TintMatrix("#00000066")
                                        on idle:
                                            matrixcolor None

                                if (len(cg_index_unlocked(i)) > 0):
                                    frame:
                                        background Solid("#000")
                                        xalign 1.0
                                        yalign 1.0

                                        text _((str(len(cg_index_unlocked(i)))) + "/" + str(len(persistent.cgs[i]["images"]))):
                                            color "#F2EE29"
                                            font "gui/Roboto-Medium.ttf"
                                            size 18
                        else:
                            null

                vbox:
                    xalign 0.5
                    yalign 0.9
                    spacing 10
                    xsize 400
                    at trans_fade(0.0, 0.5)

                    bar value StaticValue(total_cgs_unlocked(), 3):
                        xsize 300
                        xalign 0.5
                        yalign 0.5

                    text _(str(total_cgs_unlocked()) + "/3 (" + (str(round(total_cgs_unlocked() / 3 * 100, 2))) + "%) Unlocked"):
                        color "#000"
                        xalign 0.5
                        text_align 0.5

                if (hover_item is not None):
                    text _("Locked" if len(cg_index_unlocked(hover_item)) < 1 else "View larger"):
                        xalign 0.5
                        yalign 0.95
                        size 40
                        color "#000"
                        font "gui/chubhand.ttf"

                if (config.developer):
                    textbutton _("Lock all"):
                        action [Function(lock_cg, 0, 0), Function(lock_cg, 0, 1)]
                        xalign 0.5
                        yalign 0.0
                        text_color "#000"
                        text_font "gui/chubhand.ttf"
                        text_hover_underline True


screen sound_room():
    tag menu
    default show_content = False
    default currently_playing = None
    default song_placement = 0
    default pause_bar = False

    timer 1.2:
        action SetScreenVariable("show_content", True)

    use game_menu("SOUND\n ROOM", 81, [Function(renpy.music.play, "audio/music/brain_matter.mp3"), ShowMenu("main_menu", initialised=True, extras=True)]):
        if (show_content):
            grid 2 5:
                xalign 0.1
                yalign 0.4
                spacing 30
                yspacing 60
                at trans_fade(0.0, 0.5)

                for i in range(6):
                    frame:
                        background None
                        xsize 350
                        ysize 20

                        vbox:
                            if len(persistent.music_tracks) >= i + 1 and persistent.music_tracks[i]["unlocked"]:
                                textbutton _(persistent.music_tracks[i]["title"]):
                                    xsize 350
                                    action [
                                        Function(renpy.music.play, "audio/music/" + persistent.music_tracks[i]["file"]),
                                        SetScreenVariable("song_placement", 0),
                                        SetScreenVariable("currently_playing", persistent.music_tracks[i])
                                    ]
                                    selected currently_playing == persistent.music_tracks[i]
                                    hover_background Solid ("#000")
                                    selected_background Solid ("#000")
                                    text_hover_color "#F2EE29"
                                    text_selected_color "#F2EE29"
                                    text_hover_underline currently_playing == persistent.music_tracks[i]
                                if (currently_playing == persistent.music_tracks[i]):
                                    image "gui/icons/play_hover.png":
                                        yoffset -50
                                        xalign 1.0
                            else:
                                text _("???"):
                                    line_leading 12
                                    xoffset 10
                                    color "#000"

                            if len(persistent.music_tracks) >= i + 1 and currently_playing != persistent.music_tracks[i]:
                                image Solid("#000"):
                                    xsize 350
                                    ysize 1

            if currently_playing is not None:
                if (pause_bar):
                    timer 1.5:
                        action SetScreenVariable("pause_bar", False)
                timer 0.1:
                    repeat True
                    action (SetScreenVariable("song_placement", song_placement + 0.1) if not renpy.music.get_pause() and not preferences.get_mute("music") and not preferences.get_mute("all") and not pause_bar else NullAction())
                frame:
                    background None
                    xalign 0.68
                    yalign 0.4

                    xsize 600
                    ysize 500

                    hbox:
                        spacing 50
                        vbox:
                            spacing 75

                            text _(currently_playing["title"]):
                                xalign 0.5
                                yalign 0.25
                                color "#000"
                                font "gui/chubhand.ttf"

                            vbox:
                                xsize 450
                                xalign 0.5
                                yalign 0.5

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 450
                                    base_bar "gui/bar/audio_progress.png"
                                    thumb "gui/bar/audio_thumb.png"
                                    hover_thumb Solid("#000", xsize=15, ysize=30)

                                    value (renpy.music.get_pos() if renpy.music.get_pos() is not None else 0)
                                    range (renpy.music.get_duration() if renpy.music.get_duration() is not None else 999)
                                    changed jump_sound

                                hbox:
                                    xsize 450
                                    text _(convert_to_time(renpy.music.get_pos()) if not preferences.get_mute("music") else "0:00"):
                                        xalign 0.0
                                        color "#000"

                                    if (renpy.music.get_duration() > 0):
                                        text _(convert_to_time(renpy.music.get_duration())):
                                            xalign 1.0
                                            color "#000"
                            
                            hbox:
                                yalign 0.8
                                xalign 0.5
                                spacing 10
                                if (not renpy.music.get_pause()):
                                    imagebutton:
                                        auto "gui/icons/pause_%s.png"
                                        action Function(renpy.music.set_pause, True)
                                else:
                                    imagebutton:
                                        auto "gui/icons/play_%s.png"
                                        action Function(renpy.music.set_pause, False)
                                imagebutton:
                                    auto "gui/icons/stop_%s.png"
                                    action [
                                        Function(renpy.music.stop),
                                        SetScreenVariable("currently_playing", None)
                                    ]

                        vbox:
                            yalign 0.5
                            spacing 5
                            vbar:
                                xalign 0.5
                                ysize 170
                                value Preference("music volume")
                                if preferences.get_mute("music"):
                                    bottom_bar Frame("gui/slider/vertical_insensitive_bar.png", gui.vslider_borders, tile=gui.slider_tile)
                                    top_bar "#D5D5D5"

                            text _("Volume"):
                                color ("#000" if not preferences.get_mute("music") else "#707070")
                                size 24

                            imagebutton:
                                idle ("gui/icons/mute_hover.png" if preferences.get_mute("music") or preferences.get_mute("all") else "gui/icons/mute_idle.png")
                                hover "gui/icons/mute_hover.png"
                                xalign 0.5 
                                action Preference("music mute", "toggle")

            if (config.developer):
                vbox:
                    if (currently_playing is not None):
                        text _("Duration: " + str(renpy.music.get_pos()) + "/" + str(renpy.music.get_duration())):
                            color "#000"

                    #textbutton _("Lock all"):
                    #    action [Function(lock_music, "neutral_1"), Function(lock_music, "tense_1"), Function(lock_music, "ambient_1")]
                    #    xalign 0.5
                    #    yalign 0.0
                    #    text_color "#000"
                    #    text_font "gui/chubhand.ttf"
                    #    text_hover_underline True

screen cta():
    default hover_item = None
    default clickable = False

    timer 1.6:
        action SetScreenVariable("clickable", True)
    
    frame:
        style_prefix "cta"
        background Solid("#F2EE29")

        vbox:
            ysize 1080
            xfill True
            spacing 80

            text _("THANK YOU FOR PLAYING THE DEMO"):
                xalign 0.5
                yoffset 100
                xmaximum 1400
                text_align 0.5
                font "gui/Decade__.ttf"
                size 96
                at trans_fade(0.0, 0.75), fade_side_to_side(-150, 0)

            vbox:
                spacing 40
                xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 75
                    at trans_fade(0.75, 0.75), fade_side_to_side(150, 0.75)

                    vbox:
                        imagebutton:
                            idle "gui/icons/discord_cta" + ("_idle.png" if hover_item != "discord" else "_hover.png") 
                            hover "gui/icons/discord_cta_hover.png"
                            action (OpenURL("https://discord.gg/HYkSGNa5MZ") if clickable else NullAction())
                            hovered SetScreenVariable("hover_item", "discord")
                            unhovered SetScreenVariable("hover_item", None)
                        textbutton _("Join the Discord!"):
                            style "block_cta"
                            action (OpenURL("https://discord.gg/HYkSGNa5MZ") if clickable else NullAction())
                            hovered SetScreenVariable("hover_item", "discord")
                            unhovered SetScreenVariable("hover_item", None)
                            text_underline hover_item == "discord"

                    vbox:
                        imagebutton:
                            idle "gui/icons/steam" + ("_idle.png" if hover_item != "steam" else "_hover.png") 
                            hover "gui/icons/steam_hover.png"
                            action (OpenURL("https://store.steampowered.com/app/4595360/BLACKMIND_Psychic_Social_Simulator/") if clickable else NullAction())
                            hovered SetScreenVariable("hover_item", "steam")
                            unhovered SetScreenVariable("hover_item", None)
                        textbutton _("Wishlist on Steam!"):
                            style "block_cta"
                            action (OpenURL("https://store.steampowered.com/app/4595360/BLACKMIND_Psychic_Social_Simulator/") if clickable else NullAction())
                            hovered SetScreenVariable("hover_item", "steam")
                            unhovered SetScreenVariable("hover_item", None)
                            text_underline hover_item == "steam"

                    vbox:
                        imagebutton:
                            idle "gui/icons/bluesky_cta" + ("_idle.png" if hover_item != "bluesky" else "_hover.png") 
                            hover "gui/icons/bluesky_cta_hover.png"
                            action (OpenURL("https://bsky.app/profile/toomanyteeth.net") if clickable else NullAction())
                            hovered SetScreenVariable("hover_item", "bluesky")
                            unhovered SetScreenVariable("hover_item", None)
                        textbutton _("Follow on Bluesky!"):
                            style "block_cta"
                            action (OpenURL("https://bsky.app/profile/toomanyteeth.net") if clickable else NullAction())
                            hovered SetScreenVariable("hover_item", "bluesky")
                            unhovered SetScreenVariable("hover_item", None)
                            text_underline hover_item == "bluesky"
                
                hbox:
                    xalign 0.5
                    spacing 75
                    at trans_fade(0.75, 0.75), fade_side_to_side(150, 0.75)

                    vbox:
                        imagebutton:
                            idle "gui/icons/kickstarter_cta" + ("_idle.png" if hover_item != "kickstarter" else "_hover.png") 
                            hover "gui/icons/kickstarter_cta_hover.png"
                            action (OpenURL("https://www.kickstarter.com/projects/too-many-teeth/blackmind-a-psychic-social-simulator") if clickable else NullAction())
                            hovered SetScreenVariable("hover_item", "kickstarter")
                            unhovered SetScreenVariable("hover_item", None)
                        textbutton _("Kickstarter"):
                            style "block_cta"
                            action (OpenURL("https://www.kickstarter.com/projects/too-many-teeth/blackmind-a-psychic-social-simulator") if clickable else NullAction())
                            hovered SetScreenVariable("hover_item", "kickstarter")
                            unhovered SetScreenVariable("hover_item", None)
                            text_underline hover_item == "kickstarter"

                    vbox:
                        imagebutton:
                            idle "gui/icons/feedback_cta" + ("_idle.png" if hover_item != "feedback" else "_hover.png") 
                            hover "gui/icons/feedback_cta_hover.png"
                            action (OpenURL("https://forms.gle/g45xXwVSKNiM4o5f8") if clickable else NullAction())
                            hovered SetScreenVariable("hover_item", "feedback")
                            unhovered SetScreenVariable("hover_item", None)
                        textbutton _("Provide Feedback"):
                            style "block_cta"
                            action (OpenURL("https://forms.gle/g45xXwVSKNiM4o5f8") if clickable else NullAction())
                            hovered SetScreenVariable("hover_item", "feedback")
                            unhovered SetScreenVariable("hover_item", None)
                            text_underline hover_item == "feedback"

            hbox:
                xalign 0.5
                yoffset -80
                spacing 250
                at trans_fade(1.5, 0.75), fade_side_to_side(-150, 1.5)

                textbutton _("Main Menu"):
                    action MainMenu(False)

                textbutton _("Quit"):
                    action Quit(None)

style cta_text:
    color "#000"
style cta_vbox:
    spacing 25
style cta_image_button:
    xalign 0.5
style cta_button_text:
    color "#000"
    font "gui/chubhand.ttf"
    size 58
    hover_color "#F2EE29"
    outlines [ (4, "#F2EE29", 0, 0) ]
    hover_outlines [ (4, "#000", 0, 0) ]
style block_cta:
    font gui.preference("font")

screen input_checker():
    add InputChecker()

screen block_rollback():
    key ["mousedown_4", "anyrepeat_K_PAGEUP", "anyrepeat_KP_PAGEUP", "pad_leftshoulder_press", "pad_lefttrigger_pos", "pad_back_press", "repeat_pad_leftshoulder_press", "repeat_pad_lefttrigger_pos", "repeat_pad_back_press"]:
        if (config.developer):
            action Rollback()
        elif (renpy.get_widget("conversation_history", "history_viewport")):
            action SetField(renpy.get_widget("conversation_history", "history_viewport").yadjustment, "value", (renpy.get_widget("conversation_history", "history_viewport").yadjustment.value - 30))
        else:
            action NullAction()

    key ["mousedown_5", "anyrepeat_K_PAGEDOWN", "anyrepeat_KP_PAGEDOWN", "pad_rightshoulder_press", "repeat_pad_rightshoulder_press"]:
        if (renpy.get_widget("conversation_history", "history_viewport")):
            action SetField(renpy.get_widget("conversation_history", "history_viewport").yadjustment, "value", (renpy.get_widget("conversation_history", "history_viewport").yadjustment.value + 30))
        else:
            action NullAction()

screen any_key(action):
    key "K_RETURN":
        action action
    key "K_SPACE":
        action action
    key "mouseup_1":
        action action
    key "mouseup_2":
        action action
    key "mouseup_3":
        action action
    key "K_ESCAPE":
        action action

    key "K_q":
        action action
    key "K_w":
        action action
    key "K_e":
        action action
    key "K_r":
        action action
    key "K_t":
        action action
    key "K_y":
        action action
    key "K_u":
        action action
    key "K_i":
        action action
    key "K_o":
        action action
    key "K_p":
        action action
    key "K_a":
        action action
    key "K_s":
        action action
    key "K_d":
        action action
    key "K_f":
        action action
    key "K_g":
        action action
    key "K_h":
        action action
    key "K_j":
        action action
    key "K_k":
        action action
    key "K_l":
        action action
    key "K_z":
        action action
    key "K_x":
        action action
    key "K_c":
        action action
    key "K_v":
        action action
    key "K_b":
        action action
    key "K_n":
        action action
    key "K_m":
        action action
    key "K_1":
        action action
    key "K_2":
        action action
    key "K_3":
        action action
    key "K_4":
        action action
    key "K_5":
        action action
    key "K_6":
        action action
    key "K_7":
        action action
    key "K_8":
        action action
    key "K_9":
        action action
    key "K_0":
        action action

    key "K_F1":
        action action
    key "K_F2":
        action action
    key "K_F3":
        action action
    key "K_F4":
        action action
    key "K_F5":
        action action
    key "K_F6":
        action action
    key "K_F7":
        action action
    key "K_F8":
        action action
    key "K_F9":
        action action
    key "K_F10":
        action action
    key "K_F11":
        action action
    key "K_F12":
        action action
    key "K_TAB":
        action action
    key "K_BACKSPACE":
        action action
    key "K_UP":
        action action
    key "K_DOWN":
        action action
    key "K_LEFT":
        action action
    key "K_RIGHT":
        action action
    key "K_LSHIFT":
        action action
    key "K_RSHIFT":
        action action
    key "K_LCTRL":
        action action
    key "K_RCTRL":
        action action
    key "K_LALT":
        action action
    key "K_RALT":
        action action
    key "K_CAPSLOCK":
        action action

    key "K_COMMA":
        action action
    key "K_PERIOD":
        action action
    key "K_SLASH":
        action action
    key "K_SEMICOLON":
        action action
    key "K_QUOTE":
        action action
    key "K_LEFTBRACKET":
        action action
    key "K_RIGHTBRACKET":
        action action
    key "K_BACKSLASH":
        action action
    key "K_BACKQUOTE":
        action action
    key "K_DELETE":
        action action
    key "K_MINUS":
        action action
    key "K_EQUALS":
        action action

    key "pad_leftshoulder_press":
        action action
    key "pad_lefttrigger_pos":
        action action
    key "pad_rightshoulder_press":
        action action
    key "pad_righttrigger_pos":
        action action

    key "pad_y_press":
        action action
    key "pad_x_press":
        action action
    key "pad_a_press":
        action action 
    key "pad_b_press":
        action action   

    key "pad_dpleft_press":
        action action
    key "pad_dpright_press":
        action action
    key "pad_dpup_press":
        action action
    key "pad_dpdown_press":
        action action

    key "pad_guide_press":
        action action
    key "pad_start_press":
        action action
    key "pad_back_press":
        action action