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
    frame:
        xalign 1.0
        yalign 0.0
        background Solid("#F2EE29")
        padding (5, 5, 5, 5)
        
        vbox:
            if (current_thought is not None):
                textbutton _("Read Mind" if minds_read < max_mind_reads else "Power Exhausted"):
                    text_color "#000"
                    action [
                        SetVariable("minds_read", (minds_read + 1 if minds_read < max_mind_reads else max_mind_reads)),
                        (Call(current_thought, from_current=True) if minds_read < max_mind_reads else NullAction())
                    ]
            if (current_conversation is not None):
                textbutton _("Rewind Mind" if minds_rewound < max_rewinds else "Power Exhausted"):
                    text_color "#000"
                    action [
                        SetVariable("minds_rewound", (minds_rewound + 1 if minds_rewound < max_rewinds else 1)),
                        (Jump("activate_rewind") if minds_rewound < max_rewinds else NullAction())
                    ]

screen conversation_progress():
    if (progress_convo):
        bar: 
            style "convo_progress_bar"
            value AnimatedValue(convo_progress, convo_length, 1.0, (convo_progress - 1 if progress_convo else convo_progress))

        text _(str(convo_progress)):
            color "#F2EE29"
            xalign 0.5
            yalign 0.15

style convo_progress_bar:
    left_bar "#F2EE29"
    right_bar "#141414"
    xmaximum 500
    xalign 0.5
    yalign 0.1

screen map_navigation():
    default xpos = 0
    default ypos = 0

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100

        vbox:
            textbutton _("Bar"):
                action [
                    Hide("map_navigation"),
                    Jump("bar")
                ]
                hovered [
                    SetScreenVariable("xpos", 200),
                    SetScreenVariable("ypos", 300)
                ]

            textbutton _("Alternative Shop"):
                action [
                    Hide("map_navigation"),
                    Jump("alt_shop")
                ]
                hovered [
                    SetScreenVariable("xpos", 100),
                    SetScreenVariable("ypos", 75)
                ]

            textbutton _("Cafe"):
                action [
                    Hide("map_navigation"),
                    Jump("cafe")
                ]
                hovered [
                    SetScreenVariable("xpos", 280),
                    SetScreenVariable("ypos", 20)
                ]

            textbutton _("Detective's Office"):
                action [
                    Hide("map_navigation"),
                    Jump("detective")
                ]
                hovered [
                    SetScreenVariable("xpos", 150),
                    SetScreenVariable("ypos", 450)
                ]

            textbutton _("Return"):
                yoffset 100
                action [
                    Hide("map_navigation"),
                    Jump("story")
                ]

        frame:
            xsize 300
            ysize 500
            background Solid("#141414")
            #image here

            frame:
                style "map_y_coord"
                xpos 0
                at transform:
                    pause 0.2
                    linear 1.0:
                        xpos xpos

            frame: 
                style "map_x_coord"
                ypos 0
                at transform:
                    pause 0.2
                    linear 1.0:
                        ypos ypos

style map_y_coord:
    xmaximum 2
    yfill True
    background Solid("#F2EE29")

style map_x_coord:
    ymaximum 2
    xfill True
    background Solid("#F2EE29")

screen locked_message(message):
    frame:
        background Frame("gui/textbox.png")
        padding (50, 50, 50, 50)
        xalign 0.5
        yalign 0.9
        at transform:
            alpha 0.0
            linear 0.3:
                alpha 1.0

        text _(message):
            text_align 0.5
            color "#FFF"
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
    default zoom_level = 0.25
    default offset = 0
    default zooming_in = False
    default zooming_out = False
    default scrolling_up = False
    default scrolling_down = False
    default active_control = None

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
                
    frame:
        xfill True
        yfill True
        xalign 0.5
        yalign 0.5
        background None

        at transform:
            yoffset offset
            zoom zoom_level

        vbox:
            xalign 0.5
            yalign 0.5

            textbutton _("End of Day #1" if renpy.can_load(str(game_id) + "_A_01_03") else "-"):
                action (NullAction() if not renpy.can_load(str(game_id) + "_A_01_03") else [
                    #Function(renpy.log, days),
                    Function(renpy.load, str(game_id) + "_A_01_03")
                ])
            textbutton _("End of Day #2" if renpy.can_load(str(game_id) + "_A_02_03") else "-"):
                action (NullAction() if not renpy.can_load(str(game_id) + "_A_02_03") else [
                    #Function(renpy.log, days),
                    Function(renpy.load, str(game_id) + "_A_02_03")
                ])
            textbutton _("End of Day #3" if renpy.can_load(str(game_id) + "_A_03_03") else "-"):
                action (NullAction() if not renpy.can_load(str(game_id) + "_A_03_03") else [
                    #Function(renpy.log, days),
                    Function(renpy.load, str(game_id) + "_A_03_03")
                ])
            textbutton _("End of Day #4" if renpy.can_load(str(game_id) + "_A_04_03") else "-"):
                action (NullAction() if not renpy.can_load(str(game_id) + "_A_04_03") else [
                    #Function(renpy.log, days),
                    Function(renpy.load, str(game_id) + "_A_04_03")
                ])

    vbox:
        xalign 0.95
        yalign 0.9

        textbutton _("Up"):
            if (active_control == "up"):
                keysym "mousedown_1"
                alternate_keysym "mouseup_1"
            action SetScreenVariable("scrolling_up", True)
            alternate SetScreenVariable("scrolling_up", False)
            hovered SetScreenVariable("active_control", "up")
            unhovered SetScreenVariable("active_control", None)

        textbutton _("Down"):
            if (active_control == "down"):
                keysym "mousedown_1"
                alternate_keysym "mouseup_1"
            action SetScreenVariable("scrolling_down", True)
            alternate SetScreenVariable("scrolling_down", False)
            hovered SetScreenVariable("active_control", "down")
            unhovered SetScreenVariable("active_control", None)

        textbutton _("Zoom In"):
            if (active_control == "zoom_in"):
                keysym "mousedown_1"
                alternate_keysym "mouseup_1"
            action SetScreenVariable("zooming_in", True)
            alternate SetScreenVariable("zooming_in", False)
            hovered SetScreenVariable("active_control", "zoom_in")
            unhovered SetScreenVariable("active_control", None)
        
        textbutton _("Zoom Out"):
            if (active_control == "zoom_out"):
                keysym "mousedown_1"
                alternate_keysym "mouseup_1"
            action SetScreenVariable("zooming_out", True)
            alternate SetScreenVariable("zooming_out", False)
            hovered SetScreenVariable("active_control", "zoom_out")
            unhovered SetScreenVariable("active_control", None)

        textbutton _("Return"):
            xalign 0.95
            yalign 0.95
            
            action [
                Hide("flow_chart"),
                Show("debug")
            ]

screen saves_list(title="LOAD"):
    tag menu

    frame:
        background Solid("#F2EE29")
        xfill True
        yfill True

        frame:
            style "bottom_left_frame"
            at menu_bottom_left_slide

        frame:
            style "top_right_frame"
            at menu_top_right_slide

        frame:
            style "bottom_right_frame"
            at menu_bottom_right_slide
            
        text _(title):
            font "gui/Decade__.ttf"
            size 96
            color "#F2EE29"
            xalign 0.025
            yalign 0.95
            at trans_fade(1.0, 0.33)

        #Table with list of files
            #Loop through files
            #Clicking on one brings up the screenshot, details, and load/delete buttons

        #If we're saving, there should be a NEW SAVE button somewhere obvious, so we don't have to overwrite our existing save

    textbutton _("Return"):
        xalign 0.975
        yalign 0.975
        text_font "gui/chubhand.ttf"
        text_color "#F2EE29"
        text_hover_underline True
        action Return()
        at trans_fade(1.0, 0.33)

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