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
    tag menu
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
    default hover_row = None
    default selected_save = None
    default show_content = False
    tag menu

    timer 1.2:
        action SetScreenVariable("show_content", True)

    use game_menu(title, 96):

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

                                textbutton _("Save Name"):
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

                if (selected_save is not None):
                    vbox:
                        add FileScreenshot(selected_save + 1):
                            xalign 0.5

                        text _("Save Name"):
                            style "save_name"
                        text _("Day 1, Morning"):
                            style "save_details"
                        text _(add_date_suffix(FileTime(selected_save + 1, format="%d", empty=(0))) + FileTime(selected_save + 1, format=_("{#file_time}%B %Y, %H:%M"))):
                            style "save_date"

                        hbox:
                            xfill True
                            spacing 5
                            box_align 0.5
                            textbutton _("Load"):
                                style "light_yellow_button_small"
                                action (Function(renpy.load, "1-" + str(selected_save + 1)))
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
    font "gui/chubhand.ttf"
    color "#000"
    xalign 0.5
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

screen modal_popup(message, option_labels, option_actions):
    modal True

    zorder 200

    style_prefix "confirm"

    frame:
        xfill True
        yfill True
        background Solid ("#f2ef2973")
        at trans_fade(0.0, 0.5)

        frame:
            background Solid("#000000")
            xsize 588
            ysize 380

            frame:
                background Solid("#F2EE29")
                xsize 576
                ysize 368

                vbox:
                    xalign .5
                    yalign .5
                    spacing 45

                    label _(message):
                        style "confirm_prompt"
                        text_color "#000"
                        xalign 0.5

                    hbox:
                        xalign 0.5
                        spacing 150

                        for (i, label) in enumerate(option_labels):
                            textbutton _(label):
                                action option_actions[i]

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

    text _("{color=#000}BLACK{/color}{color=#F2EE29}MIND{/color}"):
        xalign 0.5
        yalign 0.1
        font "gui/Decade__.ttf"
        size 90
        xoffset -18
        at trans_fade(0.5, 0.5)

    vbox:
        xalign 0.3
        yalign 0.75
        spacing 50
        at trans_fade(1.0, 0.5), fade_side_to_side(-1000, 0.5)
        textbutton _("Flow Chart"):
            style "yellow_button_on_yellow"
            #action ShowMenu("flow_chart")
            action Show("modal_popup", message="Disabled during prototype; will add this in later", option_labels=["OK"], option_actions=[Hide("modal_popup")])
        textbutton _("Characters"):
            style "yellow_button_on_yellow"
            #action ShowMenu("characters")
            action Show("modal_popup", message="Disabled during prototype; will add this in later", option_labels=["OK"], option_actions=[Hide("modal_popup")])
        textbutton _("Load"):
            style "yellow_button_on_yellow"
            action ShowMenu("saves_list")
        textbutton _("Menu"):
            style "yellow_button_on_yellow"
            action MainMenu()
        textbutton _("Quit"):
            style "yellow_button_on_yellow"
            action Quit()

    vbox:
        xalign 0.775
        yalign 0.7
        spacing 50
        at trans_fade(1.0, 0.5), fade_side_to_side(1000, 0.5)
        textbutton _("Psychic Powers"):
            style "black_button_on_black"
            #action ShowMenu("upgrades_screen")
            action Show("modal_popup", message="Disabled during prototype; will add this in later", option_labels=["OK"], option_actions=[Hide("modal_popup")])
        textbutton _("Notes"):
            style "black_button_on_black"
            #action ShowMenu("notes")
            action Show("modal_popup", message="Disabled during prototype; will add this in later", option_labels=["OK"], option_actions=[Hide("modal_popup")])
        textbutton _("Settings"):
            style "black_button_on_black"
            action ShowMenu("preferences")
        textbutton _("Return"):
            style "black_button_on_black"
            action Return()

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