screen debug():
    
    vbox:
        xalign 0.5
        yalign 0.2

        textbutton _("Test Mind Reading"):
            action [
                Hide("debug"),
                SetVariable("minds_read", 0),
                SetVariable("minds_rewound", 0),
                SetVariable("progress_convo", True),
                Call("test_mind_reading", from_current=True)
            ]

        textbutton _("Test Map Jump"):
            action [
                Hide("debug"),
                SetVariable("progress_convo", False),
                Show("map_navigation")
            ]

        textbutton _("Test Money"):
            action [
                Hide("debug"),
                Call("test_money", from_current=True)
            ]

        textbutton _("Test Locking Choices"):
            action [
                Hide("debug"),
                Call("test_choices", from_current=True)
            ]

        textbutton _("Test Upgrading Psychic Abilities"):
            action [
                Hide("debug"),
                Show("upgrades_screen")
            ]

        textbutton _("Test Flow Chart"):
            action [
                Hide("debug"),
                Show("flow_chart")
            ]

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
                                NullAction(),
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
            key "K_3":
                action [
                    SetLocalVariable("icon_hint", None),
                    NullAction(),
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
            font "gui/DCC - Ash.otf"
            xalign 0.125
            yalign 0.25
            size 140
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

screen modal_base():
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
            ysize 490
            xalign 0.5
            yalign 0.5

            frame:
                background Solid("#F2EE29")
                xsize 900
                ysize 450
                xalign 0.5
                yalign 0.5

                vbox:
                    xalign .5
                    yalign .5
                    spacing 45

                    transclude

screen modal_popup(message, option_labels, option_actions):
    modal True
    use modal_base:
        label _(message):
            style "confirm_prompt"
            text_color "#000"
            xalign 0.5

        hbox:
            xalign 0.5
            yalign 1.0
            yoffset 70

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
            action (Show("modal_popup", message="This function is disabled during the demo", option_labels=["OK"], option_actions=[Hide("modal_popup")]) if clickable_button() else NullAction())
        textbutton _("Locked"): #"Characters"):
            style "yellow_button_on_yellow"
            #action ShowMenu("characters")
            action (Show("modal_popup", message="This function is disabled during the demo", option_labels=["OK"], option_actions=[Hide("modal_popup")]) if clickable_button() else NullAction())
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
        #    action (Show("modal_popup", message="This function is disabled during the demo", option_labels=["OK"], option_actions=[Hide("modal_popup")]) if clickable_button() else NullAction())
        textbutton _("Locked"): #Notes"):
            style "black_button_on_black"
            #action ShowMenu("notes")
            action (Show("modal_popup", message="This function is disabled during the demo", option_labels=["OK"], option_actions=[Hide("modal_popup")]) if clickable_button() else NullAction())
        textbutton _("Settings"):
            style "black_button_on_black"
            action (ShowMenu("preferences") if clickable_button() else NullAction())
        textbutton _("Help"):
            style "black_button_on_black"
            action (ShowMenu("help") if clickable_button() else NullAction())
        textbutton _("Quit Game"):
            style "black_button_on_black"
            action (Quit() if clickable_button() else NullAction())

    use cash_money("pause_menu")

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

        text _("SOCIAL PSYCHIC SIMULATOR"):
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
                                            outlines [ (2, "#000005", 0, 0) ]
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

            text _("{font=DejaVuSans.ttf}${/font}" + str(f'{money:.2f}')):
                color "#000"
                xalign 0.25
                font "gui/chubhand.ttf"
                size 40
                yoffset -5
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

            text _("{font=DejaVuSans.ttf}${/font}" + str(f'{money:.2f}')):
                color "#000"
                xalign 0.5
                font "gui/chubhand.ttf"
                size 66
                yoffset -10
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

            text _("{font=DejaVuSans.ttf}${/font}" + str(f'{money:.2f}')):
                color "#000"
                xalign 0.5
                font "gui/chubhand.ttf"
                size 66
                yoffset -10

screen attune_senses():
    #default transparency = 0.33

    #timer 0.5:
    #    action SetScreenVariable("transparency", random.randint(0, 100) / 100)
    #    repeat True

    image "images/sprites/jack_smug.png":
        at center

    text _("Tonight's a good night to continue working on the plan. Where should I go first?"):
        color "#F2EE29"
        xalign 0.75
        yalign 0.25
        xmaximum 350
        at transform:
            alpha 0.0
            block:
                ease 1.0:
                    alpha random.randint(31, 70) / 100
                pause 0.5
                linear 1.0:
                    alpha random.randint(0, 30) / 100
                pause 0.5
                repeat

    frame:
        background "gui/textbox.png"
        xalign 0.5
        yalign 0.95
        xsize 1376
        ysize 288
        at trans_fade(0.0, 1.0), fade_side_to_side(1800, 0.0)

        text _("Attune your psychic senses until the thoughts are barely visible"):
            xalign 0.5
            yalign 0.25
            color "#000"
            at trans_fade(1.0, 0.5)

        textbutton _("START GAME"):
            xalign 0.5
            yalign 0.8
            text_font "gui/chubhand.ttf"
            text_color "#000"
            text_hover_color "#F2EE29"
            text_hover_outlines [ (4, "#000005", 0, 0) ]
            text_size 72
            text_yoffset 5
            action [
                SetVariable("persistent.senses_attuned", True),
                Return()
            ]
            at trans_fade(6.0, 0.5)

    key "mouseup_3":
        action NullAction()

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

                    bar value StaticValue(total_cgs_unlocked(), 2):
                        xsize 300
                        xalign 0.5
                        yalign 0.5

                    text _(str(total_cgs_unlocked()) + "/2 (" + (str(total_cgs_unlocked() / 2 * 100)) + "%) Unlocked"):
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
    default bar_hovered = False

    timer 1.2:
        action SetScreenVariable("show_content", True)

    use game_menu("SOUND\n ROOM", 81, [Function(renpy.music.play, "audio/music/brain_matter.mp3"), ShowMenu("main_menu", initialised=True, extras=True)]):
        if (show_content):
            grid 2 5:
                xalign 0.1
                yalign 0.2
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
                timer 0.1:
                    repeat True
                    action (SetScreenVariable("song_placement", song_placement + 0.1) if not renpy.music.get_pause() and not preferences.get_mute("music") and not preferences.get_mute("all") and not bar_hovered else NullAction())
                frame:
                    background None
                    xalign 0.68
                    yalign 0.2

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
                                    hovered SetScreenVariable("bar_hovered", True)
                                    unhovered SetScreenVariable("bar_hovered", False)

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
    
    frame:
        style_prefix "cta"
        background Solid("#F2EE29")

        vbox:
            ysize 1080
            xfill True
            spacing 120

            text _("THANK YOU FOR PLAYING THE DEMO"):
                xalign 0.5
                yoffset 100
                xmaximum 1400
                text_align 0.5
                font "gui/Decade__.ttf"
                size 96
                at trans_fade(0.0, 0.75), fade_side_to_side(-150, 0)

            hbox:
                xalign 0.5
                spacing 100
                at trans_fade(0.75, 0.75), fade_side_to_side(150, 0.75)

                vbox:
                    imagebutton:
                        idle "gui/icons/discord_cta" + ("_idle.png" if hover_item != "discord" else "_hover.png") 
                        hover "gui/icons/discord_cta_hover.png"
                        action OpenURL("https://discord.gg/HYkSGNa5MZ")
                        hovered SetScreenVariable("hover_item", "discord")
                        unhovered SetScreenVariable("hover_item", None)
                    textbutton _("Join the Discord!"):
                        style "block_cta"
                        action OpenURL("https://discord.gg/HYkSGNa5MZ")
                        hovered SetScreenVariable("hover_item", "discord")
                        unhovered SetScreenVariable("hover_item", None)
                        text_underline hover_item == "discord"

                vbox:
                    imagebutton:
                        idle "gui/icons/steam" + ("_idle.png" if hover_item != "steam" else "_hover.png") 
                        hover "gui/icons/steam_hover.png"
                        action OpenURL("https://store.steampowered.com")
                        hovered SetScreenVariable("hover_item", "steam")
                        unhovered SetScreenVariable("hover_item", None)
                    textbutton _("Wishlist on Steam!"):
                        style "block_cta"
                        action OpenURL("https://store.steampowered.com")
                        hovered SetScreenVariable("hover_item", "steam")
                        unhovered SetScreenVariable("hover_item", None)
                        text_underline hover_item == "steam"

                vbox:
                    imagebutton:
                        idle "gui/icons/bluesky_cta" + ("_idle.png" if hover_item != "bluesky" else "_hover.png") 
                        hover "gui/icons/bluesky_cta_hover.png"
                        action OpenURL("https://bsky.app/profile/toomanyteeth.net")
                        hovered SetScreenVariable("hover_item", "bluesky")
                        unhovered SetScreenVariable("hover_item", None)
                    textbutton _("Follow on Bluesky!"):
                        style "block_cta"
                        action OpenURL("https://bsky.app/profile/toomanyteeth.net")
                        hovered SetScreenVariable("hover_item", "bluesky")
                        unhovered SetScreenVariable("hover_item", None)
                        text_underline hover_item == "bluesky"

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